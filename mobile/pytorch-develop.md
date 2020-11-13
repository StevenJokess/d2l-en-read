

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:37:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 22:42:32
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/tutorials/recipes/android_native_app_with_custom_op.html
-->

following packages

## ndroid NDK

```
wget https://dl.google.com/android/repository/android-ndk-r19c-linux-x86_64.zip
unzip android-ndk-r19c-linux-x86_64.zip
export ANDROID_NDK=$(pwd)/android-ndk-r19c
```

## Android SDK

```
wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
unzip sdk-tools-linux-3859397.zip -d android_sdk
export ANDROID_HOME=$(pwd)/android_sdk
```

## Gradle 4.10.3

Gradle is the most widely used build system for android applications, and we will need it to build our application. Download it and add to the path to use gradle in the command line.
```
wget https://services.gradle.org/distributions/gradle-4.10.3-bin.zip
unzip gradle-4.10.3-bin.zip
export GRADLE_HOME=$(pwd)/gradle-4.10.3
export PATH="${GRADLE_HOME}/bin/:${PATH}"
```


## openjdk

Gradle requires JDK, you need to install it and set environment variable JAVA_HOME to point to it. For example you can install OpenJDK, following instructions.

https://openjdk.java.net/install/



