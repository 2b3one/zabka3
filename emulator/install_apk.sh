#!/bin/bash

curl -L -o zappka.apk "https://apkpure.com/pl/zappka/com.zabka.zappka/download"

adb devices
adb install zappka.apk