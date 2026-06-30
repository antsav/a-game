# Libraries, Plugins & Dependencies

Keep the dependency list **short**. Hyper-casual games are deliberately thin — most tools here are
about iteration speed, monetization, and analytics, not engine power. Over-engineering risk is high
for an architect: a three-prefab tap game does not earn Addressables, DI, or a serialization library.
Pair with `unity-setup-and-hypercasual.md`. (Monetization *design* lives in `game-monetizer`.)

> Versions and Asset Store prices are sale-volatile — verify in Package Manager / on the Store at use.

## Recommended minimal stack (solo hyper-casual iOS)

**Tier 0 — day one (all free, all UPM/OpenUPM, all agent-friendly):**
1. **PrimeTween** (OpenUPM `com.kyrylokuzyk.primetween`) — tweening/juice. Zero-allocation, clean API,
   safe if target destroyed mid-tween. The modern pick over DOTween; coexists with it (incremental
   migration). DOTween is still fine and has more tutorials, but PrimeTween is more agent-friendly.
2. **UniTask** (OpenUPM `com.cysharp.unitask`) — near-essential. Zero-alloc `async/await` replacing
   coroutines; runs on Unity's PlayerLoop (works on iOS/IL2CPP). You already think in async — UniTask
   gives real async methods with return values, exceptions, cancellation, *less* garbage than coroutines.
3. **TextMeshPro** — text (folded into Unity UI / `com.unity.ugui` in Unity 6; effectively always present).
4. **GameAnalytics** (OpenUPM `com.gameanalytics.sdk`) — free, game-native DAU/retention/funnels/ad+IAP
   revenue. **You can't validate demand (the whole philosophy) without analytics.**
5. **NaughtyAttributes** (git/OpenUPM, free MIT) — inspector quality-of-life (`[Button]`, `[ShowIf]`,
   `[Required]`). The free ~70% of Odin.

**Tier 1 — when monetizing / soft-launching (the unavoidable blobs):**
6. **Unity IAP** (`com.unity.purchasing`, Unity Registry) — remove-ads / coin packs. Plenty; don't add
   a third-party purchasing SDK.
7. **Unity LevelPlay Ads Mediation** (Asset Store + EDM4U) — ad revenue. ⚠️ See dependency caveat below.
   (AppLovin MAX is the strong alternative; pick **one** mediator. Note: from **Apr 1 2026** monetizing
   Unity Ads via the *legacy* Advertisement package is deprecated — use the LevelPlay package.)
8. **Unity Mobile Notifications** (`com.unity.mobile.notifications`) — D1/D7 retention pings (check
   Apple permission UX).

**Tier 2 — buy only if the polish loop justifies it:**
9. **Hot Reload** (~$40; free OSS analog **FastScriptReload**) — edit C# without domain reload. Best
   iteration-speed ROI for a solo dev; serves the "polish to the extra mile" instinct.
10. **Easy Save (ES3)** — only if save data outgrows simple `JsonUtility`.

**Deliberately NOT in v1** (over-engineering flags): Addressables, a DI container (VContainer/Zenject),
Input System (legacy `Input.GetTouch` is simpler for tap-only), Localization, Cinemachine, a third-party
pooling lib (Unity's built-in `ObjectPool<T>` suffices). Add reactively when a concrete constraint forces it.

## Utility choices
- **JSON:** Unity's built-in **`JsonUtility`** for most save data (fast, no dependency); **Newtonsoft**
  (`com.unity.nuget.newtonsoft-json`, Unity Registry) only for dictionaries/polymorphism/nesting.
- **Save/Load:** `JsonUtility` → write to `Application.persistentDataPath`, **temp-file-then-rename**
  for atomicity, a **version field** in every save. **Never `BinaryFormatter`** (deprecated, insecure).
- **Object pooling:** built-in `UnityEngine.Pool.ObjectPool<T>` (Unity 6) — all you need.

## Dependency management (your wheelhouse — and what gates agent-driven work)
- **UPM** is npm-for-Unity. Source of truth: **`Packages/manifest.json`** (declared deps + scoped
  registries) + **`Packages/packages-lock.json`** (resolved exact tree — **commit it** for reproducible builds).
- **Install sources, ranked by reproducibility:** (1) **Unity Registry** (cleanest, fully pinned) →
  (2) **Git URL** packages pinned to a **tag/commit** (never a branch) → (3) **OpenUPM** (add as a
  scoped registry; manage with **openupm-cli**: `openupm add com.cysharp.unitask`) → (4) **Asset Store
  `.unitypackage`** (**least** reproducible: binary blob in `Assets/`, no manifest pin, no clean upgrade).
- **Bias toward UPM-installable packages; accept Asset Store blobs only where there's no UPM equivalent
  (ad SDKs, Odin).** Pin exact versions/tags, commit `packages-lock.json`.

## What aids AGENTIC development
An agent reasons over **files** — the tools it can add/pin/reason about are those declared as text in
`manifest.json`/`packages-lock.json`, not blobs an importer drops into `Assets/`. Criteria:
(a) UPM/git/OpenUPM-installable, (b) allocation-free & deterministic, (c) good public docs.
- **Strongly agent-friendly:** UniTask, PrimeTween, VContainer (if DI ever needed), NaughtyAttributes,
  all Unity official packages, GameAnalytics, Newtonsoft. ✅
- **Agent-hostile (necessary, manage out-of-band):** **ad mediation SDKs (LevelPlay/MAX/AdMob) + EDM4U +
  CocoaPods** — `.unitypackage` blobs, native iOS deps, editor-button "Force Resolve", a `Podfile`. An
  agent can't cleanly add these from files. **Budget real time for the first iOS ad build** (the classic
  pain). Also Odin/Easy Save/Hot Reload/Editor Console Pro (paid Store blobs). ❌
- **Practical rule:** keep everything you can in `manifest.json`/OpenUPM + commit the lock; treat Asset
  Store imports (ads, Odin) as a documented, manual, "human does this once" boundary, isolated in their
  own folders.

## Sources
PrimeTween (GitHub/OpenUPM) · Cysharp/UniTask · GameAnalytics OpenUPM · NaughtyAttributes · Unity IAP
docs · LevelPlay/MAX/AdMob mediation docs (incl. Apr 1 2026 legacy-Ads deprecation) · Unity Mobile
Notifications · Hot Reload / FastScriptReload · VContainer · OpenUPM docs + openupm-cli · Unity manifest
docs · game-save best practices. Full URLs in CHANGELOG notes. *Versions/prices drift — verify on use.*
