# Ad Monetization

Designing ads that earn without killing retention — the primary revenue source for a
hybrid-casual v1. Pair with `monetization-models.md` (the hybrid model) and
`design-to-metrics.md`.

> **For a solo hybrid-casual v1, your money is in ads, not IAP.** Block Blast earns
> ~$17.5M/mo from ads vs ~$66K *lifetime* IAP. Build a clean ad stack first; add IAP only
> once a meta layer exists. The "45% IAP / 55% ads" split is a *destination after you add a
> meta*, not a launch assumption.

## Mediation first (the one non-negotiable)
Use **one mediation SDK** (AppLovin MAX, ironSource/Unity LevelPlay, or AdMob) so multiple
networks bid for each impression. **Do not hand-roll network integrations** — it burns
weeks and underperforms single-network eCPM. This is plumbing, not design, and it's your
single most important monetization decision.

## eCPM hierarchy (US tier-1, 2025-2026 — order-of-magnitude, verify on your dashboard)

| Format | eCPM | Role |
|---|---|---|
| **Rewarded video** | **$15-20** (up to $40 premium) | Highest eCPM + least intrusive (opt-in). Your #1 lever. ~62% of mobile-game ad revenue. |
| **Interstitial** | $6-14 | Monetizes the silent majority at level transitions. Cap it. |
| **Banner** | <$2 | Always-on floor. Optional; run on menus to protect feel. |

## Rewarded video — design (your primary lever)

**Highest-converting placements (puzzle/sort), in priority order:**
1. **Continue / Revive after a fail** — strongest motivator (alternative = losing
   progress). Block Blast uses *only* this, capped ~1/session. **Build this first.**
2. **Double / multiply end-of-level rewards** ("2× coins" on win screen) — often >70%
   opt-in.
3. **Free coins / booster** from a shop button.
4. **Chest / daily-reward unlock or boost** — drives DAU + ad revenue together.
5. **Free spin / wheel** (only if you add a meta).

**Rules:**
- **Always opt-in, always framed as a player benefit** ("Watch to revive" / "Double your
  coins") — never forced. ~87% of players view rewarded positively; 80-90% completion.
- **Frequency-cap and audit monthly** — over-serving erodes perceived value *and*
  cannibalizes IAP. Cap revive ~1/session. Solo starting point: **~3-4 rewarded views per
  user per day**, then tune.
- **Design rewarded as acceleration, not the terminal reward** — an ad gets one extra life;
  a purchase gets a stack. The ad *teaches value*; the purchase *satisfies impatience*.

## Interstitial — tuning

Lives at level-transition screens; monetizes players who never opt into rewarded and never
pay. **Frequency is genre-dependent, not universal:**
- **Start at ~1/session**, watch D7 for 2 weeks, then step toward 2/session "where
  retention and monetization grow together." Solo heuristic: ~5-7/user/day total, or every
  ~2 levels — but **test**.
- Diminishing returns hit hard after the 5th-6th interstitial in a session.
- **Always use a first-ad delay** (no interstitial until after level 1-2): buys **+5-8% D1
  retention** at negligible revenue cost.
- **Retention tradeoff is genre-specific:** a hypercasual puzzle showing an interstitial
  after *every* level saw +34% revenue with minimal churn; the same pacing in a simulation
  game cost -18% D7. **Short-session puzzles tolerate frequent interstitials far better** —
  you can be relatively aggressive. The old "3-minute rule" is dead; pace by *natural break
  points*, not a timer.

## Segmentation (the hybrid rule)
**Suppress interstitials + banners for payers** (anyone who bought Remove Ads or any IAP);
the first IAP self-sorts them. Monetize non-payers/ad-watchers with rewarded + capped
interstitial. Energy/lives gates are the cleanest way to create rewarded-ad moments
without bespoke events.

## Solo v1 ad stack (do all, nothing more)
1. **Mediation SDK** (one).
2. **Rewarded: Continue/Revive** (opt-in, ~1/session).
3. **Interstitial at level transitions** with first-ad delay, ~1/session.
4. Later (Tier 2): rewarded **2× rewards** on win screen; optional banner.

## Sources
Gamigion ad-mon benchmark 2025 · Tenjin 2025/2026 · GameRefinery (rewarded placements) ·
Udonis (Block Blast, 16 rewarded placements) · AdReact (interstitial best practices 2025) ·
Airflux (death of the 3-minute rule) · Infatica (2025) · Balancy (Block Blast
deconstruction). Full URLs in CHANGELOG notes.
