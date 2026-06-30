---
name: unity-3d
description: >-
  Unity engine proficiency for building and shipping hyper-casual / hybrid-casual mobile games to the
  iOS App Store — calibrated to a solo developer driving Unity agentically from Claude Code. Use this
  for ANY Unity task: project/version setup (Unity 6 LTS, URP, 2D vs 3D), driving the Unity Editor via
  MCP from Claude Code (the agentic compile-and-test loop), performance optimization (draw calls,
  overdraw, GC, ASTC, IL2CPP, profiling), code architecture & structure (ScriptableObjects, asmdefs,
  testable plain-C#, agent-friendly design), libraries/plugins/dependencies (PrimeTween, UniTask,
  ad/IAP SDKs, OpenUPM), and the iOS build & App Store pipeline (Xcode export, signing, privacy
  manifests, ATT, TestFlight, Fastlane). Trigger it whenever the work involves Unity, C# gameplay code,
  Unity packages, the Unity MCP server, mobile performance, or building/shipping the game to iOS — even
  if "Unity" isn't said explicitly.
---

# Unity 3D (for hyper-casual iOS, agentic dev)

Unity proficiency for a solo dev shipping a hyper/hybrid-casual game to iOS, **driving Unity
agentically from Claude Code**. Scope is Unity-for-hyper-casual broadly (covers the **2D vs 3D**
choice — the likely first game, an arrow/sort puzzle, is 2D/simple-3D), iOS-first, mid-2026 versions.

> **Anton over-engineers (his stated risk).** A hyper-casual game is three prefabs and a tap handler,
> not a platform. The references repeatedly flag what to **deliberately NOT build** (Addressables, DI
> containers, Jobs/Burst, multi-currency economies, 15 assemblies). Default to the lean version of
> everything; add complexity only when a profiler or a concrete constraint forces it.

## How this skill is organized (scalable, self-updating)

- **`references/` (6):** the knowledge base —
  `agentic-unity-mcp` (**the centerpiece**: MCP servers + Claude Code wiring + the agentic loop),
  `unity-setup-and-hypercasual` (version/URP/structure/version-control),
  `performance-optimization` (mobile/iOS), `architecture-and-code` (patterns + **agent-friendly
  design**), `libraries-and-dependencies` (the stack + UPM/OpenUPM), `ios-build-pipeline`
  (Unity→Xcode→App Store).
- **`guides/`:** step-by-step procedures (`setup-claude-code-unity-mcp`, `ship-to-ios-testflight`).
  Add a guide when a multi-step workflow is worked out.
- **`memory/`:** dated lessons, gotchas, version-notes from real work.
- **`scripts/`:** reserved for build/helper scripts.

## Workflow

**For a Unity how/should question:** pull the matching reference, synthesize a concrete answer, and —
because Anton over-engineers — **say what to skip**, not just what to do. Cite the lean recommendation.

**For agentic Editor work (the core use):** follow `guides/setup-claude-code-unity-mcp.md` to wire the
MCP server, then run the loop (read console → edit script → recompile → re-read → run tests). Remember:
- The **Editor must be open** and **compiling** (the bridge won't start with compile errors).
- **Logic in testable plain C# + control-flow wired in code, not the Inspector** — that's what the agent
  can actually see and verify (see `architecture-and-code.md` "agent-friendly" section). EditMode tests
  are the agent's substitute for "playing the game."
- **MCP closes the engineering loop, not the juice loop** — game feel/timing needs a human in Play mode.
- Commit to a git branch before agent runs (Editor ops are hard to undo).

**For shipping:** follow `guides/ship-to-ios-testflight.md`; the privacy-manifest + ATT + age-rating
steps are the 2024-2026 additions that reject unprepared devs.

## Default stack (mid-2026)
Unity **6.3 LTS** + **URP** + **CoplayDev/unity-mcp** + Tier-0 deps (PrimeTween, UniTask, GameAnalytics,
NaughtyAttributes, TextMeshPro — all OpenUPM, agent-friendly), IL2CPP/ARM64/Metal. Add the ad mediator
(LevelPlay/MAX) + Unity IAP at soft-launch — they're the one agent-hostile, manual-setup boundary.

## How this relates to the other skills
`my-game-preference` decides *what feels right*; `game-monetizer` decides *how it pays*; `games-researcher`
decides *what's marketable*. **This skill builds and ships it.** When monetization SDK work touches the
core loop, defer to `my-game-preference` on feel and `game-monetizer` on the monetization design — this
skill owns the *technical integration*.

## Keep this skill current (the landscape moves fast — part of the job)
Unity versions, the MCP-server landscape, Apple requirements, and package versions change constantly.
On learning something new:
- **A durable technical fact / new best practice** → update the relevant `references/` file.
- **A worked-out multi-step procedure** → add/update a `guides/` file.
- **A dated gotcha, version-note, or "this broke/worked"** → add a `memory/` entry + index it.
- **Always** append a dated line to `CHANGELOG.md`.
Treat any version number, star count, price, or Apple deadline in the references as **possibly stale** —
verify before relying on it, and fix it when it's wrong.
