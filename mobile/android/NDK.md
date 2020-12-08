

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 19:24:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 19:24:46
 * @Description:
 * @TODO::
 * @Reference:
-->
Download the Android NDK and make a standalone toolchain
Download the Android NDK from the official website:

mkdir -p ~/armnn-devenv/toolchains
cd ~/armnn-devenv/toolchains
# For Mac OS, change the NDK download link accordingly.
wget https://dl.google.com/android/repository/android-ndk-r20b-linux-x86_64.zip
unzip android-ndk-r20b-linux-x86_64.zip
export NDK=~/armnn-devenv/android-ndk-r20b
export NDK_TOOLCHAIN_ROOT=$NDK/toolchains/llvm/prebuilt/linux-x86_64
export PATH=$NDK_TOOLCHAIN_ROOT/bin/:$PATH
