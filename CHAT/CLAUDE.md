# CHAT/ — Claude.ai Project mirror

## Purpose

This folder is the **source-of-truth I sync into my Claude.ai "a-game" Project**, so I can
talk through the game on the go — evening walks, phone, the Claude app — **without** the
codebase in front of me. It mirrors what my Claude Code setup knows back in the repo,
condensed into **portable summaries** the chat can reason from. Decisions I make in chat get
carried back to the repo, which stays the real source of truth.

## Structure (root of CHAT/)

- **`CLAUDE.md`** (this file) — purpose + how to maintain and sync the folder. **Local
  only — do NOT upload to the chat project.** (Claude Code auto-loads it when working here.)
- **`INSTRUCTIONS.md`** — the project's **custom instructions**: who I am, my philosophy,
  tech stack, project status, the open decisions, and the map of the six "brains."
  → goes into the Claude.ai project's **custom instructions** (or as a knowledge file).
- **`Files/`** — the six **knowledge** references, one per repo skill. → upload all into the
  Claude.ai project **knowledge**. (They land flat in the project; the `Files/` folder is
  just local organization.)

## `Files/` inventory (one per repo skill)

| File | The lens it carries |
|---|---|
| `games-researcher.md` | Concept scouting & validation (what to build, is it worth it) |
| `game-designer.md` | Design craft + mechanic pattern library (is this good design) |
| `my-game-preference.md` | My taste north-star & hard design gates (does this fit me) |
| `game-monetizer.md` | F2P monetization & economy design (how it pays) |
| `game-distribution.md` | Launch, ASO, GTM, publisher-vs-self (how it ships & grows) |
| `unity-3d.md` | Unity + iOS technical reality (how it's built) |

## How to sync into Claude.ai

1. Open the **a-game** project (claude.ai or the mobile app).
2. **Custom instructions** ← `INSTRUCTIONS.md`.
3. **Project knowledge** ← every file in `Files/` (replace the old versions).
4. On later updates, re-upload only the files that changed.

## Maintenance rules (for me — and for Claude Code when I say "update CHAT")

- **Keep `Files/` 1:1 with the repo skills.** One skill = one file. Add / rename / remove
  here whenever a skill is added / renamed / removed, and keep the count in the
  INSTRUCTIONS.md "brains" section accurate (**currently six**).
- **Summaries, not live data.** Capture durable methodology, stances, and gates — *not* live
  market numbers or full reference text. Flag anything specific (number, price, version,
  named game) as possibly stale so I verify it live before acting.
- **Re-export on meaningful change.** When a skill's durable content or the project status
  materially changes in the repo, refresh the matching `Files/` file and bump the status
  date + affected bullets in `INSTRUCTIONS.md`.
- **Decisions flow repo-ward.** Decisions made in chat get carried back to the repo (root
  `CLAUDE.md` "Decisions to make" + the relevant `DOCS/` doc). This folder is a read-mostly
  mirror, not where work is decided.
