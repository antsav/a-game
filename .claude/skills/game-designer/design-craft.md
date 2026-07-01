# Design Craft — the hybrid-casual practitioner's toolkit

The durable, taste-neutral craft: *how to design a good, shippable hybrid-casual game.* This is
the discipline; the `patterns/` library is the growing evidence; `my-game-preference` is the taste
gate that decides which of these choices are *Anton's*.

## Why hybrid casual (the trend Anton flagged), calibrated to a FIRST game

**Hybrid casual = a simple hyper-casual core loop + ONE meta/progression layer + blended
monetization (ads *and* IAP).** It's the 2026 successor to hyper-casual: hyper-casual's D7
retention and eCPMs collapsed as CPIs rose; hybrid keeps the instant-fun core but adds a reason to
stay. Reported hybrid **D7 ≈ 16%** and **LTV 3–5× hyper-casual**, because IAP adds upside ads
can't reach. (Sources dated mid-2026 — Unity, Udonis, Homa, Sensor Tower/data.ai summaries.)

**The trap for a first game (Anton's over-engineering risk — flag it):** hybrid casual tempts you
to stack meta systems (map + collection + currencies + battle pass + events…). Don't. For a
*first* ship:
- **One** polished core verb.
- **One** meta layer (a progression map *or* a collection *or* a simple upgrade track — pick one).
- Light economy: one soft currency, maybe one booster. Add the second meta system only after v1
  proves the core is fun and retains.

Industry rule of thumb: a minimum-viable meta is ~4–6 weeks of work (progression map + a
collection/upgrade + soft currency + one booster + one offer). For a first game, trim even that.
**"Simple core, one hook, ship it" beats "sprawling meta, never ship."**

## Anatomy of the game (design it in this order)

1. **Core verb** — the one thing the player does, hundreds of times. (Pull, sort, merge, unblock,
   clear.) If the verb isn't satisfying *raw*, no meta will save it.
2. **Core loop** — action → **instant feedback** → reward → next action. Seconds long. This is
   where "game feel" lives.
3. **Level / session shape** — 1–3 minute levels; the player does several per sitting. Each level
   should follow a deliberate difficulty **arc** (see `patterns/difficulty-arc-peak-end.md`).
4. **Meta loop** — what pulls them back *tomorrow*: a map advancing, a collection filling, a base
   upgrading, offline progress waiting. One horizon beyond the session.
5. **Economy** — light: a soft currency earned by playing, spent on the meta. Keep it legible.

## The core-verb test
Would this verb be satisfying to repeat **1,000 times with no reward attached**? If yes, you have
a game. If it only works because of the rewards bolted on, the loop is hollow — fix the verb
first. (This is the autotelic test; `my-game-preference` makes it a hard gate.)

## Onboarding / FTUE (first-time user experience)
- **Seconds to fun.** First interaction *is* the core verb — no menus, no lecture.
- **Teach by playing.** First level(s) trivially easy; the mechanic reveals itself. (This is also
  the front half of the peak-end arc — start on a high note.)
- **No tutorial walls, no timers, no fail on level 1.** Confidence streak first, complexity later.
- Introduce one new element at a time, and only once the previous is comfortable.

## Retention hooks (build the *pull*, not the push)
- An **always-visible next goal** — the next level, the next unlock, the next collection slot.
- **Multi-horizon goals** — a 5-second goal (this move), a 5-minute goal (this level), a 5-day
  goal (this meta milestone).
- A **daily reason to return** that's a *gift*, not a punishment (offline progress, a daily
  reward) — never a decaying-timer threat. (Taste gate: pull, not push.)

## Feedback & juice (pointer, not duplicate)
Game feel is the craft of instant, responsive, satisfying feedback (<100 ms response, snap/clear
on success, restraint over spectacle for a calm game). The taste-tuned version lives in
`my-game-preference/references/satisfaction-and-juice.md` — use that for *how much* juice is right
for Anton's calm target. Here, just remember: **the final action of a level gets the biggest
feedback** (peak-end).

## Boundary — what this skill is NOT
- Not *what Anton likes* → `my-game-preference` (taste gate; it overrides craft when they conflict
  on feel).
- Not *will it make money* → `game-monetizer`.
- Not *is it marketable / what to build* → `games-researcher`.
- Not *how to build it in Unity* → `unity-3d`.
- Not *how to launch it* → `game-distribution`.

`game-designer` answers: **is this good design craft, and what mechanic pattern applies here?**
