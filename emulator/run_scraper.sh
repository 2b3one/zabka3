#!/bin/bash

mkdir -p data/screens

adb shell monkey -p com.zabka.zappka 1
sleep 12

# menu
adb shell input tap 100 1800
sleep 3

# produkty za żappsy
adb shell input tap 300 600
sleep 5

# 5 screenshotów + scroll
for i in {1..5}
do
  adb exec-out screencap -p > data/screens/screen_$i.png
  adb shell input swipe 500 1600 500 400 500
  sleep 3
done