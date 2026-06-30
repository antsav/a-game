# Publishers vs Self-Publishing

The **"do I need a publisher, and how does it actually work?"** answer for a solo hyper/hybrid-casual
iOS dev. The honest version.

> Revenue-share numbers are mostly NDA'd — treat every figure as a range, not a quote. Confidence
> is medium unless noted.

---

## 1. What a publisher actually does

A publisher takes a game that *works mechanically* and makes it *work economically at scale*, then
funds and runs the marketing engine you can't afford:

- **Paid User Acquisition at scale** — the headline. They buy installs across Meta, TikTok, Google,
  AppLovin, Unity/ironSource, Mintegral at five-to-six-figure *daily* spend. **This is the thing a
  solo dev structurally cannot do.**
- **Industrialized creative production** — Voodoo claims ~25,000 creatives/year; Homa auto-slices
  creatives from gameplay per network. Creative win-rate is the biggest CPI lever.
- **Ad-network relationships & monetization optimization** — mediation, eCPM tuning, ad-frequency
  balancing, IAP/offer design, economy A/B tests.
- **ASO, LiveOps, analytics infrastructure** — their SDK instruments the game and feeds CPI/retention/
  LTV/ROAS dashboards; once a game scales they often run LiveOps internally.
- **Funding** — they front the UA capital (see §2, the real point).

**Hyper/hybrid-casual publishers** (high-volume prototype funnel, data-driven, decide in days):
**Voodoo, Homa, Rollic (Zynga/Take-Two), Supersonic (Unity), CrazyLabs, Kwalee, SayGames, Lion
Studios (AppLovin), TapNation.** They test hundreds of prototypes/month and greenlight ~1%.
**Broader/premium publishers** (Devolver, Annapurna, casual/mid-core houses) are curated, fewer
titles, deeper per-title investment, relationship/editorial-driven, decide in months — **not the
model for a hyper/hybrid-casual first game.**

---

## 2. Why use a publisher — and what you give up

**The real value-add is capital and the cash-flow cycle, NOT "expertise."** This is the decisive fact:

- Hyper-casual UA can be ROAS-positive in days, **but ad networks pay out on a 45–60 day lag.** To
  keep a winning game at the top of the charts you must keep buying installs *today* against revenue
  you won't see for two months.
- Worked example (Tenjin): to spend **$33,000/day** on UA you need roughly **$1,000,000 in working
  capital** to bridge the first 30 days. A solo dev doesn't have it, and ad networks don't extend
  credit to individuals.
- For **hybrid-casual**, sources warn against scaling paid UA without **~€300K–€500K of capital**;
  US hybrid CPIs run **$2.50–$6.00 in tier-1**.

So the publisher's irreplaceable function for a chart-driven genre is: **front the UA spend, absorb
the 45–60 day payout lag, recycle the cash.** That's the whole ballgame.

**What you give up:**
- **Revenue share** — often the larger share of profit after recoup (see §3).
- **Creative control** — they optimize for marketability (CTR/IPM/ad-frequency), which can override
  your design intent. **For this user this is a real risk:** marketability-driven monetization
  (aggressive interstitials, urgency framing) can betray the calm/no-timer feel. Weigh it explicitly.
- **IP / control terms** — exclusivity, control of the live build/LiveOps once scaled, sometimes IP
  assignment or sequel first-refusal. Read these.
- **Attention** — high studio-to-manager ratios; limited hand-holding.

**The middle path (self-publish but solve cash flow):** revolving credit facilities (e.g. Pollen VC)
lend against verified next-day ad revenue, letting a small budget deploy large UA without giving up
profit share. Viable but operationally heavy and high-risk for a true solo dev — not a v1 move.

---

## 3. Revenue share / commission / recoupment

**Headline structure: ~50/50 of NET profit AFTER the publisher recoups UA + costs.** Net revenue =
gross minus Apple's 30%/15%, refunds, taxes, often marketing. The publisher recoups its UA spend
(and any advance) **first**, then the remainder splits.

- **Range:** most common post-recoup split is **50/50 ± ~10%** (40/60 to 60/40).
- **The "effective 70/30" trap:** a nominal 50/50 is often undercut by bonus/milestone structures
  with geo caps and per-install thresholds that net to roughly **70/30 in the publisher's favor.**
  Read the bonus schedule, not just the headline split.
- **Advances/MGs cost you share:** deals *with* an advance pay the dev materially less than no-advance
  deals. Pure hyper-casual usually has **no advance** (a small monthly prototype fee or nothing); MGs
  appear more in hybrid/mid-core and are recouped before any split.
- **Recoupment mechanics vary:** sometimes 100% of net goes to the recoup pool until the publisher is
  whole; sometimes it's split (e.g. 50% recoup / 50% royalty paid in parallel) — the latter is better
  for you.
