# Ethics, Compliance & Platform Rules

How to monetize effectively **without getting rejected by Apple, fined by regulators, or
review-bombed.** This is risk-management and sustainable-revenue strategy, not moralizing.
*Not legal advice — for a commercial launch touching minors or loot boxes, get a games
lawyer.*

> **Three things will actually hurt a solo dev, in order of likelihood:**
> 1. **App Store rejection** (Apple 3.1.1 loot-box odds; 3.1.2 deceptive subscriptions) —
>    your biggest day-one risk, 100% avoidable.
> 2. **FTC / consumer-law exposure if you touch minors** — the $245M Fortnite and $20M
>    Genshin cases are the template.
> 3. **Forced minimum age rating** the moment you include *any* paid randomization —
>    **PEGI 16 (EU, June 2026+)** and **"M" (Australia)** — which quietly gates your market.
>
> A solo dev who **avoids paid randomization** and **treats possible-minors carefully**
> sidesteps ~90% of the regulatory surface.

## The single highest-leverage decision
**Strongly consider shipping with no paid randomization.** A cosmetic/direct-buy store +
"remove ads" + a fair subscription avoids loot-box law *and* the new min-PEGI-16 / min-"M"
ratings entirely. Everything below is the detail behind that.

## Loot box / gacha regulation (2025-2026)

Regulation targets the **paid + random + concealed-outcome** combination. Map:

| Region | Status |
|---|---|
| **Belgium** | Paid loot boxes = illegal gambling. **In force, enforced.** |
| **Netherlands** | Banned where contents have tradable real-world value. In force, weak enforcement. |
| **China** | Odds disclosure required (2017); minor spending caps (draft: under-8 no pay, 8-16 ¥50/tx ¥200/mo); real-name verification → **you bear refund liability** if a minor overspends. Needs ISBN + local publisher anyway. |
| **South Korea** | **Mandatory odds disclosure with criminal penalties** (in force Mar 2024, actively enforced; 3%-revenue fine bill pending). |
| **Japan** | **Kompu/"complete" gacha banned** (collect-a-set-to-unlock); single-pull gacha legal with self-reg odds disclosure. |
| **UK** | Self-regulation only (no statute); compliance audits failing → statutory regulation plausible. |
| **EU — Digital Fairness Act** | **Proposal ~Q4 2026, applies ~2028-2030.** Likely to restrict loot boxes/pay-to-win/addictive design for minors + mandate real-money-equivalent disclosure. The **DSA (in force Feb 2024)** already bans interfaces that "deceive, manipulate, or unduly nudge." |
| **Australia** | Paid loot boxes → **mandatory min "M" rating**; sim-gambling → R18+ (in force Sept 2024). |
| **US** | No federal statute; **FTC enforces via Section 5** (unfair/deceptive). Hawley bill + NY state activity pending. |

## Mandatory disclosures

- **Odds disclosure** for paid randomized items is **platform-mandatory worldwide** (Apple,
  Google, consoles) and legally required in China/Korea. Standard: **exact per-item or
  per-rarity-tier probabilities, in-app, before purchase.**
- **ESRB "In-Game Purchases (Includes Random Items)"** / **PEGI "Includes Random Items"** —
  applied to any paid loot box, gacha, card pack, or prize wheel. **PEGI change: any game
  with paid random items gets a minimum PEGI 16 from June 2026.** The IARC questionnaire at
  submission auto-applies these — **answer it honestly.**

## Apple App Store rules (the realistic rejection list)

- **3.1.1 IAP** — all digital unlocks via Apple IAP; purchased currency **may not expire**;
  provide a **restore** mechanism. Loot boxes **must disclose odds before purchase.**
- **3.1.2 Subscriptions** — ≥7 days, ongoing value, cross-device, price shown *before*
  purchase, **no bait-and-switch trials**, easy cancel.
- **2.3.1 / 3.2.2** — no deceptive metadata/pricing; no disguised ads or fake close
  buttons; no apps "designed predominantly for ads"; you may **incentivize** opt-in ad
  watches but **not force** ratings/reviews to gate functionality.
- **Kids Category (1.3, 5.1.4)** — **no third-party ads or analytics**; purchases/links
  behind a parental gate; can't use "For Kids" metadata unless actually in the category.
  → **Aggressively monetizing a kids' app is essentially impossible on Apple's terms.**
