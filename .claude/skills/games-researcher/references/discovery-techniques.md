# Discovery Techniques — Spotting Trends Before They Peak

How to detect an emerging hyper/hybrid-casual mechanic in its **moderate-competition
window** — proven enough to have CPI economics, not yet saturated by polished clones.

> **The one rule that ties it all together:** one publisher or one creative testing a
> mechanic = noise. The **same mechanic appearing across 3+ publishers / creatives
> within ~4-8 weeks, while CPI hasn't spiked and no polished version dominates the
> charts**, caught in test geos before US scale = a real emerging trend in its window.
> That convergence is the leading indicator. It maps exactly onto the "polished
> clone-plus of a moderate-competition trend" thesis.

> **Reframe (2026):** Pure hyper-casual is demoted, not dead — it's now the
> prototyping/UA-discovery layer that feeds **hybrid-casual** products (~1% of revenue
> but still drives the download charts). **Target a hyper-casual hook with a clear
> hybrid meta/monetization path designed in from day one.** A mechanic with no
> meta-layer headroom is a dead end.

## Signal hierarchy (most→least reliable as a *leading* indicator)

1. **Ad intelligence** (creative longevity + concentration) — leads charts by weeks.
2. **Publisher portfolio / soft-launch watching** — pre-screened concepts in test geos.
3. **App Store chart velocity** (Top Free risers not yet on Grossing).
4. **TikTok creative velocity** — fast but decays in days.
5. **Reddit / Discord / YouTube** — lagging, qualitative; confirmation not discovery.

---

## 1. Ad intelligence (the professional backbone)

Advertisers don't keep paying for ads that don't convert — money goes in *before*
installs/revenue show up, so ad signals lead the download charts by weeks.

**Signals, in order of reliability:**
1. **Creative longevity** (strongest single signal): an ad running **30+ days** is a
   validated winner (HC creatives normally refresh every 2-3 days). Read longevity at
   the *concept/angle* level, not a single video.
2. **Ad concentration:** multiple *different* publishers pushing the same mechanic =
   real trend with proven CPI economics → the moderate-competition window (3-5 in).
3. **Rising impressions** *(new Jan 2026)*: Meta Ad Library now attaches an
   **impression-range bucket** to every ad and lets you sort by it (<1K … 1M+). A
   "Low Impression Count" badge = a test (ignore); a creative climbing into 100K-1M+ =
   actively scaled.
4. **One concept fanned across many geos** = validated in test, now scaling globally.

