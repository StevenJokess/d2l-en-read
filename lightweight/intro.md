

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-30 20:19:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 20:27:08
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/45496826
-->

# 导言

深度神经网络模型被广泛应用在图像分类、物体检测等机器视觉任务中，并取得了巨大成功。然而，由于存储空间和功耗的限制，神经网络模型在嵌入式设备上的存储与计算仍然是一个巨大的挑战。

目前工业级和学术界设计轻量化神经网络模型主要有4个方向：

1. 人工设计轻量化神经网络模型；
1. 基于神经网络架构搜索（Neural Architecture Search,NAS）的自动化设计神经网络；
1. CNN模型压缩；
1. 基于AutoML的自动模型压缩。

## 基本卷积运算

手工设计轻量化模型主要思想在于设计更高效的“网络计算方式”（主要针对卷积方式），从而使网络参数减少，并且不损失网络性能。本节概述了CNN模型（如MobileNet及其变体）中使用的基本卷积运算单元，并基于空间维度和通道维度，解释计算效率的复杂度。

HxW表示输入特征图空间尺寸（如图1所示，H和W代表特征图的宽度和高度，输入和输出特征图尺寸不变），N是输入特征通道数，KxK表示卷积核尺寸，M表示输出卷积通道数，则标准卷积计算量是HWNK²M。

如图3所示标准卷积在空间维度和通道维度直观说明（以下示意图省略“spatial“，”channel“，”Input“，”Output“），输入特征图和输出特征图之间连接线表示输入和输出之间的依赖关系。以conv3x3为例子，输入和输出空间“spatial”维度密集连接表示局部连接；而通道维度是全连接，卷积运算都是每个通道卷积操作之后的求和(图2)，和每个通道特征都有关，所以“channel”是互相连接的关系。




1.2 Grouped Convolution

分组卷积是标准卷积的变体，其中输入特征通道被为G组(图4)，并且对于每个分组的信道独立地执行卷积，则分组卷积计算量是HWNK²M/G，为标准卷积计算量的1/G。



Depthwise convolution[7]最早是由Google提出，是指将NxHxWxC输入特征图分为group=C组(既Depthwise 是Grouped Convlution的特殊简化形式)，然后每一组做k*k卷积，计算量为HWK²M（是普通卷积计算量的1/N，通过忽略通道维度的卷积显著降低计算量）。Depthwise相当于单独收集每个Channel的空间特征。

AutoML自动模型压缩
CNN模型替代了传统人工设计（hand-crafted）特征和分类器，不仅提供了一种端到端的处理方法，不断逼近计算机视觉任务的精度极限的同时，其深度和尺寸也在成倍增长。工业界不仅在设计轻量化模型（MobileNet V1&V2，ShuffleNet V1&V2系列），也在不断实践如何进一步压缩模型，在便携式终端设备实现准确率、计算速率、设备功耗、内存占用的小型化。

CNN模型压缩是在计算资源有限、能耗预算紧张的移动设备上有效部署神经网络模型的关键技术。本文简介概述CNN模型压缩主流算法，重点介绍如何实现基于AutoML的模型压缩算法。

4.1 CNN模型压缩概述

CNN模型压缩是从压缩模型参数的角度降低模型的计算量。

在第2节介绍的人工设计轻量型神经网络结构，多是依赖Grouped Convlution、Depthwise、Pointwise、Channel Shuffle这些基本单元组成的Block，但是这些设计方法存在偶然性，不是搜索空间的最优解。

韩松提出的Deep compression[5]获得 ICLR2016年的best paper，也是CNN模型压缩领域经典之作。论文提出三种方法：剪枝、权值共享和权值量化、哈夫曼编码。剪枝就是去掉一些不必要的网络权值，只保留对网络重要的权值参数；权值共享就是多个神经元见的连接采用同一个权值，权值量化就是用更少的比特数来表示一个权值。对权值进行哈夫曼编码能进一步的减少冗余。 作者在经典的机器学习算法，AlexNet和VGG-16上运用上面这些模型压缩的方法，在没有精度损失的情况下，把AlexNet模型参数压缩了35倍，把VGG模型参数压缩了49倍，并且在网络速度和网络能耗方面也取得了很好的提升。

CNN模型压缩沿着Deep compression的思路，压缩算法可分为四类：参数修剪和共享、低秩分解、迁移/压缩卷积滤波器和知识蒸馏等。基于参数修剪（parameter pruning）和共享的方法关注于探索模型参数中冗余的部分，并尝试去除冗余和不重要的参数。基于低秩分解（Low-rank factorization）技术的方法使用矩阵/张量分解以估计深层 CNN 中最具信息量的参数。基于迁移/压缩卷积滤波器（transferred/compact convolutional filters）的方法设计了特殊结构的卷积滤波器以减少存储和计算的复杂度。而知识精炼（knowledge distillation）则学习了一个精炼模型，即训练一个更加紧凑的神经网络以再现大型网络的输出结果。

4.2 AMC

传统的模型压缩技术依赖手工设计的启发式和基于规则的策略，需要算法设计者探索较大的设计空间，在模型大小、速度和准确率之间作出权衡，而这通常是次优且耗时的。西安交通大学与Google提出了适用于模型压缩的AMC[8]（AutoML for Model Compres- sion，AMC），利用强化学习提供模型压缩策略。
这种基于学习的压缩策略性能优于传统的基于规则的压缩策略，具有更高的压缩比，在更好地保持准确性的同时节省了人力成本。

1、Problem Definition

模型压缩在维度上可分为Fine-grained pruning和Coarse-grained/structured pruning。Fine-grained pruning主要实现剪枝权重的非重要张量，实现非常高的压缩率同时保持准确率。Coarse-grained pruning旨在剪枝权重张量的整个规则区域（例如，通道，行，列，块等），例如在MobileNet V1&V2均存在宽度因子α对通道特征进行瘦身，但是宽度因子α对每一层的通道特征都固定比率压缩。

假设权重张量是n x c x k x k，c,n分别是输入输出通道数，k是卷积核尺寸。对于fine-grained pruning，稀疏度定义为零元素的数量除以总元素的数量既zeros/(n x c x k x h)，而channel pruning，权重张量缩小为n x c’ x k x k，既稀疏度为c’/c。

但是压缩模型的精度对每层的稀疏性非常敏感，需要细粒度的动作空间。因此，论文在一个离散的空间上搜索，而是通过 DDPG agent 提出连续压缩比控制策略（图 20），通过反复试验来学习：在精度损失时惩罚，在模型缩小和加速时鼓励。actor-critic 的结构也有助于减少差异，促进更稳定的训练。

