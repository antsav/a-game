# Tower Defense — the calm-vs-stressful switches

**Core loop:** Place/upgrade towers along a path during planning → enemies advance in waves →
towers auto-fire → earn currency from kills → spend to reinforce before the next wave.

**Source of the no-pressure pull (in *calm* TD):** **Player-controlled wave start.** Cozy TD
*Dampf*: "Allow as much time as you need for preparation. The start of the next wave is up to
you!" When the player presses "next wave," all time-pressure evaporates and satisfaction becomes
**planning, not reacting**. The pull is the *optimization puzzle* — "best layout/upgrade for the
gold I have?" — solved at leisure.

**The calm-vs-stressful switches (extract these as explicit rules):**
| Switch | Calm setting | Stressful setting |
|---|---|---|
| Wave trigger | **Player-initiated** (untimed planning) | Auto-countdown timer |
| Placement | **No timer**, deliberate | Real-time placement under fire |
| Fail-state | Soft (lose a life/retry, keep meta) | Hard wipe / "emotionally paralyzing" spikes |
| Monetization | **No ads, no energy, no IAP gates** | Energy timers, forced ads |
| Aesthetic | **Cozy/minimal, "limited violence, stylistic"** | Frantic spectacle |

⚠️ **TD is not inherently calm** — sources note later-chapter difficulty *spikes* that feel
"emotionally paralyzing." **Calm is a design choice** made via the switches above.

**Difficulty / pacing:** Wave-based pacing is naturally **rhythmic** — plan (calm) → execute
(brief) → resolve → plan again. With a player-pressed wave button, the player controls the
breathing rhythm of the whole game.

**DNA to extract:** **Make the wave-start player-initiated** — the cheapest, highest-leverage way
to convert any action-y mechanic into a calm one (the same "player advances time" switch as
Strategery's end-turn). Plus soft fail, no energy/ads, cozy art, reward *layout optimization* over
reflexes.

**Solo-dev buildability: MEDIUM-HIGH.** More moving parts than idle (pathfinding, wave spawning,
targeting/projectiles, collision) — exactly where Anton's existing Unity exposure (colliders,
GameObjects) applies. Very well-trodden Unity tutorial genre (path-following, object pooling).
Risk: scope creep on tower variety/levels — cap it.

**Sources:** Dampf – The Cozy Tower Defense (Steam) · Towers of Minimalism (Steam) · Mini TD 2:
Relax Tower Defense. Accessed Jun 2026. *(Several are store/aggregator pages — directional.)*