- **Anti-steering (2024-2026):** in the **US** (post-Epic, 9th Cir. Dec 2025) you *may*
  link out to your own cheaper web purchase with no Apple commission — but you take on
  payments/tax/refunds/fraud and lose frictionless checkout (which usually *raises*
  conversion). **For most solo devs, stick with IAP**; external links pay off at scale.

**Rejection causes:** loot box w/o odds · subscription hiding price / <7 days /
bait-and-switch · unlock not via IAP · ad-spam · forcing reviews · kids-implying metadata
without Kids Category · Kids Category app with 3rd-party ads/analytics.

**Google Play (brief):** odds disclosure required since 2019; Age-Restricted Content
policy (full enforcement Jan 28 2026) blocks minors from gambling-like apps; Families
policy restricts IAP/ads for child-directed apps.

## Dark patterns — the line

Taxonomies to know: Brignull's 12 · Gray et al. (nagging, obstruction, sneaking,
interface interference, forced action) · FTC "Bringing Dark Patterns to Light" (2022).

- **Deceptive / illegal** = the user is **misled** about price, odds, what they bought,
  whether they're buying at all, or how to cancel. Fake scarcity, disguised ads,
  accidental-charge UIs, hidden auto-renew. FTC §5, EU DSA/UCPD, Apple 2.3.1/3.1.2 bite here.
- **Aggressive but legal** = honest information, manipulative *framing*. Real timers,
  genuine limited offers, optional pay-to-skip, persuasive store design. Legal today,
  increasingly DFA-targeted for minors, and a churn/reputation risk regardless.
- **The test:** *"If I explained this mechanic out loud to the user, would they feel
  tricked?"* If yes, it's a dark pattern — fix it.

## The business case for fair monetization (not just ethics)

- **Asymmetric tail risk:** $245M Fortnite, $20M Genshin FTC settlements. A solo dev has no
  legal war-chest — one deceptive subscription flow or accidental-kid-charge complaint can
  mean **removal + Developer Program termination** (your whole catalog gone).
- **Churn destroys LTV:** aggressive extraction spikes short-term ARPU but raises churn and
  kills D7/D30 — and F2P is retention-driven. Predation suppresses the multiplier.
- **Refunds/chargebacks** threaten payment standing; **review-bombing** crushes the organic
  rating that *is* a no-budget solo dev's distribution.
- **Fair value exchange is the strategy:** sell convenience, cosmetics, content people are
  glad they paid for; show real-money equivalents; honest odds; easy cancel. Happy payers
  repeat and refer — the only growth a solo dev can afford.

## Compliance checklist (solo iOS dev, 2026)

- [ ] **Prefer no paid randomization** (avoids loot-box law + min PEGI-16/"M").
- [ ] If gacha: publish exact odds in-app before purchase; **no kompu/complete-gacha**.
- [ ] Show **real-money equivalents** next to virtual currency; sane denominations.
- [ ] **Decide deliberately whether minors are in scope** (COPPA/GDPR-K). Don't enter Kids
      Category if monetizing with 3rd-party ads. Parental gate before any purchase;
      **never let a single tap cause a charge** (the literal Fortnite violation).
- [ ] All unlocks via Apple IAP; currency doesn't expire; restore present.
- [ ] Subscriptions: ≥7 days, value clear, price before purchase, no bait-and-switch.
- [ ] No disguised ads / fake X / forced reviews. Honest metadata. Answer IARC honestly.
- [ ] If shipping loot boxes: expect min PEGI 16 (EU) / "M" (AU); geo-disable in
      Belgium/Netherlands; treat China/Korea as "needs local partner."
- [ ] Run the "would they feel tricked?" audit before each release. No *fake* scarcity, no
      confirm-shaming, no roach-motel cancellation.

**Watch-list (not yet law):** EU DFA (~Q4 2026 proposal, ~2028-2030), Korea 3%-revenue
fine bill, US Hawley bill + NY state activity, UK statutory regulation. Build accordingly
now — cheaper than retrofitting.

## Sources
Apple App Review Guidelines · FTC dark-patterns report (2022) + Epic/Fortnite + Genshin
settlements · EU Parliament DFA (Oct 2025) + Goodwin/Chambers · Korea GIPA (Kim & Chang) ·
China draft rules (Niko Partners) · Japan kompu gacha (Lexology) · UK GOV.UK + Royal
Society 2025 · Australia (Game Developer, The Conversation) · ESRB/PEGI · Brignull
Deceptive.design · Journal of Business Ethics 2021 (predatory monetization). Full URLs in
CHANGELOG notes.
