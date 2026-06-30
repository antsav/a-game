# Egg, Inc. (idle / clicker) — the anchor case for "pull to reach more"

**Core loop:** Tap to hatch chickens → chickens lay eggs → sell for cash → buy upgrades/research
that automate and multiply output → when growth plateaus, **prestige** (reset the farm) for
permanent Soul Egg multipliers → start a new, faster farm toward a bigger egg.

**Source of the no-pressure pull:**
- **Numbers always go up — and go up while you're gone.** Offline/idle progress means opening the
  app is *always* a reward, never a chore. "A continuous sense of growth throughout the day."
- **The prestige carrot.** Soul Eggs are a *permanent* currency that survives every reset, so
  resetting never feels like loss — it feels like **banking power.** There's always a bigger egg
  and a bigger multiplier on the horizon. *This is the literal "reach more" pull Anton cited.*
- **Opt-in, non-aggressive monetization** — no forced ads, no energy timers. Nothing takes
  progress away. Cited as the game's *"primary moat: lack of aggressive monetization, building
  long-term trust."*

**Engaging without urgency:** The tension is **optimization** (which upgrade/research next for max
marginal growth), not "survive the clock." Classified as a **run-based prestige system** (rewards
tied to *progression reached*, not raw idle time) → keeps the brain on a tiny optimization puzzle.
**Difficulty scales *with* you** — "progress feels earned but never impossible."

**Difficulty / pacing — three nested horizons (the longevity secret):** seconds-minutes (tap, buy,
watch the counter tick) · hours-days (next egg type, contracts/research) · weeks-months (accumulate
Soul Eggs toward the ultimate egg). The long horizon is deliberately *un-rushable* — rewards
patience, not panic.

**DNA to extract:**
1. **Persistent meta-currency that survives resets** → resets = *banking*, never *losing* (the
   single most important idle mechanic to steal).
2. **Offline/passive progress** → every session-open is a gift; voluntary return without nagging.
3. **Run-based (not time-based) rewards** → keeps the brain on optimization.
4. **Multi-horizon goals** (5-second / 5-day / 5-week carrots).
5. **Non-punishing economy** — costs scale exponentially but the next thing is always affordable soon.

**Solo-dev buildability: HIGH** (Egg Inc. is essentially one developer, Auxbrain). The core math is
a spreadsheet (exponential cost curves, multipliers, a few saved floats); offline-progress = elapsed
time × rate on resume (trivial in C#); the 3D chickens are polish, not the loop. No real-time engine
load, physics, or netcode for v1. **The real risk is economy balancing** — budget spreadsheet time;
treat prestige as your balancing tool, not just a feature. **Best layered *into* a calm puzzle (see
`../references/genre-dna.md` bridge insight)**, not shipped raw.

**Sources:** Egg, Inc. Wikipedia + Fandom wiki · "Math of Idle Games" Part III (GameDeveloper, Feb
2017) · eScholarship idle-engagement study. Accessed Jun 2026. *(One 2026 sentiment source is an
aggregator — directional.)*
