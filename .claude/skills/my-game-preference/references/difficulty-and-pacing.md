# Difficulty & Pacing — Oscillation, Not a Ramp

How to deliver Anton's "simple start, cycling easy/moderate/hard, bursts of challenge"
without a timer or a stressful ramp. Pair with `relaxing-engaging-design.md` and
`satisfaction-and-juice.md`.

> **The headline finding:** every credible source — flow research, Jesse Schell, Valve's AI
> Director, King's Candy Crush team, the motivation studies, the Jan-2026 Block Blast
> teardown — converges on the same point: **a monotonic difficulty ramp is a design
> mistake.** The oscillation Anton wants (easy → moderate → hard → breather, repeat) is *the
> best practice*, not a casual softening. Build it with confidence.

## The flow channel

Flow = total absorption when **challenge ≈ skill**. The channel runs between **boredom**
(challenge below skill) and **anxiety** (challenge above skill). The 8-channel refinement
adds "arousal" (productive stretch) and "relaxation" (the comfortable breather) — which maps
almost exactly onto Anton's easy/moderate/hard cycling. A *single fixed* curve serves nobody
(Jenova Chen). **No-timer puzzles create challenge through spatial/logical complexity instead
of reflex pressure** — and the sources actively *warn against timers* as a difficulty lever
("frustration unrelated to problem-solving" → churn). No timer is a **strength**.

*Solo-dev flag:* skip real-time ML difficulty adjustment for v1. Ship a hand-authored curve
and **tune offline from data** (attempts-per-level, time-to-abandon) — literally King's method.

## Oscillation / the sawtooth rhythm

- **Schell's tension–release:** "Too much tension and we wear out, too much relaxation and we
  get bored. But when we oscillate between the two we enjoy both." This is Anton's "bursts of
  satisfaction and challenge," in the field's standard textbook.
- **The interest curve is fractal:** hook → escalating peaks, nested at every scale (game →
  world → level → single puzzle). **Valleys aren't dead time — "rest periods make the action
  that much sweeter."** Design rhythm at two scales at once: across-level *and* within-level.
- **Valve's AI Director** (Left 4 Dead): an explicit Build-up → **Peak** → **Relax** (~30-45s,
  spawns nothing) → Fade — a "breathing, pulsating rhythm of tension and relief." Genre-agnostic.
- **Why oscillation beats a ramp (research-backed):** (1) **"Peaks are created by the dips
  after them"** — a breather is what converts a hard solve into a *felt win* (mastery
  afterglow). (2) A peer-reviewed study: **"curves with peaks have the strongest impact on
  motivation"**, and the ideal is **"rising peaks and valleys, each crest slightly higher than
  the last."** → oscillate, but let the overall envelope drift gently upward.

## Simple start

- **Teach by playing, not by text** — the first levels *are* the tutorial; one mechanic at a
  time (The Witness, World 1-1 as gold standards).
- **Make early levels almost trivially easy** — Candy Crush Level 1 ≈ 62% first-try win. The
  opening's job is a *confidence-building win streak*, not a test. Keep early levels
  **snackable** (completable in a bus-stop wait).
- **One mechanic per "chapter," spaced out** — Room 8's rule: don't repeat a mechanic for
  ~50 levels (novelty, not raw difficulty, carries long-term engagement).
- **The designer blind spot** (critical for Anton): *you know the solutions, so you will badly
  underestimate difficulty.* **External playtesting is non-negotiable.**

## "Aha" moments & bursts within a level

