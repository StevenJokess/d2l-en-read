

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 00:39:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-12 01:44:18
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/108679717
-->

PyTorch1.3 把检测+识别的所有代码都转成TorchScript之后，放到移动端运行，却发现在移动端的推理速度比PC慢了好几倍，不得不放弃这个方案。

TODO: 具体几倍？

https://github.com/Arctanxy/learning_notes/tree/master/DeepLearningDeploy/PyTorch_ONNX_TVM

文章分为四个部分：

1. 环境准备----编译安装LLVM/TVM/ONNX
2. PyTorch转ONNX
3. ONNX转TVM
4. TVM模型优化


## 1. 环境准备


### 1.1 LLVM编译

为了编译TVM，首先要编译LLVM，LLVM是一个编译器框架。

tips 1: 我之前尝试过使用预编译的LLVM来编译TVM，但是编译完成之后，TVM还是会提示Target llvm is not enabled. 所以才会使用源码编译
tips 2: 因为库比较大，可以考虑从Gitee下载

## 下载LLVM

```sh
git clone https://gitee.com/mirrors/LLVM.git
```

## 编译LLVM

这里选择编译Release版，因为我们也不需要对LLVM进行debug，而且Release版本比较容易编译成功。

```sh
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ../llvm
make -j4
```

### 1.2 TVM编译与PythonAPI安装

编译完LLVM之后就可以编译TVM了，TVM同样需要下载源码进行编译

下载TVM

```
git clone https://gitee.com/mirrors/tvm.git
git submodule init
git submodule update
```

编译TVM

```
mkdir build
cp cmake/config.cmake build
```







### 1.3 ONNX编译安装
本来ONNX直接用pip或者conda安装应该是很方便的，但是ONNX1.4.0老是安装失败；ONNX1.5.0生成的onnx模型无法通过onnx.checker.check_model的检验（可能是Resize算子造成的）；最后，直接使用pip安装的onnx1.6.0在tvm中加载会出现segmentationfault，而从源码安装的ONNX1.6.0就不会。

```sh
git clone https://github.com/onnx/onnx.git
sudo apt-get install protobuf-compiler libprotoc-dev
cd ONNX
python setup.py install
```




## TVM优化

通过修改early_stopping可以控制搜索次数(调优过程其实有点看运气)





TODO:
https://tvm.apache.org/docs/tutorials/autotvm/tune_relay_mobile_gpu.html


