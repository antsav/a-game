# Pattern: The Intra-Level Difficulty Arc (Easy → Hard → Easy) + Peak-End

> **One line:** Within a *single level*, difficulty should rise **and then fall** — open
> easy (fast wins, many options), peak in the middle (the real puzzle / crux), then resolve
> easy (the board opens up, a cascade of quick clears). The player **starts on a high note
> and ends on a high note**, and jumps straight into the next level.

**Tags:** `pacing` · `difficulty` · `retention` · `subtractive-puzzle` · `satisfaction` · `flagship`
**Status:** load-bearing — this is a core engagement lever for our genre.

---

## Where observed (evidence in the wild)

- **Bus Traffic Fever! / Bus Jam / Car Jam** (traffic-unblock / parking-jam family). Early in a
  level there are lots of free cars to move and obvious progress; mid-level it gridlocks and you
  have to *find* the one car that unblocks the knot; late-level, once paths are freed, the
  remaining cars pour out in a rapid cascade. All within **one level**.
- **Arrows / Pin-out untangle puzzles.** Perimeter arrows pull off trivially at the start; the
  tangled middle is the challenge; once the field is thinned, the last arrows come out
  effortlessly. Same arc.
- Also visible in: color/ball-sort endgames, Unblock Me, nonogram closing moves, match-3
  board-clear cascades. Any **"clear the board"** puzzle tends to have this shape.

## Why it works (the psychology — this is not folklore)

1. **Peak-End Rule (Kahneman).** People judge an experience retrospectively by its **peak** and
   its **end**, not its average. End a level easy + triumphant and the *whole level* is
   remembered as satisfying → the player says "just one more." This is **empirically validated
   for casual games specifically** — Gutwin et al., *Peak-End Effects on Player Experience in
   Casual Games*, CHI 2016. Ending on the hardest move (or a fail) is the worst possible thing
   for retention.
2. **Confidence on-ramp / low activation energy.** An easy open means the player never bounces
   off the start. They're *in* before they notice they started.
3. **Flow (Csikszentmihalyi).** Difficulty tracks up into the challenge zone, then **releases
   before frustration tips into anxiety.** You visit the flow channel and exit on the good side.
4. **Completion cascade / momentum.** The easy tail is a burst of rapid successes — a dopamine
   cascade, the "sweet release" after tension. This is exactly the *burst of satisfaction* the
   game is supposed to deliver.
5. **Tension-and-release.** Same structure as music or story: the mid-level knot is tension, the
   endgame unspooling is release. Release is what feels *good*.

## The structural trick — why SUBTRACTIVE puzzles get this arc for FREE

- In a **subtractive** puzzle (you *remove* pieces: pull arrows, drive cars out, sort items away),
  the state space **shrinks** as you play → constraints relax → the late game is **naturally
  easier**. The easy→hard→easy arc is **emergent, not hand-authored**. You get it for free.
- Contrast **additive** games (Tetris, stacking, endless runners): they get **harder** toward the
  end (board fills, speed rises) and end on a **stress/low** note. Great for arcade tension —
  **wrong** for a calm, peak-end, "finish happy" game.
- **Design implication for us:** favor a **subtractive / clearing** core verb. It hands you the
  arc *and* the calm, no-pressure ending for free. (This dovetails with Anton's taste — clearing
  verbs, no timer, no punishing fail; see `my-game-preference`.)

## How to apply (tuning knobs)

- **Open easy:** front-load *free moves* — many valid opening actions so the level starts with
  obvious, satisfying progress.
- **Engineer one crux:** design a single mid-level bottleneck — the tangle/gridlock that *is* the
  puzzle. That's your peak. One crux per level, not a wall of them.
- **Guarantee the tail resolves:** once the crux is solved, the rest should be near-automatic — a
  cascade. **Never place a second hard spike after the crux.** That murders the peak-end.
- **Make the final action juicy:** the last car exits / last arrow pulled → board-clear
  celebration. This is the **"end" the memory anchors on** — give it the biggest (calm-tuned)
  feedback in the level.
- **Measure difficulty structurally, not by time:** branching factor, # of blocked pieces,
  solution-path constraint — *not* a clock. (No timers; see the taste gate.)

## Anti-patterns (things that break it)

- Level ends on its hardest move, or on a fail/retry loop → worst case for peak-end.
- Flat difficulty (no crux) → no peak, forgettable, no satisfaction spike.
- Monotonic ramp that ends at max difficulty → sends the player away tense/frustrated.
- Over-juicing the *middle* and under-juicing the *finish* → the memory anchor is weak.

## Distinction — this is the INTRA-level arc

Don't confuse with the **level-sequence** oscillation (a breather *level* after a hard *level*),
which `my-game-preference/references/difficulty-and-pacing.md` already covers. Both are real and
they **stack**:
- **Intra-level** (this pattern): easy→hard→easy *inside one level* → peak-end → "just one more."
- **Inter-level** (sequence): Introduce → Test → Breather → Stabilize *across levels* → the macro
  rhythm.

## Related patterns

- Satisfaction bursts / completion cascade (the juicy tail).
- The "just one more" loop (peak-end is the engine behind it).
- Subtractive vs additive core verbs (which genre gives you calm endings for free).

---
*Origin: Anton, 2026-06-30 — observed while playing **Bus Traffic Fever!** and an **arrows
untangle** puzzle. First entry in this library; the articulation ("start high → challenge → finish
high → jump to next level") is his.*
