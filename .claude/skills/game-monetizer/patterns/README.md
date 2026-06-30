# patterns/ — actionable monetization design recipes

`references/` holds the *knowledge* (how monetization works). **`patterns/` holds the
*recipes* — concrete, implementable design patterns** a solo dev can drop into a game,
each with when-to-use, how-to-build, tuning numbers, pitfalls, and the psychology it
leverages. One pattern per file, kebab-case (`starter-pack-offer.md`).

This folder is meant to **grow**. Add a pattern whenever a reusable monetization
technique is researched, observed in a live game, or learned from experience. Keep
each pattern self-contained and skimmable.

## Pattern file template

```markdown
# <Pattern name>

**What:** one-line description.
**Monetization goal:** which metric it moves (conversion / ARPPU / ad ARPDAU / retention).
**Best for:** genre/stage where it fits (e.g. hybrid-casual puzzle, v1 vs LiveOps).
**Psychology:** the bias/loop it leverages (link to references/spend-psychology.md).

## How it works
Step-by-step structure of the mechanic.

## Tuning
Concrete numbers/defaults (price points, frequency caps, reward sizes) + how to test.

## Pitfalls
What kills retention, gets App Store rejected, or reads as predatory.

## Live examples
Real games using it (with dates), + source links.

## Effort (solo dev)
Build cost / complexity, and whether it belongs in v1 or later.
```

## Index

- [rewarded-revive](rewarded-revive.md) — opt-in revive-after-fail; highest-value ad placement; build first
- [starter-pack](starter-pack.md) — one-time first-purchase bundle; crosses non-payer → payer
- [piggy-bank](piggy-bank.md) — passive coin accumulator unlocked by one real-money purchase
