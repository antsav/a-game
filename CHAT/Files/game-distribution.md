# game-distribution — Launch, ASO & go-to-market (iOS)

**Purpose:** how to **distribute, launch, and grow** a game on the iOS App Store — the layer
*after* "is the concept good?" and "is it built?" Calibrated to a **solo, iOS-first,
hybrid-casual dev with no UA budget.**

**Use this lens for:** the launch checklist/phases, TestFlight & soft-launch strategy (which
geos, what to measure), App Store submission / App Review / rejection / privacy (App Privacy
labels, privacy manifests, ATT) / age rating, ASO, getting **featured by Apple**, phased
release, post-launch live-ops — and the **publisher-vs-self-publish** decision.

## The core stance (read once)
- **No UA budget → organic-first, always.** Paid UA is a *publisher's* game or a late
  amplifier — never the solo dev's primary engine. Sequence everything for organic reach:
  **short-form video + ASO + Apple featuring.**
- **The single biggest free lever is Apple editorial featuring** — and a calm, design-forward,
  well-being-adjacent puzzle is *unusually well-suited* to it. Treat the **featuring
  nomination as a first-class launch task** (you nominate ~3+ weeks ahead via App Store
  Connect), not an afterthought.
- **Marketability is a pre-build property.** If the core loop isn't legible + satisfying in a
  **6-second clip**, organic growth is impossible — this is a gate *before* heavy build.
- **Guard against launch scope creep.** A solo dev does the lean subset and explicitly skips
  the rest until there's traffic (see below).

## The lean solo launch (do this subset; skip the rest for v1)
**Do:** internal TestFlight → small soft launch (a cheap US-like geo: CA / AU / NZ) → manual
App Store release + **featuring nomination** + a steady clip habit (7–14 short-form/week).
**Skip until there's traffic:** PPO/CPP A/B tests, full localization, heavy live-ops, paid UA.

## The pipeline (stages)
1. **Pre-submission:** App Store Connect setup, privacy manifest + App Privacy labels, ATT
   decision (needed for ad attribution), age rating questionnaire, metadata + ASO assets.
2. **TestFlight:** internal → small external, shake out crashes and the FTUE.
3. **Soft launch:** limited geo; measure retention before any scale. (Gates below.)
4. **Submission & review:** watch the tightened **Guideline 4.3 anti-clone** rule —
   directly relevant to a "clone-plus": the differentiation must be *real*. Also SDK
   minimums, privacy, age rating (all shifted 2025–2026).
5. **Release:** manual or phased (7-day % rollout); time it to a featuring nomination.
6. **Post-launch:** light live-ops cadence *only* once retention holds.

## Metrics — the go/kill gates (organic read, free)
- **Retention:** D1 ≥ ~38–40%, **D7 ≥ ~12–15%** (hybrid target D7 ~20%); **D7 < 10% = core
  loop broken, do not scale.**
- Cohort analysis, stickiness (DAU/MAU), ARPDAU, LTV, ROAS — these are a **scale-decision
  gate** here (the raw benchmark tables live in `games-researcher`).

## Publisher vs self-publish
- **A publisher's one irreplaceable function is CAPITAL** — fronting paid UA and absorbing
  the **45–60 day ad-network payout lag** — *not* "expertise." Frame the decision around
  that, honestly, including what you give up (revenue share, control, marketability pressure
  that can push the game toward urgency and betray the calm feel).
- Roster: Voodoo, Homa, Rollic, Supersonic, CrazyLabs, Kwalee, SayGames. They want proof —
  CPI, D1/D7 retention, LTV, ROAS from a testable prototype (usually via their SDK).
- **Two paths:** submit a prototype pre-launch (they fund UA) **or** prove-then-pitch
  (self-publish, prove retention organically, pitch from strength). For a first game with a
  calm/organic thesis, prove-then-pitch keeps control; a publisher only makes sense if
  scaling needs capital you don't have.

## Organic GTM
Channels: TikTok / Reels / Shorts (primary), Reddit, Discord. Creatives for ~$0 = the
satisfying core loop clipped tight. Community + pre-launch audience; PR/influencers as
amplifiers; featuring as the big free spike. Build the **clip habit early** — it's the
engine.

## Boundary — what this is NOT
Not the *technical* build/export/signing/TestFlight-wiring mechanics (→ `unity-3d`), not the
economy/ads/IAP *design* (→ `game-monetizer`), not *what to build* (→ `games-researcher`).
This owns the **strategic pipeline**: what phase, which geos, when to submit, how to get
featured.

> Apple's rules (age ratings, SDK minimums, privacy, 4.3 anti-clone) move fast — treat any
> specific rule/number here as **possibly stale** and verify live before a real launch.
