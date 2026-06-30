# Candy Crush (match-3) — mine for ideas, do NOT build first

**Core loop:** Swap two adjacent candies to line up 3+; matches clear, candies fall to fill gaps
(**cascade** → chain clears), special matches (4/5/L/T) create combinable power-ups — toward a
per-level objective.

**Source of satisfaction / pull:** The **cascade** is the signature engine — one swap triggers a
falling chain of unplanned extra clears (*more reward than you input*, a tiny slot-machine of
competence). Plus deliberate **combo construction** (build + detonate). "Opening space is very
satisfying — players feel the progression."

**Relaxing vs pressure (the most instructive case — Candy Crush split itself on this exact axis):**
| KEEP (relaxing) | DROP (pressure) |
|---|---|
| **Move-limited** levels (N moves, infinite *time* per move) | **Timed** levels (real countdown) |
| Cascades, combos, "opening space" | Lives/energy gating |
| "No booster should be *required*" | Time-bound competitive events |

**The key rule:** **a move-limit is a "soft clock" — stakes without speed.** You can sit on a
move forever. Same principle as the arrow game's collision-stakes.

**Difficulty / pacing:** Authored levels, three rules: one interesting idea per level; ≤4 element
types; player should never *need* boosters. Difficulty varied via **objective type** (clear jelly
/ route ingredients / collect) not timer. Hard spikes every ~3-7 levels with easy runs between.

**DNA to extract:**
- **Cascade = give the player more reward than their input** (gold for calm-yet-engaging).
- **Move-limit, not time-limit** — the canonical way to add stakes to a relaxing puzzle.
- **Objective variety** keeps one mechanic fresh without speed pressure.
- **Never *require* paid help** — keeps it fair and calm.

**Solo-dev buildability: MEDIUM.** Core (swap, match-detect, gravity, cascade) is well-trodden but
fiddly (cascade timing, no-move shuffles, special-piece interaction matrix), and it needs
**thousands of hand-balanced levels** (King has a dedicated team). **Heaviest content burden of all
— don't build as game #1; mine the cascade + move-limit ideas instead.**

**Sources:** PocketGamer.biz "spectrum of flavours" · Fran Ruiz match-3 level-design study ·
Lootbar "Why Candy Crush still feels satisfying 2026." Accessed Jun 2026.
