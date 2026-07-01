# unity-3d — Unity + iOS technical reality

**Purpose:** Unity proficiency for building and shipping hyper/hybrid-casual games to the iOS
App Store — calibrated to a **solo dev driving Unity agentically from Claude Code.**

**Use this lens for:** project/version setup, driving the Unity Editor via MCP, performance
optimization, code architecture, libraries/plugins, and the iOS build & App Store pipeline.
(Detail lives in the repo skill's `references/` and `guides/`; this is the portable summary.)

## Setup defaults (boring & stable on purpose)

> **Spend the novelty budget on game feel, not infrastructure.** Versions move — verify EOL/
> pricing before locking in.

- **Unity 6.3 LTS (6000.3)** — released Dec 2025, supported through Dec 2027. LTS = API
  stability long enough to ship + run LiveOps without a forced mid-life migration. ⚠️ Unity Hub
  defaults new projects to the newest *Supported Update* (e.g. 6.5) — fine for throwaway
  prototyping, but **drop to 6.3 LTS the moment you commit to a shippable game** (Supported-
  Update APIs can be removed in the next release). **Pin the exact patch version.**
- **URP** (Universal Render Pipeline), always — the mobile standard; Built-in RP deprecated as
  of 6.5; HDRP is for high-end PC/console, ignore.
- **2D vs 3D:** match the template to how the core mechanic moves. An arrow/sort/tile puzzle =
  **2D (URP)** template.
- **IL2CPP + ARM64** — mandatory for iOS.
- **Licensing:** Runtime Fee was cancelled (Sept 2024, hasn't returned). **Personal = free**
  (revenue/funding cap $200K, splash optional in Unity 6) — almost certainly all that's needed
  for v1. Start free.

## Agentic Unity stack (how I actually build)

- Drive the Unity Editor from Claude Code via the **CoplayDev/unity-mcp** MCP server — the
  agentic compile-and-test loop (agent edits C#, triggers compile, reads errors, iterates).
- The **official Unity MCP is paid / pre-release** — use the open CoplayDev one for now.
- Tier-0 dependencies via **OpenUPM**. Keep the dependency list lean.

## Code architecture (agent-friendly)

- **ScriptableObjects** for data/config; **asmdefs** to split assemblies (faster compiles,
  clear boundaries); keep gameplay logic in **testable plain C#** decoupled from MonoBehaviours
  where practical. Structure so an agent can reason about and modify it without re-deriving the
  whole project.

## Performance (mobile budget)

Watch **draw calls, overdraw, GC allocations**; use **ASTC** texture compression; profile real
frames (don't guess); IL2CPP for release. Hyper-casual is graphically simple — most wins come
from batching, avoiding per-frame allocations, and keeping overdraw down.

## Useful libraries

- **PrimeTween** — tweening/animation (juice, feel).
- **UniTask** — allocation-free async/await.
- **Ad / IAP SDKs** — via a mediation layer (ties into the monetizer's ads-first v1 stack).

## iOS → App Store pipeline (the gotchas)

Unity → **Xcode export** → signing → **TestFlight**. Watch the solo-dev landmines: code
**signing**, **privacy manifests** (PrivacyInfo.xcprivacy — required), **ATT** (App Tracking
Transparency prompt, relevant for ad attribution), and automate the repetitive build/upload
with **Fastlane**. There's a step-by-step "Unity → Xcode → TestFlight" guide in the repo skill.

> Unity / MCP / Apple landscape moves fast. Treat specific versions, dates, SDK names, and
> pricing here as **possibly stale** — verify before locking anything in.
