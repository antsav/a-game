# Piggy Bank (coin accumulator)

**What:** premium currency accrues passively as the player plays; they pay real money once
to "break" the bank and claim the accumulated total.
**Monetization goal:** conversion + ARPPU (raises basket size; converts mid-spenders).
**Best for:** hybrid-casual with a currency loop; a strong *second* IAP after starter pack.
Proven specifically in sort games (Hexa Sort).
**Psychology:** loss aversion + endowment (the visible growing total feels "owned" and at
risk of being lost) — see [[references/spend-psychology.md]].

## How it works
A visible meter fills with premium currency as the player earns/plays, up to a cap. The
accumulated coins are **only claimable by a one-time real-money purchase** (e.g. $1.99-4.99).
When full (or near), prompt the player to unlock it before it "overflows."

## Tuning
- Price **$1.99-4.99** (Hexa Sort $4.99, Gardenscapes $2.99).
- Cap + "near full / overflowing" prompt creates the urgency.
- Optionally personalize capacity/price by segment later (Monopoly GO does) — not v1.

## Pitfalls
- Don't make accrual feel mandatory-to-progress (keep it a bonus, not a gate — pay-to-
  progress is DFA-targeted; see [[references/ethics-compliance-and-platform-rules.md]]).
- Keep the premium-currency faucet it feeds stingy elsewhere or you inflate the economy
  (see [[references/economy-design.md]]).

## Live examples
Hexa Sort ($4.99), Gardenscapes ($2.99); found in ~45% of top puzzle games (2025).

## Effort (solo dev)
Low — mostly a counter + a buy button; leverages currency you already mint. High ROI; a
Tier-2 build once retention is proven. See [[references/pricing-and-offers.md]].
