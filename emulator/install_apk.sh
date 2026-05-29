#!/bin/bash
set -e

# 1. Czekamy aż emulator się zgłosi do ADB
echo "Czekam na emulator..."
adb wait-for-device

echo "Lista urządzeń:"
adb devices

# 2. Pobieramy APK
echo "Pobieram APK Żappki..."
curl -L -o zappka.apk "https://apkpure.com/pl/zappka/com.zabka.zappka/download"

# 3. Instalacja
echo "Instaluję APK..."
adb install zappka.apk