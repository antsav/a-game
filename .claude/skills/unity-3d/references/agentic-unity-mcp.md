# Agentic Unity via MCP + Claude Code (the centerpiece)

How to drive the Unity Editor from Claude Code via MCP so an agent can write a script →
compile → read console errors → fix → enter Play mode → run tests, in a loop. Pair with the
`guides/setup-claude-code-unity-mcp.md` walkthrough.

> **Fast-moving space — verify on use.** Unity shipped its *own* official MCP server in
> **May 2026** (open beta, paid). Star counts/versions below are ~late-June-2026 snapshots.
> Re-check before relying on specifics; log changes in `../CHANGELOG.md`.

## The recommendation (solo dev on Claude Code, mid-2026)

**Primary pick: `CoplayDev/unity-mcp` ("MCP for Unity").** Free (MIT), ~11.2k stars, most
active, best Claude-Code integration (a single documented `claude mcp add … stdio` command +
an official Coplay Claude Code guide), and covers the whole loop you care about: console read,
**Roslyn script validation**, GameObject/prefab/scene tools, Play mode, tests, screenshots.
Repo: https://github.com/CoplayDev/unity-mcp · docs: https://coplaydev.github.io/unity-mcp/
(Originally `justinpbarnett/unity-mcp`, acquired by Coplay; old links redirect here.)

**Strong alternative: `IvanMurzak/Unity-MCP`** (~3.4k stars, Apache-2.0, ~52 tools, ships
constantly) — pick it for the tightest develop-and-test loop, **runtime (in-play) AI debugging**,
and "any C# method → a tool in one line." Slightly higher security surface (reflection/dynamic
exec) — keep it localhost+stdio.

**Watch, don't depend on yet: Unity's official MCP server** (`com.unity.ai.assistant`,
2.0.0-pre.1). Nicer security (per-connection approval dialog in Edit > Project Settings > AI >
Unity MCP) but **pre-release and gated behind a paid Unity AI subscription (~$10/mo)**. Revisit
once it leaves beta / decouples from paid AI credits.

(Also exists: `CoderGamester/mcp-unity` — Node/TS over WebSocket; pick only if you want a Node
toolchain.)

## How a Unity MCP server works (architecture)

Two pieces, always:
1. **A Unity Editor package/bridge (C#)** installed into your project (Package Manager git URL,
   OpenUPM, or `.unitypackage`). Runs *inside* the Editor, performs the operations (create
   GameObject, recompile, read console, enter Play mode). **Only acts while the Editor is open**
   with your project loaded.
2. **An MCP server process** (Python for Coplay/IvanMurzak; Node for CoderGamester; a relay
   binary for official) that Claude Code spawns over **stdio**; it translates MCP tool calls into
   messages to the in-Editor bridge and relays results back.

## Wiring it into Claude Code

The Claude Code side (docs-verified, mid-2026):

```bash
# CoplayDev/unity-mcp — official Coplay command (stdio, user scope, long timeout for compiles)
claude mcp add --scope user --transport stdio coplay-mcp \
  --env MCP_TOOL_TIMEOUT=720000 \
  -- uvx --python ">=3.11" coplay-mcp-server@latest

claude mcp list      # expect: coplay-mcp  ✓ Connected
```

- **Transport is `stdio`** (a local process). The `--` separates the launch command. Prereqs:
  Node/npm, **Python ≥3.11**, Claude Code CLI, and **Unity open** with the Coplay package installed.
- **Scopes:** `local` (default, `~/.claude.json`, this project only) · `project` (`.mcp.json` at
  repo root — commit to share; first use needs approval, shows `⏸ Pending approval`) · `user`
  (all your projects). A committable `.mcp.json` entry:
  ```json
  {
    "mcpServers": {
      "coplay-mcp": { "type": "stdio", "command": "uvx",
        "args": ["--python", ">=3.11", "coplay-mcp-server@latest"],
        "env": { "MCP_TOOL_TIMEOUT": "720000" } }
    }
  }
  ```
- **Manage:** `claude mcp get <name>`, `claude mcp remove <name>`, and `/mcp` in-session (status,
  reconnect, per-server token cost). `claude mcp reset-project-choices` resets approvals.
- **MCP startup timeout** default 30s — raise with `MCP_TIMEOUT=60000 claude` (ms) if the server
  is slow to init. (Distinct from the per-tool `MCP_TOOL_TIMEOUT` above for slow Editor ops.)

## Permissions — stop the agentic loop from prompting every call

MCP tools are namespaced **`mcp__<server>__<tool>`** and require approval. Pre-approve in
`.claude/settings.json` (commit it) so the loop runs unattended — but **split read from write**:

