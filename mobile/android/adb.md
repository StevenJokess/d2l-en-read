

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 19:26:01
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 19:34:30
 * @Description:
 * @TODO::
 * @Reference:https://adbshell.com/commands/adb-push
 * https://developer.android.com/studio/command-line/adb
 * Android Debug Bridge (adb) is a command line tool that lets you communicate with an emulator or connected Android device. You can find the adb tool in android sdk/platform-tools or Download ADB Kits.
-->

## adb push
copy local files/directories to Android device

adb push pc.apk /mnt/sdcard/Download/test.apk
only push files that are newer on the host than the Android device

adb push --sync pc.apk /mnt/sdcard/Download/test.apk

## adb shell

adb shell // Open or run commands in a terminal on the host Android device.
