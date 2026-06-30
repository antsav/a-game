# Performance Optimization (Unity 6, mobile/iOS)

> **Calibration:** a hyper-casual/simple-puzzle game is **fill-rate and CPU-frame-time bound**, not
> geometry-bound. You will almost never need ECS/DOTS, Burst, GPU Resident Drawer, or Addressables.
> The whole performance story is usually: **zero-GC gameplay + low overdraw + compressed assets + a
> sane mobile URP asset + on-device profiling.** Everything heavier is the over-engineering trap.
> Dev-blog byte/percentage figures below are directional — verify against your own device profiling.

## The most impactful 20% (do these; skip the rest)
1. **Kill per-frame GC → 0 B/frame in gameplay** (object-pool spawns; cache strings/`WaitForSeconds`;
   update UI text only on change). The #1 cause of hitches.
2. **Control overdraw, esp. UI** (tight sprite meshes, no big transparent panels, disable
   `raycastTarget` on non-interactive UI). Fill rate is your likely bottleneck.
3. **Cache component refs; no `GetComponent`/`Find`/`Camera.main` in Update.**
4. **Enable SRP Batcher + atlas sprites** → low draw calls.
5. **ASTC 6×6 textures, capped sizes, mipmaps off for UI/2D; Vorbis+Streaming music, 22 kHz mono SFX.**
6. **Tune the mobile URP asset** (render scale 0.8-0.9, MSAA ≤2× or off, HDR off, no realtime
   shadows, Unlit/Simple Lit, Store Actions = Auto/Discard).
7. **2D physics if 2D; trim collision matrix; primitive colliders only.**
8. **IL2CPP + managed stripping Medium/High (+link.xml) + Strip Engine Code + "smaller builds."**
9. **Profile on the lowest-end iPhone you support, dev build, every milestone. Steady 60 fps, watch thermals.**

**Consciously skip/defer:** Jobs/Burst/DOTS, GPU Resident Drawer, Addressables, static batching,
aggressive LOD — add only when a profiler on a real device demands it.

## Rendering / draw calls
- **SRP Batcher** (URP default, on in Unity 6): batches objects sharing the **same shader variant** —
  the single most important rendering setting. Keep shader count low so batches stay long.
- **GPU Instancing** (material checkbox): many copies of the *same mesh+material* (grid of identical
  tiles). ⚠️ **Mutually exclusive with SRP Batcher per object** — SRP Batcher for many *different*
  meshes sharing a shader; instancing for many *identical* meshes.
- **Sprite atlasing** (the big 2D win): packs sprites into one texture → batches to **one draw call**
  (Unity 6 = Sprite Atlas V2). Only works if sprites also share material/shader and aren't interleaved
  in sort order by other renderers.
- **Overdraw = the real mobile GPU killer.** UI is the worst (all Canvas geometry is transparent,
  back-to-front, alpha-blended). Detect: Scene view → draw-mode dropdown → **Overdraw**; step draw
  calls in the **Frame Debugger**. Fix: sprite **Mesh Type = Tight**, disable `raycastTarget` on
  non-interactive UI, avoid large transparent images.
- Static/dynamic batching: mostly redundant with SRP Batcher — leave off unless profiling says otherwise.

## Textures & assets (build size + memory)
- **ASTC is the iOS format.** Default **6×6** for most sprites; 5×5 for hero art, 8×8 for backgrounds.
  Power-of-two dims. **Mipmaps OFF for UI/2D** (saves 33% memory), ON for 3D world textures at distance.
  Cap import "Max Size" to display size.
- **Audio:** Vorbis for music (Streaming load type — else whole file in RAM); ADPCM for short frequent
  SFX (taps); 22,050 Hz, mono for SFX. Decompress-On-Load for clips <200 KB.
- **Build size:** target well under ~100 MB (smaller = higher install conversion). Biggest offenders
  are uncompressed/oversized textures and audio.

## Memory & GC (the #1 hitch cause)
Aim **0 B/frame** in steady gameplay (Profiler "GC Alloc" column). Culprits: `new` collections/classes
in Update; **string allocations** (concat, `ToString()` per frame, `Debug.Log`); LINQ; boxing.
- **Object pooling** = the workhorse — reuse via Unity 6's built-in `UnityEngine.Pool.ObjectPool<T>`
  instead of Instantiate/Destroy.
