# CyberTest

CyberTest is a Kivy-based diagnostic/demo application.

## Current behavior and limitations

- The UI contains a user view and an admin view.
- The admin view scans a small set of Android media paths when they exist. On desktop these paths normally do not exist, so the scan may report zero files.
- The network engine currently **simulates** inbound updates and outbound handling. It does not connect to a real server or transmit telemetry.
- The `admin_secret` string in the UI is a demo gate, **not secure authentication**. Do not use it to protect sensitive functions in a production app.
- This project does not currently upload, copy, or exfiltrate media files.

## Run on desktop

Use Python 3.10 or 3.11 in a virtual environment, then:

```bash
python -m pip install -r requirements.txt
python main.py
```

## Build Android APK with Buildozer

Buildozer's Android toolchain is most reliable on Linux. On Windows, use WSL2 with Ubuntu.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install buildozer
buildozer -v android debug
```

The APK is usually placed under `bin/`. First Android builds can take a while and require internet access to download the Android toolchain.

## GitHub

Commit the source, `buildozer.spec`, `requirements.txt`, `README.md`, and `assets/icon.png`. Do not commit virtual environments, build output, API secrets, or signing keys. Buildozer can be run locally or through a Linux CI runner; CI requires the Android SDK/NDK dependencies and should cache its toolchain to reduce build time.

## Scope of this review

The supplied archive contains six Python source files and no existing Buildozer configuration, dependency manifest, automated tests, or existing icon. Syntax was checked, packaging files and an icon were added, and the misleading storage-success condition was corrected. A successful Android build still needs to be run in a configured Buildozer/Linux environment.
