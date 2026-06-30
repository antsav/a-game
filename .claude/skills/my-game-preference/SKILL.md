---
name: my-game-preference
description: >-
  Anton's personal game-taste north-star — what makes a game one HE will love and polish to
  the extra mile: meditative, relaxing yet engaging, single-player puzzle, NO timer, simple
  start, oscillating easy/moderate/hard difficulty, bursts of satisfaction, and an intrinsic
  "pull to reach more" (idle/clicker style) with no pressure. Use this whenever designing or
  evaluating ANY aspect of the game — core loop, mechanics, difficulty, pacing, feel/juice,
  progression, modes, art/audio direction — or deciding whether a feature fits Anton's taste,
  or choosing between concepts/mechanics. Also use to check that a monetization or design
  choice doesn't betray the calm/no-pressure feel. Trigger it for any "should the game do X",
  "does this fit what I like", "how should this feel", or game-design-decision question.
---

# My Game Preference

This skill encodes **Anton's taste** and turns it into a usable design north-star, so whatever
gets built is something he'll love enough to polish to the extra mile. It complements the other
skills: `games-researcher` finds a *marketable* concept, `game-monetizer` makes it *pay* — and
**this makes sure it's a game Anton actually wants to make.** The best concept sits at the
intersection of all three (and happily, his taste — no-timer arrow/sort puzzles + idle pull —
overlaps with what's trending).

## The taste in one line
**Engagement through absorption, not arousal.** Calm focus + satisfying loops + an intrinsic
urge to reach for more — never stress, urgency, threat, or pressure. Meditative *and* engaging
at once.

## How this skill is organized (scalable, self-updating)

- **`preference-profile.md`** — the durable source-of-truth: what Anton loves/avoids, his hard
  rules, and the games he likes with *why*. **Read this first for any taste question.** It's HIM.
- **`design-north-star.md`** — the **actionable decision filter**: run every feature/mechanic
  through it. The fast "does this fit?" checklist.
- **`references/`** — research-backed craft for *achieving* his feel (5 files):
  `relaxing-engaging-design`, `no-pressure-motivation`, `difficulty-and-pacing`,
  `satisfaction-and-juice`, `genre-dna`.
- **`teardowns/`** — per-game DNA analyses of the titles he loves (the evidence + extractable
  mechanics). Grows as he plays more games.
- **`memory/`** — dated lessons and new taste discoveries over time.

## Workflow

**When evaluating a design/feature/mechanic decision:**
1. Run it through **`design-north-star.md`** — especially the one test (*gain+freedom vs
   loss+pressure*) and the hard gates (no timer, no punishing fail, pull-not-push, oscillating
   difficulty, player controls pace).
2. If it touches a specific dimension (difficulty, feel, motivation, a genre choice), pull the
   matching `references/` file for the craft detail; cite a `teardowns/` example where useful.
3. Give a clear verdict — **fits / redesign-to-fit / cut** — with the *why* in Anton's terms and
   a concrete calm-compatible alternative if it doesn't fit.

**When designing something new (a loop, a level system, a mode):**
1. Start from `preference-profile.md` + `genre-dna.md` (and the bridge insight: fuse a calm
   puzzle with an idle/prestige pull + a visibly-growing board).
2. Apply the craft references to make it relaxing-yet-engaging, oscillating, satisfying, calm-juiced.
3. Sanity-check the result against the full `design-north-star.md` checklist.

**When `game-monetizer` and this conflict:** the **feel wins for the core loop.** Monetize via
calm-compatible tools (opt-in rewarded *acceleration*, remove-ads, cosmetic/relaxing IAP, gentle
non-gating boosters); never pressure that betrays the calm. Run monetization through the one test too.

## Output
Answer in chat — a verdict + the why in Anton's terms + a concrete alternative when needed. For a
substantial design artifact (a full core-loop or game-feel spec), save a dated doc to `DOCS/`
(e.g. `DOCS/design/YYYY-MM-DD-<topic>.md`).

## Keep this skill current (it's part of the job)
Anton's taste evolves and he'll discover new games/likes. Proactively update:
- **A new game he enjoys** → add a `teardowns/<game>.md` (extract its calm DNA) + index it.
- **A refined/changed preference** → update `preference-profile.md` (it's the source of truth)
  and, if it changes the filter, `design-north-star.md`.
- **A dated observation, playtest insight, or "this fits / this doesn't" lesson** → add a
  `memory/` entry and index it in `memory/MEMORY.md`.
- **New design research/craft** → fold into the relevant `references/` file.
- **Always** append a dated line to `CHANGELOG.md`. When in doubt whether something is a durable
  preference vs a passing reaction, **ask Anton** before rewriting the profile — it's *his* taste,
  not a guess.
