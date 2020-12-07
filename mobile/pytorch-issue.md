

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 20:19:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 20:22:10
 * @Description:
 * @TODO::
 * @Reference:
-->
https://discuss.pytorch.org/t/torchvision-ops-nms-on-android-mobile/81017
 use torchvision.ops.nms in my model
 E/AndroidRuntime: Caused by: com.facebook.jni.CppException:
    Unknown builtin op: torchvision::nms.
    Could not find any similar ops to torchvision::nms. This op may not exist or may not be currently supported in TorchScript.
    :

    https://github.com/pytorch/vision/issues/2581

---
