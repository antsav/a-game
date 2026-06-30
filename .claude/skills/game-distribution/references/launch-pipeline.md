# Launch Pipeline — iOS, End-to-End (solo dev)

The phases from "build is done" to "live and growing." This is the **"what are the steps?"**
answer. Apple-official facts are solid; third-party/practitioner claims are flagged.

> **Verify before a real launch:** Apple changed age ratings, the SDK minimum, privacy rules,
> and Guideline 4.3 in 2025–2026. Specific rules below carry a date — re-check the live Apple
> docs near any hard launch date. The *technical* build/export/signing/Fastlane mechanics live
> in the `unity-3d` skill; this file is the strategic pipeline.

The phases, in order: **0 Setup → 1 Testing (internal → beta → soft launch) → 2 Submission &
review → 3 ASO (see `aso.md`) → 4 Launch timing & featuring → 5 Post-launch live-ops.**

---

## PHASE 0 — Pre-submission setup (decisions locked at upload)

**Release option** (per release, distinct from phased release): **Manual / Automatic / Scheduled.**
- **Manual** is the default for an organic launch — the approved build waits in "Pending
  Developer Release" and you press go, so you're not live at 3 a.m. whenever review clears.
- Changeable any time **before** approval; **locked after**. After you press release it can take
  up to ~24h to appear.

**Age rating ⚠️ (changed 2026).** Apple moved to **4+, 9+, 13+, 16+, 18+** with a new mandatory
questionnaire (in-app controls, capabilities, social-media declaration; a further update landed
July 2026). Ratings are now **per region**. A calm single-player puzzle with no chat/UGC lands at
**4+** — but you must still answer the new questions or updates get blocked.

---

## PHASE 1 — Pre-launch testing (three gates, three DIFFERENT purposes)

Don't collapse these — each exists for a different reason:

| Gate | Purpose | Audience |
|---|---|---|
| Internal QA / internal TestFlight | **Find bugs** | You + a tiny trusted circle |
| External TestFlight beta | **Polish feel, FTUE, feedback** | Enthusiast testers (NOT representative payers) |
| Soft launch | **Measure retention + tune monetization at scale** | Real users in a live store geo |

### TestFlight
- **Internal testers: up to 100** (your App Store Connect team) — **no Beta App Review**, builds
  live within minutes of processing.
- **External testers: up to 10,000** by email or public link.
- **External builds need Beta App Review — but only the first build of a new version** (minor
  bumps usually don't re-trigger). Beta review is lighter/faster than full review.
- **Builds expire 90 days after upload** — refresh before day 90 during an active beta.
- **Use beta for game feel, FTUE clarity, crashes across devices — NOT for retention/monetization
  signal** (testers are enthusiasts, not a representative cohort).

### Soft launch — the only phase that gives trustworthy retention/LTV signal
A limited **geographic release of the real, store-listed app** (not TestFlight) to read
retention, monetization, and infra before a global push. Run in two stages:

| Geo | Why |
|---|---|
| **Philippines** | CPI < ~$0.50, ~92% English — cheap funnel/tracking/FTUE validation (used in ~half of soft launches) |
| **Canada / Australia / New Zealand** | English, US-like behavior & ARPU — read real retention/ARPDAU at low risk to the main market |
| **Nordics / UK** | Higher CPI, strong payments — good for *monetization* tuning |

**Pattern:** Philippines first (validate tracking + FTUE cheaply) → CA/AU/NZ (read US-like
retention & ARPDAU). **Duration:** no fixed number; the decision rule is **3–4 weeks of *stable*
D7 retention + ARPDAU before any meaningful scale.** See `launch-metrics.md` for the gate numbers.

**Solo-dev note:** you need **~1,000–5,000 users for significance, not 100,000.** A small organic
soft launch + App Store Connect's free peer-benchmark analytics gets you a real read without a
UA budget.

---

## PHASE 2 — Submission & App Review (2026 mechanics)

**SDK gate ⚠️ (since Apr 28, 2026):** uploads must be built with the **iOS/iPadOS 26 SDK or
later.** An older Unity/Xcode toolchain can't upload — a `unity-3d` concern, but it blocks
distribution, so check it early.

**Privacy — three SEPARATE obligations (don't conflate):**
1. **App Privacy "nutrition labels"** — declare every data type collected, why, and whether used
   to track — *including what your third-party SDKs do* (ad/analytics SDKs count). Self-reported
   but legally enforceable.
2. **Privacy manifests + signatures** (`PrivacyInfo.xcprivacy`, since May 2024) — declare
   Required-Reason API usage; bundle the manifest/signature for listed third-party SDKs (Firebase,
   ad SDKs, etc.). Apple scans the binary — you can't hide an SDK. Most SDKs ship their own
   manifest; you must include them. (Wiring = `unity-3d`.)
3. **ATT (App Tracking Transparency)** — only required if you/your SDK access the IDFA or track
   across apps. ⚠️ **SKAdNetwork is superseded by AdAttributionKit**; iOS 26 closed fingerprinting
   workarounds. **A no-tracking, rewarded-ads-only or no-ads v1 can often skip ATT entirely** and
   declare "data not used to track" — much simpler. Prefer that for v1 if monetization allows.

**Top rejection reasons for games:**
- **Guideline 4.3 (Spam/duplicate) — #1 reason (~28%), ⚠️ TIGHTENED June 2026.** New wording
  penalizes apps "indistinguishable from what's already widely available" and "opportunistically
  creating variants." **Directly relevant to a clone-plus strategy: the clone must be a clearly
  better/different experience, not a reskin, or it risks 4.3.** This is the distribution-side
  enforcement of the "clone-PLUS, real differentiation" thesis.
- **Guideline 2.1 (Completeness) — ~22%.** Any crash/freeze/placeholder during review = rejected.
  Test across devices and iOS versions.
- Metadata/keyword stuffing, hidden SDKs, IAP violations (digital goods must use Apple IAP),
  privacy mislabeling, unlicensed assets, broken links.

**Review timeline:** Apple cites ~90% within 24h (mostly updates from established teams). Reality
for a **new app: typically 2–5 days** in "Waiting for Review," longer in Sept/Dec. **Build a
buffer; don't promise a hard launch date assuming 24h.**

---

## PHASE 3 — ASO

The store listing is the bottom of every funnel (organic clip → store page → install). Covered in
depth in **`aso.md`**. The 80/20 for a solo dev: distinct high-contrast icon + 3 captioned portrait
gameplay screenshots + a tuned title/subtitle/keyword field + one secondary English locale +
Spanish (Mexico) for keyword space + a post-win `requestReview` call to climb past 4.0★.

---

## PHASE 4 — Launch timing, phased release & featuring

**Phased release is UPDATES ONLY — not your first launch.** It rolls a *version update* to
auto-update users over 7 days (1→2→5→10→20→50→100%); pausable up to 30 cumulative days (your
kill-switch). Your **first release cannot be phased.** Skip phasing for urgent hotfixes (it delays
the fix).

**Launch is a ramp, not a day.** There's a brief new-release algorithmic window (~48–72h, 3rd-party
characterization), but the stores now weight **retention over raw install spike** — spike-and-churn
is penalized. An organic dev can't manufacture day-one velocity (that's what ads buy), so you win by
**compounding signals over weeks**: steady downloads, strong D1/D7, accumulating 4★+ ratings.
Polish > early. Don't burn the window on a buggy build. **First launch = Manual release.**

