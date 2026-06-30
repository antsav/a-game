# guides/ — step-by-step Unity workflows

`references/` holds the *knowledge* (how Unity works); **`guides/` holds the *procedures*** —
concrete, ordered, copy-pasteable walkthroughs for the things you do repeatedly (wire up the
Unity MCP server, ship a build to TestFlight, profile a frame, set up a new project). One guide
per file, kebab-case.

This folder grows. Add a guide whenever a multi-step workflow is worked out, so it's repeatable
and an agent can execute it without re-deriving the steps.

## Guide template
```markdown
# <Task>
**Goal:** what you'll have at the end.
**Prerequisites:** tools/accounts/versions needed.
**Steps:** numbered, exact commands/menu paths, expected output per step.
**Verify:** how to confirm it worked.
**Troubleshooting:** common failures + fixes.
**Sources:** URLs + dates.
```

## Index
- [setup-claude-code-unity-mcp](setup-claude-code-unity-mcp.md) — wire CoplayDev/unity-mcp into Claude Code for the agentic loop
- [ship-to-ios-testflight](ship-to-ios-testflight.md) — Unity → Xcode → TestFlight, with the privacy/signing gotchas
