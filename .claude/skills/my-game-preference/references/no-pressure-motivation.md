# No-Pressure Motivation — The "Pull, Not Push" Engine

Why Anton's preference (no rushing, "just a pull to reach more, like Egg Inc.") is
textbook intrinsic-motivation design — and how to build the pull without pressure. Pair
with `relaxing-engaging-design.md` and the idle teardowns in `../teardowns/`.

> **The validating fact:** the foundational academic paper is literally titled *"The
> Motivational Pull of Video Games: A Self-Determination Theory Approach"* (Ryan, Rigby &
> Przybylski, 2006). Anton's "pull" instinct has an academic name.

## Self-Determination Theory (SDT) in one screen

Intrinsic motivation — playing for its own satisfaction — is sustained by three needs:
**Autonomy** (acting from your own volition), **Competence** (feeling effective), and
**Relatedness** (connection). The **PENS model** (Ryan, Rigby & Przybylski 2006) showed
games earn intrinsic motivation via: controls easily mastered, **clear/informational
feedback**, and **choice over goals and strategies**.

**Why AUTONOMY is exactly why no-timer games appeal to Anton:** autonomy = "feeling in
control of your own life," that actions are self-endorsed (NOT independence, NOT "lots of
choices"). The mechanism that *breaks* it is **pressure**. Per **Cognitive Evaluation
Theory** (the SDT sub-theory): *deadlines, surveillance, and evaluations shift the felt
reason for acting from internal ("I want to") to external ("I have to"), undermining
intrinsic motivation.* **A timer is a deadline.** Anton's aversion to timers is the
textbook signature of protecting intrinsic motivation. No-timer / pause-anytime /
persistent-progress games are autonomy-supportive *by construction*.

## Push vs Pull (the actionable distinction)

| | **PULL (keep — intrinsic, autonomy-supportive)** | **PUSH (cut — controlling, extrinsic)** |
|---|---|---|
| Motivator | Anticipation, curiosity, mastery, visible progress | Deadlines, loss-aversion, FOMO, punishment |
| Felt reason to play | "I *want* to see what's next" | "I'll *lose* something if I don't" |
| Emotional tone | Relaxed, absorbed, eager | Anxious, obligated, guilty |
| Examples | Next unlock teased, number climbing, offline gains waiting | Draining energy, breakable login streak, limited-time event, "crops will wither" |

**The clean rule for the game:** *never make the player play to avoid a loss; always make
them play to reach a gain.* Same engagement target, opposite emotional valence.

**The litmus test for ANY mechanic** (incl. monetization): *Does this make the player play
to **gain** something, with freedom to stop — or to **avoid losing** something, under
pressure?* Gain + freedom = healthy pull (keep). Loss + pressure = dark push (cut).

## Concrete PULL levers

- **Anticipation** — tease the *next* unlock/upgrade so the player leans forward. Idle
  design's core engine: each action leads to a bigger payoff later; the anticipation is the hook.
- **Curiosity** — unknowns to reveal (Universal Paperclips is almost pure curiosity).
- **Mastery / competence** — optimization decisions with **informational** (not evaluative)
  feedback. Shifting which choice is optimal keeps decisions interesting without pressure.
- **Visible progress — "numbers go up"** — the single most reliable intrinsic pull. Note the
  appeal is **low-arousal**: "not adrenaline — the satisfaction of setting up a system and
  watching it execute." Optimization, not panic.
- **Offline progress** — accrues while away → growth feels non-stop, gives a *pleasant*
  reason to return without *demanding* it, and closing the app never costs anything. Pure
  pull ("come back to a reward"), never push ("come back or lose").
- **Player-initiated reset (prestige)** — Egg Inc.'s Soul Eggs: *you* choose when to reset
  for a permanent bonus; each run is faster. Escalating ambition the **player controls** —
  the "reach more" pull with zero imposed pressure. (Forced resets would violate autonomy.)

## Designing autonomy (feature checklist)

- **No fail states / no timers.** Zen/endless framing is the purest form (Alto's Odyssey Zen,
  Bejeweled Zen — "can't run out of moves, play as long as you want").
- **Pause anytime / persistent progress** — the game waits for the player, not vice versa.
- **Optional goals, not mandatory** — offer milestones/quests as *available* targets; avoid
  mandatory daily obligations and breakable streaks.
- **Informational, not controlling, feedback** — "here's your rate," not "you're falling
  behind everyone." Be cautious with leaderboards: they can flip competence into evaluative
  pressure. Frame prompts as invitations ("Ready to prestige?"), not guilt ("Don't lose your
  streak!").

## Healthy pull vs dark compulsion

The same compulsion loop (do → reward → want again) underlies both healthy idle games and
manipulative ones. The difference: **gain-driven + autonomy-to-stop = healthy pull;
loss-driven + pressure = dark push.** The tell of unhealthy compulsion is motivation
shifting "from enjoyment and mastery to a desperate need to avoid discomfort." Anton wants
relaxing-engaging, not addictive-anxious — design the pull, strip the push. (This directly
intersects `game-monetizer`: keep the litmus test in mind whenever a mechanic touches spend.)

## Bottom line for the game
1. **Engine of pull:** numbers-go-up + always-visible next unlock + offline gains waiting.
2. **"Reach more" without rushing:** player-initiated prestige/reset (Egg Inc. model).
3. **Strip every push:** no draining timers, breakable streaks, FOMO, or loss-framing —
   replace each with a gain-framed equivalent.
4. **Lock in autonomy:** Zen/endless framing, pause-anytime, persistent progress, optional
   goals, informational feedback.
5. **Litmus-test every mechanic:** gain+freedom (keep) vs loss+pressure (cut).

## Sources
Ryan/Rigby/Przybylski "Motivational Pull of Video Games" (2006) + PENS (selfdeterminationtheory.org)
· Przybylski/Rigby/Ryan motivational model (2010) · Ballou (SDT-in-games misconceptions) ·
Cognitive Evaluation Theory (Deci/Koestner/Ryan meta-analysis 1999) · Pecorella "Math of
Idle Games" (2016) + GDC idle talks · Egg Inc. prestige/Soul Eggs (fandom wiki) · idle
psychology (designthegame.com, playmushies) · dark-pattern line (ACM CHI 3519837; arXiv
2412.05039, 2024). Full URLs in CHANGELOG notes. *Practitioner blogs are directional —
weight the academic SDT/CET sources more.*
