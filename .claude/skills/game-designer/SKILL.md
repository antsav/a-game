---
name: game-designer
description: >-
  The craft of designing a shippable hybrid-casual mobile game — core loop, the core verb,
  mechanics, difficulty and pacing (incl. the intra-level easy→hard→easy arc and peak-end
  "finish on a high note"), onboarding/FTUE, retention hooks, meta/progression layering, and
  hybrid-casual anatomy calibrated to Anton's simple FIRST game. ALSO a living, scalable
  PATTERN LIBRARY of game-design mechanics harvested from games Anton plays. Use this whenever
  designing or critiquing a mechanic/loop/level, asking "why is this game engaging / what makes
  this fun," working out difficulty pacing or session shape, deciding how to layer meta on a
  simple core, comparing hybrid vs hyper casual as a craft choice — AND especially whenever
  Anton shares an observation or insight from playing a game and wants it captured, logged, or
  turned into a reusable design pattern ("I noticed X in game Y", "add this insight", "why does
  this mechanic work"). Complements my-game-preference (his taste gate), game-monetizer (pay),
  games-researcher (marketable), unity-3d (build). Trigger it for any game-design-craft or
  "capture this mechanic" request, even when "design" isn't said.
---

# Game Designer

The **craft** of designing a good, shippable hybrid-casual game — and a **living pattern
library** that grows every time Anton plays something and spots why it works. This is the
practitioner's toolkit; it turns loose observations into reusable design leverage.

## The one line
**Good design craft = a satisfying core verb, a loop with instant feedback, and pacing that makes
every level start *and* finish on a high note.** Everything else is layering.

## How this skill is organized (scalable, self-updating)

- **`design-craft.md`** — the durable toolkit: hybrid-casual anatomy, the core-verb test, core
  loop, onboarding/FTUE, retention hooks, meta layering, and the **scope discipline for a first
  game** (Anton's over-engineering guardrail). *Read this for any "how should this be designed"
  question.*
- **`patterns/`** — the **growing** library: one file per mechanic/insight, most harvested from
  games Anton plays. `patterns/README.md` is the index; `_TEMPLATE.md` is the copy-me starter.
  The flagship entry is **`difficulty-arc-peak-end.md`** (the easy→hard→easy intra-level arc).
- **`CHANGELOG.md`** — dated log of every craft update and new pattern.

## When to use
- Designing/critiquing a **mechanic, core loop, level, or difficulty curve**.
- "**Why is this game engaging / what makes this fun**" — decompose it into named patterns.
- Deciding **how much meta** to layer on a simple core, or hybrid-vs-hyper as a *craft* call.
- **Anton shares a play observation** and wants it captured as a pattern — this is a primary
  trigger (see the ritual below).

## Workflow

**Designing or critiquing something:**
1. Frame it with `design-craft.md` (verb → loop → level arc → meta).
2. Pull any matching `patterns/` file for the specific mechanic and its psychology.
3. Run the result through the taste gate — `my-game-preference` — before calling it done. **When
   craft and taste conflict on *feel*, taste wins for the core loop.**
4. Give a verdict + the *why* + a concrete alternative if it doesn't fit.

**Capturing a new insight (do this proactively — it's the point of the skill):**
When Anton says "I noticed X in game Y" / "this mechanic is why it's fun" / "add this":
1. Name the pattern. Copy `patterns/_TEMPLATE.md` → `patterns/<kebab-name>.md`.
2. Fill it: where observed, **why it works** (find the real principle — peak-end, flow, variable
   reward, SDT, Zeigarnik, loss aversion… research it, don't hand-wave), how to apply it to our
   game, anti-patterns, fit check vs Anton's taste.
3. Add a row to `patterns/README.md` and a dated line to `CHANGELOG.md`.
4. Attribute it to Anton + the game + the date. If an existing pattern already covers it,
   **extend that file** instead of duplicating.
5. Verify current facts before writing (game names, mechanics, any cited study) — don't rely on
   stale memory.

## Output
Answer in chat: verdict + why + the pattern(s) at play. For a substantial design artifact (a full
core-loop or level-arc spec), save a dated doc to `DOCS/design/YYYY-MM-DD-<topic>.md`. New
insights become `patterns/` files (above), not chat-only.

## Keep this skill current (it's part of the job)
This skill is meant to **grow with every game Anton plays.** Proactively:
- **A mechanic insight from play** → new `patterns/` file + index + changelog.
- **New craft knowledge / research** → fold into `design-craft.md`.
- **A pattern proven or disproven in our own playtests** → update its Status and note the evidence.
- **Always** append a dated line to `CHANGELOG.md`. When unsure whether an observation is a
  durable pattern vs a one-off, capture it as `Status: promising` rather than dropping it.
