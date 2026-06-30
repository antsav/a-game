# Rewarded Revive (Continue-after-fail)

**What:** offer an opt-in rewarded video to continue/revive right after the player fails.
**Monetization goal:** ad-ARPDAU (the single highest-value rewarded placement).
**Best for:** any hybrid-casual puzzle/arcade — the first ad mechanic to build, v1.
**Psychology:** loss aversion (the alternative is losing progress) — see
[[references/spend-psychology.md]].

## How it works
On a fail/game-over, before showing the result, present "Watch to continue" with a clear
benefit (revive at the failure point / keep your streak). Player opts in → rewarded video →
resume. Decline → normal game-over.

## Tuning
- **Cap ~1 revive per game/session** (Block Blast pattern) — protects difficulty integrity
  and the ad's perceived value.
- Make the revive *meaningfully* valuable (resume in place, not a token nudge).
- Overall rewarded budget: start ~3-4 rewarded views/user/day across all placements; tune.

## Pitfalls
- **Never force it** — must be opt-in and framed as a gift (preserves 80-90% completion +
  goodwill). Forcing risks Apple 3.2.2 and tanks retention.
- Don't let unlimited revives trivialize difficulty (kills the loss-aversion driver).

## Live examples
Block Blast (revive only, capped); near-universal in puzzle/arcade (2025-2026).

## Effort (solo dev)
Low — one rewarded placement behind your mediation SDK. **Build first**, alongside the
mediation layer. See [[references/ad-monetization.md]].