- **Data points:** CrazyLabs ran a *promotional* 55%-to-dev challenge (not standard). Voodoo uses two
  contract types — a *prototyping* contract (monthly fees) and a *publishing* contract whose revenue
  share **decreases as they invest more** (more funding → smaller your cut).

---

## 4. The pitch / submission process

Hyper/hybrid-casual publishing is **not a pitch-deck business — it's a "test it on our SDK" business.**

1. Sign up on the publisher's dev platform (Voodoo Publishing dashboard, Homa Lab + the **Homa Belly**
   SDK, Supersonic, CrazyLabs CrazyHub, SayGames…).
2. **Integrate their SDK** (analytics + ad mediation). Budget time for integration pain (Gradle/NDK
   conflicts are commonly reported).
3. **Submit a build** — you don't need a finished game, you need a *testable prototype.*
4. They (or you, via the dashboard) run a **paid marketability test** — a small ad campaign (often
   $100–$300+) measuring CPI and early retention from real installs.
5. Dashboard returns numbers. Hit the thresholds → greenlight to iterate/soft-launch. Miss → iterate
   and resubmit, or it's killed.

**Speed & odds:** decisions come within days of a test; **~1% of submitted prototypes get published.**
First-hand account: emailing ~30 publishers got ~4 replies in a week (Kwalee, Voodoo, Homa, SayGames) —
responsiveness itself is a filter. **Hybrid-casual prototype → scalable global launch is now ~9–18
months**, with a 2–3 month A/B iteration phase before scaling.

---

## 5. What metrics publishers require (so YES — they want cohorts, stickiness, LTV)

Publishers gate on a **paid test**, not opinion. Two universal gates: **CPI** (marketability) and
**D1 retention** (the core loop works); playtime/LTV gate the *scale* decision.

**Pure hyper-casual prototype (Supersonic's 3 KPIs):** CPI **< $0.30** (test target), cumulative
playtime **> 2,000 sec by D7**, **D1 ≥ ~38%** (Android).

**Hybrid-casual prototype (the relevant bar — greenlight targets):** D1 **35–45%**, D7 **18–22%**,
D30 **8–12%**, blended ARPDAU **$0.15–$0.25**, D30 payer conversion **3–5%**, rewarded-video
impressions/DAU **4–7**, D90 LTV (US) **$4–$12**. Sustainable US puzzle CPI **$2.00–$3.50**.

**Do they want cohort analysis / stickiness / LTV?** **Yes, for hybrid-casual specifically.** They
require **cohort retention curves (D1/D7/D30)**, **DAU/MAU stickiness**, **ARPDAU/ARPPU**, and
**modeled D90 LTV vs CPI (ROAS)** — and they want **3–4 weeks of stable D7 + ARPDAU** before
committing meaningful UA. (Pure hyper-casual is simpler: CPI + D1 + playtime, because there's no IAP
tail.) See `launch-metrics.md` for what these mean and how to read them with no budget.

---

## 6. The strategic question: launch solo first, or submit pre-launch?

**Path A — submit prototypes pre-launch (native hyper/hybrid-casual model).** Build a testable
prototype, integrate the publisher SDK, let *their* paid test produce CPI/D1. You don't self-fund a
launch. **Fits:** genuinely hyper/hybrid-casual, chart-driven, no UA capital. **Reality:** ~1%
greenlight; expect rejections and fast iteration.

**Path B — launch/soft-launch solo, prove metrics, then pitch.** Ship and gather organic + small-budget
cohort data, then approach a publisher with *proven* D1/D7/ARPDAU/LTV. **Fits:** a game with a meta
layer/IAP depth where retention/LTV — not raw CPI — is the story. A clean retention curve de-risks the
publisher's decision and improves your terms (better split, possible MG). **Risk:** thin/slow sample
without UA budget; a weak public launch can taint the title.

**Recommendation for this user (solo, no UA capital, calm hybrid-leaning puzzle):** the concept is
**hybrid-casual leaning, not pure hyper-casual** — retention/LTV is the story (favors Path B's *data*)
but you lack capital (favors Path A's *funding*). Practically: **build a well-instrumented prototype
(cohort retention + ARPDAU from day one), get cheap early retention signal yourself, then submit to a
hybrid-casual publisher's SDK** so their paid test confirms CPI. You get the publisher's capital (the
thing you can't replicate) while walking in with retention data that improves your terms. **Guard the
calm/no-pressure feel against marketability-driven monetization pressure** — if a publisher demands
monetization that betrays the experience, that's a real, weighable cost. A polished, retention-strong
calm puzzle is *more* publisher-attractive **and** truer to the taste north-star than a disposable
hyper-casual reskin.

**Do you even need one?** Only if you intend to scale on paid UA. If the plan is **organic-first**
(short-form video + ASO + Apple featuring), you can ship and grow **without a publisher** — and *that*
is the default for a first game. Approach a publisher only once you've proven retention and want to
pour capital on a validated winner.