**Tools (free → paid, solo-dev lens):**
- **Meta Ad Library** — FREE, no login: [facebook.com/ads/library](https://www.facebook.com/ads/library).
  The #1 free tool. Search a publisher page, sort oldest-first for longevity, filter by
  the new impression buckets. Has a free API (see `data-sources-and-apis.md`).
- **TikTok Creative Center → Top Ads** — FREE: filter Industry=Gaming, country, 7/30d.
  Cross-check the same hook on a second channel.
- **BigSpy** (free tier; Pro ~$99/mo), **AppGrowing Global** (~$57/mo, best China/Asia
  network coverage the free libraries miss), **AdSpy** ($149/mo, deep FB/IG).
- **SocialPeta / Sensor Tower / Apptica** — enterprise ($11k-150k/yr), overkill solo.

The **free stack covers ~80% of trend-scouting**; paid mainly adds spend estimates +
Asia coverage. Spend numbers are *modeled estimates* — use directionally.

---

## 2. Publisher portfolio & soft-launch watching (best leading indicator)

Every game that reaches a public soft launch already survived internal
CPI/marketability screening (Voodoo tests ~2,000 prototypes/yr, ships ~4 globally).
Watching their newest live releases lets you skip the prototyping graveyard.

**A brand-new app live ONLY in test geos (not US) = a game in test = your earliest
signal.** 2026 soft-launch geos by model:
- HC / ad-monetized → **Philippines, Indonesia** (very low CPI; English penetration).
- Hybrid / IAP → **Poland, Türkiye, Brazil**; puzzle → **Poland, Romania**.
- Retention/monetization reads → **Canada, Australia, New Zealand, Nordics** (US-like
  behavior). **Avoid US/UK for soft launch** (burns >50%-of-lifetime-revenue audience)
  and avoid cheap geos for *retention* reads (cheap installs skew the data).

**Monitoring (free-first):**
1. **mobilegamer.biz "Soft Launch Games You Need to Know About"** — recurring curated
   list sorted by publisher with test geos. Highest-ROI free resource.
2. **AppMagic** free Top Publishers chart + **soft-launch detector** + publisher pages.
   (⚠️ free tier being trimmed since Jan 2026 — see tooling note below.)
3. **App Store / Play developer pages** — bookmark each target publisher; check newest
   titles + which geos they're live in.
4. **Publisher "submit your game" pages** (Voodoo/Kwalee/CrazyLabs/Homa) — a public
   statement of *what mechanics they want now*.
5. **NextBigGames** monthly publisher ranking — re-baseline who's healthy.

**Healthy publishers to watch (mid-2026):** Rollic (#1), Voodoo, plus SayGames, Homa,
iKame, CrazyLabs, Azur, and newcomer "Arcade." **Do NOT watch Supersonic as a pipeline
signal** — Unity is selling the label and shut its ironSource ad network (Apr 2026);
use it for education only.

---

## 3. App Store chart signals

**Mental model:**
- **Top FREE = leading** (UA-driven volume). A game rocketing up Free = someone is
  pouring UA in *and the creative converts*. Read "what mechanic + creative acquires
  cheaply right now."
- **Top GROSSING = lagging** (monetization, takes weeks to tune). A title that
  dominates Free but is **absent from Grossing** = a fresh hook in its UA-scaling phase
  → study it now. When that studio's later titles hit Grossing, the genre is maturing
  (window closing).
- **Paid chart = irrelevant** for HC.

**Breakout-detection (replicable):**
| Metric | Definition | Breakout threshold |
|---|---|---|
| Growth Multiplier | (3-day install avg) ÷ (30-day baseline) | > 2.5× potential; 3×+ strong |
| Rank Velocity | chart-position change / 24h | ~200 positions in 48h is canonical |

High velocity at *mid-chart* is the strongest early tell — by #1 Free you're late.
Apply a **spike filter**: distinguish a sustained breakout from a one-day pop caused by
an editorial feature or a viral Reel.

**Free chart tools:** AppFigures (free Connect tier + free monthly "most downloaded"
reports; independent), AppMagic free Top Free/Grossing/Featured charts, Sensor Tower
free public Top Charts page + free monthly "Top 10 Worldwide Mobile Games" blog. See
`data-sources-and-apis.md` for the Apple RSS chart feeds you can pull programmatically.

**Watch emerging-market charts** (Brazil, India, Philippines, Indonesia) — HC breaks
there first. Apple's signal is degraded by the new algorithm-driven Apple Games app
(iOS 26, Jun 2025) — monitor competitors' **In-App Events** as the emerging proxy.

---

## 4. TikTok / short-form creative velocity

~59% of users discover games via short-form. Read **velocity, not volume** — a hook
*climbing steeply* (the second derivative), not one already plateaued.

- **TikTok Creative Center → Top Ads** (free): Industry=Gaming, last 7/30 days. Analyze
  15-20 ads/session; build a 50-100 ad swipe file over weeks.
- **Decay is brutal in 2026:** a TikTok creative loses ~50% effectiveness in **72
  hours** (was ~120h in 2024). The window from "spotted" to "saturated" is days-weeks.
- **Skeptic flag:** don't confuse a viral *sound* with a viral *mechanic*. Most
  "trending sound" coverage is music/lip-sync. Look for a rising sound/hashtag
  *attached to a gameplay format*.

**Confirmation surfaces (lagging, qualitative):** r/incremental_games (genuinely the
idle/merge early-adopter base + ~11k Discord), r/iosgaming, r/AndroidGaming; YouTube
Shorts/Gaming for which mechanics *travel* as shareable clips. A spike of "how do I
clone X" on r/gamedev = saturation warning.

---

## 5. Mechanic taxonomy & spotting a fresh twist

**Best framework — GameRefinery (Liftoff) CORE + META decomposition:** every game = a
CORE layer (primary gameplay) + a META layer (retention/progression). HC subgenres:
HC-Puzzle, HC-Tap, HC-Steer, HC-Swipe/Drag, HC-.io, HC-Other. Sensor Tower's Game
Taxonomy (built with Deconstructor of Fun) is the rigorous hierarchical alternative.

**Working vocabulary scouts use:** .io, idle, merge (merge-2), runner, ASMR/satisfying,
snowball/growing, parkour, sorting/organizing, stacking, drawing, swerve, tap/timing.

**Rising proven cores worth twisting (2025-26):** merge-2 (now mostly an *embedded
sub-system*), sorting/organizing (screw/cube/block jam), idle/tycoon × casino blends,
roguelite + idle-RPG mashups.

**How to spot a fresh twist (fits a solo first-timer):**
1. **Mix two proven loops** (Voodoo doctrine): "copying is fine if the design improves;
   the highest-leverage move is to mix two successful gameplays." Find a novel *pairing*.
2. **Swap the meta, keep the core** (GameRefinery): proven core + a meta layer borrowed
   from a genre it hasn't been paired with yet.
3. **Re-theme onto a fresh "oddly satisfying" visual** — same mechanic, more clip-able.
4. **Design the hybrid monetization path from day one** — no meta headroom = dead on arrival.

⚠️ **Don't copy the publisher volume model** (2,000 prototypes/yr) — that's anti-strategy
for a solo dev. Your edge is methods 1-3 (one deliberate bet) + the timing signals to
pick the *one* mechanic before the chart leaders arrive.

---

## 6. Timing — emerging vs saturated

**Window length:** old pure-HC was ~1-3 months emergence→saturation; hybrid-casual
retains players 60-90 days, so **windows are now quarters, not weeks** (~70% of the
2026 top-HC chart launched/scaled in 2025).

**Still EMERGING (room to enter):** subgenre showing month-over-month chart movement;
divergent outcomes among similar games (audience splitting → unserved niche); a
category indexing on one demographic (adjacent demographic underserved); **CPI still
low** in the genre.

**SATURATED (too late):** **CPI spike** (first warning — more advertisers bidding);
downloads up but revenue flat; revenue concentration (top-5 casual publishers already
take 62%); 5+ near-identical clones in the charts.

**For a first-timer the bigger risk is TOO LATE** — by the time you notice, clones may
already be saturating. Too early = no proven CPI benchmark, educating users on a
mechanic they don't want yet.

---

## A concrete weekly routine (free-first)

1. **Ad layer (leading):** Meta Ad Library sweep of Rollic/Voodoo/SayGames/Homa/
   CrazyLabs/Azur — flag creatives 30+ days old AND in 100K+ impression buckets.
   Cross-check on TikTok Creative Center.
2. **Pipeline layer:** read mobilegamer.biz soft-launch column; note any mechanic
   across 2+ publishers. Check target publishers' store pages for new titles + geos.
3. **Chart layer:** AppMagic free Top Free (US + Brazil/India/Philippines) +
   soft-launch detector; flag risers *not yet on Grossing*. Confirm UA-driven, not an
   editorial pop.
4. **Confirm the mechanic:** download and play risers — one-finger control? <30s to
   first "win"? obvious ad-break loop? Then ask the twist questions and whether a
   hybrid meta path exists.
5. **Monthly:** read the free reports (AppFigures, AppMagic casual, Sensor Tower Top-10,
   NextBigGames) to confirm a riser is part of a *category* trend, not a one-off.

**Trigger to act:** cross-publisher + cross-creative convergence on one mechanic, CPI
not yet spiked, no polished version dominating the charts.

---

## Skeptic's caveats (bake these in)

- **Most "how-to" content is vendor marketing.** The *methodologies* (rank velocity,
  free-vs-grossing, creative longevity, core/meta swap) are sound and cross-corroborated;
  specific *thresholds* and "we catch it 5 days early" claims are sales copy.
- **All third-party numbers are estimates** — downloads more reliable than revenue.
- **The space restructures fast** — the Sensor Tower/AppMagic acquisition, Supersonic
  sale, Apple Games app, and Meta impression buckets all happened in the last ~3-12
  months. Re-verify anything time-sensitive at decision time and log it in CHANGELOG.
