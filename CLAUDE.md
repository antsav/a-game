# CLAUDE.md

Context for working on this project. Read this first.

## Who I am

I'm Anton — an experienced software architect and engineer with deep knowledge of
complex systems. **I have zero game development experience.** Calibrate accordingly:
I don't need software engineering fundamentals explained, but I do need game-specific
concepts, Unity conventions, and gamedev intuition made explicit rather than assumed.

I previously built a text-to-speech Chrome extension that earns ~$2,200/month. It
succeeded by solving a real problem and iterating on emerging demand — **not** by
inventing a new category. I'm applying that same philosophy to games.

## My philosophy for this project

- Find an emerging trend with **moderate competition**, build a **better version**, and ship.
- **Validation and market fit over complexity.** Practical, ship-able games — not
  groundbreaking concepts.
- Iterate on real demand rather than betting on novelty.
- I'd rather ship a focused, polished clone-plus than a sprawling original idea.

When advising me, bias toward what gets a real product in front of real users on the
App Store. Push back on scope creep. Flag when I'm over-engineering (a known risk given
my background).

## What I know / don't know

- **Strong:** software architecture, complex systems, scripting, general engineering.
- **Some exposure:** Unity basics — colliders, GameObjects, interactions, scripting.
- **No experience with:** the gamedev craft (game feel, juice, level/loop design),
  the iOS publishing pipeline, mobile monetization, ASO, or shipping a game end-to-end.

## Tech stack

- **Engine:** Unity
- **Target platform:** iOS (mobile-first)
- **Language:** C#

## Secrets & API keys

- API keys and secrets live in **`.keys.local`** files (gitignored, `KEY=value` per
  line). There is a **root** `.keys.local` for repo-wide keys, and a scope may keep
  its **own** `.keys.local` for keys local to that scope (e.g. an upload token or a
  signing credential under a specific scope, e.g. an upload or signing key).
- **Resolution:** read the nearest scope's `.keys.local` first, then fall back to the
  root for anything not defined there.
- Each `.keys.local` has a committed **`.keys.local.example`** next to it documenting
  which keys exist — keep it in sync (add the key name with an empty value when a new
  secret is introduced), but never put real values in it.
- The `.keys.local` ignore rule matches at any depth, so scope-level files are
  excluded automatically.
- **Never** hardcode a secret in source, scripts, or docs; never print a real key
  value to the terminal or commit it. If a key looks exposed, flag it for rotation.

## Project status

- **Stage:** very early. Repo: `antsav/a-game`.
- **Game concept:** NOT YET LOCKED IN. Still at the trend-scouting / validation stage.
  *(This is the single most important section to update once a concept is chosen —
  see "Decisions to make" below.)*

## How I want you to help

1. **Scout game trends** — surface emerging mobile/iOS trends with moderate competition.
2. **Validate ideas** — sanity-check market fit, competition, and demand before building.
3. **Think through gameplay mechanics** — core loop, controls, progression, retention.
4. **Guide technical decisions** — Unity architecture and iOS-specific concerns,
   kept proportionate to a first shippable game.
5. **Map out learning paths** — what I need to learn, in what order, to ship.

## How to work with me

- Be concise and direct. Skip engineering 101; don't skip gamedev specifics.
- Prefer practical, ship-oriented advice over theoretical completeness.
- Call out scope creep and over-engineering explicitly.
- When recommending an approach, note the validation/market-fit angle, not just the tech.
- For anything time-sensitive (trends, App Store data, Unity/iOS changes), verify
  current info rather than relying on stale assumptions.

## Decisions to make (update as resolved)

- [ ] Lock in the game concept (genre, core loop, the "better version" angle).
- [ ] Identify the specific trend being targeted and the competition being improved upon.
- [ ] Define the minimum shippable scope for a v1 App Store release.
- [ ] Choose monetization model (ads / IAP / paid) and how it shapes design.
- [ ] Set up the Unity project structure and iOS build pipeline.
- [ ] Decide on a validation method before heavy building.

## Repo conventions

This is a **monorepo** consolidating everything for the game effort — research,
context, iterations, and (later) the shipped game.

- **Structure is intentionally flat.** Current top-level layout:
  - `DOCS/` — durable material: research & trend scouting, concept validation, the
    decision log, learning paths, build/release notes.
  - `.claude/skills/` — project-scoped custom skills (build them with
    `/skill-creator`).
- Add a new top-level scope **only when there's real material to put in it** — don't
  pre-create empty folders (avoids speculative scaffolding).
- **Context scopes are `CLAUDE.md` files** (uppercase). The root one is global; a
  scope dir may carry its own `CLAUDE.md` that Claude Code auto-loads when working
  there.
- Secrets: see "Secrets & API keys" above — `.keys.local` only, never committed.
- *(Unity scene organization, naming, asset pipeline, branch strategy: fill in once
  a concept is locked and a Unity project exists.)*