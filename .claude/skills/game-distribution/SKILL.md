---
name: game-distribution
description: >-
  Guide how to DISTRIBUTE, LAUNCH, and GO-TO-MARKET a mobile game on the iOS App Store —
  the steps and phases from "build is done" to "live and growing," calibrated to a solo
  iOS hybrid-casual developer with no UA budget. Use this whenever the user asks how to
  ship/launch/release a game, the launch checklist or phases, TestFlight/beta/soft-launch
  strategy and which geos, App Store submission / App Review / rejection / privacy
  (App Privacy labels, privacy manifests, ATT) / age rating, App Store Optimization (ASO:
  keywords, icon, screenshots, preview video, ratings, localization, A/B testing), getting
  featured by Apple, phased release, post-launch live-ops cadence — AND the publisher
  question: whether to use a publisher (Voodoo, Homa, Rollic, Supersonic, CrazyLabs,
  Kwalee, SayGames) vs self-publish, what publishers do, revenue share / commission /
  recoupment, how to pitch/submit a prototype, what metrics they require (CPI, D1/D7
  retention, cohort analysis, stickiness, ARPDAU, LTV, ROAS) — AND marketing / GTM for a
  first game (organic TikTok/Reels/Shorts, creatives, community, PR, influencers, the
  launch sequence). Trigger it for any question about getting a finished (or near-finished)
  game in front of users, growing it, or deciding publisher-vs-solo — even when the word
  "distribution" isn't used.
---

# Game Distribution

Guide the **distribution, launch, and go-to-market** of a mobile game on the iOS App Store —
**calibrated to a solo, iOS-first, hybrid-casual developer on a tiny/zero UA budget** (zero
gamedev experience, validate-before-build philosophy, building a calm single-player puzzle
with an idle/clicker pull). This is the layer *after* "is the concept good?" and "is it built?":
how it gets to players, how it grows, and whether a publisher should carry it.

Give concrete, sequenced, ship-oriented answers — what to do, in what order, with the numbers
and the why. Push back on over-engineering the launch (a known risk for this user) and on any
distribution choice that betrays the calm/no-pressure feel of the game.

## Where this sits among the other skills (don't duplicate them)

- **`games-researcher`** — picking/validating the concept *before* building. Owns the
  CPI/CTR/IPM/retention *validation benchmarks* and the stage-gate funnel. This skill
  **references those numbers, doesn't restate them** — pull benchmarks from there.
- **`game-monetizer`** — designing the economy, ads, IAP, offers, LiveOps that make players
  spend. Distribution decides *how the game reaches players and scales*; monetizer decides
  *how it earns per player*. ARPDAU/LTV live in both — here they're a **scale-decision gate**,
  there they're a **design target**.
- **`unity-3d`** — owns the *technical* iOS build/export/signing/TestFlight/Fastlane mechanics
  (Xcode export, IL2CPP, privacy manifest wiring). This skill owns the *strategic* pipeline
  (what phase, which geos, when to submit, how to get featured). When the question is "how do
  I wire the build," defer to `unity-3d`; when it's "what's my launch sequence," answer here.
- **`my-game-preference`** — the taste north-star. Check distribution/marketing choices against
  it: the marketability and ASO angle must not push the game toward urgency/pressure framing.

## Who this is for (calibrate every recommendation)

- **No UA budget → organic-first, always.** Paid UA (CPI/ROAS) is a *publisher's* game or a
  later amplifier — never the solo dev's primary engine. Score and sequence everything for
  organic reach (short-form video + ASO + Apple featuring).
- **The single biggest free lever is Apple editorial featuring**, and a calm, design-forward,
  well-being-adjacent puzzle is *unusually well-suited* to it. Treat the featuring nomination
  as a first-class launch task, not an afterthought.
- **Marketability is a pre-build property, not a launch-time bolt-on.** If the core loop isn't
  legible and satisfying in a 6-second clip, organic growth is impossible — flag this *before*
  heavy build (it's also a `games-researcher` gate).
- **The publisher's one irreplaceable function is capital** (fronting paid UA and absorbing the
  45–60 day ad-network payout lag) — not "expertise." Frame the publisher decision around that,
  honestly, including what you give up.
- **Guard against scope creep in the launch itself** — a solo dev should do a lean subset
  (internal TestFlight → small soft launch → manual release + featuring nomination) and
  explicitly *skip* PPO/CPP A/B tests, full localization, and heavy live-ops until there's
  traffic. Call these out.
- **Apple's rules move fast** — age ratings, SDK minimums, privacy, and Guideline 4.3
  (anti-clone) all changed in 2025–2026. Treat any specific rule in the references as
  *possibly stale* and verify live for time-sensitive launches.

## How this skill is organized

