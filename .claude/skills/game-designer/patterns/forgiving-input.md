# Pattern: Forgiving Input — Resolve Tap Ambiguity in the Player's Favor

> **One line:** When a tap is ambiguous (small or overlapping targets, fat-finger reach), don't
> take the input literally and don't punish — **infer the target the player most likely wanted**,
> and among plausible targets pick the one that lets them **progress further**.

**Tags:** `input` · `game-feel` · `forgiveness` · `accessibility` · `retention` · `hyper-hybrid-casual` · `flagship`
**Status:** load-bearing — a core game-feel rule for any tap-select game with small targets.

---

## Where observed (evidence in the wild)

- **Arrows / arrow-untangle** (Anton, 2026-06-30) — in zoomed-out mode the arrows are **small**, and
  a fingertip easily covers **several** at once. The game doesn't reject the tap, doesn't fire a
  random arrow, and doesn't punish the imprecision. It **selects the "good" arrow** at the tap spot —
  the one that lets you progress further. The player experiences it as "the game read my mind," not
  "I misclicked."
- **Apple's iOS keyboard** (Anton's analogy) — the keyboard does **not** rely purely on the raw
  touch coordinate. It biases toward keys that are statistically likely given nearby geometry and the
  word being typed, so a slightly-off press still lands the intended letter. Same principle: the
  literal tap point is *evidence*, not *the answer*.
- **General craft:** platformers ship **coyote time** and **jump-input buffering**; shooters ship
  **aim assist / bullet magnetism**; match-3 and sort games snap to the nearest legal target. All are
  the same move — the engine quietly corrects for human motor imprecision so the *intent* lands.

## Why it works (the psychology)

1. **Separates intent from execution.** Players form an intent ("select *that* arrow") and then
   execute imperfectly on a small touch target (fingertip ≈ 44–57px; a zoomed-out arrow is smaller).
   Punishing the execution error blames the player for a **hardware/ergonomics** limit they can't
   fix. Forgiving input scores the *intent*, which is what the player actually controls.
2. **Fitts's Law is against you on mobile.** Small, dense targets make fast accurate taps
   near-impossible. Rather than force the player to slow down and aim (kills flow, kills calm),
   **shrink the effective difficulty of acquisition** by widening hit areas and disambiguating
   smartly. Speed stays; frustration drops.
3. **Errors feel like the game's fault — unless the game absorbs them.** A misfire from an honest
   fat-finger reads as *unfair* (the harshest emotion in casual play). Silently doing the sensible
   thing converts a would-be frustration into an invisible non-event — or even a small delight
   ("how did it know?").
4. **Progress-biased disambiguation compounds the goodwill.** When several targets are plausible,
   picking the one that **advances the player** turns ambiguity into a *lucky break* instead of a
   coin-flip. The game feels generous and on-your-side — a retention driver, especially for the
   calm, no-pressure player who is here to feel good, not to be tested on dexterity.

## How to apply (to our game)

- **Widen the hit target beyond the sprite.** Give tappable elements an invisible touch area padded
  to ≥ 44pt even when the drawn art is tiny (especially in zoomed-out states). The *visual* can be
  small; the *hittable* region should not be.
- **On an ambiguous tap, gather candidates, then rank — don't random-pick.** When one tap overlaps
  N targets, build the candidate set and choose by a priority rule, in order:
  1. **Legal / actionable** over inert (never select something that can't do anything).
  2. **Maximizes progress** — the move that clears the most, unblocks the most, or advances the goal.
  3. **Closest to the tap centroid** as the tiebreak.
  Avoid "first in z-order" or "random" — both feel arbitrary and occasionally punish.
- **Bias toward the player, not the challenge.** Where it's genuinely a toss-up, resolve *for* the
  player. In a calm game the cost of over-helping is near zero; the cost of a felt injustice is high.
- **Use context as a prior (the keyboard trick).** The touch point is one signal; combine it with
  game state — which targets are currently useful, what the player did last, what's near the goal.
  This is cheap and makes selection feel intelligent.
- **Keep the assist invisible.** No "auto-corrected" toast, no highlight of the rejected targets. The
  best forgiveness is unfelt. (Contrast juice: the *selected* target should still get a satisfying
  confirm animation — forgive the input, celebrate the result.)
- **Tune, then hide the seams:** log ambiguous taps in playtest; if the assist ever picks a target
  the player didn't want, that's a bug in the ranking, not a reason to drop assist.

## Anti-patterns (how it breaks)

- **Literal tap → nearest pixel wins.** Punishes honest imprecision; the #1 "this game feels unfair"
  cause on dense boards.
- **Random pick among overlapped targets.** Feels arbitrary; occasionally makes a *worse* move than
  the player would have, which reads as betrayal.
- **First-in-draw-order pick.** Couples input correctness to an implementation detail (sprite
  layering) the player can't see or predict.
- **Over-helping into no-challenge.** If the *entire* puzzle is "the game plays itself," you've
  removed agency. Forgive **acquisition** (which target), not **strategy** (whether it was the right
  target to want). Assist the finger, not the brain.
- **Visible auto-correct.** Announcing the assist makes the player self-conscious and can feel
  condescending; it also invites arguing with the game's guess.
- **Punish-on-miss feedback** (shake, buzz, deduct) for what is really an ergonomics limit — corrosive
  to the calm feel.

## Fit check (Anton's taste + hybrid-casual)

- **Strong fit — arguably required.** Anton's north-star is **meditative, no-pressure, relaxing**
  play. Fighting a small touch target is the opposite of calm; every fat-finger misfire is a tiny
  pressure spike. Forgiving input is what *lets* the player zoom out, relax, and tap loosely without
  paying for it. Cross-links `my-game-preference` (calm, bursts-of-satisfaction, intrinsic pull).
- Reinforces `single-input-modality`: both are about making the **input** disappear so only the
  *decision* remains. One gate removes mode errors; this one removes acquisition errors.

## Related patterns

- [One Input Modality](single-input-modality.md) — sibling input-friction rule; that one kills
  *mode* errors (wrong gesture), this one kills *acquisition* errors (wrong target). Together they
  make the control layer invisible.
- [Intra-Level Difficulty Arc + Peak-End](difficulty-arc-peak-end.md) — progress-biased
  disambiguation feeds the "finish on a high note" arc: ambiguity resolves *toward* progress, not
  against it.

---
*Origin: Anton, 2026-06-30 — observing the **arrows** game: small arrows in zoomed-out mode get
multiple tapped at once, yet the game doesn't punish or random-pick — it selects the arrow that lets
you progress further. His analogy: iOS keyboard statistically picks nearby-likely keys instead of
trusting the raw tap spot. Insight: a good game **helps with misclicks** — it forgives control
limits instead of punishing them.*
