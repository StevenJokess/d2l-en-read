

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 20:19:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 21:25:05
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
We tried to deploy a object detection model in Android. In PyTorch model, ‘nn.functional.interpolate’ was used in forward path to upsample feature maps . Torch script converted the model without any issues. We are not able to load the model in Android app using ‘Module.load( )’ API. This API is throwing an exception.

