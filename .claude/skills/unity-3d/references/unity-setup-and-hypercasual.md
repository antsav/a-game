# Unity Setup & Project Structure for Hyper-Casual iOS

Boring, stable defaults for a new hyper/hybrid-casual iOS game. **Spend your novelty budget on
game feel, not infrastructure.** Pair with `architecture-and-code.md` and `ios-build-pipeline.md`.

> **Versions move — verify before locking in.** Figures below are ~late-June-2026. Confirm EOL
> dates on unity.com/releases and pricing on unity.com/products/pricing; log changes in CHANGELOG.

## Which Unity version

Unity 6 uses a **yearly LTS + intra-year "Supported Update"** cadence:

| Version | Type | Released | Support | Note |
|---|---|---|---|---|
| 6.0 LTS (6000.0) | LTS | Oct 2024 | EOL **Oct 2026** | aging out |
| 6.1 / 6.2 | Supported Update | 2025 | **no longer supported** | don't start here |
| **6.3 LTS (6000.3)** | **LTS** | **Dec 2025** | through **Dec 2027** | **← use this for production** |
| 6.4 / 6.5 | Supported Update | 2026 | until next release | 6.5 (Jun 2026) **deprecates Built-in RP** |

**Use Unity 6.3 LTS (6000.3).** LTS = 2 years of bug fixes + API stability — long enough to
ship and run LiveOps without a forced mid-life migration. ⚠️ **Unity Hub defaults new projects to
the newest Supported Update (6.5)** — fine for throwaway prototyping, but **drop to 6.3 LTS the
moment you're committing to a game you'll ship and patch** (Supported-Update APIs can be *removed*
in the next release). Hyper-casual is graphically simple — you gain nothing from bleeding-edge
rendering. **Pin the exact patch version** in Hub; never change minor version mid-project unless a
store-blocking bug forces it. Use **IL2CPP + ARM64** (mandatory for iOS).

**Licensing:** the **Runtime Fee was cancelled Sept 2024 and has not returned.** Seat-based subs:
**Personal = free** (revenue/funding cap raised to **$200K**, seat cap removed, splash optional in
Unity 6) — almost certainly all you need for v1. Pro (~$2,200/seat/yr) only above $200K. Start free.

## Render pipeline: URP, always

**Use URP (Universal Render Pipeline)** — the default and standard for mobile; "when in doubt,
choose URP." **Built-in RP is deprecated as of 6.5** — don't start on it. **HDRP is for high-end
PC/console** — wrong tool for phones, ignore. URP's only "cost" is dropping high-end features
(volumetrics, motion blur) you actively don't want for hyper-casual.

**2D vs 3D (a real decision for your genre):** match the template to how your core mechanic moves.
- **2D game** (puzzle/match/tile/swipe — e.g. your arrow/sort puzzle): **2D (URP)** template —
  Sprite renderer, 2D physics/lights, tilemaps. Cleaner if fundamentally flat.
- **Simple-3D game** (one satisfying 3D mechanic): **3D (URP)**, kept **unlit / single
  directional light, flat-gradient materials, no realtime shadows or baked GI** — that flat look is
  *both* the hyper-casual visual language and trivially cheap on a phone.
- **Don't build a 2D game in a 3D project "for flexibility"** — that's the over-engineering to avoid.

## Day-one settings (the gamedev defaults a first-timer misses)

**Player Settings → iOS:**
- **Graphics API: Metal only** (remove OpenGLES — deprecated on iOS; Metal required for Linear).
- **Orientation: lock it** — most hyper-casual is **Portrait** (one-handed). Set Default = Portrait,
  not Auto.
- **Minimum iOS version:** a sane floor (≈ current-minus-2/3 majors); verify against App Store minimums.
- **Bundle identifier + signing team** — set early so device builds just work.

**Player → Other:**
- **Color Space: Linear** (correct lighting/gradients; requires Metal — set now, recoloring later
  is painful).
- **Scripting Backend: IL2CPP**, **ARM64**.

**Quality:** trim to **1-2 mobile levels** (not the 6 desktop presets); disable realtime shadows /
high AA / soft particles you won't use. With URP these knobs live on the `UniversalRenderPipelineAsset`.

**Frame rate (do in code — classic beginner gap):**
```csharp
// In a persistent bootstrap manager's Awake():
Application.targetFrameRate = 60;   // mobile defaults to 30 — feels sluggish for "juicy" feel
QualitySettings.vSyncCount = 0;     // required for targetFrameRate to take effect
```
60 is the safe, battery-friendly default (120 on ProMotion is optional later).

