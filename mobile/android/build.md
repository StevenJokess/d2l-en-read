

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 23:59:32
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-14 00:04:58
 * @Description:
 * @TODO::
 * @Reference:https://developer.android.com/studio/build
-->
配置您的构建

Android构建系统编译应用程序资源和源代码，并将它们打包到APKs中，您可以对其进行测试、部署、签名和发布。Android Studio使用Gradle，一个先进的构建工具包，来自动化和管理构建过程，同时允许你定义灵活的自定义构建配置。每个构建配置可以定义自己的一组代码和资源，同时重用应用程序所有版本的公共部分。Gradle的Android插件与构建工具包一起提供特定于构建和测试Android应用程序的进程和可配置设置。

Gradle和Android插件独立于Android Studio运行。这意味着你可以在Android Studio中，在你的机器上，或者在没有安装Android Studio的机器上(比如持续集成服务器)构建你的Android应用程序。如果你不使用Android Studio，你可以学习如何从命令行构建和运行你的应用程序。无论您是从命令行、远程机器还是使用Android Studio构建项目，构建的输出都是相同的。

注意:因为Gradle和Android插件是独立于Android Studio运行的，所以你需要分别更新构建工具。阅读发布说明了解如何更新Gradle和Android插件。

Android构建系统的灵活性使您能够执行自定义构建配置，而无需修改应用程序的核心源文件。本节帮助您理解Android构建系统如何工作，以及它如何帮助您定制和自动化多个构建配置。如果你只是想了解更多关于部署你的应用程序，请参见build and Running from Android Studio。要立即使用Android Studio创建自定义构建配置，请参阅配置构建变体。


## gradle.properties

This is where you can configure project-wide Gradle settings, such as the Gradle daemon's maximum heap size. For more information, see The Build Environment.

## local.properties
Configures local environment properties for the build system, including the following:
ndk.dir - Path to the NDK. This property has been deprecated. Any downloaded versions of the NDK will be installed in the ndk directory within the Android SDK directory.
sdk.dir - Path to the SDK.
cmake.dir - Path to CMake.
ndk.symlinkdir - in Android Studio 3.5+, creates a symlink to the NDK that can be shorter than the installed NDK path.