`references/` is the textbook — five files, read the ones a question needs (don't recite blindly):

- **`launch-pipeline.md`** — the end-to-end iOS phases: pre-submission setup, TestFlight,
  soft launch (which geos, what to measure), App Store submission & review (privacy, ATT,
  age rating, rejection reasons incl. the tightened anti-clone 4.3), launch timing & phased
  release, Apple featuring, post-launch live-ops. **The "what are the steps/phases" answer.**
- **`aso.md`** — App Store Optimization: keywords, icon/screenshots/preview video, ratings &
  reviews, localization-to-rank, PPO vs CPP A/B testing. The free, always-on conversion layer.
- **`publishers.md`** — publisher vs self-publish: what a publisher does, why (capital/cash-flow),
  the hyper/hybrid-casual roster, revenue share & recoupment mechanics, the SDK pitch/submission
  process, the two strategic paths (submit prototype pre-launch vs prove-then-pitch). **The
  "do I need a publisher and how does it work" answer.**
- **`launch-metrics.md`** — the go/kill gates that decide soft-launch→scale and what publishers
  require: retention (D1/D7/D30), cohort analysis & LTV *explained plainly*, stickiness, ROAS,
  and how a no-budget solo dev reads these organically for free. Cross-references
  `games-researcher` for the raw benchmark tables.
- **`gtm-and-marketing.md`** — organic-first go-to-market: the marketability gate, channels
  (TikTok/Reels/Shorts/Reddit/Discord) and current 2026 reach reality, creatives for ~$0,
  community/pre-launch, PR/influencers/featuring, and the week-by-week launch sequence.

## Workflow for answering a distribution / launch / GTM question

1. **Locate the stage.** Pre-build (marketability gate) vs built-not-launched (pipeline + ASO)
   vs soft-launched (metrics → scale-or-kill, publisher decision) vs live (live-ops + growth).
   Answer to *that* stage — a pre-retention game shouldn't be pitching publishers or buying UA.
2. **Pull the right reference(s)** and synthesize into a sequenced, concrete recommendation —
   not a recital. Name the geos, the gate numbers, the order of operations.
3. **Calibrate to solo / iOS / no-budget:**
   - Default to **organic-first**; treat paid UA as publisher-only or a small late amplifier.
   - Make the **featuring nomination** and the **clip habit** first-class, early tasks.
   - **Trim the launch to the lean subset**; name what to skip and why.
   - For the publisher question, lead with the **capital/cash-flow** reality and the honest
     trade (revenue share, control, the calm-feel risk from marketability pressure).
4. **Apply the compliance/feel guardrails.** Flag the 2025–2026 Apple changes when relevant
   (SDK minimum, age questionnaire, privacy manifests, **4.3 anti-clone** — directly relevant
   to a "clone-plus" strategy: differentiation must be real). Flag when a marketing/ASO choice
   would push the game toward pressure/urgency and betray the taste north-star.
5. **Give a prioritized, sequenced answer** — what to do now vs at soft launch vs at scale,
   with the metric each step moves and the go/kill gate.

## Output

Answer in chat by default — concrete, sequenced, with numbers and the why. For a substantial
deliverable (a full launch plan, a GTM playbook, a publisher-vs-solo decision for the chosen
game), save a dated doc to `DOCS/` (e.g. `DOCS/distribution/YYYY-MM-DD-<topic>.md`) with the
phased plan, the gate numbers, what to defer, and the sources. Always separate **"do now (v1
launch)"** from **"later (post-traction / at scale)."** Label benchmark numbers as directional
(they vary 2–3× by source) and flag any Apple rule that may have changed since the reference
was written.

## Keep this skill current (do this when you learn something — it's part of the job)

The user wants this skill **proactively updated as the landscape shifts and lessons land.**
Route updates by type:
- **An Apple platform/policy change** (App Review rules, privacy, age ratings, SDK minimums,
  featuring, ASO mechanics, ATT/AdAttributionKit) → update `launch-pipeline.md` or `aso.md`.
- **A publisher term, roster change, or pitch-process detail** → update `publishers.md`.
- **A new benchmark, channel, or marketing tactic** (organic reach shifts fast) → update
  `launch-metrics.md` or `gtm-and-marketing.md`.
- **A dated lesson from our own launches** ("this geo worked," "this clip format popped,"
  "this rejection happened") → record it; if it recurs, consider a `memory/` notebook like the
  other skills have.
- **Always** append a dated one-line entry to `CHANGELOG.md` describing what changed and why.
Treat any named publisher, revenue split, benchmark, geo, or Apple rule as **possibly stale** —
verify before relying on it, and fix it when it's wrong. Apple changed multiple rules in
2025–2026; this space does not sit still.