## Folder structure (small game — flat and obvious)

```
Assets/
  _Project/              # YOUR game (leading underscore sorts it to the top)
    Scenes/  Scripts/  Prefabs/
    ScriptableObjects/   # data assets: levels, difficulty curves, configs, balance tables
    Art/ (Models, Materials, Textures, Sprites)
    Audio/ (Music, SFX)   UI/   Settings/  # URP assets, input actions
  ThirdParty/            # Asset Store / SDK imports (.unitypackage)
  Plugins/               # native plugins / iOS frameworks
```
Rules: keep your code/art under one root (`_Project/`), third-party isolated (clean upgrades/
removals); **no spaces in names** (CamelCase — build tools choke on spaces); group by *type* for a
small game (only graduate to group-by-feature when large); **ScriptableObjects for config/levels**
so you can tune balance in the Inspector without code (fits the ship-and-iterate-on-data instinct).

**Assembly definitions (`.asmdef`):** yes, but lightly. Primary payoff = **compile-time/iteration
speed** (edits recompile only that assembly + dependents — matters a lot for the agentic
compile loop). Minimal split: one gameplay assembly (`Game.Core`) + one `Game.*.Editor` for
editor tooling; leave SDKs with their own. **Don't shard into ten assemblies on day one** — split
only when compile times or coupling actually hurt.

## Why Unity for hyper-casual (vs Godot/native)

It's the de-facto standard, and the reasons are **ecosystem, not raw tech**:
- The whole monetization toolchain is first-party/first-class: **Unity LevelPlay**, **Unity IAP**,
  analytics integrate *inside the Editor*. Ad-funded hyper-casual lives on mediation SDKs.
- **Publishers (Voodoo, Homa, Rollic, Supersonic) build their SDKs/tooling Unity-first** — being on
  Unity removes pitch friction; Godot adds it.
- **Every ad network ships an official Unity SDK** (MAX, AdMob, LevelPlay); on **Godot first-party
  mobile ad SDKs don't exist** (community plugins lag) — real revenue risk for an ad-funded game.
- Best docs + biggest tutorial pool for your zero-gamedev ramp.

Godot is fine for a *paid* indie game; **native** throws away the tooling/asset/cross-platform layer.
For ad-monetized hyper-casual, **Unity is the obvious pick.**

## Version control (Unity is not a normal codebase)

Set up **before the first commit**:
1. **Asset Serialization → Force Text** (Project Settings → Editor) — scenes/prefabs/SOs as YAML so
   Git can diff/sometimes merge (binary scenes can *never* merge).
2. **Commit `.meta` files always**, beside their asset — they store the **GUID** linking assets to
   references. Lose a `.meta` → Unity regenerates a new GUID → silently breaks every reference. **The
   #1 Unity-Git footgun.** Never gitignore them.
3. **Unity `.gitignore`** (GitHub's official Unity template): ignore `Library/ Temp/ Obj/ Build(s)/
   Logs/ UserSettings/` + IDE files. (Repo root `.gitignore` already has these.)
4. **Git LFS** via `.gitattributes` for binaries (`*.png *.psd *.fbx *.wav *.mp3 *.unity`) — the
   `nemotoo/.gitattributes` gist is the reference. (Watch GitHub's small free LFS quota.)
5. **UnityYAMLMerge / "Smart Merge"** as the mergetool for `*.unity/.prefab/.asset/.meta` (ships in
   `Editor/Data/Tools/`). Even solo it saves branch merges.

Commit: `Assets/` (+`.meta`), `Packages/manifest.json` + `packages-lock.json`, `ProjectSettings/`.
Never commit: `Library/ Temp/ Logs/`, build output, `UserSettings/`.

## Standard stack (names only — see `libraries-and-dependencies.md`)
Minimum viable v1: **one ad mediator (AppLovin MAX or Unity LevelPlay) + GameAnalytics + Unity IAP.**
Resist adding more until retention is proven. (Monetization *design* lives in `game-monetizer`.)

## Sources
unity.com/releases/unity-6/support · unity.com/blog Unity 6.3 LTS (Dec 2025) · CGChannel 6.4/6.5
(2026) · endoflife.date/unity · makaka.org best-version · unity.com/blog runtime-fee cancellation ·
URP docs · Metal/color-space/iOS-requirements docs · unity.com/how-to/organizing-your-project ·
asmdef docs · SmartMerge docs · nemotoo gitattributes · unity.com/products/levelplay. Full URLs in
CHANGELOG notes. *Version EOL + pricing are time-sensitive — verify on use.*
