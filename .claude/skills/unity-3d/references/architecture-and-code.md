# Architecture & Code Structuring (Unity 6)

Unity-specific patterns for a strong engineer new to gamedev (OOP/SOLID assumed). The
throughline: the patterns that make Unity code clean are **also** what make a project
agent-friendly. Pair with `agentic-unity-mcp.md` and `unity-setup-and-hypercasual.md`.

> Anton's known failure mode is over-engineering. Most "architecture pain" comes from fighting
> Unity's model instead of leaning into it. For a small calm puzzle game, **adopt the light
> version of every pattern below** — skip the maximalist versions.

## The one mental-model shift

Unity is **not** classic OOP where you model a domain as a class hierarchy and `new` it up. It's
a **component-composition runtime** (`GameObject` = identity + bag of `Component`s) with a
**data-as-assets layer** (`ScriptableObject`, prefabs, scenes) serialized and edited *outside
code*. A "player" isn't `Player : Character : Entity` — it's a GameObject with `Health`,
`Movement`, `InputReader` components composed together (a class has single inheritance; a
GameObject holds many components — composition is structurally enforced).

## MonoBehaviour lifecycle (encode in muscle memory)

`Awake → OnEnable → Start → [FixedUpdate* → Update → LateUpdate] → OnDisable → OnDestroy`
- **Awake:** init internal state + cache `GetComponent` refs (runs once, before any Start).
- **OnEnable/OnDisable:** subscribe/unsubscribe events here (symmetric → no leaks).
- **Start:** resolve *cross-object* references (safe — all Awakes done).
- **Update:** per frame (`Time.deltaTime`). **FixedUpdate:** physics/Rigidbody forces only.
  **LateUpdate:** camera follow / react to this frame's movement.
- Never `new` a MonoBehaviour or use its constructor — Unity instantiates them.

