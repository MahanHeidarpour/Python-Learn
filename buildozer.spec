[app]
title = Python Learn
package.name = pythonlearn
package.domain = org.pythonlearn

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 1.0

requirements = python3,kivy==2.3.1,arabic-reshaper,python-bidi

icon.filename = %(source.dir)s/assets/icon.png

orientation = portrait
fullscreen = 0

android.permissions =

android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
