# App Store Optimization (ASO) — iOS

Your **free, always-on conversion layer** and the bottom of every funnel (organic clip → store page →
install). Two jobs: **discoverability** (rank for the right keywords) and **conversion** (turn a tap into
an install). For games, **creatives drive installs; keywords drive visibility.**

> Apple never publishes ranking weights or the exact cross-indexed locale set, and changes ASO mechanics
> (PPO/CPP, screenshot specs, OCR) periodically. Field weights and specifics below are practitioner-
> derived — verify current specs in App Store Connect before finalizing.

---

## Keywords / text relevance

Indexed fields by approximate weight: **Title (30 char) > Subtitle (30 char) > Keyword field (100 char,
comma-separated, NO spaces).** In-app event title (30) and promotional/short description (50) are also
indexed.

Rules:
- **No duplication** — a term counts once across all fields; don't repeat your title words in the keyword
  field.
- **Don't waste the keyword field** on your app name, category, the word "app," or competitor trademarks.
- **Research like the Chrome-extension philosophy:** seed from mechanic + fantasy words, pull competitor
  keyword sets with a tool, target **moderate-volume / moderate-difficulty** terms (the beatable middle).
  Put best in Title, mid in Subtitle, long-tail in the keyword field.
- ⚠️ **Screenshot caption OCR** for keyword indexing was reported ~mid-2025 (vendor-reported, not in Apple
  docs) — treat as a bonus, not a strategy.
- For a calm puzzle: target words like **relaxing, calm, offline, no timer, brain, zen, puzzle.**

---

## Visual assets — the conversion layer (dominant for games)

- **Icon** — highest-leverage single test; small changes drive double-digit conversion swings. Simple,
  high-contrast, **distinct from genre competitors** (shown next to your first screenshots in search).
- **Screenshots** — 1–10 per locale. Author the two large source sizes (Apple auto-scales):
  **6.9″ iPhone = 1320×2868** and **13″ iPad = 2064×2752** ⚠️ (ignore old 1290×2796 guides — use Apple's
  current spec). **Only the first 1–3 show in search results** and decide most installs — lead with the
  strongest gameplay moment, one captioned message each, real gameplay. **A portrait one-handed puzzle
  should use portrait** (most action games go landscape; match your game, not the crowd).
- **App preview video** — up to 3 per locale, 15–30s, poster frame at 5s, **autoplays muted** → the first
  ~3 seconds and on-screen text must carry the message with no sound.

**Everything visual must pass the same 3-second legibility test as your marketing clips** (see
`gtm-and-marketing.md`) — it's the same skill applied to the same funnel.

---

## Ratings & reviews

- **4.0★ is the cliff** — 3.9→4.0 matters far more than 4.4→4.5; below ~3.5★ search visibility drops
  sharply. 3★→4★ can lift conversion up to ~89%.
- **`SKStoreReviewController` / `requestReview`:** system-enforced **3 prompts per 365-day rolling window
  per user**; you can't control *when* it appears and **must not tie it to a button or gate content** —
  call it only after a "win" moment (a satisfying puzzle completion).
- **Responding to reviews** correlates with ~+0.7★; a user *editing a low rating upward* is a top positive
  signal — converting a 1★ bug report is one of the few direct rating levers you control.
- **Ratings do NOT auto-reset on update.** You can manually reset the summary rating per territory but
  Apple says use sparingly (written reviews aren't reset).

---

## Localization ("localize to rank")

The US storefront cross-indexes keywords from **~10 localizations**, not just en-US. Adding **English
(UK/AU/CA)** + **Spanish (Mexico)** each grants a fresh ~160 indexable chars to expand keyword space — a
legitimate, cheap scaling tactic (metadata only, not full translation). ⚠️ Apple doesn't publish the exact
cross-indexed locale set and has changed it — verify with a tool. **Defer full app localization**
(DE/FR/JP/KR/zh/pt-BR) — that's real market expansion, not a v1 task.

---

## A/B testing — PPO vs CPP

- **Product Page Optimization (PPO)** — native A/B test of your default page: up to **3 treatments**, tests
  **icon/screenshots/previews only** (not text), you set traffic %, runs up to **90 days**, reports lift
  with a confidence indicator. Icon variants must ship inside the binary. ⚠️ **Low-traffic indie apps often
  never reach significance** — then decide qualitatively.
- **Custom Product Pages (CPP)** — not a test; up to **70 per app** ⚠️ (doubled from 35 in Oct 2025), each a
  unique URL for campaigns. ⚠️ **2025 change: a CPP can now hold keywords and replace your default page in
  organic search** — now an organic lever, not just paid.

**Solo-dev call: DEFER PPO/CPP A/B testing** until you have a few hundred daily page views — below that,
tests won't reach Apple's confidence indicator and you're better off iterating on judgment. Get the icon +
first 3 screenshots + preview *right* by hand first.

---

## The 80/20 for a solo dev (do this, skip the rest)

Distinct high-contrast **icon** + **3 captioned portrait gameplay screenshots** + tuned
**title/subtitle/100-char keyword field** of moderate-difficulty terms + **one secondary English locale +
Spanish (Mexico)** for keyword space + a post-win **`requestReview`** call to climb past 4.0★. Watch the
free **App Store Connect conversion-rate peer benchmark** and improve the icon/first screenshot until you
beat it. Everything else (PPO/CPP, full localization, OCR tricks) waits for traffic.
