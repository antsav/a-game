# game-designer — Design craft & mechanic pattern library

**Purpose:** the **craft** of designing a good, shippable hybrid-casual game — core verb,
core loop, difficulty/pacing, onboarding, retention hooks, meta layering — plus a **growing
pattern library** of mechanics harvested from games I play. This is the practitioner's
toolkit; `my-game-preference` is the taste gate that decides which choices are *mine*.

**Use this lens for:** "is this good design craft," "why is this mechanic fun," designing/
critiquing a loop or level, difficulty pacing and session shape, how to layer meta on a
simple core, hybrid-vs-hyper as a craft choice — and **capturing a mechanic I noticed in a
game** ("I saw X in game Y — why does it work / log it as a pattern").

## The one line
**Good craft = a satisfying core verb + a loop with instant feedback + pacing that makes
every level start *and* finish on a high note.** Everything else is layering.

## Hybrid casual, calibrated to a FIRST game
- **Hybrid casual = a simple hyper-casual core loop + ONE meta/progression layer + blended
  monetization (ads *and* IAP).** The 2026 successor to hyper-casual (whose D7 + eCPMs
  collapsed as CPIs rose). Reported hybrid **D7 ≈ 16%**, **LTV 3–5× hyper-casual**.
- **The over-engineering trap (my known risk — flag it):** hybrid tempts you to stack meta
  (map + collection + currencies + battle pass + events). **Don't.** For a first ship:
  **one** polished core verb, **one** meta layer (a map *or* a collection *or* an upgrade
  track — pick one), a light economy (one soft currency, maybe one booster). Add the second
  system only after v1 proves the core is fun. *"Simple core, one hook, ship it"* beats
  *"sprawling meta, never ship."*

## Design it in this order (the anatomy)
1. **Core verb** — the one thing done hundreds of times (pull, sort, unblock, clear). Must
   be satisfying *raw*, and be **one input gesture** (all tap or all slide — never mixed).
2. **Core loop** — action → **instant feedback** (<100 ms) → reward → next action. Seconds
   long. This is where "game feel" lives.
3. **Level / session shape** — 1–3 min levels, several per sitting, each following a
   deliberate difficulty **arc**.
4. **Meta loop** — the one horizon beyond the session that pulls you back tomorrow (a map
   advancing, a collection filling, offline progress waiting).
5. **Economy** — light and legible: one soft currency earned by play, spent on the meta.

## Two hard gates on the verb
- **Autotelic test:** would the verb be satisfying repeated **1,000× with no reward**? If
  only the bolted-on rewards make it work, the loop is hollow — fix the verb first.
- **Single-gesture test:** can the whole loop be played with *one repeated gesture*? If it
  needs both tap and slide, simplify.

## Onboarding / FTUE
Seconds to fun; first interaction *is* the core verb (no menus, no lecture). **Teach by
playing** — first levels trivially easy, no fail on level 1, no timer. Confidence streak
first; introduce one new element at a time, only once the previous is comfortable.

## Retention = pull, not push
An always-visible next goal; **multi-horizon goals** (5-second move · 5-minute level ·
5-day meta milestone); a daily reason to return that's a **gift** (offline progress, a daily
board) — **never a decaying-timer threat**. (Taste gate: pull, not push.)

## The pattern library (the growing part)
One file per mechanic/insight, harvested from games I play. Current flagship patterns:
- **difficulty-arc-peak-end** — the easy→hard→easy intra-level arc; the final action gets
  the biggest feedback ("finish on a high note"). Peak-end rule → stickiness.
- **single-input-modality** — one gesture for the whole loop.
- **forgiving-input** — generous hit targets / undo / no punishing misfires (calm-fit).
> When I share an observation from a game, this is where it gets logged as a reusable
> pattern. Ask me to capture it.

## Boundary — what this is NOT
Not *what I like* (→ `my-game-preference`, which overrides craft on feel), not *will it pay*
(→ `game-monetizer`), not *is it marketable* (→ `games-researcher`), not *how to build it*
(→ `unity-3d`), not *how to launch it* (→ `game-distribution`).

> Retention/LTV numbers are mid-2026 aggregate estimates — directional, verify before acting.
