

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:35:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 20:23:37
 * @Description:
 * @TODO::
 * @Reference:
-->
https://pytorch.org/javadoc/

PyTorch Java Demo
This repository is a demonstration of how to use PyTorch from Java.

Setup
Download and unpack libtorch nightly (or 1.4 or greater once it is released). From the pytorch.org homepage under "Quick Start Locally", make sure "LibTorch" is the selected package. As of this writing, only Linux is supported. Mac and Windows will follow.

Run export LIBTORCH_HOME=/path/to/libtorch. The build.gradle file will use this to set java.library.path when running the application. If you are using PyTorch in your own environment, LIBTORCH_HOME is not necessary. Instead, you will need to set java.library.path to /path/to/libtorch/lib.

Run ./gradlew run to build and run the demo application. It will load demo-model.pt and run it on some simple data. This notebook was used to generate the model.

https://github.com/dreiss/java-demo