The neuroscience is real and recent: a **May 2025 Duke/*Nature Communications* fMRI study**
found insight moments spike hippocampal activity and **nearly DOUBLE memory retention** (5
days later); the insight rush is a dopamine hit in the reward center. **Designed-for insight
isn't just pleasant — it's what makes the game stick and pull the player back.**

Script a mini tension→insight→payoff arc *inside* the better levels (the fractal curve):
- **Cascade/combo payoff ("Wow" levels):** boards where one good placement detonates a
  satisfying chain — the "burst." (Pair with `satisfaction-and-juice.md`.)
- **"Almost-not-enough" tension ("Fuu" levels):** 1-2 moves always seem to be lacking → the
  clear feels earned. **Use sparingly — spice, not the meal** (it borders on pressure).

## How no-timer puzzles scale difficulty (levers instead of a clock)

| Lever | Raises difficulty by |
|---|---|
| Move / piece budget | Fewer moves = tighter puzzle (match-3 ≈ 15-20 moves/level) |
| Board size & shape | Smaller/irregular board = fewer easy options |
| Piece / color variety | More types = lower match odds, more planning |
| Blockers / constraints | Should create *interesting choices*, not pure obstruction |
| Number of simultaneous goals | One → several objectives |

**King's "complexity staircase":** introduce blockers progressively, each understood before
the next escalates; use bots to estimate pass-rates but treat them as *support, not a
replacement for human judgement.* King confirms the oscillation explicitly: *"a deliberate
effort to vary difficulty rather than constantly increasing it"* — hard levels followed by
lighter ones for "variation and momentum."

**The copyable template — Supersonic's 4-phase loop (per mechanic):**
1. **Introduce** — new mechanic, kept easy, focus on teaching.
2. **Test** — a harder level applying the just-learned mechanic.
3. **Breather** — an easier level for recovery and confidence.
4. **Stabilize** — challenging-but-manageable; repeat with the next mechanic.

Candy Crush data: hard spikes roughly **every 3-7 levels** with easy runs between — "the
promise of fun is always just one level away."

## Avoiding frustration in a no-fail game

Calm-puzzle toolkit (2025 consensus): no timers, **no/soft fail state**, unlimited retries,
and a **graduated hint system** (subtle nudge → show where to start → reveal a move) — offer
the first hint only after ~3 failed attempts so the player still gets the aha. King's
authoritative tuning rules:
- **"Retention always wins"** — easier levels reduce churn; retained players compound.
- **"Crazy hard levels never pay off long-term"** — hard spikes are seasoning, not the diet.
- **"If a level is really hard, it should also be really short"** — concentrate difficulty
  into short bursts, never long grinds (pairs with snackable, no-timer sessions).
- **Measure "time to abandon" alongside "time to pass"** to separate *difficulty* from *fun*;
  tune to **median attempts per level**, not raw pass-rate. **Instrument both from day one.**

## Synthesis for the game
1. Codify oscillation via the **4-phase loop** per mechanic — it's validated, not a concession.
2. Engineer **aha + cascade bursts** inside levels (nearly doubles stickiness).
3. **Breather levels are the mechanism** that makes hard ones feel good — always follow a hard
   level with an easy/satisfying one.
4. **No timer is a strength** — challenge from a constrained board + planning.
5. Let the envelope **drift up gently** — each peak slightly higher than the last.
6. Calm-difficulty: soft fail, unlimited retries, graduated hints, "if hard, make it short."
7. **Tune offline** from attempts-per-level + time-to-abandon; **playtest externally** (beat
   the designer blind spot).

## Sources
Schell *Art of Game Design* 3rd ed. (2019) · Csikszentmihalyi flow · Jenova Chen "Flow in
Games" (2006) · Booth/Valve AI Director (GDC 2009) · GameDeveloper "Difficulty Curves Start at
Their Peak" · Springer difficulty-pacing/motivation (2022) · Supersonic puzzle best practices
· PocketGamer.biz + MobileGamer.biz on King/Candy Crush (Mar 2024) · Room 8 Studio (2019) ·
Duke/*Nature Communications* aha-moment fMRI (May 2025) · DoF "Tetris to Block Blast" (Jan
2026). Full URLs in CHANGELOG notes. *Candy Crush per-level win-rates are from an older sample
dataset — illustrative of the pattern, not current values.*
