# Relaxing AND Engaging — Design for Absorption, Not Arousal

The central craft of Anton's taste: a game that's meditative *and* pulls you back. Pair
with `no-pressure-motivation.md` (the pull engine) and `satisfaction-and-juice.md`.

## The core reframe

Most games manufacture engagement through **arousal** (stress, urgency, threat, FOMO) —
which spikes the nervous system. Anton's games work through **absorption**: a calm,
anchored focus where the activity itself is the reward and rumination goes quiet. Mental
model: an absorbing calm action **anchors attention with *just enough* to do that the
brain's default-mode network (rumination/mind-wandering) goes quiet, without spiking
arousal.** That's the target state.

**The design problem isn't "make it relaxing" (trivial — just remove everything). It's
"relaxing *and* still pulls the player back."** Two failure edges bound a narrow band:
- **Too little → boring** (DMN wakes, player ruminates and quits).
- **Too much → stressful** (arousal spikes, no longer calm).
That narrow calm band is the whole craft.

## The cozy framework: safety, abundance, softness

The canonical model (Project Horseshoe 2017 / Daniel Cook "Cozy Games," 2018; Tanya Short
"Designing for Coziness"). Coziness = how strongly a game evokes the fantasy of **safety,
abundance, and softness** — and it's **not a genre, it's an ingredient** you can add to
any mechanic.

| Pillar | Meaning | For Anton's game |
|---|---|---|
| **Safety** | No danger/risk (physical, emotional, social); activities are opt-in | No fail-punishment, no hard timers, no leaderboard shaming; a bad move costs little |
| **Abundance** | Needs met; "nothing lacking, pressing, or imminent" → pursue beauty/mastery | Generous resources, regenerating lives, plentiful undo/retry, no scarcity anxiety |
| **Softness** | Gentle, comforting sensory stimulus; slower pace, warm familiar senses | Desaturated palette, rounded shapes, soft sounds (see aesthetics below) |

**What negates coziness (keep these OUT):** extrinsic/transactional pressure, danger/threat,
mandatory responsibility or needy entities, intrusive notifications, intense stimulus,
non-consensual social situations, deception, and *opulence* (excess reads as inauthentic).
⚠️ Note the tension: overt transactional pressure fights coziness — design IAP/ads to feel
like **generosity, not extortion** (see `game-monetizer` + the litmus test in
`no-pressure-motivation.md`).

**Contrast deepens coziness:** a small moment of mild tension (a near-full board) makes the
*clear* feel like relief. Coziness is partly the felt absence of an imaginable threat.

**Market validation:** the "cozy/wholesome" audience is large, organized (Wholesome
Direct, 50+ titles/yr since 2020), and growing — and academic work treats calm games as
**restorative environments** for mood repair and stress reduction. Real demand. *(Caveat:
most cozy titles are narrative/PC; Anton's set is mobile abstract-puzzle/idle — the
principles transfer, the farm/animal aesthetic does not have to.)*

## Low-arousal flow

Csikszentmihalyi's flow = absorption when **challenge ≈ skill**. Below → relaxation/boredom;
above → anxiety. Calm games ride the **lower edge of the flow channel** ("relaxed
concentration"): keep flow's **clear goals + immediate feedback** (which produce
absorption), but **dial the challenge gradient down and flat** so it never tips into
anxiety, while staying *just* above pure relaxation so it doesn't drift into boredom.
(A 2017 physiological study found both boredom *and* anxiety produce *disintegrated*
attention; only the flow band produces focused attention — the calm sweet spot is narrow
and real.)

**The autotelic test:** would the player do the core verb 1,000× with *no* reward attached?
If yes, you have a calm-flow loop. Block Blast's pull is the legible goal + instant feedback,
not any (absent) threat.

## What makes an action soothing

1. **Predictable outcome** — anticipatable, so no startle/threat.
2. **Immediate, proportionate feedback** — a satisfying click/pop/cascade the instant you act.
3. **Rhythm** — a repeatable cadence the hands fall into (tap, drag, place, clear). Calm
   games are like **looms/knitting**: the pleasure is in the repeated gesture itself.
