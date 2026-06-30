# Monetization Models

The revenue structures: IAP types, ad formats, the hybrid model, and battle
pass/subscriptions. Pair with `economy-design.md` (the currency/economy that these sell)
and `ad-monetization.md` (ad placement detail).

## IAP taxonomy

| Type | What | When it fits | Examples |
|---|---|---|---|
| **Consumable** | Used up, re-buyable — the F2P revenue workhorse | Needs a recurring sink | Currency packs, energy refills, gacha pulls, continues |
| **Non-consumable / durable** | Bought once, owned forever | Low-friction first purchase | **Remove Ads ($2.99-4.99)**, permanent unlocks, cosmetics |
| **Subscription** | Auto-renewing (weekly/monthly) | Stickiest revenue, highest compliance overhead | VIP, "double coins forever", monthly card |
| **Battle/Season Pass** | Time-boxed tiered reward track | Repeatable loop + meta progression | See below |

**Modern stacking (2025-2026):** top casual games layer all of these by
friction/commitment: **Remove Ads** (cheapest, durable, first purchase) → **starter
bundle** (anchored discount) → **currency packs** (recurring) → **battle pass**
(monthly) → **VIP subscription** (highest commitment). 2025 trend: customizable IAP
bundles (player picks contents) migrating from midcore into casual.

**Solo-dev order:** ship **Remove Ads + one currency-pack ladder** first. Battle pass
only once a meta loop is worth grinding. Subscriptions add Apple compliance/refund/churn
complexity — defer to v2.

## Ad formats & eCPM hierarchy

eCPM = revenue per 1,000 impressions. Numbers are **order-of-magnitude (2024-2026), swing
hard by quarter/geo/network** — verify against your own mediation dashboard.

| Format | Placement | Rough eCPM (Tier-1 / global) | Notes |
|---|---|---|---|
| **Rewarded video** | Player opts in for a reward | $15-30 / $8-18 (US iOS ~$20-30) | Highest eCPM *and* least intrusive. The cornerstone of hybrid; also advertises IAP. |
| **Interstitial** | Full-screen at natural breaks | $5-8 / $2.50-5 (US ~$14-19) | Second-highest. **Cap frequency** (e.g. every 2-3 levels, 30-60s floor) or you wreck retention. |
| **Playable** | Interactive mini-ad | High | Mostly a UA creative format, not a solo monetization slot. |
| **Offerwall** | Menu of tasks for rewards | Variable | Niche; needs a deep economy. |
| **Banner** | Persistent strip | $0.50-1.50 / $0.20-0.80 | Lowest; always-on. Run on menus only, or skip to protect feel. |

Use a **mediation layer** (AppLovin MAX, ironSource/LevelPlay, AdMob) so networks bid —
single-network eCPM leaves money on the table. Detail in `ad-monetization.md`.

## Hybrid monetization (the dominant 2025-2026 model)

~72% of devs now combine streams. Hybrid drives ~28% higher ARPU than ad-only
(hypercasual); for Android midcore, ~146% ROAS by D90 vs 93% IAP-only vs 58% ads-only.
Hybrid-casual pulls ~40-50% of revenue from IAP, rest ads.

**The cannibalization problem & the fix — segment by behavior, don't show everyone
everything:**
1. Spend is brutally concentrated (~2-5% pay; whales+dolphins carry IAP; the 85-90%
   minnows/non-payers are monetized by ads).
2. **Detected/likely payers** → suppress interstitials + banners, push IAP/bundles/pass.
   **Ad-watchers/non-payers** → monetize with rewarded + capped interstitial.
   **The first IAP (Remove Ads) self-sorts players** and flags them as payers to target.
3. **Don't let rewarded ads substitute for IAP** — design rewarded to give
   convenience/acceleration (one extra life), not the terminal reward (a stack). The ad
   *teaches value*; the purchase *satisfies impatience*.

**The one-rule playbook:** build two paths from day one — an ad-supported free path and
an IAP path that removes ads + accelerates. Tag a user "payer" on first purchase and
mute their ads.

## Battle pass / subscription design

Battle passes are the dominant recurring mechanic (in ~60% of top-20%-grossing games).

**Structure:** two tracks — **Free** (baseline, for everyone) + **Premium** (paid,
richer). Tiers unlock via XP/playtime/missions. **Monthly reset.** Basic tier **$5-15**
(keep low → repeat purchases). Good passes deliver **10-20× reward value vs cost** — the
"this much for so little?!" hook.

**Why dominant:** recurring revenue without aggressive pressure; a retention engine
(quests push players across modes); perceived fairness (effort-based, far less backlash
than loot boxes/P2W); broad appeal (converts mid-spenders, not just whales).

**Completion psychology:** all FOMO — fear of losing grinded rewards at expiry, of
wasting time, of missing exclusive cosmetics, plus per-tier achievement dopamine.

**⚠️ Cannibalization warning:** *Clash Royale* added a pass **without** deepening
spending → revenue *dropped*. *Clash of Clans* added progression layers **first**, then
the pass. **Rule: add monetization depth before/with the pass, never bolt a pass onto a
shallow economy.** Make the free track genuinely good — it's what makes premium feel worth it.

**Subscription price points:** monthly card $4.99-9.99 (daily currency drip + perks,
tuned so the drip slightly exceeds the price's worth → feels free to keep); VIP up to
~$29.99/mo (casino/RPG). iOS auto-renewing subs need StoreKit + App Review scrutiny.

**Solo-dev:** don't ship a pass at launch — needs (a) a repeatable loop, (b) a meta
economy with real sinks, (c) enough content for a meaningful track. Defer subs to v2.

## Sources
Liftoff 2025 Casual Report · CAS.ai hybrid guide (Oct 2025) · AppSamurai hybrid LTV
(Nov 2025) · Gamigion hybridcasual (Jun 2025) · Tenjin ad-mon 2025/2026 · DoF Battle
Passes (Jun 2022) · GameRefinery battle-pass / IAP mechanics. Full URLs in CHANGELOG notes.
