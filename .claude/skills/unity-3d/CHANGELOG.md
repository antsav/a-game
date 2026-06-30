# unity-3d — changelog

Append a dated line whenever the references, guides, or memory change. The Unity/MCP/Apple landscape
moves fast — keep this current. Newest on top.

## 2026-06-29 — initial version
- Created the skill from a 7-stream deep-research pass (6 web agents + the claude-code-guide agent;
  mid-2026 sources, dated & flagged).
- **SKILL.md:** workflow (lean-by-default, agentic-loop guidance, ship guidance) + scalable
  references/guides/memory/scripts structure + self-update protocol + relation to the other skills.
- **references/ (6):** agentic-unity-mcp (centerpiece), unity-setup-and-hypercasual, performance-
  optimization, architecture-and-code, libraries-and-dependencies, ios-build-pipeline.
- **guides/ (2):** setup-claude-code-unity-mcp, ship-to-ios-testflight.
- **memory/ (1 seed):** the agentic Unity stack (6.3 LTS + URP + CoplayDev/unity-mcp + Tier-0 deps).
- Key load-bearing facts (verify on update): **Unity 6.3 LTS (6000.3, Dec 2025)** is the production LTS
  (6.5 deprecates Built-in RP); **URP** always; runtime fee cancelled (Personal free to $200K).
  **Unity shipped an official MCP server May 2026** (paid/pre-release) — **CoplayDev/unity-mcp** is the
  free recommended pick, wired via `claude mcp add --transport stdio`; permissions via
  `mcp__<server>__<tool>` allow/deny, pre-approve for the loop. Perf = zero-GC + low overdraw + ASTC +
  mobile URP asset + on-device profiling (skip Jobs/DOTS/Addressables). Architecture: logic in testable
  plain C#, control-flow in code not Inspector, asmdefs, EditMode tests = agent's feedback loop. Stack:
  PrimeTween/UniTask/GameAnalytics/NaughtyAttributes via OpenUPM; ad SDKs are the agent-hostile manual
  boundary. iOS: privacy manifests (May 2024), ATT + NSUserTrackingUsageDescription, age-rating
  questionnaire deadline Jan 31 2026, Guideline 4.3 spam = #1 hyper-casual rejection.

### Research source URLs (for reference files)
**MCP/agentic:** CoplayDev/unity-mcp (github, coplaydev.github.io, docs.coplay.dev claude-code-guide,
wiki, issue #750) · IvanMurzak/Unity-MCP · CoderGamester/mcp-unity · Unity official MCP
(unity.com/blog/unity-ai-mcp-how-to-get-started, docs.unity3d.com com.unity.ai.assistant@2.0) · Claude
Code docs (code.claude.com/docs mcp, permissions, settings, env-vars, agent-sdk/mcp) · Rider 2026.1
(blog.jetbrains.com) · MCP security (helpnetsecurity May 2026). **Setup:** unity.com/releases/unity-6/
support · Unity 6.3 LTS blog · CGChannel 6.4/6.5 · endoflife.date/unity · makaka.org best-version ·
runtime-fee cancellation · URP/Metal/color-space/iOS-requirements docs · organizing-your-project ·
asmdef docs · SmartMerge · nemotoo gitattributes. **Perf:** Unity docs (SRP Batcher, GPU instancing, URP
configure-for-performance 6000.3, IL2CPP/stripping, GC, audio compression, physics layer matrix, app
thinning, mobile profiling) · ARM ASTC · thegamedev.guru · Unity Blog Instruments · Memory Profiler.
**Architecture:** Hipple "Game Architecture with ScriptableObjects" (Unite Austin 2017) · Unity design-
patterns-SOLID e-book + Design Patterns (Unity 6) course · SO-event-channels how-to · asmdef/ExecutionOrder/
EditMode-vs-PlayMode docs · VContainer · clarkkromenaker · technicallyshane (Humble Object) · YAML
serialization blog · UI Toolkit runtime binding. **Libraries:** PrimeTween · Cysharp/UniTask · GameAnalytics
OpenUPM · NaughtyAttributes · Unity IAP · LevelPlay/MAX/AdMob docs (Apr 1 2026 legacy-Ads deprecation) ·
Mobile Notifications · Hot Reload/FastScriptReload · OpenUPM + openupm-cli · manifest docs · game-save
best-practices. **iOS:** Apple (upcoming-requirements, privacy-manifest-files, required-reason-api, user-
privacy-and-data-use, updated age ratings Jul 2025, App Review Guidelines, ITSAppUsesNonExemptEncryption) ·
Unity iOS build/Player-Settings docs (6000.3) + apple-privacy-manifest-policy · Fastlane gym/match/pilot/
deliver · GameCI iOS · applaunchflow screenshot sizes.
