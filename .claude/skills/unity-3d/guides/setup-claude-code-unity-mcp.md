# Set up the Unity MCP server with Claude Code

**Goal:** Claude Code can drive your open Unity Editor — read the console, edit/validate scripts,
wire scenes/prefabs, enter Play mode, run tests — in an agentic loop. Uses **CoplayDev/unity-mcp**
(the recommended free pick). Background + alternatives: `../references/agentic-unity-mcp.md`.

**Prerequisites:** macOS, the Unity project open in the Editor (Unity 6.3 LTS), **Python ≥3.11**,
Node/npm, Claude Code CLI, and the project **committed to git on a branch** (Editor ops are hard to
undo). Verify the current install command at https://docs.coplay.dev/coplay-mcp/claude-code-guide —
it changes; treat the commands below as a starting point.

## Steps

1. **Install the Unity Editor package.** In Unity: **Window → Package Manager → + → Add package from
   git URL**:
   ```
   https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main
   ```
   (or via OpenUPM `com.coplaydev.unity-mcp`). Open the **"MCP for Unity"** window; confirm the
   in-Editor bridge shows **Running (green)**. ⚠️ It won't start if the project has **compile errors** —
   fix those first.

2. **Register the server with Claude Code** (run in the project dir):
   ```bash
   claude mcp add --scope user --transport stdio coplay-mcp \
     --env MCP_TOOL_TIMEOUT=720000 \
     -- uvx --python ">=3.11" coplay-mcp-server@latest
   ```
   The long `MCP_TOOL_TIMEOUT` (12 min) is important — Editor compiles + domain reloads are slow.
   For a committable, shared setup use `--scope project` (writes `.mcp.json`; first use needs approval).

3. **Verify the connection:**
   ```bash
   claude mcp list      # expect:  coplay-mcp  ✓ Connected
   ```
   In-session, `/mcp` shows status + per-server token cost; `/context` shows context usage.

4. **Pre-approve tools so the loop doesn't prompt every call.** In `.claude/settings.json` (commit it),
   **split read from write**:
   ```json
   {
     "permissions": {
       "allow": [
         "mcp__coplay-mcp__read_console",
         "mcp__coplay-mcp__manage_script",
         "mcp__coplay-mcp__manage_gameobject",
         "mcp__coplay-mcp__run_tests"
       ],
       "deny": ["mcp__coplay-mcp__delete_*"]
     }
   }
   ```
   (Tool names are namespaced `mcp__<server>__<tool>`; precedence is deny > ask > allow. Avoid blanket
   `mcp__*`.)

5. **Run the loop.** Start `claude`, then e.g.:
   ```
   Read the Unity console, fix any compile errors, then enter Play mode and run the EditMode tests.
   ```
   The agent reads errors → edits a script (Roslyn-validated before recompile) → Unity recompiles →
   re-reads → iterates.

## Verify it works
Ask the agent to "create an empty GameObject named MCPTest in the active scene" and confirm it appears
in the Hierarchy. Then have it delete it.

## Troubleshooting
- **`✗ Failed to connect` / exit 127** — `uvx`/`python3` not in PATH. On macOS, **launch Unity Hub from
  Terminal** (Finder-launched Unity may not inherit your shell PATH), or use absolute paths.
- **Tool calls hang/timeout** — a domain reload (after a script edit) briefly dropped the bridge; the
  12-min timeout covers it. If persistent, check the bridge is still green in the MCP-for-Unity window.
- **Bridge won't start** — existing compile errors. The agent that *introduced* an error can deadlock
  itself; fix-forward fast or revert via git.
- **Changed stdio↔http transport** — restart Claude Code to pick it up.

## Safety
Localhost + stdio only (never `0.0.0.0`/HTTP on a network interface). Commit everything to a branch
before agent runs. Keep the tool surface minimal (you don't need reflection/dynamic-exec). MCP tool
output is untrusted input (prompt-injection). MCP runs **outside** the bash sandbox — rely on the
permission rules above.

## Sources
docs.coplay.dev Claude Code guide · github.com/CoplayDev/unity-mcp (+ wiki "Fix Unity MCP and Claude
Code", issue #750) · code.claude.com/docs MCP + permissions. See `../references/agentic-unity-mcp.md`.