4. **Low cognitive load per action** — one clear decision at a time.
5. **A sense of "tending"** — pruning, sorting, tidying, filling. *Restoring order is
   intrinsically pleasant* (Block Out! Color Sort's sort-into-order verb is archetypal).

⚠️ A real "relax mode" is more than the normal game with the timer deleted — it's mindful
attention by design.

## Replace pressure, don't just subtract it (the substitution principle)

The #1 trap: delete the timer and the game has nothing left to pull the player. **Take out
each pressure source and install a calm replacement:**

| Remove (arousal) | Replace with (absorption) |
|---|---|
| Hard timers/countdowns | Self-paced sessions; pull from progression + curiosity, not the clock |
| Fail states/punishment | Productive failure — retry without penalty; elegance/mastery becomes the goal |
| Competition/leaderboards | Personal progression, collection completion, opt-in low-cost social (gifting) |
| Scarcity/resource anxiety | Abundance — generous/regenerating resources, no hoarding panic |
| Intrusive notifications/FOMO | Gentle return hooks (offline progress, "your garden grew") as *gift*, not obligation |

## Aesthetics of calm (signals "relax" before a mechanic is understood)

- **Palette:** soft, warm, **desaturated**, low-contrast; rounded shapes over sharp. (Blues/
  greens lower heart rate vs high-saturation reds.)
- **Audio:** slow-tempo, harmonically simple, few instruments; nature soundscapes activate
  the parasympathetic system. Prefer diegetic sound. *(Binaural-beat claims are soft — flavor only.)*
- **Feedback / juice:** ASMR-like micro-rewards (soft pop, gentle cascade) that reinforce
  *without arousal*. **Crucial nuance: don't over-juice a calm game** — 2024-25 game-feel
  research finds *coherent, restrained, clean* feedback often beats maximal juice for calm
  experiences. See `satisfaction-and-juice.md`.
- **Haptics (iOS edge):** the Taptic Engine is excellent for soft precise haptics — a gentle
  tap on place, soft rumble on clear. Keep intensities **low and soft**
  (`UIImpactFeedbackGenerator` / Core Haptics). An entire "ASMR/satisfying" App Store
  sub-genre runs purely on tap-pop-haptic loops — validates the appetite.
- **Cognitive load:** minimize UI clutter (Cognitive Load Theory) — one clear decision at a
  time, generous whitespace, no UI noise.

## Failure modes (calm → dull or calm → stressed)
No goal gradient (player wanders off) · feedback too quiet (actions feel inert/broken) ·
flat difficulty + no novelty (boredom) · progression stalls/walls (injects stress) ·
decision overload · **removing tension without replacing the pull** (the #1 trap).

## Distilled checklist
1. Core verb passes the **autotelic test** (satisfying to repeat 1,000× rewardless).
2. Ride the **lower edge of the flow channel** (clear goal + instant feedback, gentle low ceiling).
3. Install the **three cozy pillars** (safety, abundance, softness).
4. **Replace every pressure source**, don't just delete it.
5. **Engineer the pull** (goal gradient + variable discovery + idle-style progression + ASMR micro-rewards).
6. Tune the **sensory layer to "relax"** (desaturated, slow/simple audio, *coherent* juice, soft haptics, low load).
7. Watch the **two failure edges** — under-fed (boring) and over-fed (stressful).

## Sources
Daniel Cook "Cozy Games" (Lost Garden 2018) · Project Horseshoe 2017 report · Tanya Short
"Designing for Coziness" · Guul Games "Pixels and Peace" (Feb 2026) · Ben Serviss "In Search
of Meditative Games" (2013) · Csikszentmihalyi flow (Yu-kai Chou summary) · Harmat et al.
*Frontiers in Psychology* 2017 (flow physiology) · ACM FDG 2025 "Beyond Satisfaction" (game
feel) · Sweller Cognitive Load Theory · Wholesome Games / cozy-games restorative research.
Full URLs in CHANGELOG notes. *Practitioner blogs directional; weight academic sources.*
