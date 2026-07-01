#!/usr/bin/env python3
"""daily_scan.py — daily emerging-candidate tracker for games-researcher.

Two scanning lanes, one CSV datastore. Free Apple endpoints only (iTunes RSS charts
+ Lookup). Pure stdlib, no dependencies.

  Lane A (broad recall): classify EVERY charting app by mechanic family, so we can
    track rating-count velocity within each family — catches self-published sleepers
    before any publisher grabs them.
  Lane B (high precision): flag brand-new app IDs from watchlist publishers — a
    publisher only ships what already cleared its soft-launch gates, so a new
    watchlist title is pre-validated proof the mechanic has legs.

The scan APPENDS a row per (app, geo, chart, scan day). Velocity/deltas/recency are
NOT stored — they're derived at read time by --report. See ../data/README.md.

Usage:
  python daily_scan.py                     # scan today → write scans/<date>.csv + append master
  python daily_scan.py --report            # read the series → print ranked shortlist (no network)
  python daily_scan.py --geos us,br        # override geos (default: us + one rotating emerging)
  python daily_scan.py --limit 100         # apps per chart (default 100)
  python daily_scan.py --date 2026-07-01   # override scan date (backfill/testing)
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(HERE, "..", "data"))
SCANS_DIR = os.path.join(DATA_DIR, "scans")
MASTER_CSV = os.path.join(DATA_DIR, "candidates.csv")
ALIASES_JSON = os.path.join(DATA_DIR, "aliases.json")

# Apple genre IDs we scan. "Casual" has no dedicated legacy-RSS id — it's captured
# via games-all (6014) and separated by mechanic tag. Idle/tycoon lives in Simulation.
GENRES = {"games": 6014, "puzzle": 7012, "arcade": 7003, "simulation": 7015}
FEEDS = {"free": "topfreeapplications",
         "grossing": "topgrossingapplications",
         "new": "newapplications"}
EMERGING_GEOS = ["br", "in", "ph", "id"]  # rotate weekly; US is always the anchor

# Mechanic taxonomy — MIRROR of references/mechanic-taxonomy.md. Keep the two in sync.
# Substring, case-insensitive, matched against (title + description).
TAXONOMY = {
    "sort": ["color sort", "water sort", "ball sort", "pin sort", "block sort",
             "nuts & bolts", "nuts and bolts", "unscrew", "screw", "bolt", "tidy",
             "declutter", "organize", "organise", "sort"],
    "unblock": ["unblock", "untangle", "tangle", "knot", "rope", "escape", "jam",
                "traffic", "parking", "pull the pin", "pull pin", "get them out",
                "get out", "extract"],
    "merge": ["merge", "combine", "fusion", "evolve", "2048"],
    "stack": ["block blast", "wood block", "woodoku", "tangram", "stack", "packing",
              "pack", "fill", "fit"],
    "idle": ["idle", "tycoon", "manager", "empire", "incremental", "prestige",
             "offline", "clicker", "tap"],
    "physics": ["pachinko", "plinko", "ricochet", "brick breaker", "breakout",
                "bounce", "aim", "drop", "ball", "physics"],
    "draw": ["coloring", "colouring", "sketch", "draw", "paint", "color", "colour",
             "fill", "line"],
    "crowd": ["runner", "crowd", "counting", "count", "army", "gate", "multiplier",
              "horde", "run"],
    "dig": ["excavate", "mining", "mine", "reveal", "scratch", "power wash",
            "powerwash", "wash", "clean", "dig", "sand"],
}

CSV_HEADER = ["scan_date", "geo", "chart", "category", "rank", "app_id", "title",
              "seller_name", "price", "avg_rating", "rating_count",
              "version_release_date", "first_seen_date", "mechanic_tags",
              "is_watchlist_publisher", "notes"]

UA = {"User-Agent": "games-researcher-daily-scan/1.0"}


# ---------------------------------------------------------------------------
# HTTP (polite: retries + throttle for Apple's ~20 req/min)
# ---------------------------------------------------------------------------
def fetch_json(url, tries=3):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise last


def fetch_chart(geo, feed, genre_id, limit):
    """Return [(rank, app_id)] for one geo/feed/genre chart."""
    url = (f"https://itunes.apple.com/{geo}/rss/{FEEDS[feed]}"
           f"/limit={limit}/genre={genre_id}/json")
    data = fetch_json(url)
    out = []
    for i, e in enumerate(data.get("feed", {}).get("entry", []), 1):
        app_id = e.get("id", {}).get("attributes", {}).get("im:id")
        if app_id:
            out.append((i, app_id))
    return out


def batch_lookup(ids, geo, chunk=100):
    """Return {app_id: metadata} via the Lookup API. Batched + throttled.

    rating_count is storefront-specific, so lookups are done per-geo.
    """
    meta = {}
    ids = list(dict.fromkeys(ids))  # de-dupe, preserve order
    for i in range(0, len(ids), chunk):
        batch = ids[i:i + chunk]
        q = urllib.parse.urlencode({"id": ",".join(batch), "country": geo})
        try:
            data = fetch_json(f"https://itunes.apple.com/lookup?{q}")
        except Exception as e:  # noqa: BLE001
            print(f"  ! lookup batch failed ({geo}): {e}", file=sys.stderr)
            continue
        for r in data.get("results", []):
            tid = str(r.get("trackId"))
            meta[tid] = r
        time.sleep(1.5)  # stay well under the throttle
    return meta


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------
def normalize(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def classify(title, description):
    hay = normalize(f"{title} {description}")
    tags = [fam for fam, kws in TAXONOMY.items()
            if any(kw in hay for kw in kws)]
    return tags


def load_alias_index():
    try:
        with open(ALIASES_JSON, encoding="utf-8") as f:
            raw = json.load(f)
    except (OSError, ValueError) as e:
        print(f"  ! could not read aliases.json ({e}) — Lane B disabled", file=sys.stderr)
        return []
    idx = []
    for canonical, aliases in raw.items():
        if canonical.startswith("_"):
            continue
        for a in aliases:
            idx.append((canonical, normalize(a)))
    return idx


def is_watchlist(seller, artist, alias_index):
    hay = f" {normalize(seller)} | {normalize(artist)} "
    return any(sub and sub in hay for _, sub in alias_index)


# ---------------------------------------------------------------------------
# Series I/O
# ---------------------------------------------------------------------------
def read_master():
    if not os.path.exists(MASTER_CSV):
        return []
    with open(MASTER_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def first_seen_map(rows):
    """{app_id: earliest scan_date str} across all history."""
    seen = {}
    for r in rows:
        aid, d = r["app_id"], r["scan_date"]
        if aid not in seen or d < seen[aid]:
            seen[aid] = d
    return seen


def pick_geos(arg):
    if arg:
        return [g.strip().lower() for g in arg.split(",") if g.strip()]
    week = dt.date.today().isocalendar()[1]
    return ["us", EMERGING_GEOS[week % len(EMERGING_GEOS)]]


# ---------------------------------------------------------------------------
# Scan (the default action)
# ---------------------------------------------------------------------------
def run_scan(scan_date, geos, limit):
    os.makedirs(SCANS_DIR, exist_ok=True)
    existing = read_master()
    fseen = first_seen_map(existing)
    alias_index = load_alias_index()

    rows = []
    for geo in geos:
        print(f"[{geo}] fetching charts…", file=sys.stderr)
        # (app_id -> set of (chart) it appears in, and its best rank / where)
        placements = {}  # app_id -> list of (chart, category, rank)
        for cat, gid in GENRES.items():
            for chart in FEEDS:
                try:
                    entries = fetch_chart(geo, chart, gid, limit)
                except Exception as e:  # noqa: BLE001
                    print(f"  ! {geo}/{chart}/{cat} failed: {e}", file=sys.stderr)
                    continue
                for rank, aid in entries:
                    placements.setdefault(aid, []).append((chart, cat, rank))
                time.sleep(0.3)

        ids = list(placements.keys())
        print(f"[{geo}] {len(ids)} unique apps → looking up metadata…", file=sys.stderr)
        meta = batch_lookup(ids, geo)

        for aid, places in placements.items():
            m = meta.get(aid)
            if not m:
                continue  # app pulled from lookup (region-locked/removed) — skip
            title = m.get("trackName") or ""
            seller = m.get("sellerName") or ""
            artist = m.get("artistName") or ""
            tags = classify(title, m.get("description") or "")
            watch = is_watchlist(seller, artist, alias_index)
            first_seen = min(fseen.get(aid, scan_date), scan_date)

            charts_here = {c for c, _, _ in places}
            note = []
            if "free" in charts_here and "grossing" not in charts_here:
                note.append("open-window")
            if watch and first_seen == scan_date:
                note.append("watchlist-new")

            for chart, cat, rank in places:
                rows.append({
                    "scan_date": scan_date,
                    "geo": geo,
                    "chart": chart,
                    "category": cat,
                    "rank": rank,
                    "app_id": aid,
                    "title": title,
                    "seller_name": seller,
                    "price": m.get("price"),
                    "avg_rating": m.get("averageUserRating"),
                    "rating_count": m.get("userRatingCount"),
                    "version_release_date": (m.get("currentVersionReleaseDate") or "")[:10],
                    "first_seen_date": first_seen,
                    "mechanic_tags": "|".join(tags),
                    "is_watchlist_publisher": str(watch).lower(),
                    "notes": ";".join(note),
                })

    # write the day's snapshot
    day_path = os.path.join(SCANS_DIR, f"{scan_date}.csv")
    with open(day_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_HEADER)
        w.writeheader()
        w.writerows(rows)

    # append to master, de-duped on (scan_date, geo, chart, category, app_id)
    key = lambda r: (r["scan_date"], r["geo"], r["chart"], r["category"], r["app_id"])
    kept = [r for r in existing if r["scan_date"] != scan_date or key(r) not in {key(x) for x in rows}]
    with open(MASTER_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_HEADER)
        w.writeheader()
        w.writerows(kept + rows)

    print(f"\n✓ {len(rows)} rows → {os.path.relpath(day_path)} and candidates.csv "
          f"({len(geos)} geos, {len(GENRES)} categories, {len(FEEDS)} charts)")
    print("  Next: python daily_scan.py --report")


# ---------------------------------------------------------------------------
# Report (read-time velocity — no network)
# ---------------------------------------------------------------------------
def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def build_series(rows):
    """(app_id, geo) -> {scan_date: {...}} collapsing charts within a day."""
    series = {}
    for r in rows:
        k = (r["app_id"], r["geo"])
        d = r["scan_date"]
        day = series.setdefault(k, {}).setdefault(d, {
            "rating_count": _f(r["rating_count"]),
            "best_rank": None, "charts": set(), "title": r["title"],
            "seller": r["seller_name"], "tags": r["mechanic_tags"],
            "watch": r["is_watchlist_publisher"] == "true",
            "first_seen": r["first_seen_date"],
        })
        day["charts"].add(r["chart"])
        rk = _f(r["rank"])
        if rk is not None and (day["best_rank"] is None or rk < day["best_rank"]):
            day["best_rank"] = rk
    return series


def _rc_at_or_before(days, target):
    """rating_count on the latest scan_date <= target."""
    best = None
    for d in sorted(days):
        if d <= target:
            best = days[d]
    return best


def run_report(top_n):
    rows = read_master()
    if not rows:
        print("No data yet. Run: python daily_scan.py", file=sys.stderr)
        sys.exit(1)
    series = build_series(rows)
    # first_seen is per app_id GLOBALLY (first day the ID appeared anywhere in our data).
    # Derive it from the full series here rather than trusting the stored column, so it's
    # correct even if scans ever ran out of date order.
    global_first_seen = first_seen_map(rows)
    latest = max(r["scan_date"] for r in rows)
    latest_d = dt.date.fromisoformat(latest)
    week_ago = (latest_d - dt.timedelta(days=7)).isoformat()

    cands, faded = [], []
    for (aid, geo), days in series.items():
        dates = sorted(days)
        last = dates[-1]
        cur = days[last]
        rc_now = cur["rating_count"]

        # deltas
        prev = days[dates[-2]] if len(dates) >= 2 else None
        d1 = (rc_now - prev["rating_count"]) if prev and rc_now is not None and prev["rating_count"] is not None else None
        ref7 = _rc_at_or_before(days, week_ago)
        d7 = (rc_now - ref7["rating_count"]) if ref7 and rc_now is not None and ref7["rating_count"] is not None else None
        rankd7 = (ref7["best_rank"] - cur["best_rank"]) if ref7 and ref7["best_rank"] and cur["best_rank"] else None

        first_seen = global_first_seen.get(aid, cur["first_seen"])
        dsfs = (dt.date.fromisoformat(last) - dt.date.fromisoformat(first_seen)).days
        open_window = ("free" in cur["charts"]) and ("grossing" not in cur["charts"])
        watch_new = cur["watch"] and first_seen == latest
        velocity = d7 if d7 is not None else ((d1 or 0) * 7)

        rec = {
            "aid": aid, "geo": geo, "title": cur["title"], "seller": cur["seller"],
            "tags": cur["tags"], "rc": rc_now, "d1": d1, "d7": d7, "rank": cur["best_rank"],
            "rankd7": rankd7, "dsfs": dsfs, "open": open_window, "watch": cur["watch"],
            "watch_new": watch_new, "velocity": velocity, "on_latest": last == latest,
        }

        # faded: was tracked recently, but fell off the latest scan OR velocity died
        if last != latest and last >= week_ago:
            faded.append(rec)
            continue

        # eligible = plausibly in-window OR a Lane-B new launch OR clearly rising
        eligible = (dsfs <= 45) or watch_new or open_window or (velocity and velocity > 0)
        if not eligible or not rec["on_latest"]:
            continue

        # pre-ranking heuristic (NOT the six-axis score — the agent re-ranks by judgment)
        score = velocity or 0
        if open_window:
            score *= 1.25
        if dsfs <= 45:
            score *= 1.15
        if watch_new:
            score += 500_000  # push pre-validated Lane-B launches to the top
        rec["score"] = score

        # lane label
        laneA = velocity and velocity > 0 or open_window
        if rec["watch"] and (open_window or (velocity and velocity > 0)):
            rec["lane"] = "A+B"
        elif rec["watch"]:
            rec["lane"] = "B"
        else:
            rec["lane"] = "A" if laneA else "-"
        cands.append(rec)

    cands.sort(key=lambda r: r["score"], reverse=True)

    def num(x, plus=False):
        if x is None:
            return "·"
        s = f"{int(x):+,}" if plus else f"{int(x):,}"
        return s

    print(f"\n# Daily candidate shortlist — as of {latest}")
    print(f"# ranked by a pre-heuristic (velocity × open-window × recency, +Lane-B new). "
          f"Re-rank with the six-axis model + calm-taste gate.\n")
    hdr = f"{'#':>2}  {'title':<26} {'geo':<3} {'tags':<16} {'seen':>4} {'ratings':>9} {'Δ1d':>8} {'Δ7d':>9} {'rank':>4} {'Δrk7':>5} {'open':>4} {'lane':>4}"
    print(hdr)
    print("-" * len(hdr))
    for i, r in enumerate(cands[:top_n], 1):
        print(f"{i:>2}. {r['title'][:25]:<26} {r['geo']:<3} {(r['tags'] or '-')[:15]:<16} "
              f"{r['dsfs']:>4} {num(r['rc']):>9} {num(r['d1'], True):>8} {num(r['d7'], True):>9} "
              f"{('#'+str(int(r['rank']))) if r['rank'] else '·':>4} {num(r['rankd7'], True):>5} "
              f"{'yes' if r['open'] else '·':>4} {r['lane']:>4}")

    if faded:
        print(f"\n# Faded / pruning candidates (were tracked ≤7d ago, off the latest scan):")
        for r in sorted(faded, key=lambda x: x["title"])[:10]:
            print(f"  - {r['title'][:40]} ({r['geo']}, {r['tags'] or 'untagged'}) "
                  f"— last ratings {num(r['rc'])}, dropped off charts")

    print(f"\n{len(cands)} eligible candidates from {len(series)} tracked (app,geo) series. "
          f"Data: {os.path.relpath(MASTER_CSV)}")


# ---------------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--report", action="store_true", help="read the series, print ranked shortlist (no network)")
    p.add_argument("--geos", help="comma list, e.g. us,br (default: us + one rotating emerging geo)")
    p.add_argument("--limit", type=int, default=100, help="apps per chart (default 100)")
    p.add_argument("--date", help="scan date YYYY-MM-DD (default today)")
    p.add_argument("--top", type=int, default=15, help="rows in --report shortlist")
    a = p.parse_args()

    if a.report:
        run_report(a.top)
        return

    scan_date = a.date or dt.date.today().isoformat()
    geos = pick_geos(a.geos)
    print(f"Scanning {scan_date} — geos={geos}, categories={list(GENRES)}, charts={list(FEEDS)}",
          file=sys.stderr)
    run_scan(scan_date, geos, a.limit)


if __name__ == "__main__":
    main()
