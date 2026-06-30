# Conversion Funnel

Moving a player from install → first dollar → repeat → high-value. The whole store is a
funnel; this file is its spine. Pair with `spend-psychology.md` (why) and
`pricing-and-offers.md` (the offers).

```
Install → Engaged/retained → FIRST purchase → Repeat purchase → High-value/whale
```

## The first purchase is the whole game

New players arrive with **near-zero spending intent.** But the first dollar is a
**psychological threshold, not a revenue event** — a player who buys once is **5-10× more
likely to buy again** (it removes the "am I someone who pays for games?" identity barrier),
and **the first purchase anchors all future spend.** ~2-5% of players ever pay; well-designed
first-purchase offers correlate with **3-5× higher** conversion (directional). This is the
single highest-leverage point in the funnel.

## Triggering the first purchase

1. **The planted "moment of need."** Surface the first offer exactly when the player hits
   friction — out of a key resource, stuck on a difficulty wall, just after a loss, or at a
   milestone. They're far more receptive when they feel an *immediate* need. (Royal Match's
   entire model: "out of moves → buy" pop-up.)
2. **The starter pack / High-Conversion Item** — cheap entry ($0.99-4.99) combining **high
   anchored value + pays-off-over-time + scarcity**. Over-deliver value: first-purchase
   *satisfaction* drives the repeat rate, which is the real IAP engine.
3. **Remove-ads** — often the #1 first IAP in hybrid games; low-friction, and it
   **self-sorts the player as a payer** (mute their ads, target them with IAP).
4. **Price for conversion, not max willingness-to-pay** — you can upsell later; the goal of
   the first offer is to cross the threshold, not to extract.

**Timing:** most first purchases land on the **2nd-3rd store visit**, so design to bring the
player *back* (free daily gift in the shop, claimable timers), not to close on visit one.

## After the first dollar

- **Repeat purchase:** escalating offers, the currency-pack ladder, piggy bank, LTOs. The
  leftover-balance trap (pack sizes mismatched to item prices) nudges the next buy.
- **High-value / whale:** whales convert **slowly (~18 days vs ~8 for minnows)** — they're
  *not* visible in week 1, so **D7-D30 retention is the precondition for whale revenue.**
  Identify likely whales by *behavioral signal* (depth of engagement, early small
  purchases, completionist patterns), then have escalating high-end offers ready. For a solo
  dev: leave whale *headroom* (high-tier packs, no spend ceiling) but **bias to broad
  minnow/dolphin conversion** — don't build a whale-dependent LiveOps machine.

## Instrument the funnel
Map every touchpoint install→first-purchase as analytics funnel events (GameAnalytics
custom-event funnels). Find the friction screens. You can't improve conversion you can't see.

## Solo-dev funnel build (priority)
1. Retention first — no funnel matters if players churn (gate at D7 ≥ ~15%).
2. **Starter pack + remove-ads**, surfaced at a planted moment-of-need.
3. **Contextual "out of moves/lives → buy" pop-up** (the core monetization moment).
4. Bring-back-to-store hooks (free daily gift) for the visit-2-3 first purchase.
5. Escalating repeat offers (ladder, piggy bank) once first-purchase conversion works.
6. Whale headroom (high-tier packs) — but don't court whales with ops you can't run.

## Sources
Mobile Free To Play (first purchase) · Solar Engine (first-purchase conversion, 5-10×) ·
DoF Starter Pack Pricing (Apr 2024) · Udonis (whale conversion timing) · GameAnalytics
(funnels, finding whales) · Naavik (Royal Match). Full URLs in CHANGELOG notes.
