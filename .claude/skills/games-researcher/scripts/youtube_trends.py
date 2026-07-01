#!/usr/bin/env python3
"""Detect rising game interest via YouTube view-velocity on a keyword watchlist.

Free — YouTube Data API v3 needs only an API key (no OAuth). Quota is 10,000 units/day:
each keyword costs 100 (search.list) + 1 (videos.list) = 101 units, so ~90 keywords/day.

For each keyword it pulls the most-viewed recent videos (default: last 45 days), hydrates
their view counts, and reports a VELOCITY score = median(views / age-in-days) across those
videos — a proxy for how fast public interest in that mechanic is accelerating right now.
Compare keywords against each other, and re-run weekly to watch a term break out.

Key resolution (per repo convention): env YOUTUBE_API_KEY first, else the nearest
`.keys.local` walking up from this script to the repo root (scope file wins over root).

Examples:
  python youtube_trends.py                          # default arrow/sort watchlist
  python youtube_trends.py --keywords "arrow puzzle game" "color sort puzzle"
  python youtube_trends.py --days 30 --per-keyword 15 --json
"""
import argparse
import json
import os
import statistics
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://www.googleapis.com/youtube/v3"
KEY_NAME = "YOUTUBE_API_KEY"

# Default watchlist — the mechanics this project is scouting. Edit freely.
DEFAULT_KEYWORDS = [
    "arrow puzzle game",
    "arrows puzzle escape",
    "color sort puzzle",
    "block sort puzzle",
    "traffic jam puzzle game",
    "pin pull puzzle",
]


def load_key():
    """env var, else nearest .keys.local walking up to filesystem root (scope wins)."""
    if os.environ.get(KEY_NAME):
        return os.environ[KEY_NAME]
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        path = os.path.join(d, ".keys.local")
        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#") or "=" not in line:
                        continue
                    k, _, v = line.partition("=")
                    if k.strip() == KEY_NAME and v.strip():
                        return v.strip()
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def call(path, params):
    url = f"{API}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "games-researcher/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def velocity_for(keyword, key, days, per_keyword):
    published_after = (datetime.now(timezone.utc) - timedelta(days=days)).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    search = call("search", {
        "key": key, "part": "snippet", "q": keyword, "type": "video",
        "order": "viewCount", "publishedAfter": published_after,
        "maxResults": per_keyword, "relevanceLanguage": "en",
    })
    ids = [it["id"]["videoId"] for it in search.get("items", [])
           if it.get("id", {}).get("videoId")]
    if not ids:
        return {"keyword": keyword, "videos": 0, "velocity": 0.0, "total_views": 0}
    vids = call("videos", {"key": key, "part": "statistics,snippet", "id": ",".join(ids)})
    now = datetime.now(timezone.utc)
    per_day, total = [], 0
    top = None
    for v in vids.get("items", []):
        views = int(v.get("statistics", {}).get("viewCount", 0))
        published = datetime.fromisoformat(
            v["snippet"]["publishedAt"].replace("Z", "+00:00"))
        age_days = max((now - published).total_seconds() / 86400, 0.5)
        vpd = views / age_days
        per_day.append(vpd)
        total += views
        if top is None or views > top[1]:
            top = (v["snippet"]["title"], views, round(vpd))
    return {
        "keyword": keyword, "videos": len(per_day),
        "velocity": round(statistics.median(per_day)) if per_day else 0,
        "total_views": total,
        "top_video": {"title": top[0], "views": top[1], "views_per_day": top[2]} if top else None,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--keywords", nargs="+", help="override the default watchlist")
    p.add_argument("--days", type=int, default=45, help="recency window (default 45)")
    p.add_argument("--per-keyword", type=int, default=20,
                   help="videos to sample per keyword (max 50, default 20)")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    key = load_key()
    if not key:
        print(f"error: no {KEY_NAME} found (env or .keys.local). Add a free Google Cloud "
              f"API key with YouTube Data API v3 enabled.", file=sys.stderr)
        sys.exit(2)

    keywords = a.keywords or DEFAULT_KEYWORDS
    rows = []
    for kw in keywords:
        try:
            rows.append(velocity_for(kw, key, a.days, min(a.per_keyword, 50)))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            print(f"error on '{kw}': HTTP {e.code} — {body}", file=sys.stderr)
            if e.code in (400, 403):  # bad key / quota / API not enabled — stop early
                sys.exit(1)
        except Exception as e:  # noqa: BLE001
            print(f"error on '{kw}': {e}", file=sys.stderr)

    rows.sort(key=lambda r: r["velocity"], reverse=True)
    if a.json:
        print(json.dumps(rows, indent=2))
        return
    print(f"# YouTube interest velocity — last {a.days}d — "
          f"{datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    print(f"# velocity = median views/day across top ~{a.per_keyword} recent videos\n")
    for r in rows:
        print(f"{r['velocity']:>10,}  vel   {r['keyword']}   "
              f"({r['videos']} vids, {r['total_views']:,} total views)")
        if r.get("top_video"):
            t = r["top_video"]
            print(f"{'':>10}         ↳ top: {t['title'][:60]}  "
                  f"({t['views']:,} views, {t['views_per_day']:,}/day)")


if __name__ == "__main__":
    main()
