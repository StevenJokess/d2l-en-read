

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 00:06:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-12 00:11:52
 * @Description:
 * @TODO::
 * @Reference:
-->



https://zhuanlan.zhihu.com/p/104649426#Lecture%2012:%20Model%20Serving

## Lecture 1: Introduction to Deep Learning


关注系统层面内容，比如加快训练等（System aspect of deep learning: faster training, efficient serving, lower memory consumption）
（别人博客里的一句话）ML System是模型与硬件之间的桥梁

## Lecture 3: Overview of Deep Learning System

System Components
Computation Graph Optimization：如去除无用节点、内存计划与优化
Parallel Scheduling：在多个设备、线程中同时运行代码，Detect and schedule parallelizable patterns等
Architecture：应该指的是与硬件相关的内容。
不同设备、不同厂商有不同的库。
现在的一种解决方案是Compiler based Approach，即通过 High level operator description 加上 Tensor Compiler Stack 来实现，这就是TVM。

## Lecture 12: Model Serving

模型服务的主要三个限制
时间限制（Latency constraint）：batch size较小，在部分设备上只能运行较小模型
资源限制（Resource constraint）：设备的电源电量、内存都有限，使用云时资金有限制
精度限制（Accuracy constraint）：Multi-level QoS（没看懂这是啥）
运行时环境概要
大概意思就是在获取数据的时候先处理了一波，然后传输到云端进行进一步处理。

进一步优化预算就需要模型压缩以及构建部署系统（Serving System）
模型压缩（Model compression）
张量分解（Tensor decomposition）：几个更小的矩阵代替大矩阵。在分解后一般还需要finetune。
网络剪枝（Network pruning）：简化网络结构，降低计算量。
模型量化（Quantization）：时候不同的数据类型。
使用小模型（Smaller model）
部署系统（Serving System）
目标：方便部署新的应用、GPU高利用率、Satisfy latency SLA（SLA是啥？服务质量协议？不太懂这个是啥意思，猜测是时间延时符合要求）
挑战：为不同的深度学习框架提供相同的高层抽象、如何提高效率
举了个例子 Nexus，没细看，就过了一边资料，了解了下相关内容。

