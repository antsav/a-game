---
date: 2026-06-29
type: discovery
tags: [mcp, stack, agentic, versions]
---

**Lesson:** The recommended agentic Unity stack for a solo Claude Code dev as of mid-2026:
**Unity 6.3 LTS (6000.3)** + **URP** + **CoplayDev/unity-mcp** (free, ~11k stars) wired via
`claude mcp add --transport stdio` + a Tier-0 dependency set (PrimeTween, UniTask, GameAnalytics,
NaughtyAttributes, TextMeshPro) — all UPM/OpenUPM and agent-friendly.

**Context:** Built the `unity-3d` skill from a 7-stream research pass. Two big 2026 facts that
override older knowledge: (1) **Unity shipped an official MCP server in May 2026** (`com.unity.ai.assistant`),
but it's pre-release and **gated behind a paid Unity AI subscription** — CoplayDev's free server is the
better pick right now. (2) **Unity 6.3 LTS (Dec 2025) is the current production LTS**, not 6.0/6.2;
6.5 (Jun 2026) deprecated the Built-in Render Pipeline.

**How to apply:** Start a new project on 6.3 LTS/URP; install the Tier-0 deps via OpenUPM (commit
`packages-lock.json`); set up the Coplay MCP server per `../guides/setup-claude-code-unity-mcp.md`.
Keep the ad SDKs (LevelPlay/MAX + EDM4U/CocoaPods) as a documented manual boundary — they're the one
agent-hostile, reproducibility-breaking part of the stack.

**Related:** [[../references/agentic-unity-mcp]] · [[../references/unity-setup-and-hypercasual]] ·
[[../references/libraries-and-dependencies]] · [[../guides/setup-claude-code-unity-mcp]]
