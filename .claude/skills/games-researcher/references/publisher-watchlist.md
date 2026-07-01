# Publisher Watchlist — Lane B (High-Precision, Pre-Validated)

**The Lane B thesis:** a publisher only launches a title that already cleared its internal
soft-launch gates (D1/D7 retention, CPI, marketability). So a **brand-new app ID from a
watchlist publisher** is *pre-validated proof the mechanic has legs* — the highest-precision
signal we get for free. It tells us which mechanic **families** are hot right now. Lane A
(the taxonomy scan) then tells us where inside those families the window is still open.

`scripts/daily_scan.py` sets `is_watchlist_publisher = true` on any charting app whose
`sellerName` **or** `artistName` matches this list (via the alias map). A watchlist app we
have **never seen before** (`days_since_first_seen == 0`) is the high-priority Lane B flag.

## The watchlist

Voodoo, Rollic (Zynga), Homa, Supersonic (AppLovin), Lion Studios, CrazyLabs, Kwalee,
SayGames, Grand Games, Beresnev Games, Azur Games, TapNation, Popcore, Green Panda,
Yso Corp, Kayac.

## Matching is not exact — maintain the alias map

The Lookup API returns two name fields and they **diverge from the brand name**, often wildly:

- `sellerName` = the **legal entity** (e.g. `GRAND GAMES OYUN VE YAZILIM ANONIM SIRKETI`,
  `OAKEVER GAMES PTE. LTD.`).
- `artistName` = the **display name** (e.g. `Grand Games`, `Oakever Games`).

So a plain equality match on "Grand Games" **misses its own titles that are charting right
now**. The script normalizes (lowercase, strip punctuation/legal suffixes) and does a
**substring match** of each alias against both name fields. Aliases live in
`data/aliases.json` — a `{ "Canonical Publisher": ["alias", "legal entity fragment", ...] }`
map. Extend it whenever you spot a watchlist publisher charting under a name the matcher
missed (and log it in `CHANGELOG.md`).

Seed aliases (in `data/aliases.json`):
- **Rollic** → rollic, rollic games (Zynga-owned)
- **Supersonic** → supersonic, supersonic studios (AppLovin; note: the *ironSource ad
  network* shut Apr 2026 — the game label still ships, keep watching it as a *pipeline*
  signal even though it's dead as an ad-network signal)
- **Grand Games** → grand games, grand games oyun (legal entity is Turkish: "…OYUN VE
  YAZILIM ANONIM SIRKETI")
- **Homa** → homa, homa games
- **Voodoo** → voodoo
- **CrazyLabs** → crazylabs, crazy labs
- **Kwalee** → kwalee
- **SayGames** → saygames, say games
- **Lion Studios** → lion studios, lion studios plus
- **Azur Games** → azur, azur games, azur interactive
- **Beresnev Games** → beresnev
- **TapNation** → tapnation, tap nation
- **Popcore** → popcore
- **Green Panda** → green panda
- **Yso Corp** → yso, yso corp
- **Kayac** → kayac

## Caveats (bake these in)

- **Publishers relabel and use shell/vendor entities.** Some titles ship under a
  sub-studio or a work-for-hire developer's `sellerName` while the publisher is only named
  in the description. If a title *looks* watchlist-quality but the matcher didn't flag it,
  read the description for "published by …" and add the alias.
- **A watchlist match is precision, not gospel.** Publishers also ship duds and re-skins.
  The flag raises priority; it doesn't replace the six-axis scoring or the calm-taste gate.
- **Keep the list current.** Publisher health changes fast (see `discovery-techniques.md`
  §2 — Rollic #1 mid-2026; Supersonic label being sold). Re-baseline every few weeks off
  mobilegamer.biz / NextBigGames and prune/add here.
