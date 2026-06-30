# Unity Project Setup & Agentic-Dev Plan (v0) — 2026-06-29

*First run of the `unity-3d` skill. A concrete, lean technical starting plan for the likely first game
(arrow/untangle or color-sort puzzle — 2D), calibrated to a solo dev driving Unity from Claude Code.
Anti-over-engineering throughout: what to build, and what to deliberately skip.*

## TL;DR
Unity **6.3 LTS + 2D (URP)**, IL2CPP/ARM64/Metal, a flat `Assets/_Project/` layout with **1-2
assemblies**, the **CoplayDev/unity-mcp** server wired into Claude Code, and a **5-package Tier-0 stack**
(all OpenUPM, agent-friendly). Logic in **testable plain C#** so the agent can verify via EditMode tests.
Defer everything heavy (Addressables, DI, ad SDKs) until it's earned.

## 1. Project creation (per `references/unity-setup-and-hypercasual.md`)
- Unity Hub → install **Unity 6.3 LTS (6000.3)** with **iOS Build Support**. (Hub will nudge 6.5 — drop
  to 6.3 LTS for anything you'll ship.) Pin the exact patch version.
- New project: **2D (URP)** template (the arrow/sort puzzles are 2D). Don't build 2D in a 3D project.
- **Day-one settings:** Graphics API **Metal** only; **Linear** color space; **Portrait** orientation
  locked; trim Quality to 1-2 mobile tiers; in a bootstrap `Awake()`:
  `Application.targetFrameRate = 60; QualitySettings.vSyncCount = 0;`
- **Player Settings:** IL2CPP + ARM64; Managed Stripping = Medium; bundle id `com.fenvox.<game>`.

## 2. Version control (per same reference)
Already have a Unity-aware root `.gitignore`. Before first Unity commit: **Asset Serialization → Force
Text**; **Visible Meta Files**; **commit `.meta` files always** (GUIDs); add **Git LFS** `.gitattributes`
for binaries; configure **UnityYAMLMerge**. Commit `Assets/` + `Packages/manifest.json` +
`packages-lock.json` + `ProjectSettings/`.

## 3. Folder & assembly layout (per `references/architecture-and-code.md`)
```
Assets/_Project/  Scenes/ Scripts/ Prefabs/ ScriptableObjects/ Art/ Audio/ UI/ Settings/
Assets/ThirdParty/   Assets/Plugins/
```
Assemblies (start with 2-3, not 15): `Game.Core` (pure logic) ← `Game.Gameplay` ← `Game.UI`, plus
`Game.Tests.EditMode`. Deps point one way, toward Core.

## 4. The agentic loop (per `references/agentic-unity-mcp.md` + `guides/setup-claude-code-unity-mcp.md`)
- Install **CoplayDev/unity-mcp** (Package Manager git URL), confirm the in-Editor bridge is green.
- `claude mcp add --scope user --transport stdio coplay-mcp --env MCP_TOOL_TIMEOUT=720000 -- uvx --python ">=3.11" coplay-mcp-server@latest`
- Pre-approve read/write tools (split) in `.claude/settings.json`; deny `delete_*`.
- **Loop:** agent reads console → edits a script (Roslyn-validated) → recompiles → re-reads → runs
  EditMode tests. Keep the Editor open and *compiling*; commit to a branch before agent runs.

## 5. Agent-friendly architecture from day one (the highest-leverage choice)
- **Puzzle rules / solver / level-gen / validity / scoring = plain C# in `Game.Core`** (no MonoBehaviour)
  → the agent can read, edit, and **verify via EditMode tests** without the Editor.
- **Wire control-flow in code, not the Inspector** (subscribe in `OnEnable`, resolve in `Start`, one
  bootstrap composition root). Inspector = tuning values only.
- Thin MonoBehaviours delegate to the plain-C# core (Humble Object). SO assets for level/config data.

## 6. Tier-0 dependency stack (per `references/libraries-and-dependencies.md`)
All via OpenUPM, commit `packages-lock.json`: **PrimeTween** (juice), **UniTask** (async), **GameAnalytics**
(retention — you can't validate demand without it), **NaughtyAttributes** (inspector QoL), **TextMeshPro**
(bundled). That's it for v1.

## 7. Performance defaults (per `references/performance-optimization.md`)
Bake in the cheap wins now: **object-pool** spawns (built-in `ObjectPool<T>`), **0 B/frame** in gameplay,
**sprite atlas**, **ASTC 6×6** textures, mipmaps off for UI/2D, tuned mobile URP asset (render scale ~0.85,
MSAA off, no realtime shadows, Unlit). **2D physics.** Profile on a real low-end iPhone each milestone.

## Deliberately NOT in v0 (over-engineering flags)
Addressables · DI container (VContainer/Zenject) · Input System (legacy `Input.GetTouch` for tap) ·
Jobs/Burst/DOTS · GPU Resident Drawer · Cinemachine · Localization · multi-currency economy · 15
assemblies · ad SDKs (add at soft-launch — they're the one agent-hostile, CocoaPods/EDM4U manual boundary).

## Path to first build (per `guides/ship-to-ios-testflight.md`)
Once there's a playable loop: Unity → Xcode export → automatic signing (`UnityFramework`=Automatic) →
archive on "Any iOS Device (arm64)" → upload → **TestFlight internal** on your iPhone. Handle the privacy
manifest (`Assets/Plugins/PrivacyInfo.xcprivacy`), `ITSAppUsesNonExemptEncryption=NO`, and (at store
submit) the age-rating questionnaire + privacy-policy URL. ATT/IDFA only matters once ad SDKs are in.

## Cross-skill note
Feel decisions → `my-game-preference`; monetization design → `game-monetizer`; concept/market →
`games-researcher`. This plan is the **technical build** that those three steer.

*Sources: this skill's references + guides. Versions/Apple deadlines are mid-2026 — verify before acting.*
