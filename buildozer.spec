[app]
title = XAU Smart Scanner
package.name = xauscanner
package.domain = org.xau.scanner
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,cython==0.29.36,pyjnius==1.6.1,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
