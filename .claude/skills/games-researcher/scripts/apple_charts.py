#!/usr/bin/env python3
"""Pull Apple App Store top charts for Games (free, no auth, no deps).

Uses the legacy iTunes RSS feeds, which — unlike the newer applemarketingtools
feed — support filtering by Games genre/subgenre. This is the cheapest leading
signal for trend scouting: read Top FREE for UA-driven risers, and note which
titles are NOT yet in Top GROSSING (a fresh hook still in its scaling phase).

Examples:
  python apple_charts.py --country us --feed free --limit 50
  python apple_charts.py --country br --feed free --genre 7003   # Action subgenre, Brazil
  python apple_charts.py --feed grossing --limit 25 --json > grossing.json

Watch emerging-market charts (br, in, ph, id) — hyper-casual breaks there first.
"""
import argparse
import json
import sys
import urllib.request

# Apple genre IDs. 6014 = Games (all). Common HC-relevant subgenres:
GENRES = {
    "games": 6014, "action": 7001, "adventure": 7002, "arcade": 7003,
    "board": 7004, "card": 7005, "casino": 7006, "casual": 7003,  # casual≈arcade slot
    "family": 7009, "music": 7011, "puzzle": 7012, "racing": 7013,
    "roleplaying": 7014, "simulation": 7015, "sports": 7016,
    "strategy": 7017, "trivia": 7018, "word": 7019,
}
FEEDS = {
    "free": "topfreeapplications",
    "paid": "toppaidapplications",
    "grossing": "topgrossingapplications",
    "new": "newapplications",
    "newfree": "newfreeapplications",
}


def fetch(country, feed, limit, genre):
    url = (f"https://itunes.apple.com/{country}/rss/{FEEDS[feed]}"
           f"/limit={limit}/genre={genre}/json")
    req = urllib.request.Request(url, headers={"User-Agent": "games-researcher/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    out = []
    for i, e in enumerate(data.get("feed", {}).get("entry", []), 1):
        out.append({
            "rank": i,
            "name": e.get("im:name", {}).get("label"),
            "developer": e.get("im:artist", {}).get("label"),
            "category": e.get("category", {}).get("attributes", {}).get("label"),
            "id": e.get("id", {}).get("attributes", {}).get("im:id"),
            "url": e.get("id", {}).get("label"),
            "release_date": e.get("im:releaseDate", {}).get("label"),
        })
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--country", default="us", help="ISO country code (us, br, in, ph, id...)")
    p.add_argument("--feed", default="free", choices=FEEDS, help="chart type")
    p.add_argument("--limit", type=int, default=50, help="number of apps (max ~200)")
    p.add_argument("--genre", default="games",
                   help="genre name or numeric id (default games=6014)")
    p.add_argument("--json", action="store_true", help="emit raw JSON")
    a = p.parse_args()

    genre = GENRES.get(str(a.genre).lower(), a.genre)
    try:
        rows = fetch(a.country, a.feed, a.limit, genre)
    except Exception as e:  # noqa: BLE001
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    if a.json:
        print(json.dumps(rows, indent=2))
        return
    print(f"# Apple App Store — top {a.feed}, genre={genre}, {a.country.upper()}")
    for r in rows:
        print(f"{r['rank']:>3}. {r['name']}  —  {r['developer']}  [{r['category']}]  id={r['id']}")


if __name__ == "__main__":
    main()
