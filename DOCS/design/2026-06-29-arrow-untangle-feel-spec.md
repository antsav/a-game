# Core-Loop & Feel Spec — Arrow/Untangle Puzzle (run through the taste north-star) — 2026-06-29

*First run of the `my-game-preference` skill. Applies Anton's design north-star to the leading
candidate (arrow/untangle), and stress-tests tempting mechanics through the one test
(gain+freedom = keep / loss+pressure = cut).*

## The loop (fits the profile)

Tap an arrow → it flies off in its direction → if its path is clear it leaves (satisfying
declutter); if blocked, you lose a life. Deduce the *order* that empties the board. **This is
"stakes without a clock" — the #1 DNA of Anton's taste:** real puzzle tension, meditative pace.
Passes the hard gates: no timer, player-paced, order-from-disorder verb, simple start.

## Difficulty & pacing (per `references/difficulty-and-pacing.md`)

- **Simple start:** first ~5 boards near-trivial (1-2 obvious moves) — teach by playing, build a
  confidence streak. No tutorial text.
- **Oscillate** via the 4-phase loop per new rule (Introduce → Test → Breather → Stabilize); drop
  an easy/satisfying board after each hard one. Envelope drifts up gently.
- **Bursts within a board:** design some boards as a tension→insight→**chain** — one correct first
  arrow opens a satisfying cascade of now-clearable arrows (the "aha," which 2025 neuroscience says
  nearly doubles stickiness).
- **Calm-fail toolkit:** unlimited retries, instant restart, **graduated hint after ~3 fails**
  (highlight one safe arrow). "If a board is hard, keep it short."
- Instrument **attempts-per-board + time-to-abandon**; **playtest externally** (you'll underestimate
  difficulty — designer blind spot).

## Feel (per `references/satisfaction-and-juice.md`, calm-tuned)

- Response **< 100 ms**; arrow launches with ease-out, a soft *whoosh*, gentle trail that fades.
- Board-empty climax: gentle full-screen bloom + a held warm chord + `.notification(.success)` haptic.
- Per-arrow: soft `.impact(.soft)` haptic + light particle, time-aligned to the sound. **Restrained,
  not maximal** — drain/dissolve, not detonation. Quiet still baseline so each clear registers.
- Minimalist palette, soft audio bed; reduced-motion + haptics-off toggles.

## The "pull to reach more" (per `genre-dna.md` bridge insight)

Pure logic puzzles can feel finite. Add a **gentle, gain-only progression** so there's always a
next thing — *without* pressure:
- Solving boards fills a **visibly-growing world** (e.g. a constellation/garden that expands) —
  tangible "numbers go up."
- Optional **collection** of arrow skins/themes unlocked by progress (cosmetic, never power).
- A possible **idle/prestige** layer (reach-more, player-initiated) — defer; validate the core first.
- **No streaks-you-can-break, no daily-or-lose.** Return hooks framed as a *gift* ("3 new boards
  waiting"), never an obligation.

## Filter stress-test (the skill rejecting tempting-but-wrong mechanics)

| Tempting mechanic | One test | Verdict | Calm alternative |
|---|---|---|---|
| **Timer / "beat the clock" mode** | loss + pressure | **CUT** (hard gate) | Move-efficiency *score* (gain), or a no-fail Zen mode |
| **Lives/energy gate** ("wait or pay to keep playing") | loss + pressure | **CUT** | Unlimited play; monetize via opt-in rewarded *acceleration* + remove-ads |
| **Daily streak you lose if you miss a day** | loss + pressure | **CUT** | A daily *bonus board* that's simply there when you return (gain, no penalty) |
| **Leaderboard / ranked PvP** | evaluative pressure | **REDESIGN** | Personal-best + the growing world; opt-in async only |
| **Combo/cascade payoff on a good first arrow** | gain + freedom | **KEEP** | — (this is the "burst") |
| **Visibly-growing world from solves** | gain + freedom | **KEEP** | — |

## Monetization note (feel wins for the core loop)
Per `game-monetizer` × this north-star: ads-first (rewarded *hint/continue* opt-in + a delayed,
gentle interstitial between boards), remove-ads, cosmetic theme IAP. **No timed-offer FOMO, no
energy.** Every monetization mechanic also runs the one test.

## Verdict
The arrow/untangle loop is a **strong fit** — it natively satisfies the hard gates and embodies
"stakes without a clock." The work to "go the extra mile" is in the **pacing oscillation**, the
**calm-tuned juice**, and a **gain-only progression pull** — exactly the three things the
references detail. Build the core + feel first; validate retention; then consider the idle layer.

*Sources: this skill's `preference-profile.md`, `design-north-star.md`, and `references/`. Genre
volumes are mid-2026 — re-verify with `games-researcher` before committing.*
