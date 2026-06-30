# Satisfaction & Juice — Calm-Tuned Game Feel

How to deliver the "bursts of satisfaction" Anton wants while keeping the whole thing
meditative. Pair with `relaxing-engaging-design.md` (which warns: don't over-juice a calm
game).

> **Thesis:** Juice = disproportionate, multi-sensory feedback for a player action. The job
> is **not to maximize it but to tune it** — enough crunch that each clear feels earned,
> soft and readable enough that the experience stays meditative. The canon teaches the
> toolbox; the calm tuning dials it down without losing the payoff.

## The canon (learn the toolbox)

- **Steve Swink, *Game Feel* (2009):** "real-time control of virtual objects, with
  interactions emphasized by polish." The load-bearing rule for a puzzle: **response under
  ~100 ms** — a piece must snap / a line must start clearing the instant the finger lifts.
  Latency kills satisfaction faster than any missing particle.
- **Jonasson & Purho, "Juice it or lose it" (GDC Europe 2012):** the talk that named juice.
  Little moments of surprise and delight separate flat from alive.
- **Nijman/Vlambeer, "The Art of Screenshake" (2013):** the toolbox — bigger feedback, sound
  with low-end weight, particles, permanence, and especially **hit pause / freeze frames**
  (a 1-3 frame freeze at the moment of a clear makes it *land* harder). The most transferable
  trick to a puzzle game.

**Juice toolbox (consolidated):** **easing/tweening** (never move linearly — ease-out for
arrivals; *the* highest-leverage, lowest-cost juice) · squash & stretch · anticipation
(a wind-up) · particles · hit-pause · sound (low end = weight) · haptics · scale/color
flashes · score pops. **Unity:** DOTween/LeanTween + the built-in Particle System do ~80% of
juice in a few lines. *Juice should always echo the core gameplay.*

## Why sorting / snapping / popping / clearing feels good

The "oddly satisfying" engine (well-documented, not vibes): **closure & completion**
(chaos → order, a visible "done" — the core of sort/untangle), **predictability** (the brain
enjoys correctly predicting the outcome), **ASMR-adjacent sensory gratification** (soft,
crisp, slow detail), and the dopamine/serotonin of completion. **The satisfying part of the
game is the resolution moment** — the snap into the right slot, the column draining, the
tangle resolving into a clean shape. Stage everything to make that moment legible and tactile.

## Bursts of satisfaction within a level (the escalation ladder)

Layer payoffs by magnitude; let feedback intensity **scale with the achievement**:
- **Base hit** (single placement / 3-match): pop + small particle + soft sound + score pop.
- **Bigger hit** (4-5 / area clear): larger blast, special-piece creation, slightly louder.
- **Cascade / chain:** each link escalates — **rising pitch per step** is the single most
  effective audio trick — plus growing particles + a "Combo!" pop. This is Anton's "burst."
- **Board clear (climax):** the emotional peak — full-screen *gentle* bloom/confetti, a held
  warm chord. Reserve your loudest feedback strictly for this.
- Untangle/sort climax: the final un-cross/last tube snapping into a **clean, symmetric,
  glowing resolved state.**
- Block Blast adds **verbal pops on input** ("Perfect," "Great") — a micro-payoff on the move
  *before* the clear resolves, partly *cognitive* (I solved it well).

## Multi-sensory feedback on iOS (practical, Unity solo dev)

The "crunch"/"pop" = **stacking visual + sound + haptic on the same event, time-aligned to
the same frame.** Misalignment (haptic 80 ms late) feels *worse* than no haptic.

- **iOS haptics:** `UIImpactFeedbackGenerator` (styles light/medium/heavy/**soft**/rigid —
  use **soft/light** for calm), `UINotificationFeedbackGenerator` (success on a clear),
  `UISelectionFeedbackGenerator` (subtle tick when cycling a piece). **Core Haptics**
  (`CHHapticEngine`) for custom soft "swells" (low sharpness) — where calm haptics live.
- **Into Unity without writing Swift:** **Nice Vibrations** (More Mountains) is the de-facto
  standard wrapper; open-source alternatives exist. Best solo time-saver.
- **Sound for calm:** swap "boom" for **thunk/woody/glassy/marimba/harp** — soft, short,
  rounded transients. **Tetris Effect / Lumines (Mizuguchi "synesthesia")** is the gold
  reference: each input is *musical* and adds to an evolving soundscape rather than firing an
  isolated SFX — satisfying *and* meditative.

## The calm end of juice (the tuning that matters most for Anton)

Same tools, opposite tuning. **2024-25 game-feel research: coherent, restrained feedback
often beats maximal juice for calm experiences.** Concrete substitutions:
- **Easing:** prefer ease-out / gentle elastic; **slightly longer durations (250-400 ms)**
  read as calm; very fast snaps read arcadey.
- **Particles:** soft, low-velocity, **fade rather than explode**; bloom/drift not debris;
  lower counts.
- **Sound:** soft mallet/glass/wood, gentle reverb, low attack; each action *adds to an
  ambient bed* (Mizuguchi-style). Avoid sharp high-attack SFX.
- **Haptics:** low sharpness, gentle swells; `.soft`/`.light`. Avoid `.heavy`/`.rigid`/`.error`.
- **Think drain/dissolve/bloom, not detonation.**

## Restraint — when juice becomes noise

- **Readability first** — in a puzzle the board *is* the game; if juice ever hides what
  happened, cut it.
- **Reserve intensity for magnitude** — soft for routine moves, big only for combos/clears.
  If everything is loud, nothing is.
- **Screenshake is the most overused tool** — for a calm game, near-never (a whisper on a
  full board-clear at most).
- **Respect a quiet baseline** — meditative feel depends on *contrast*: most of the screen
  calm and still so the small satisfying moments register.
- **Test on real iPhone hardware** with sound + haptics on (editor misleads on timing/feel).
- Offer **reduced-motion / haptics-off** toggles — this audience expects them.

## Quick tuning sheet
| Event | Visual | Sound | Haptic (iOS) |
|---|---|---|---|
| Select piece | slight scale-up, ease-out | soft tick | `.selection` |
| Snap into slot | squash + gentle overshoot | soft woody "thunk" | `.impact(.soft)` |
| Line/area clear | soft glow + color-fade dissolve | mallet/glass note | `.impact(.light)` |
| Combo/cascade | growing bloom per step | **rising pitch** per link | escalating soft impacts |
| Board clear (climax) | full-screen gentle bloom | held warm chord | `.notification(.success)` |
| Baseline | still board, minimal motion | low ambient pad | none |

## Sources
Swink *Game Feel* (2009) · Jonasson/Purho "Juice it or lose it" (2012) · Nijman "Art of
Screenshake" (2013) · GameAnalytics juice (2018) · SAGE "oddly satisfying" (2022) · DoF
"Tetris to Block Blast" (Jan 2026) · ACM FDG 2025 "Beyond Satisfaction" · Nice Vibrations ·
Tetris Effect/Mizuguchi · Folmer Kelly restraint critique (GDC 2014). Full URLs in CHANGELOG
notes. *Tuning tables are synthesis applying the canon to Anton's goal, not a cited spec.*
