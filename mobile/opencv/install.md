

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 21:39:31
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 21:40:01
 * @Description:
 * @TODO::
 * @Reference:
-->

2.1 下载 OpenCV-Android-SDK，下载地址: https://opencv.org/releases.html，我下载的版本是３.４.１

2.2 点击 File -> new -> Import Module, 选中 OpenCV-Android-SDK/sdk/java 文件夹,点击确定，就会自动识别处模块，如下图所示：



完成后会发现 app目录下的 build.gradle 中的 dependencies 增加了 opencv 的依赖。如上图所示。

2.5 统一OpenCV 库的版本和工程的版本号，即把 OpenCV 库目录下的 build.gradle 中的编译版本，构建版本等参数设置成和工程一样。


Open CV的版本号


工程版本号

将opencv的版本号改成和工程的一致。然后同步更新gradle，编译。

2.6 将 OpenCV-Android-SDK/sdk/native/libs 目录下全部内容复制到 工程目录/app/src/main/jniLibs 目录下（这里可以针对特定的手机做裁剪，为了方便可以全部复制）
