# game-designer — changelog

Append a dated line whenever the craft doc or the pattern library changes. Newest on top.

## 2026-06-30 — pattern: One Input Modality
- **patterns/single-input-modality.md** (flagship) — Anton's insight after playing **Arrow Stack**
  ("nicely done, but a 3D rotating cube, not tap-only"): successful hyper-hybrid-casual games keep
  **the same interaction** for the whole core loop — *all* tap or *all* slide, **never mixed during
  gameplay**. Grounded in motor-schema consolidation, seconds-to-fun onboarding, and mode-error
  avoidance (mixing inputs → misfires → breaks the calm, no-pressure feel). Added as a **second
  gate on the core verb** in `design-craft.md` (satisfying-raw *and* single-gesture) and as a
  concept **screening question** ("can the whole loop be played with one repeated gesture?").
  3D-object manipulation flagged as inherently multi-gesture → an anti-pattern for this genre.

## 2026-06-30 — initial version
- Created the skill: the **craft** of designing a shippable hybrid-casual game + a **living,
  scalable pattern library** that grows from Anton's own play observations.
- **SKILL.md** — entry point, boundary vs sibling skills (taste/pay/marketable/build/launch), the
  design & critique workflow, and the **insight-capture ritual** (how a play observation becomes a
  reusable pattern).
- **design-craft.md** — hybrid-casual anatomy (verb → loop → level arc → meta), the core-verb
  (autotelic) test, onboarding/FTUE, retention hooks, and the **first-game scope discipline**
  (one core verb + one meta layer; resist stacking meta — Anton's over-engineering guardrail).
  Hybrid ≈ D7 16% / LTV 3–5× hyper (mid-2026 sources).
- **patterns/** — the growing library. `README.md` index + `_TEMPLATE.md` starter.
  - **difficulty-arc-peak-end.md** (flagship) — Anton's insight from **Bus Traffic Fever!** +
    **arrows untangle**: the intra-level **easy→hard→easy** arc; start *and* finish on a high note
    → "just one more." Grounded in the **Peak-End Rule** (Kahneman) — empirically shown for casual
    games in **Gutwin et al., "Peak-End Effects on Player Experience in Casual Games," CHI 2016** —
    plus flow, tension-and-release, and the completion cascade. Key craft insight: **subtractive /
    clearing** verbs produce this arc (and the calm no-pressure ending) *for free*, because the
    state space shrinks as you play; **additive** games (Tetris) get harder toward the end and end
    on a stress note. Distinguished from the inter-level breather oscillation that
    `my-game-preference` already owns.

### Source notes
Hybrid vs hyper casual (mid-2026): Unity "Mobile Gaming's Shift from Hyper to Hybrid-Casual";
Udonis casual-games-2026 + hybrid-casual recipe; Homa hybridcasual guide; StudioKrew/Antier 2026
strategy pieces; GameAnalytics "six games that layer meta." Peak-end: Gutwin/Johnson et al. CHI
2016 (benlafreniere.ca PDF); Kahneman peak-end rule; Gameful Bits "peak-end influences enjoyment."
Traffic-unblock family: Bus/Car Jam, Bus Craze, Bus Escape store/review pages.
