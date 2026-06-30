#!/usr/bin/env python3
"""Look up App Store app metadata via the free iTunes Search/Lookup API (no auth).

Use to profile a candidate or competitor: publisher, genres, rating count (a rough
popularity proxy), release/update dates, price, and description. Combine with
apple_charts.py to turn a chart name into full metadata.

Examples:
  python app_lookup.py --search "block blast" --limit 5
  python app_lookup.py --id 1635248994
  python app_lookup.py --bundle com.activision.callofduty.shooter --json
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

FIELDS = ["trackName", "artistName", "trackId", "bundleId", "primaryGenreName",
          "genres", "averageUserRating", "userRatingCount", "price", "formattedPrice",
          "releaseDate", "currentVersionReleaseDate", "version", "sellerName",
          "trackViewUrl", "description"]


def call(url):
    req = urllib.request.Request(url, headers={"User-Agent": "games-researcher/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--search", help="search term")
    g.add_argument("--id", help="numeric track id")
    g.add_argument("--bundle", help="bundle id, e.g. com.foo.bar")
    p.add_argument("--country", default="us")
    p.add_argument("--limit", type=int, default=5, help="search result count")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    if a.search:
        q = urllib.parse.urlencode({"term": a.search, "country": a.country,
                                    "entity": "software", "limit": a.limit})
        url = f"https://itunes.apple.com/search?{q}"
    elif a.id:
        url = f"https://itunes.apple.com/lookup?id={a.id}&country={a.country}"
    else:
        url = f"https://itunes.apple.com/lookup?bundleId={a.bundle}&country={a.country}"

    try:
        data = call(url)
    except Exception as e:  # noqa: BLE001
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

    results = data.get("results", [])
    if a.json:
        print(json.dumps([{k: r.get(k) for k in FIELDS} for r in results], indent=2))
        return
    if not results:
        print("no results", file=sys.stderr)
        sys.exit(1)
    for r in results:
        print(f"\n{r.get('trackName')}  —  {r.get('artistName')}")
        print(f"  genre: {r.get('primaryGenreName')}  | ratings: {r.get('userRatingCount')}"
              f" (avg {r.get('averageUserRating')})  | {r.get('formattedPrice')}")
        print(f"  updated: {(r.get('currentVersionReleaseDate') or '')[:10]}"
              f"  | released: {(r.get('releaseDate') or '')[:10]}  | id={r.get('trackId')}")
        print(f"  {r.get('trackViewUrl')}")


if __name__ == "__main__":
    main()
