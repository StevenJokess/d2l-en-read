

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:37:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-14 00:17:32
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/tutorials/recipes/android_native_app_with_custom_op.html
-->

following packages

## Android NDK

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

## OpenCV SDK for Android

Our custom operator will be implemented using the OpenCV library. To use it for Android, we need to download OpenCV SDK for Android with prebuilt libraries. Download from OpenCV releases page. Unzip it and set the environment variable OPENCV_ANDROID_SDK to it.


## 使用自定义C ++运算符准备TorchScript模型



这段代码生成了compute.pt文件，它是使用自定义op my_op .warp_perspective的TorchScript模型。


https://pytorch.org/tutorials/recipes/android_native_app_with_custom_op.html


使Android应用程序

在成功获得compute.pt之后，我们想在Android应用程序中使用这个TorchScript模型。在Android上使用通用的TorchScript模型(没有自定义操作符)，使用Java API，你可以在这里找到。我们不能在我们的例子中使用这种方法，因为我们的模型使用了一个自定义操作符(my_op .warp_perspective)，默认的TorchScript执行将无法找到它。

ops的注册不暴露在PyTorch Java API中，因此我们需要用native part (c++)构建Android应用程序，并使用LibTorch c++ API为Android实现和注册相同的自定义操作符。由于我们的操作员使用OpenCV库-我们将使用预构建的OpenCV Android库并使用OpenCV相同的功能。

让我们开始在NativeApp文件夹中创建Android应用程序。


```
import torch
import torch.utils.cpp_extension

print(torch.version.__version__)
op_source = """
#include <opencv2/opencv.hpp>
#include <torch/script.h>

torch::Tensor warp_perspective(torch::Tensor image, torch::Tensor warp) {
  cv::Mat image_mat(/*rows=*/image.size(0),
                    /*cols=*/image.size(1),
                    /*type=*/CV_32FC1,
                    /*data=*/image.data_ptr<float>());
  cv::Mat warp_mat(/*rows=*/warp.size(0),
                   /*cols=*/warp.size(1),
                   /*type=*/CV_32FC1,
                   /*data=*/warp.data_ptr<float>());

  cv::Mat output_mat;
  cv::warpPerspective(image_mat, output_mat, warp_mat, /*dsize=*/{64, 64});

  torch::Tensor output =
    torch::from_blob(output_mat.ptr<float>(), /*sizes=*/{64, 64});
  return output.clone();
}

static auto registry =
  torch::RegisterOperators("my_ops::warp_perspective", &warp_perspective);
"""

torch.utils.cpp_extension.load_inline(
    name="warp_perspective",
    cpp_sources=op_source,
    extra_ldflags=["-lopencv_core", "-lopencv_imgproc"],
    is_python_module=False,
    verbose=True,
)

print(torch.ops.my_ops.warp_perspective)


@torch.jit.script
def compute(x, y):
    if bool(x[0][0] == 42):
        z = 5
    else:
        z = 10
    x = torch.ops.my_ops.warp_perspective(x, torch.eye(3))
    return x.matmul(y) + z


compute.save("compute.pt")
```

This snippet generates compute.pt file which is TorchScript model that uses custom op my_ops.warp_perspective.

You need to have installed OpenCV for development to run it.






## Building the app

To specify to gradle where is Android SDK and Android NDK, we need to fill NativeApp/local.properties.

```
cd NativeApp
echo "sdk.dir=$ANDROID_HOME" >> NativeApp/local.properties
echo "ndk.dir=$ANDROID_NDK" >> NativeApp/local.properties
```

To build the result apk file we run:

```
cd NativeApp
gradle app:assembleDebug
```

To install the app on the connected device:

```
cd NativeApp
gradle app::installDebug
```


After that, you can run the app on the device by clicking on PyTorchNativeApp icon. Or you can do it from the command line:

```
adb shell am start -n org.pytorch.nativeapp/.MainActivity
```

If you check the android logcat:

```
adb logcat -v brief | grep PyTorchNativeApp
```

你应该看到带有标签' PyTorchNativeApp '的日志，它打印x, y，以及模型forward的结果，我们用log函数在NativeApp/app/src/main/cpp/pytorch_nativeapp.cpp打印。

---

在最后一行，我们打印输出的前5个条目。因为在本教程的前面，我们在Python中为模型提供了相同的输入，所以理想情况下，我们应该看到相同的输出。让我们通过重新编译我们的应用程序并使用相同的序列化模型运行它来尝试一下:



To move your model to GPU memory, you can write model.to(at::kCUDA);. Make sure the inputs to a model are also living in CUDA memory by calling tensor.to(at::kCUDA), which will return a new tensor in CUDA memory.


获取帮助并探索API

希望本教程使您对PyTorch模型从Python到c++的路径有了一个大致的了解。通过本教程中描述的概念，您应该能够从一个普通的、“迫切的”PyTorch模型过渡到Python中编译的ScriptModule，到磁盘上的序列化文件，然后(结束循环)过渡到c++中的可执行脚本::模块。

当然，还有许多概念我们没有涉及。例如，你可能会发现自己想用c++或CUDA实现的自定义操作符扩展ScriptModule，并在纯c++生产环境中加载的ScriptModule中执行这个自定义操作符。好消息是:这是可能的，而且得到了很好的支持!现在，您可以查看这个文件夹中的示例，稍后我们将提供一篇教程。目前，以下连结可能会对你有所帮助:

The Torch Script reference: https://pytorch.org/docs/master/jit.html
The PyTorch C++ API documentation: https://pytorch.org/cppdocs/
The PyTorch Python API documentation: https://pytorch.org/docs/
