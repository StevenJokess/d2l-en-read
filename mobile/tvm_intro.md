

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 00:28:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-12 00:39:43
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/50529704
-->

# 手把手带你遨游TVM

## Why we need TVM?

目前对于Training来说，比较流行的是TensorFlow，PyTorch等，市场主流框架基本上已经确定下来了。而对于Inference来说，以我之所见，其实是“群雄逐鹿”，因为模型Training一次，但是会跑到的设备可能会是多种多样的，如Intel CPU / Intel GPU / ARM CPU / ARM GPU / NV GPU / FPGA / AI芯片等

### 硬件设备厂商的框架并不具备通用性

各种硬件设备的特性千差万别，要如何保持一个统一的高效执行，是一个非常难做到的事情。而各大硬件厂商针对这样的情况都推出了自己的Inference 框架（相比TensorFlow等这样的框架孱弱的Inference性能，各大设备厂商的Inference框架性能都比较不错），比如Intel的OpenVINO，ARM的ARM NN，NV的TensorRT

这里面有一个问题，
各大设备厂商的框架并不具备通用性，比如对训练框架模型产生的算子支持不全（尤其是像TensorFlow这种算子很多的），通常在一个设备厂商的Inference框架能跑，但是不一定在另外一个设备厂商的Inference框架上能跑。同时，对于业务开发来说也是非常痛苦的事情，我在这个硬件上要用这个，我在另外一个硬件上要用另外一个，而且两者还没有统一的使用体验，算子支持也不一样，性能还不一定是最好的...其实对于业务方来说，也是想要一个统一的Inference框架，然后我业务场景的各种硬件设备都能高效的跑，使用体验都是一致的，我只要换一个device_target参数就好了。

## 类比编译器

编译器后面解决了这个问题，其具体解决办法是这样的：抽象出编译器前端，编译器中端，编译器后端等概念，引入IR (Intermediate Representation)

编译器前端：接收C / C++ / Fortran等不同语言，进行代码生成，吐出IR


编译器中端：接收IR，进行不同编译器后端可以共享的优化，如常量替换，死代码消除，循环优化等，吐出优化后的IR
编译器后端：接收优化后的IR，进行不同硬件的平台相关优化与硬件指令生成，吐出目标文件