- **Structs** for small short-lived value data (positions, grid coords); classes for identity/shared.
- **Incremental GC** (configurable) spreads collection across frames (smoother), but **not allocating
  is the real fix.** Call `GC.Collect()` deliberately at safe moments (between levels, loading screens).
- **Avoid `Resources/`** (loads its entire contents into the build). Direct prefab refs are fine at v1;
  Addressables only when memory profiling demands it or you need remote content.

## CPU / scripting
- Cache component refs in Awake/Start; `GetComponent` is ~4-5× slower than a cached field — **never in
  Update/loops.** Cache `Camera.main` (it does a tag search). Consider one manager Update over hundreds
  of individual Updates when counts grow.
- **Coroutines vs UniTask:** each `yield`/`WaitForSeconds` allocates — at minimum reuse a cached
  `WaitForSeconds`; **UniTask** is near-zero-alloc async (adopt for lots of timed/async logic).
- **Physics tick:** default Fixed Timestep 0.02s (50 Hz) — often lowerable to 30 Hz on mobile. Set a
  sane Maximum Allowed Timestep (avoid spiral-of-death).

## Physics
- **2D physics (Box2D) if your game is 2D** (~40% less CPU than 3D — directional). Don't pay the 3D tax
  for a flat game.
- **Layer Collision Matrix:** disable pairs that never interact — cheapest high-leverage win.
- **Primitive colliders** (Box/Circle/Sphere/Capsule) over Polygon/Mesh (~6× cheaper per contact).
- Rigidbodies **Discrete** (default); **Continuous** ~doubles cost — only for fast tunneling objects.
  Let idle bodies **sleep**.

## URP mobile settings (the URP Asset)
Dedicated low-end tier: **Render Scale 0.8-0.9**, **MSAA off or ≤2×**, **HDR off**, **Store Actions =
Auto/Discard**, **Depth & Opaque Texture off** (unless a feature needs them), **reduce/disable
shadows** (use a blob-shadow sprite — realtime shadows are very expensive on mobile), **Additional
Lights = Disabled or Per-Vertex**, **Unlit/Simple Lit shaders** (Unlit cheapest, ideal for stylized
hyper-casual). **Post-processing:** each effect is a fill-rate cost; bloom/DoF pricey, Color
Adjustments/Vignette cheap — and post-processing can *negate* MSAA/Render-Scale savings, so measure
the combo on-device.

## Profiling (FIRST, on-device — non-negotiable)
Measure → find the real bottleneck (CPU- vs GPU-bound) → fix → re-measure. **Unity Profiler** (CPU,
Rendering, Memory, GC Alloc), **Frame Debugger** (batch breaks/overdraw), **Memory Profiler package**
(heap snapshots, leaks). **Profile on the lowest-end iPhone you support, in a Development build** over
USB/Wi-Fi — the Editor hides thermal throttling and memory limits. **Xcode Instruments** (Allocations +
VM Tracker for true dirty memory, the metric iOS uses to kill apps) for deep native work. Target steady
**60 fps** (16.6 ms) with frame-time headroom — a steady cooler 60 beats 60-then-throttle-to-30.

## IL2CPP & build
IL2CPP is mandatory on iOS (IL→C++→native). **Managed Stripping Level Medium/High** (+ `link.xml` to
preserve reflection-only code — High can cause "works in Editor, crashes on device" bugs). Enable
**Strip Engine Code**. IL2CPP Code Generation = **"Faster (smaller) builds"** (runtime diff negligible
for hyper-casual). Combine with asset compression + iOS **App Thinning** (Apple ships the device's
variant only).

## Sources
Unity docs (SRP Batcher, GPU instancing, URP "configure for better performance" 6000.3, IL2CPP/stripping,
GC modes, audio compression, physics layer matrix, app thinning, mobile profiling) · ARM ASTC · The
Gamedev Guru (overdraw, texture, GC) · Unity Blog Profiling with Instruments · Memory Profiler docs.
Full URLs in CHANGELOG notes. *Byte/percentage figures are dev-blog directional — verify on device.*
