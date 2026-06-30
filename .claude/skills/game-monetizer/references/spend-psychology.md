# Spend Psychology

Why players pay — the behavioral mechanisms behind monetization. Pair with
`conversion-funnel.md` (how to move a player from install to first dollar to repeat)
and `ethics-compliance-and-platform-rules.md` (where persuasion becomes a dark pattern
and a legal/platform risk).

> **Reliability note:** The famous whale stats (0.15% of players = 50% of revenue; 2.3%
> conversion) are from **2014-2016** — still quoted everywhere, foundational for the
> *shape* of the distribution, but **not current magnitudes.** The 2024-2026 data shows
> a real shift: payer bases are **widening** and whale concentration is **softening**
> (esp. iOS). Design for broad conversion, not whale dependence.

## Player spender taxonomy

The segmentation splits the **paying** population (~2-5% of installs), not the whole base:

| Segment | Spend | Behavior |
|---|---|---|
| Non-payers (~95-98% of installs) | $0 | The social fabric (opponents, leaderboards) whales pay to dominate. Monetized via ads. |
| Minnows | ~$1-5/mo | Convert fast (~8 days post-install), small, churn-prone. |
| Dolphins | ~$5-20/mo | Steady, loyal once converted — the growable middle. |
| Whales | $100s-1,000s | ~1-2% of base; convert **slowly (~18 days)**; historically 50-70% of revenue. |
| "Krakens" / super-whales | $1,000s+ | Fraction of a %; need VIP handling (a LiveOps function, not a v1 concern). |

**2024-2026 shift:** whale revenue share in NA iOS fell ~34%→27% (Q1'23→Q1'24); the
global payer base passed ~1.6B with payer *growth* outpacing revenue growth — more
people paying, each a little less. Even pro designers now prefer "10% spend $100" over
"1% spend $1,000" for equal LTV (DoF 2024 survey, 81.5%).

**Solo-dev takeaway:** do **not** architect a v1 economy that *requires* a whale to be
profitable — that's a casino-grade LiveOps operation you can't staff. Design for broad
minnow/dolphin conversion; leave whale *headroom* (high-end bundles, no spend ceiling)
so a whale *can* spend if one appears.

## Cognitive biases that drive spend

Each = the bias → how F2P applies it → example.

- **Loss aversion** (losses hurt ~2× gains): streaks, expiring boosts, decaying league
  rank, "your base is under attack." Threat of losing progress > promise of new gains.
- **Sunk-cost fallacy:** deep progression + collections make quitting/stopping-paying
  feel wasteful. The engine behind battle passes and long upgrade trees.
- **Endowment effect** (overvalue what we own): free trials of premium
  characters/skins — once it feels *theirs*, paying to keep it = avoiding a loss
  (synergizes with loss aversion).
- **Anchoring:** show a struck-through "$99.99 value" above a "$4.99" pack. The first
  number frames everything after as cheap. **The first purchase anchors all future spend.**
- **Decoy effect:** a deliberately bad middle currency pack makes the largest look like
  obvious value, steering spend upward.
- **Social proof:** guilds, leaderboards, visible whale cosmetics, "12,000 bought this."
  Others' spending normalizes your own.
- **Scarcity / FOMO:** limited-time offers, rotating shops, countdowns, "only 5 left."
  Scarcity converts hesitation into impulse.
- **Commitment & consistency:** daily login chains, "complete 3/5 quests." Small early
  commitments make later paid ones feel consistent with a "daily player" identity.
- **Fresh-start effect:** new seasons/passes reset motivation and willingness to commit.
- **Hyperbolic discounting / present bias** — the core driver of **timer-skipping.**
  Energy timers, build queues, craft waits manufacture *delay*; a purchase *removes* it
  instantly. Monetization sells the *end* of waiting/effort/ambiguity.

## Variable reward / compulsion loops

- **Variable-ratio reinforcement** (Skinner box / slot-machine schedule): rewards after
  an *unpredictable* number of actions — the stickiest reinforcement schedule known.
  Gacha/loot boxes run on it. Fixed-price purchases don't produce the same compulsion.
- **Near-miss effect** (from gambling): a reveal that *almost* lands on the rare item
  spikes arousal and drives "one more pull." A deliberate trick — and an ethical red line.
- **Gacha dopamine:** the *anticipation of the reveal* drives the response, not the
  reward. 60%+ of top-grossing games use gacha (directional). 2025 research links
  loot-box spend to later gambling initiation — hence rising regulation.
- **Appointment / compulsion loop:** timed crops, daily-reset shops, "come back at 8pm"
  — manufactures a recurring appointment that builds habit and the impatience that monetizes.

**Engaging vs predatory (the test):** does spending *enhance fun the player already
has* (optional acceleration), or does the design *manufacture impatience/anxiety* so
that relief-from-pain is the thing being sold? The latter is predatory, courts
regulation (UK 2024, Australia 2024), and needs LiveOps muscle a solo dev lacks. See
`ethics-compliance-and-platform-rules.md`.

## Pain-of-payment reduction

The "pain of paying" (cash activates pain regions in the brain) is the friction
monetizers engineer away — in priority order:
1. **Premium currency as a buffer:** real money → gems → items inserts psychological
   distance; players stop tracking dollars. Awkward bundle sizes (450 gems for a
   500-gem item) leave a dangling balance that nudges the next purchase.
2. **Pre-purchased currency:** buy gems once (one pain spike), spend many times (each
   feels free) — separates the pain of buying from the pain of spending.
3. **Frictionless rails:** Apple IAP / Face-ID one-tap, stored payment.

**Solo-dev note:** on iOS you're on Apple's (already low-friction) IAP rails; a *simple*
hard-currency layer is the expected pattern. A *multi-currency* economy (soft + hard +
event currencies) is a LiveOps scope trap — over-engineering unless the loop needs it.

## Why whales spend (and how to keep payers)

Four drivers: **status** (visible superiority), **competition** (pay to win/stay top),
**completion** (collection/completionist drive — gacha exploits this), **time-saving**
(affluent, time-poor players skip grind). One purchase makes a player **5-10× more
likely** to buy again → the highest-leverage retention move is converting the *first
dollar*, then escalating offers. VIP concierge (personal recognition, account managers)
is real but a human-staffed LiveOps function — for a solo dev the analog is *automated
tiered VIP*, and only after retention + whales are proven. Premature VIP = over-engineering.

## Load-bearing takeaways

1. **The first dollar is the whole game** — ~2-5% convert; one purchase → 5-10× likelier
   to buy again. Engineer a cheap, anchored, scarcity-wrapped starter pack at a planted
   moment-of-need (see `conversion-funnel.md` and `patterns/`).
2. **The market shifted to broad payer bases** — for a solo dev, ethics + regulation-
   safety + operational feasibility all point the same way: convert minnows/dolphins,
   leave whale headroom, don't build a whale-dependent machine.
3. **Premium currency + frictionless IAP are accepted tools; hard gacha/P2W is the risky
   frontier** — use the funnel and currency buffer fully; use variable reward sparingly
   and **with disclosed odds**; avoid the predatory end.

## Sources
DoF "Peak Gaming" (Sep 2025) & "Starter Pack Pricing" (Apr 2024) · Mobile Free To Play
(first purchase) · Swrve (2014-16, stale baselines) · Udonis whales (2024) · Solar
Engine (first-purchase conversion) · GameAnalytics (finding whales, funnels) · Quantic
Foundry (gamer motivations) · GameMakers/GameDiscover (compulsion loops) · PMC/ResearchGate
(gacha & gambling, 2025). Full URLs in CHANGELOG research notes.
