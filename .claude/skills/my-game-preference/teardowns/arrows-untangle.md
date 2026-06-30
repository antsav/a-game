# Arrows / Line Untangling — Amaze GO!, Arrows: Puzzle Escape (Anton's top current love)

**Core loop:** Tap an arrow and it flies off the board in the direction it points — but if
it would collide with another arrow in its path you lose a life, so you must deduce the
*order* to fire arrows that keeps every path clear until the board is empty.

**Source of satisfaction / pull:** A **dependency-ordering / deadlock puzzle** (mechanical
cousin of Rush Hour / unblock). The pull is the *"aha" of sequence* — scan a cluttered board,
spot the one arrow with a free lane, fire it, and that opens a lane for the next. **Each tap
visibly declutters the screen** — the satisfaction is *decongestion*: chaos → order, one
clean removal at a time. Store copy: "declutters the screen and mind."

**Engaging without a timer:** Tension is **consequence, not clock**. Wrong order = collision
= lost life, so there are real stakes and you must *think before tapping* — but infinite time
to think. Reviewers use it as a bedtime wind-down ritual: "helps get my mind off the day."
Engaged brain, zero adrenaline — the exact target.

**Difficulty / pacing:** Generated levels with **alternating difficulty** (hard then easier) —
a reviewer praised this rhythm specifically. Board size and arrow count scale over thousands
of levels.

**DNA to extract:**
- **Stakes without a clock** (collision fail-state) — the single most transferable idea in the
  whole library: real puzzle tension at a meditative pace.
- **Visible decongestion** — every action makes the board emptier/cleaner ("I made the mess smaller").
- **Difficulty oscillation** (hard→easy), not a monotone ramp.
- **Minimalist black-and-white art** — keeps focus on logic, reads as calm.

**Solo-dev buildability: HIGH (the standout).** Simple logic (arrow direction + raycast for
collisions along the firing line). No physics, no art-heavy assets, no animation craft. The
catch is *content* — but the rules are simple enough to **procedurally generate-then-verify**
solvable boards (generate backwards from a solved state). Caveat: pure-logic puzzles monetize
weakly on fail-driven IAP → plan **ads-first**.

**Why this is the recommended bet:** rare alignment of *trend Anton personally loves* +
*validated but still-early demand* (May 2026 breakout, 50M+ combined downloads, multiple
publishers entering) + *lowest craft barrier*. Same wave `games-researcher` flagged as the
freshest breakout — taste and market coincide. Ship soon and differentiate (better level-gen,
a novel arrow rule, daily puzzles).

**Sources:** Gamigion "Arrows & Amaze GO! hit 50M downloads in May" (May 2026) · Amaze GO!
App Store (Oakever Games) · Arrows – Puzzle Escape App Store (Lessmore GmbH, 4.9★/275K) ·
Arrow Escape (CrazyGames). Accessed Jun 2026; volumes shift fast — re-verify before committing.
