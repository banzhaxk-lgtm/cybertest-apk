[app]
title = CyberTest
package.name = cybertest
package.domain = org.cybertest
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,md
version = 0.1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/assets/icon.png

# Android build settings
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

# No Android permissions are requested by default because the current
# implementation does not perform real network transmission or access
# Android media storage through the Android permission API.
# Add only permissions needed by features you intentionally implement.

[buildozer]
log_level = 2
warn_on_root = 1
