

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 17:23:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 18:23:35
 * @Description:
 * @TODO::
 * @Reference:
-->
https://github.com/pytorch/pytorch/tree/master/android

https://github.com/pytorch/pytorch/blob/master/android/pytorch_android_torchvision/src/androidTest/java/org/pytorch/torchvision/TorchVisionInstrumentedTests.java

```java
package org.pytorch.torchvision;

import static org.junit.Assert.assertArrayEquals;

import android.graphics.Bitmap;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.pytorch.Tensor;

@RunWith(AndroidJUnit4.class)
public class TorchVisionInstrumentedTests {

  @Test
  public void smokeTest() {
    Bitmap bitmap = Bitmap.createBitmap(320, 240, Bitmap.Config.ARGB_8888);
    Tensor tensor =
        TensorImageUtils.bitmapToFloat32Tensor(
            bitmap,
            TensorImageUtils.TORCHVISION_NORM_MEAN_RGB,
            TensorImageUtils.TORCHVISION_NORM_STD_RGB);
    assertArrayEquals(new long[] {1l, 3l, 240l, 320l}, tensor.shape());
  }
}
```


```cmake
cmake_minimum_required(VERSION 3.4.1)
project(pytorch_vision_jni CXX)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_VERBOSE_MAKEFILE ON)

set(pytorch_vision_cpp_DIR ${CMAKE_CURRENT_LIST_DIR}/src/main/cpp)

file(GLOB pytorch_vision_SOURCES
  ${pytorch_vision_cpp_DIR}/pytorch_vision_jni.cpp
)

add_library(pytorch_vision_jni SHARED
    ${pytorch_vision_SOURCES}
)

target_compile_options(pytorch_vision_jni PRIVATE
  -fexceptions
)

set(BUILD_SUBDIR ${ANDROID_ABI})

target_link_libraries(pytorch_vision_jni)
```


https://oss.sonatype.org/#nexus-search;quick~pytorch_android
