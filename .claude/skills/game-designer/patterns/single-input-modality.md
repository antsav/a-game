# Pattern: One Input Modality — Don't Mix Tap and Slide Mid-Gameplay

> **One line:** A hyper/hybrid-casual game should be driven by **one consistent interaction**
> for its whole core loop — *all* tap, or *all* slide/drag — never switching input verbs during
> play. One finger, one gesture, learned once, never re-learned.

**Tags:** `core-verb` · `input` · `onboarding` · `game-feel` · `hyper-hybrid-casual` · `flagship`
**Status:** load-bearing — a screening criterion for the core verb itself.

---

## Where observed (evidence in the wild)

- **Arrow Stack** (Anton, 2026-06-30) — "nicely done," but the core is a **3D rotating cube** and
  it is **not tap-only**. The interaction mixes: you're both manipulating a 3D object *and* doing
  something else. That mixing is exactly the friction — it reads as a well-made game that isn't as
  clean/frictionless as the top hyper-casual hits, which commit to a single gesture.
- **Contrast — the clean single-verb hits:** the best hyper-casual games are ruthlessly
  mono-input. Tap-only: *Flappy*-likes, *Helix Jump* (one tap), stack-timing games (*Stack*),
  color-switch tappers. Slide/drag-only: *arrows untangle* / pin-out (drag to pull), color/ball
  **sort** (tap-to-pour but a *single* tap verb), *2048*-style swipers, draw-a-line puzzles,
  *Bus Jam* (tap a car to move it). Each of these teaches **one** gesture and never asks for
  another.

## Why it works (the psychology)

1. **Motor-schema consolidation.** A single repeated gesture becomes automatic (procedural memory).
   The player stops thinking about *how* to act and thinks only about *what* to do. Mixing inputs
   forces a mode-switch — the hand has to re-decide which gesture applies — which breaks flow and
   raises cognitive load on every action.
2. **Seconds-to-fun / zero onboarding.** One verb = the tutorial is "do the thing once." A game
   that needs tap **and** slide needs to teach two things, and needs the player to learn *when*
   each applies. That's a menu of friction in a genre whose entire edge is frictionlessness.
3. **Mode errors are the enemy of calm.** When two input verbs coexist, the player will
   occasionally use the wrong one (slide when the game wanted a tap) → an unintended action, a
   misfire, a small punishment. In a *calm, no-pressure* game (Anton's taste) those misfires are
   disproportionately annoying — they feel like the game's fault, not the player's.
4. **Reads as "polished."** Single-input games *feel* more premium precisely because there's no
   seam. The "nicely done but…" reaction to Arrow Stack is this seam being felt.

## How to apply (to our game)

- **Pick the input verb *before* the mechanic is finalized**, and let it constrain the design:
  decide "this is a **tap** game" or "this is a **drag/slide** game" and then only accept mechanics
  expressible in that one gesture. Treat a design that needs a second input as a **red flag on the
  core verb**, not a feature to add.
- **Tap** suits: select / place / pour / activate / time-a-press. **Slide/drag** suits: pull /
  move-along-a-path / connect / sort-by-dragging / aim. Choose the family that fits the core verb
  and commit.
- **One gesture, escalating *content*.** Difficulty should come from the *board / puzzle*, not from
  adding a second control. Levels get harder by needing smarter taps — never by adding a swipe.
- **Camera/UI gestures don't count** *if* they're outside the core loop (a pinch-zoom on a map
  between levels is fine). The rule is about the **in-play action verb**.
- **Screening question for any candidate concept** (see `games-researcher`): *"Can the entire core
  loop be played with one repeated gesture?"* If no, either simplify to one, or pass on the concept.

## Anti-patterns (how it breaks)

- **Tap + slide in the same loop** (Arrow Stack's issue): the player context-switches every action.
- **3D manipulation as the core verb.** Rotating/orbiting a 3D object is inherently a multi-axis,
  multi-gesture input — it fights the one-gesture rule and adds spatial-reasoning load. Hyper-casual
  overwhelmingly wins with 2D or "2.5D" where one gesture fully expresses the verb.
- **"Hold to charge, then swipe to release"** and similar compound gestures — reads as one verb but
  is really two motor acts stitched together; higher failure rate, worse for calm play.
- **Adding a second input to create difficulty** instead of making the *content* harder. This is
  the lazy way to raise the skill ceiling and it costs you the frictionless on-ramp.

## Fit check (Anton's taste + hybrid-casual)

- **Strong fit.** No-timer, no-pressure, meditative play *depends* on the input being automatic and
  misfire-free — mode errors are the opposite of calm. A single learned gesture is what lets the
  player zone out. Cross-links `my-game-preference` (relaxing-engaging, no-pressure) directly.
- Reinforces the **subtractive/clearing** lean from `difficulty-arc-peak-end.md`: clearing verbs
  (pull, sort, pour, unblock) are naturally single-gesture.

## Related patterns

- [Intra-Level Difficulty Arc + Peak-End](difficulty-arc-peak-end.md) — difficulty from *content*,
  not from a second control, is the shared through-line.
- The core-verb test in `../design-craft.md` — this pattern is a second gate on the same verb:
  satisfying-raw **and** single-gesture.

---
*Origin: Anton, 2026-06-30 — after playing **Arrow Stack** ("nicely done, but a 3D rotating cube,
not tap-only"). His articulation: successful hyper-hybrid-casual games keep **the same interaction**
throughout — all tapping or all sliding, never mixing during gameplay.*
