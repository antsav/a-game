# Ship a Unity build to iOS / TestFlight

**Goal:** get a signed build from Unity onto your iPhone via TestFlight (then App Store). Condensed
procedure; full detail + 2024-2026 gotchas in `../references/ios-build-pipeline.md`.

**Prerequisites:** Apple Developer Program ($99/yr) active · latest stable Xcode · Unity 6.3 LTS with
**iOS Build Support** · macOS · bundle ID decided (`com.fenvox.<game>`).

## Steps

1. **Unity Player Settings → iOS:** set Bundle Identifier, Version, **Build number (increment every
   upload)**, Signing Team ID. Configuration: **IL2CPP + ARM64 + Metal**, min iOS version, Managed
   Stripping = Medium, C++ = Release. Orientation = Portrait.

2. **Privacy (do not skip):**
   - Put your `PrivacyInfo.xcprivacy` in **`Assets/Plugins/`** if your code collects data / uses
     required-reason APIs (Unity adds its own; you add yours).
   - Ad/analytics SDKs on **current versions** (they ship manifests + SKAdNetwork IDs; let their
     Integration Manager auto-add IDs).
   - If using IDFA: add **`NSUserTrackingUsageDescription`** + wire the ATT prompt.
   - Add **`ITSAppUsesNonExemptEncryption = NO`** to Info.plist (standard HTTPS is exempt).

3. **Build:** File → Build Profiles → iOS → **Build** → choose an output folder. Unity exports an
   **Xcode project** (not an `.ipa`).

4. **Xcode:** open the generated `Unity-iPhone.xcodeproj` (**or the `.xcworkspace` if pods/ad SDKs
   present**). Signing & Capabilities → **Automatic** signing, select your Team; **leave `UnityFramework`
   target on Automatic**. Set destination **"Any iOS Device (arm64)"** → Product → **Archive** →
   Organizer → **Distribute App → App Store Connect → Upload**.

5. **App Store Connect:** create the app record (unique name, bundle ID, SKU). Wait for the build to
   finish processing. **TestFlight → Internal Testing** → add yourself (≤100, no review) → install via the
   TestFlight app on your iPhone. (External testers/soft-launch need a ~24h Beta App Review.)

6. **For the actual App Store submit (later):** complete the **App Privacy** label (consistent with
   SDKs), **answer the age-rating questionnaire** (mandatory by Jan 31 2026), add screenshots
   (1320×2868 6.9"), **privacy-policy URL** + support URL → Submit for Review (~24-48h).

## Verify
The build appears under TestFlight → Internal, installs on your device, and launches without crashing.

## Troubleshooting
- "No matching provisioning profile" → bundle ID mismatch (fix in Unity, regenerate).
- IL2CPP/linker errors after ad SDKs → you opened `.xcodeproj` instead of `.xcworkspace`.
- "Duplicate build number" on upload → bump the Build number in Unity.
- Crash on launch in TestFlight but fine in Editor → IL2CPP managed-stripping removed reflection-only
  code; lower stripping or add a `link.xml`. **Always test the archived build on a real device.**
- App stuck on "Missing Compliance" each build → add `ITSAppUsesNonExemptEncryption = NO`.

## Automation (optional, agent-drivable)
`Unity -quit -batchmode -nographics -buildTarget iOS -executeMethod BuildScript.PerformiOSBuild` →
`fastlane gym` (signed `.ipa`) → `fastlane pilot` (TestFlight). Use `fastlane match` for certs and an
App Store Connect API key for non-interactive auth. See `../references/ios-build-pipeline.md`.

## Sources
Apple Developer docs (build process, privacy manifests, age ratings, encryption compliance) · Unity iOS
docs (6000.3) · Fastlane. Full URLs in `../references/ios-build-pipeline.md` + CHANGELOG.
