

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-19 15:44:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-19 15:48:09
 * @Description:
 * @TODO::
 * @Reference:https://github.com/zergtant/pytorch-handbook/tree/master/chapter4/distributeddataparallel
-->

什么是分布式训练?
在研究分布式和数据并行之前，我们需要先了解一些关于分布式训练的背景知识。

目前普遍使用的分布式训练基本上有两种不同形式:数据并行化和模型并行化。

在数据并行化中，模型训练作业是在数据上进行分割的。作业中的每个GPU接收到自己独立的数据批处理切片。每个GPU使用这些数据来独立计算梯度更新。例如，如果你要使用两个GPU和32的批处理大小，一个GPU将处理前16条记录的向前和向后传播，第二个处理后16条记录的向后和向前传播。这些梯度更新然后在gpu之间同步，一起平均，最后应用到模型。

(同步步骤在技术上是可选的，但理论上更快的异步更新策略仍是一个活跃的研究领域)

在模型并行化中，模型训练作业是在模型上进行分割的。工作中的每个GPU接收模型的一个切片，例如它的层的一个子集。例如，一个GPU负责它的输出头，另一个负责输入层，另一个负责中间的隐藏层。

虽然这两种技术各有优缺点，但数据并行化在这两种技术中更容易实现(它不需要了解底层网络架构)，因此通常首先尝试这种策略。

(也可以结合使用这些技术，例如同时使用模型和数据并行化，但这是一个高级主题，我们不在这里介绍)

因为这篇文章是对DistributedDataParallel并行API的介绍，所以我们不会再进一步讨论模型并行化的细节——但请关注以后关于这个主题的文章!😉

---


为了对分布式模型训练性能进行基准测试，我在PASCAL VOC 2012数据集（来自torchvision数据集）上训练了20个轮次的DeepLabV3-ResNet 101模型（通过Torch Hub）。 我启动了五个不同版本的模型巡训练工作：一次在单个V100上（在AWS上为p3.2xlarge），一次在V100x4（p3.8xlarge）和V100x8（p3.16xlarge）上使用 DistributedDataParallel和DataParallel。 该基准测试不包括运行开始时花在下载数据上的时间-仅模型训练和节省时间计数。



在后台，DataParallel使用多线程而不是多处理来管理其GPU工作器。 这极大地简化了实现：由于工作进程是同一进程的所有不同线程，因此它们都可以访问相同的共享状态，而无需任何其他同步步骤。

由于存在全局解释器锁，在Python中将多线程用于计算作业的效果很差。 如下一节中的基准测试所示，使用DataParallel并行化的模型比使用DistributedDataParallel并行化的模型要慢得多。


