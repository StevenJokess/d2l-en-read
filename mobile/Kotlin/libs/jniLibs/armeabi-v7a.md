

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 20:02:38
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 20:03:06
 * @Description:
 * @TODO::
 * @Reference:https://github.com/t-vi/AICamera/
-->
# copy arm libs
rm -rf $AICAMERA_ROOT/app/src/main/jniLibs/armeabi-v7a/
mkdir $AICAMERA_ROOT/app/src/main/jniLibs/armeabi-v7a
cp -r build_android_arm/lib/lib* $AICAMERA_ROOT/app/src/main/jniLibs/armeabi-v7a/
