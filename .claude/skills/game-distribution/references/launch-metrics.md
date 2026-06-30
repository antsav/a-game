# Launch & Scale Metrics — the go/kill gates

The metrics that decide **soft-launch → scale-or-kill** and that **publishers require** — and how a
**no-budget solo dev reads them for free.** This file *explains* the metrics (the engineer-new-to-
gamedev gap); for the raw benchmark tables (CPI/CTR/IPM/retention bands by genre) the source of truth
is **`games-researcher/references/validation-and-testing.md`** — pull numbers from there, don't restate
them here.

> Every number swings **2–3× by source, geo, platform, and quarter.** iOS CPIs run ~2× Android; iOS
> monetizes better long-term. Treat published numbers as **decision bands**. Once you have **~1,000+
> real installs, your own cohort data overrides every benchmark.**

---

## The order that matters (why this sequence)

Each gate is cheaper than the next and screens out the most ideas:
**creative/CTR → CPI/IPM → retention (D1 then D7) → monetization (ARPDAU) → ROAS.**
- **CTR** needs only an ad. **CPI** needs a prototype. **Retention** needs a build. **ROAS** needs real
  ad spend. Fail an early gate and you never pay for the later one.
- **You can read the front half (creative appeal + retention + monetization) organically; the back half
  (CPI/ROAS) is paid-UA-only** — irrelevant to a solo dev until there's budget and a curve worth scaling.

---

## Retention — the first gate (D1, D7, D30)

**Why D1 is first:** it's the cheapest, fastest signal that the **core loop is fun and onboarding
works** — readable within 48h of a cohort, before any depth spend. *"Below 10% D7 signals core-loop
issues no amount of UA budget can fix."* If players won't come back once, nothing downstream is buyable.

Hybrid-casual scale targets (directional): **D1 35–45%, D7 18–22%, D30 8–12%.** Hyper-casual is lower
(D1 25–35%, D7 6–9%, D30 1–3%). Note: all-genre *medians* (GameAnalytics, 16k+ games) are far lower
than these "good" targets — those tell you your percentile, not your goal.

---

## Cohort analysis — explained for an engineer

**What it is:** a cohort = all users who installed on the same day (or week, or from the same
campaign/creative). Instead of one blended "retention = 30%," you track each install-group separately
over days-since-install. Think `GROUP BY install_date`, then watch each group decay over time.

**Why aggregate numbers lie:** a blended DAU/retention number mixes a 6-month-old loyal cohort with
yesterday's fresh installs. **10× your UA and blended retention *drops*** (flood of new users) even if
quality is identical. Cohorts isolate "is the product getting better?" from "did we just buy a lot of
users?"

**How cohorts project LTV (the actual math):**
1. Plot the cohort's **retention curve** (% still active at D1, D3, D7, D14, D30…).
2. Fit it to a **power-law decay.**
3. **LTV ≈ (area under the retention curve) × ARPDAU.** Area = average active days per user;
   × daily revenue/user = lifetime revenue. Integrate the fitted curve to D90/D180.
4. **Accuracy grows with time:** D7 predictions beat D1; D30 approaches reliable.
5. **Known trap:** power-curve fits **miss late-converting whales** (first IAP after D7), so pure-
   retention LTV models can under-count hybrid-casual's best payers.

**Why publishers insist on cohorts:** they scale *specific* cohorts (a creative, a geo, a channel) that
hit ROAS, and **exclude cohorts that deteriorate after a breakpoint** even if they make short-term money
— because they'll lose money at scale.

---

## Stickiness (DAU/MAU)

DAU ÷ MAU = the fraction of monthly players who show up on an average day ("days played out of 30").
**Good ≈ 20%, world-class 30%+, problem below ~7%.** Casual/puzzle runs lower in practice (~17%).
It matters because casual games monetize per-session (ad impressions) and per-day (ARPDAU) — stickiness
multiplies both at zero extra UA cost, and it's a leading indicator of habit formation (the long tail).

---

## ARPDAU / ARPU / ARPPU / LTV (plain definitions)

- **ARPDAU** = revenue ÷ daily active users (per day). The casual game's heartbeat.
- **ARPU** = revenue ÷ all users over a period. **ARPPU** = revenue ÷ *paying* users (much higher;
  whale-driven). **LTV** = lifetime revenue per user (the cohort-curve integral above).
- Hybrid ARPDAU (**$0.10–$0.25**) is 4–7× hyper-casual because IAP + meta layers reach payers ads
  leave behind. Hybrid D90 LTV (US) ~**$4–$12** vs hyper-casual ~$0.50–$1.20.

---

## CPI vs LTV, and ROAS — the scaling gate (paid-UA only)

**The one equation that governs scaling: scale only when LTV > CPI with margin.** Minimum
**LTV:CPI ≥ 1.5×**; UA teams more often demand **LTV:CAC ≥ 3:1.**

**ROAS** = cohort revenue ÷ acquisition spend, at a day-window. **ROAS ≥ 100% at your payback window =
recouped = scale.** The window must match the model — the most misused benchmark:
- **Ad-driven (hyper-casual):** must hit ~100% within **~30 days.**
- **IAP-driven (hybrid-casual):** **90–180 day** payback is normal.
- **Diagnostic rule:** *strong D0 ROAS but sharp D30 drop = a retention problem, not a UA problem.*
- **Only scale UA after D7 retention + ARPDAU are stable for 3–4 weeks.**

---

## Reading these for FREE as a no-budget solo dev

You can approximate the *predictive front half* and skip the *paid back half*:

1. **CTR proxy, ~$0:** post the gameplay-teaser clip organically (TikTok/Reels/Shorts). **Organic
   view-through + save/share rate is a free proxy for ad CTR** — no traction = the concept lacks pull.
2. **Retention + monetization via a small soft launch:** release to 1–2 small English geos (Philippines,
   then CA/AU/NZ). **~1,000–5,000 users = significance, not 100,000.**
3. **Free tooling:**
   - **App Store Connect Analytics** — now 100+ metrics incl. D7/D30/D90 retention **and free,
     privacy-preserving peer-group benchmarks** (your conversion/retention/crash/proceeds vs similar
     apps) — no SDK. *An hour a week gets real value.*
   - **GameAnalytics** (free) — D1/D7/D30, DAU/MAU, session length, ARPDAU with genre benchmarks.
   - **Firebase Analytics** (free) — event funnels + retention; pair with Crashlytics (keep crash <1%).
   - **Adjust/AppsFlyer** (MMP) — only worth it once you spend on paid UA; overkill pre-revenue.
4. **Gates to act on:** **D1** is your #1 free go/kill (48h). Then **D7 + session/stickiness.** Then
   ASC **conversion rate** vs peer benchmark (your free ASO gate). The **organic multiplier** (organic ÷
   paid installs) — healthy 1.5–2.0× — is what a no-budget dev is implicitly betting everything on.
5. **The discipline:** **don't spend a dollar on UA until the retention gate passes** — it can't be
   bought back.

---

## Confidence note

The richest genre-specific bands (hybrid "scalable/elite" numbers) come from a single-author blog
(GameGrowthAdvisor), directionally consistent with Liftoff/GameAnalytics/Segwise but **treat the precise
cutoffs as informed estimates, not audited data.** Keep "test CPI" (cheap early traffic) and "scaled-UA
CPI" (3–8× higher) separate or you'll misjudge.
