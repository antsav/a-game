# iOS Build & App Store Pipeline

End-to-end: Unity → Xcode → App Store. **Unity does not produce an `.ipa` — it exports an Xcode
project**; Xcode (or `fastlane gym`) turns that into a signed `.ipa` uploaded to App Store Connect. Plan
for the **privacy-manifest** and **age-rating** steps — the 2024-2026 additions that trip people up.
*Not legal/compliance advice for monetization — see `game-monetizer` for loot-box/odds rules.*

> Apple's requirements move ~annually. Verify the current Xcode/SDK minimum and pricing before building.

## Prerequisites
- **Apple Developer Program — $99/yr** (individual is fastest; org needs a D-U-N-S). Required to upload,
  use TestFlight, ship.
- **A Mac** — mandatory; iOS must be compiled+signed on macOS with Xcode. (Anton is on macOS ✓.)
- **Latest stable Xcode** — Apple requires building with **iOS 18 SDK / Xcode 16+ since Apr 24, 2025**;
  by mid-2026 expect Xcode 17 / iOS 26 SDK (verify on Apple Developer downloads). This governs the SDK you
  *compile against*, not the minimum iOS you *support*.
- **Unity + iOS Build Support module** (tick it in Hub). Use **Unity 6.3 LTS** for a new project.

