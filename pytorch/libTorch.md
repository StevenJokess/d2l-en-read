

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 20:20:22
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 17:21:05
 * @Description:
 * @TODO::
 * @Reference:
-->

# 使用libTorch

除了TorchScript之外，PyTorch 1.0还引入了libTorch，这是一个用于与PyTorch交互的c++库。可以使用各种级别的c++交互。最低的级别是ATen和autograd，这是PyTorch本身所建立的张量和自动微分的c++实现。在这些之上是一个c++前端，它重复了Python在c++中的PyTorch API，一个到TorchScript的接口，最后是一个扩展接口，允许新的自定义c++ /CUDA操作符被定义并暴露给PyTorch的Python实现。在本书中，我们只关心c++前端和TorchScript的接口，但是关于其他部分的更多信息可以在PyTorch文档中找到。让我们从libTorch开始。

## 获得libTorch和Hello World

在我们做任何事情之前，我们需要一个c++编译器和在我们的机器上构建c++程序的方法。这是本书中少数几个不适合使用谷歌Colab的部分之一，因此如果您不能方便地访问终端窗口，您可能需要在谷歌Cloud、AWS或Azure中创建一个VM。(我敢打赌，那些无视我的建议、不去打造专用机器的人现在都在沾沾自喜了!)libTorch的要求是一个c++编译器和CMake，所以让我们安装它们。在基于debian的系统中，使用以下命令:

apt install cmake g++

If you’re using a Red Hat–based system, use this:

yum install cmake g++

接下来，我们需要下载libTorch本身。为了使事情更简单一些，接下来我们将使用基于cpu的libTorch发行版，而不是处理支持gpu的发行版带来的附加CUDA依赖。创建一个名为torchscript_export的目录并获取分发版:

wget https://download.pytorch.org/libtorch/cpu/libtorch-shared-with-deps-latest.zip

Use unzip to expand the ZIP file (it should create a new libtorch directory) and create a directory called helloworld. In this directory, we’re going to add a minimal CMakeLists.txt, which CMake will use to build our executable:

```cmake
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(helloworld)

find_package(Torch REQUIRED)

add_executable(helloworld helloworld.cpp)
target_link_libraries(helloworld "${TORCH_LIBRARIES}")
set_property(TARGET helloword PROPERTY CXX_STANDARD 11)
```

And then helloworld.cpp is as follows:

```cpp
#include <torch/torch.h>
#include <iostream>

int main() {
  torch::Tensor tensor = torch::ones({2, 2});
  std::cout << tensor << std::endl;
}
```

Create a *build* directory and run **cmake**, making sure that we provide an absolute path to the libtorch distribution:

```
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=/absolute/path/to/libtorch ..
cd ..
```

```
make
./helloworld

1  1
1  1
[ Variable[CPUType]{2,2} ]
```



祝贺您使用libTorch构建了您的第一个c++程序!现在，让我们对此展开，看看如何使用这个库来加载之前用torch.jit.save()保存的模型。


## 导入TorchScript模型

我们将从第3章导出完整的CNNNet模型，并将其加载到c++中。在Python中，创建一个CNNNet实例，将其切换到eval()模式，忽略Dropout、trace和save to disk:

```py
cnn_model = CNNNet()
cnn_model.eval()
cnn_traced = torch.jit.trace(cnn_model, torch.rand([1,3,224,224]))
torch.jit.save(cnn_traced, "cnnnet")
```


Over in the C++ world, create a new directory called load-cnn and add in this new CMakeLists.txt file:

```cmake
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(load-cnn)

find_package(Torch REQUIRED)

add_executable(load-cnn.cpp load-cnn.cpp)
target_link_libraries(load-cnn "${TORCH_LIBRARIES}")
set_property(TARGET load-cnn PROPERTY CXX_STANDARD 11)
```

Let’s create our C++ program, load-cnn.cpp:

```cpp
load-cnn.cpp:

#include <torch/script.h>
#include <iostream>
#include <memory>

int main(int argc, const char* argv[]) {

  std::shared_ptr<torch::jit::script::Module> module = torch::jit::load("cnnnet");

  assert(module != nullptr);
  std::cout << "model loaded ok\n";

  // Create a vector of inputs.
  std::vector<torch::jit::IValue> inputs;
  inputs.push_back(torch::rand({1, 3, 224, 224}));

  at::Tensor output = module->forward(inputs).toTensor();

  std::cout << output << '\n'
}
```



```sh
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=/absolute/path/to/libtorch ..
cd ..
make
./load-cnn

0.1775
0.9096
[ Variable[CPUType]{2} ]
```


瞧!一个c++程序，执行一个定制的模型，在我们这方面不费什么力气。请注意，c++接口仍处于编写的beta测试阶段，因此这里的一些细节可能会发生变化。在愤怒地使用它之前，一定要查看一下文档!

---

https://zhuanlan.zhihu.com/p/52154049

获取libtorch
获取libtorch的方式有两种：

从官网下载最新的编译好的文件：https://pytorch.org/cppdocs/installing.html
自己进行源码编译
我这里推荐第二种，因为官方编译好的版本为了兼容性，选择了旧式的C++-ABI(相关链接：https://github.com/pytorch/pytorch/issues/13541 ; https://discuss.pytorch.org/t/issues-linking-with-libtorch-c-11-abi/29510)，如果你使用的gcc版本>5，那么如果你将libtorch与其他编译好的库(使用gcc-5以及以上)进行联合编译，很有可能出现冲突，为了避免环境上面的问题，建议自己对源码进行编译。当然大家也可以测试下官方的

当然还有一点需要说明，如果你仅仅只单独使用libtorch库(从官方下载，并没有链接其他库，例如opencv)，那么你这样编译那么是没有任何问题的。大家可以直接下载官方编译好的包进行快速尝试。


编译好之后的libtorch在path/to/pytorch/torch/lib/tmp_install中。

我们之后在cmake时需要添加-DCMAKE_PREFIX_PATH=/path/to/pytorch/torch/lib/tmp_install引入libtorch路径。

不懂什么是Cmake的可以看这里：编译器gcc、clang、make、cmake辨析