**When NOT to use a MonoBehaviour → use a plain C# class (POCO):** pure logic/rules/algorithms
(scoring, puzzle validity, a state machine's transition table), data models, and **anything you
want to unit-test without the editor.** Rule: *MonoBehaviour for "things in the world + the
event loop"; plain C# for "logic and data."*

## ScriptableObject architecture

An SO is a serializable data container that lives as an **asset on disk** (not on a GameObject).
The seminal talk: **Ryan Hipple, "Game Architecture with ScriptableObjects," Unite Austin 2017**
(commonly mis-cited as GDC). Three patterns:
1. **SO Variables** — a primitive wrapped in an asset (`FloatVariable`). Systems reference the
   *asset*, not each other (player writes `PlayerHealth`, UI reads it — neither knows the other).
2. **SO Event Channels** — an SO acts as a broadcast channel; raise on the asset, listeners
   subscribe to it. Zero hard refs between broadcaster and listener.
3. **Runtime Sets** — an SO holding a `List<T>` objects add/remove themselves to on
   OnEnable/OnDisable (e.g. "all active enemies"). Replaces `FindObjectsOfType`/singletons.

**Upside:** decoupling, designer-tweakable in the Inspector (balance without recompiles),
testable in isolation, shared state survives scene loads. **Cons:** runtime edits to SO assets
*persist into the asset* in-editor (surprises everyone once); indirection overload + asset
sprawl; "who raised this event?" is harder to trace. **For a small game:** adopt SO **events** +
a handful of SO **variables** for genuinely cross-system/cross-scene state (level, score,
settings). **Skip the "everything is an SO" maximalism** (over-engineering).

## Dependency injection / services

**Don't reach for a full DI container (VContainer/Zenject) on a v1 small game** — wiring overhead
> benefit at that scale. **Do** apply DI's *principle*: depend on interfaces, pass dependencies
in explicitly (constructor injection on plain-C# logic classes), wired in **one bootstrap
"composition root" MonoBehaviour**. 80% of the testability/decoupling for ~0% framework cost. If
manual wiring ever becomes genuinely painful (many systems/scenes), **VContainer** is the modern
pick (zero-alloc, ~5-10× faster than Zenject, OpenUPM-installable).

- **"Managers" anti-pattern:** `GameManager` as a junk drawer = god-object. Prefer focused
  **services** with one responsibility (`ScoreService`, `LevelLoader`, `AudioService`).
- **Singletons:** pragmatically fine for a *genuinely single* global coordinator (one
  `AudioManager` via `DontDestroyOnLoad`). Abuse = ambient global access for everything (hidden
  coupling, kills testability). A **Service Locator** is the less-coupled middle ground.

## Event/messaging (decoupling toolbox)

| Mechanism | Use when | Watch out for |
|---|---|---|
| **C# `event`/`Action<T>`** (the workhorse) | code-to-code decoupling; fast, debuggable | must unsubscribe (leaks); not Inspector-visible |
| **UnityEvent** | designer wires UI responses in Inspector | slower, harder to debug, **invisible to code/agents** |
| **SO Event Channel** | cross-system/scene events, zero hard refs | traceability; asset sprawl |
| **Static event bus** | quick global decoupling | global state, ordering, can become a junk drawer |

C# events are the default for logic↔logic; SO event channels for designer-visible, scene-
independent decoupling. ⚠️ **UnityEvents are invisible to anything that only reads code** — see
agent-friendly note below.

## State machines

Two uses: **game flow** (`Boot → Menu → Playing → Paused → GameOver` — a single high-level FSM on
a persistent manager is one of the highest-value structural decisions) and **entity behavior**
(minimal for a calm puzzle). Implementations lightest→heaviest: `enum`+`switch` (≤3 states) →
**State pattern** (one plain-C# class per state implementing `Enter/Tick/Exit` + a `StateMachine`
— recommended, scalable, **unit-testable, keep out of MonoBehaviours**) → hierarchical FSM
(overkill v1). ⚠️ **Don't encode game logic in the Animator state machine** — it's for animation,
and it's invisible to code and untestable.

## Assembly definitions (asmdef)

Carve scripts into separately-compiled DLLs → **faster iteration** (only changed assembly +
dependents recompile — matters for the agentic compile loop), **compile-time-enforced layering**
(cycles are *forbidden*: if Gameplay→Core, Core *cannot* →Gameplay), test isolation. Recommended
small-game layout (deps point one way, toward Core):
```
Core/      Game.Core.asmdef        ← pure C# logic, minimal Unity-scene deps
Gameplay/  Game.Gameplay.asmdef    ← references Core
UI/        Game.UI.asmdef          ← references Core (+Gameplay if needed)
Tests/EditMode/ Game.Tests.EditMode.asmdef   Tests/PlayMode/ ...
```
**Start with ~3-4 assemblies, not 15** — each has overhead and forbidden cycles can box you in.

## Testing

**Unity Test Framework** (NUnit). **EditMode** tests (no runtime, no MonoBehaviour callbacks,
fast — where most worthwhile tests live) vs **PlayMode** (spins up runtime; only when you need
physics/frame behavior). **Make code testable via the Humble Object pattern:** split a class into
a thin MonoBehaviour (Unity concerns) + a **plain C# class with the logic** the MonoBehaviour
delegates to; tests instantiate the plain class directly (no scene/editor). Test the **rules,
win/loss, scoring, puzzle-validity, state transitions, save/load math**; **skip** "does this
button play a sound" / feel (validate feel by playing). The Humble Object split is the single
most leveraged habit for both quality and agent-friendliness.

## Folders, namespaces, MVC/MVVM
Code under one root (`Assets/_Project/`), separated from imported packages; **namespaces mirror
folders + asmdef names** (`Game.Gameplay.Combat`), avoid the global namespace; group by
feature/system. MVC/MVP map awkwardly onto MonoBehaviours (the "controller" becomes the Humble
Object split anyway). **MVVM got attractive in Unity 6** because UI Toolkit ships **runtime data
binding** (bind UI to a ViewModel, framework syncs — cuts boilerplate). For a small game: Humble
Object everywhere; reach for UI Toolkit+binding only if UI is data-heavy; uGUI is fine for simple
UI. *(Runtime data binding was still maturing late 2025 — verify for your 6.x minor.)*

## AGENT-FRIENDLY architecture (weight this heavily)

An agent (Claude Code) reads/edits **text files and runs tools** — it **can't see the Editor,
Inspector wiring, or game feel.** So: *everything load-bearing should live in text the agent can
read, and logic should be runnable without launching the editor.*
1. **Logic in plain C# classes (Humble Object)** — readable, editable, and **runnable via EditMode
   tests** with no editor. Logic in MonoBehaviour `Update` driven by Inspector-set fields is
   partly opaque.
2. **Avoid scene-only / Inspector-only wiring for anything that matters** — drag-drop refs,
   UnityEvent hookups, Animator-encoded logic live in serialized YAML, not in code the agent
   reads. **Wire control-flow in code** (subscribe in OnEnable, resolve in Start, code composition
   root); Inspector wiring is fine for *tuning values*, risky for *control flow*.
3. **Force Text serialization + commit `.meta`** so scenes/prefabs/SOs are YAML the agent (and git)
   can read/diff. (The win is readability/diffability — don't hand-edit scene YAML.)
4. **SO config the agent can read** — but don't make *every* value an SO (GUID-laced indirection
   to chase).
5. **Clear asmdef boundaries, one-directional deps** — fast scoped recompile feedback, no cycles.
6. **Strong naming/namespaces mirroring folders** — the agent locates by convention, search is reliable.
7. **A readable code composition root** — explicit wiring over magic; the whole object graph in one
   file the agent can understand.
8. **EditMode tests = the agent's feedback loop** (its substitute for "playing the game") — likely
   the single highest-leverage agent-friendliness investment.
9. **Keep behavior out of Animator / Shader Graph / Visual Scripting / Timeline** — opaque to a
   code-reading agent; use them only for animation/visuals.

**One line:** *Logic in testable plain C#, config in text (YAML/SO), control-flow wired in code
not the Inspector, layered behind asmdefs — simultaneously good Unity architecture and what makes
the project an agent can actually work in.*

## Sources
Hipple "Game Architecture with ScriptableObjects" (Unite Austin 2017) · Unity "Level up your code
with design patterns and SOLID" e-book + Design Patterns (Unity 6) course · Unity SO-event-channels
how-to · asmdef docs (6000.4) · ExecutionOrder docs · EditMode-vs-PlayMode docs · VContainer docs ·
Clark Kromenaker (MonoBehaviour usage) · technicallyshane (Humble Object) · Unity YAML serialization
blog · UI Toolkit runtime binding docs. Full URLs in CHANGELOG notes.