## Unity iOS build settings (File → Build Profiles → iOS; Player Settings → iOS)
**Identity:** Bundle Identifier (reverse-DNS `com.fenvox.yourgame` — must match the registered App ID;
lock early) · Version (`CFBundleShortVersionString`, user-facing) · **Build number** (`CFBundleVersion`
— must be **unique & incrementing per upload**; duplicate build numbers are the #1 upload rejection) ·
Signing Team ID.
**Configuration:** **IL2CPP** (mandatory) · **ARM64** · Target minimum iOS version (separate from build
SDK) · **Metal** (required) · Managed Stripping = **Medium** (High can strip reflection-only code → add
`link.xml`) · C++ Compiler = Release (Master for final ship).
**Presentation:** Default Orientation = **Portrait** (one-handed) — must match screenshots + age questionnaire.
**Export:** building produces a **folder with an Xcode project** (`Unity-iPhone`), not an `.ipa`. Use
**Build** (fresh export) or **Build And Run** (to a connected device); "Append" preserves manual Xcode changes.

## Xcode side
1. Open the generated `Unity-iPhone.xcodeproj` — **open the `.xcworkspace` instead if CocoaPods/ad SDKs
   added one.**
2. **Signing & Capabilities:** **Automatic signing** (recommended solo — Xcode makes the cert + profile).
   ⚠️ **Known Unity gotcha:** the **`UnityFramework` target doesn't support provisioning profiles — leave
   it Automatic** even if you manually sign the main app target. This stops many first builds.
3. **Archive:** run destination = **"Any iOS Device (arm64)"** (can't archive against a simulator) →
   Product → Archive.
4. **Distribute:** Organizer → Distribute App → App Store Connect → Upload.
- Common errors: bundle-ID mismatch ("no matching profile") · distribution cert's private key not in
  this Mac's Keychain (export the `.p12` *with private key*; or use `fastlane match`) · IL2CPP/linker
  errors after ad SDKs (you opened the `.xcodeproj` not the `.xcworkspace`).

## Apple privacy requirements — CRITICAL (the cluster that rejects unprepared devs)
1. **Privacy Manifest (`PrivacyInfo.xcprivacy`)** — declares data collected + **required-reason API**
   usage. **Enforced since May 1 2024.** Xcode auto-merges yours + every SDK's into a Privacy Report.
   **Unity auto-includes its own** required-reason declarations (file timestamp, user defaults, boot
   time, disk space). **You still must declare your own** code's data collection / required-reason APIs —
   put your `PrivacyInfo.xcprivacy` in **`Assets/Plugins/`**.
2. **Third-party SDK manifests** — ad/analytics SDKs must ship their own manifest + **SKAdNetwork IDs**.
   **Use current SDK versions** (old ones predate the requirement → rejection). Let the SDK's Integration
   Manager auto-add SKAdNetwork IDs (AppLovin MAX auto-adds; LevelPlay 8.8.0+ via Network Manager).
3. **App Privacy "nutrition label"** — a **questionnaire in App Store Connect**, must be **consistent**
   with your manifests/SDKs. Ad-funded games typically declare Identifiers (IDFA), Usage Data, Crash data,
   often "used for Third-Party Advertising / Tracking."
4. **ATT + IDFA** — if any SDK uses the IDFA for cross-app tracking, you **must** call
   `requestTrackingAuthorization` (the ATT prompt) **and** add **`NSUserTrackingUsageDescription`** to
   Info.plist (without it the app crashes/rejects when the prompt fires). On denial → SKAdNetwork
   fallback (populate `SKAdNetworkItems`, usually auto by the ad SDK).

## App Store Connect
- Register the App ID/bundle ID; create the app record (unique name, SKU); upload a build (Xcode or
  `fastlane pilot`).
- **TestFlight:** **Internal** testers (≤100 team members, **no review**, minutes — your device testing);
  **External** (≤10,000, first build per version needs a ~24h Beta App Review — good for a small soft launch).
- **Metadata:** description, keywords, **privacy-policy URL (required — a dead link is a frequent
  rejection)**, support URL, category, **screenshots** (primary iPhone **1320×2868** 6.9", 6.7" 1290×2796
  fallback; supply the largest and Apple downscales).
- **Age rating (IARC questionnaire) — overhauled 2025/2026:** new 13+/16+/18+ tiers; **all devs must
  answer the updated questionnaire by Jan 31 2026 or be blocked from submitting updates.** Loot boxes /
  random items push ratings up — **a hyper-casual game with no gacha stays simple; answer honestly.**
- **Export compliance:** add **`ITSAppUsesNonExemptEncryption = NO`** to Info.plist (standard HTTPS is
  exempt) to skip the per-build "Missing Compliance" prompt.
- **Submit for review** (~24-48h); phased / manual release available.

## Build automation (and the agentic angle)
The whole pipeline is **command-line drivable** — relevant for an agent on a Mac:
- **Unity headless export:** `Unity -quit -batchmode -nographics -projectPath <p> -buildTarget iOS
  -executeMethod BuildScript.PerformiOSBuild -logFile -` (you write a small static `BuildScript` calling
  `BuildPipeline.BuildPlayer`).
- **Fastlane:** **`match`** (sync certs/profiles from an encrypted git repo — solves "key on another Mac")
  · **`gym`** (wraps `xcodebuild` → signed `.ipa`) · **`pilot`** (→ TestFlight) · **`deliver`** (→ App
  Store + metadata). Auth on CI via an **App Store Connect API key** (Key ID + Issuer ID + `.p8`, no 2FA).
  Lanes: `fastlane ios beta`, `fastlane ios release`.
- **Unity Build Automation** (hosted Mac agents, uses Fastlane) and **GitHub Actions + GameCI** are CI options.
- **Agent feasibility:** an agent **can** drive `Unity -batchmode` → `fastlane gym` → `pilot/deliver` from
  the shell given a configured account, an ASC API key, and certs in `match`. **Human-gated** (agent can't
  self-serve): Program enrollment, first cert/identifier creation, App Review, and the privacy/age
  questionnaires (judgment calls).

## Common rejections for a hyper-casual game
- **Guideline 4.3 (Spam/Duplicate)** — **the #1 rejection (~28% in 2025);** hyper-casual is highly exposed
  (shared templates). Ship genuinely distinct content/mechanics, not a reskin; don't flood from one account.
- Privacy: missing/old SDK manifest · ATT without `NSUserTrackingUsageDescription` · App-Privacy label
  contradicting the merged report.
- Ads: hard-to-dismiss interstitials, ads before content loads, deceptive creatives.
- Crashes (test the **archived TestFlight build on a real device**, not just the Editor — IL2CPP stripping
  crashes hide here) · broken privacy-policy/support links · placeholder metadata · age-rating mismatch.

## First-ship checklist (condensed)
Apple Program active · latest Xcode · Unity 6.3 LTS + iOS module · bundle ID locked · IL2CPP/ARM64/Metal/
min-iOS/stripping set · **build number incremented** · SDKs on current versions · your `PrivacyInfo.xcprivacy`
in `Assets/Plugins/` · `NSUserTrackingUsageDescription` + ATT wired · `ITSAppUsesNonExemptEncryption=NO` ·
automatic signing + `UnityFramework`=Automatic · archive on "Any iOS Device (arm64)" → upload · App Privacy
label · **age questionnaire answered** · screenshots + privacy-policy URL · TestFlight-tested on real device.

## Sources
Apple: Upcoming Requirements, Privacy manifest files, Required-reason API, User Privacy & Data Use, Updated
age ratings (Jul 2025), App Review Guidelines, ITSAppUsesNonExemptEncryption · Unity iOS build/Player
Settings docs (6000.3), Apple privacy manifest policy · Fastlane gym/match/pilot/deliver · GameCI iOS.
Full URLs in CHANGELOG notes. *Xcode/SDK minimums + ASC screenshot specs + age-rating deadline are
time-sensitive — verify before building.*