**Apple editorial featuring — the best no-budget velocity substitute.** Surfaces on the Today and
Games tabs.
- **Nominate via App Store Connect → [app] → Featuring → Nominations → Create.** Types:
  **App Launch / New Content / App Enhancements.** Write a detailed pitch, set a publish date,
  attach in-app events + up to 5 supplemental URLs. Needs Account Holder/Admin/App Manager/Marketing
  role.
- **Submit ≥3 weeks before** the desired moment (major launches: up to ~3 months ahead).
- **What editors weigh:** visual craft / distinctive UI (highest-weighted), innovation/use of latest
  Apple APIs, accessibility, localization, and a **human/editorial story**. ~90% of featured apps
  hold **4.0★+**.
- **Biggest mistake:** pitching the *version* ("we shipped 2.0") instead of a *story* ("a calm,
  no-timer puzzle a solo dev built to feel meditative"). A well-being-adjacent calm puzzle is a
  *gift* for this pitch — lead with the story and the design craft.

**In-App Events** (time-bound: challenges, seasonal drops) surface as event cards, are indexed in
Search, and can be attached to a featuring nomination as the "why now." Post-launch growth tool;
design the loop so recurring content is cheap to stamp out.

---

## PHASE 5 — Post-launch live-ops (sustainable, solo-scale)

- **Iteration loop:** analytics → hypothesis → update → measure, on a light content calendar.
- **Cadence that compounds:** a couple of well-messaged updates in the first 90 days can roughly
  double the tail; each update is a fresh featuring-nomination hook. Hit clear Day-30 and Day-90
  beats (a patch + a content drop).
- **Reviews:** reply in App Store Connect; converting a 1★ bug report into an edited-up rating is
  one of the few direct rating levers you control.
- **Keep it lean:** lightweight analytics (D1/D7, crash rate, ratings), one re-skinnable event
  template, fast hotfixes. **Don't build a data warehouse or a bespoke event engine** — an
  over-engineering trap for this user.

---

## The lean solo-dev pipeline (do vs skip)

**DO:** internal TestFlight QA → small external beta for FTUE feel → lean soft launch (PH → NZ/CA/AU)
→ get privacy right (prefer no-tracking v1) → 80/20 ASO → **featuring nomination filed 3+ weeks
ahead** → Manual first release → treat launch as a multi-week ramp → sustainable monthly content via
phased-release updates.

**SKIP / DEFER until there's traffic or revenue:** PPO/CPP A/B tests (won't reach significance at
low traffic), full app localization beyond metadata, large paid UA, bespoke per-event live-ops,
heavy analytics infrastructure.