```json
{
  "permissions": {
    "allow": [
      "mcp__coplay-mcp__read_console",
      "mcp__coplay-mcp__manage_script",
      "mcp__coplay-mcp__run_tests"
    ],
    "deny": [
      "mcp__coplay-mcp__delete_*"
    ]
  }
}
```

Precedence is **deny > ask > allow**. Allow read/inspect tools freely; require thought for
destructive ones. Avoid blanket `mcp__*`. (2026 note: Claude Code uses **tool search** by default,
deferring tool schemas — so a 40+-tool Unity server doesn't bloat context; check `/context` and `/mcp`.)

## The loop & its friction (real, well-documented)

**The loop:** agent reads Console errors → edits a C# script (`manage_script`, Roslyn-validated
*before* recompile) → Unity recompiles + domain-reload → agent re-reads Console → fixes → enters
Play mode / runs tests → iterates. **Closing the compile loop is the single biggest win** — the
agent self-corrects C# errors without you copy-pasting logs.

**Friction to expect:**
- **The Editor must be open** (no headless agent loop) and focused enough to compile.
- **Domain reloads & compile waits:** after a script edit Unity recompiles + domain-reloads,
  which briefly drops the bridge and stalls tool calls — hence the 12-min `MCP_TOOL_TIMEOUT`.
- **The bridge won't start if there are existing compile errors** — an agent that just introduced
  an error can deadlock itself. Keep the project compiling; fix-forward fast.
- **macOS PATH:** launching Unity from Finder/Hub may not inherit your shell PATH, so the
  relay/CLI can't find `claude`/`uvx`. Launch Unity Hub from Terminal, or use absolute paths.
- **Transport change** (stdio↔http) requires restarting Claude Code.

## What's worth automating (and what isn't)

High value: **(1) close the compile loop** (console read → fix → recompile); **(2) scene setup &
prefab wiring** (assemble scene, attach scripts, wire serialized refs — the tedious click-work);
**(3) Play-mode + EditMode/PlayMode test runs** (verify behavior, not just compilation).
Lower: screenshots (visual feedback, but code-heavy work rarely needs it).

⚠️ **MCP closes the *engineering* loop, not the *juice* loop.** Game feel, timing, and polish need
a human in Play mode — see `../references/` on feel. Don't over-invest agent automation there.

## Security (these are arbitrary-code-execution engines for your Editor)

They run menu items, compile + execute C#, read/write project files, and (IvanMurzak) invoke
arbitrary methods via reflection. ~1 in 4 MCP servers exposes code-execution risk (Help Net
Security, May 2026). Concrete:
- **Bind to localhost/127.0.0.1, use stdio** — never `0.0.0.0`/HTTP on a network interface
  (anyone on your LAN could hit the tools; HTTP can leak keys).
- **Commit everything to a git branch before letting an agent loose** — Editor ops are hard to
  undo and touch many files.
- **Keep the tool surface minimal** (you don't need reflection/dynamic-exec for basic gamedev);
  review tool calls, don't blanket-approve. MCP tool *output is untrusted input* (prompt-injection).
- The official Unity MCP's **per-connection approval dialog** is a genuine edge over community
  servers' "just connect" model.

## Adjacent AI tooling (2026)
- **Unity Muse: DEPRECATED** (killed 2024) → replaced by **"Unity AI"** (in-editor assistant +
  generators, open beta May 4 2026, metered by "Unity Points", paid).
- **Unity Sentis → renamed "Inference Engine"** (`com.unity.ai.inference`) — *runtime* on-device
  ONNX inference; relevant only if the *game itself* uses ML, orthogonal to agentic dev.
- **JetBrains Rider 2026.1** — strong agentic story (AI agent mode, bundled Junie/Claude/Codex,
  redesigned Unity Profiler). Best-in-class C# refactoring also makes a codebase agent-friendlier.
- **Cursor** works with any community MCP server (overlaps Claude Code).

## Sources
CoplayDev/unity-mcp (repo, docs, Claude Code guide at docs.coplay.dev, fix wiki, issue #750) ·
IvanMurzak/Unity-MCP · CoderGamester/mcp-unity · Unity official MCP (unity.com/blog/unity-ai-mcp-how-to-get-started,
docs.unity3d.com com.unity.ai.assistant@2.0) · Claude Code MCP docs (code.claude.com/docs mcp,
permissions, settings, env-vars) · Rider 2026.1 (blog.jetbrains.com) · MCP security (helpnetsecurity
May 2026). Full URLs in CHANGELOG notes. *Stars/versions/subscription gating drift — verify on use.*
