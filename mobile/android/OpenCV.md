

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-09 00:29:22
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-09 00:33:57
 * @Description:
 * @TODO::
 * @Reference:如何从源码编译OpenCV4Android库 - 稚晖的文章 - 知乎
https://zhuanlan.zhihu.com/p/83226948
-->

由于在实际的应用中难免会遇到一些问题，比如在Android工程中如果要同时使用SNPE（一个高性能神经网络加速库）和OpenCV时，由于SNPE使用的STL链接的是libc++，而OpenCV默认使用的是gnu_stl，所以会导致gradle不管怎么配置都无法正常编译过的情况。

这种情况下如果gradle中选择arguments '-DANDROID_STL=c++_shared'的话SNPE可以正常编译，但是在使用像imwrite这样的OpenCV函数时就会报链接错误。相反如果gradle中选择arguments '-DANDROID_STL=gnu_stl'则SNPE无法编译通过。
另外一方面，官方预编译好的OpenCV4Android库是不带contrib模块的，所以无法使用像是`xfeatures2d`这样的类。

开始编译
跟第一节中的方法一样，切换到build目录执行下面的命令即可编译：

python ../opencv/platforms/android/build_sdk.py \
--extra_modules_path=/workspace/_net/opencv_contrib/modules/ \
--config ../opencv/platforms/android/ndk-17.config.py
由于cmake configure可能会失败，多试几次就好了。
所有的指令集都编译完成后，生成的库就在OpenCV-Android-SDK目录下。



看到在ndk-17.config.py中传入的配置参数会在这里被解析更新，比如如果要使用clang编译带NEON支持的armeabi-v7a库并链接c++_shared的话，就改成下面的参数：

ABIs = [
    ABI("2", "armeabi-v7a", None, cmake_vars=dict(ANDROID_ABI='armeabi-v7a with NEON',ANDROID_STL="c++_shared"))
]
