# Strategery (light turn-based territory strategy)

*Note: the game is from 2008-2010 (shipped on the original iPhone); its design lessons are
timeless even though the coverage is old.*

**Core loop:** On your turn, reinforce your territories, then tap an owned region and a neighboring
enemy region to attack (dice-roll resolution: more armies = more dice); capture territory, end your
turn when *you* decide; repeat until you own the map. (Risk-like.)

**Source of the no-pressure pull:**
- **You end your turn whenever you like** — "you can choose to end your turn whenever you'd like,"
  and you can *speed up* the AI turns so you're not waiting. The clock is entirely yours.
- **Territory capture as visible, accumulating gain** — the map turning your color is the "numbers
  go up" of strategy. The pull is "one more territory → map domination."

**Engaging without urgency:** **Turn-based with no move-timer = think at your own pace.** Deliberate
a move for one second or one minute; the game waits. Combat is a *fair, simple, transparent* dice
system (each troop = one d6), so depth is in *positioning and sequencing*, not execution speed.
Solo-vs-AI and pass-and-play enable "relaxed, asynchronous gameplay without real-time reflexes." AI
personalities (conservative vs aggressive) keep matches varied without pressure.

**Difficulty / pacing:** Per-match arc (small skirmish → map domination) + replayability via map
sizes / difficulty / AI personalities. Pacing entirely player-gated by the end-turn button.

**DNA to extract:**
1. **No move-timer, player-pressed turn advance** — the turn-based twin of TD's player-pressed
   wave. The core "calm switch": *the player advances time.*
2. **Visible accumulating capture** (board changing color/state) as progression feedback.
3. **Simple, *fair*, transparent resolution** (dice = legible odds) → strategy stays accessible and
   low-anxiety.
4. **AI variety** to sustain engagement without difficulty *spikes*.

**Solo-dev buildability: MEDIUM.** No real-time engine load (its biggest plus — shipped on the 2008
iPhone). The hard part is **AI** (even simple heuristics + difficulty tiers take iteration).
Map/adjacency data and turn-state are straightforward in C#. A v1 could ship solo-vs-AI only; add
pass-and-play later (online multiplayer = netcode = avoid for v1).

**Sources:** Macworld "Strategery" (App Gem Award 2009) · 148Apps Strategery review (Jul 11 2010).
