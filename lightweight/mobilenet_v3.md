

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 22:27:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 20:43:21
 * @Description:
 * @TODO::
 * @Reference:
-->

# Searching for MobileNetV3

论文地址：https://arxiv.org/pdf/1905.02244.pdf

MobileNetV3，是谷歌在2019年3月21日提出的网络架构。首先，引入眼帘的是这篇文章的标题，“searching”一词就把V3的论文的核心观点展示了出来——用神经结构搜索（NAS）来完成V3。虽然本人没有接触过NAS，但是我已经闻到了金钱的味道。

## MobileNetV3的相关技术

0.网络的架构基于NAS实现的MnasNet（效果比MobileNetV2好）

1.引入MobileNetV1的深度可分离卷积
2.引入MobileNetV2的具有线性瓶颈的倒残差结构
3.引入基于squeeze and excitation结构的轻量级注意力模型(SE)
4.使用了一种新的激活函数h-swish(x)
5.网络结构搜索中，结合两种技术：资源受限的NAS（platform-aware NAS）与NetAdapt
6.修改了MobileNetV2网络端部最后阶段

第0点，关于MnasNet也是基于NAS的，也不是很了解。大家感兴趣的话，可以参考曲晓峰老师的这个回答如何评价 Google 最新的模型 MnasNet？- 曲晓峰的回答 - 知乎，写的很棒！所以我们只要认为MnasNet是一个比MobileNet精度和实时性更高的模型就行了。

第1,2点在前面的MobileNetV1和V2上有讨论，在这里就不赘述了。

第3点引入SE模块，主要为了利用结合特征通道的关系来加强网络的学习能力。先不仔细讨论，之后在【深度回顾经典网络】系列的时候再详细讨论吧，感兴趣的同学，可以看看这一篇文章。

## 网络结构搜索NAS

由于不熟，就简单写一点吧。

主要结合两种技术：资源受限的NAS（platform-aware NAS）与NetAdapt。

资源受限的NAS，用于在计算和参数量受限的前提下搜索网络来优化各个块（block），所以称之为模块级搜索（Block-wise Search） 。

NetAdapt，用于对各个模块确定之后网络层的微调每一层的卷积核数量，所以称之为层级搜索（Layer-wise Search）。

一旦通过体系结构搜索找到模型，我们就会发现最后一些层以及一些早期层计算代价比较高昂。于是作者决定对这些架构进行一些修改，以减少这些慢层(slow layers)的延迟，同时保持准确性。这些修改显然超出了当前搜索的范围。

对V2最后阶段的修改
作者认为，当前模型是基于V2模型中的倒残差结构和相应的变体（如下图）。使用1×1卷积来构建最后层，这样可以便于拓展到更高维的特征空间。这样做的好处是，在预测时，有更多更丰富的特征来满足预测，但是同时也引入了额外的计算成本与延时。



所以，需要改进的地方就是要保留高维特征的前提下减小延时。首先，还是将1×1层放在到最终平均池之后。这样的话最后一组特征现在不是7x7（下图V2结构红框），而是以1x1计算（下图V3结构黄框）。





这样的好处是，在计算和延迟方面，特征的计算几乎是免费的。最终，重新设计完的结构如下：



在不会造成精度损失的同时，减少10ms耗时，提速15%，减小了30m的MAdd操作。

V3的block
综合以上，V3的block结构如下所示：



与V2的block相比较：




MobileNetV3是Google于2019年提出的一种基于NAS的新的轻量级网络，为了进一步提升效果，将relu和sigmoid激活函数分别替换为hard_swish与hard_sigmoid激活函数，同时引入了一些专门减小网络计算量的改进策略。[1]

MobileNetV3代表了目前主流的轻量级神经网络结构。在MobileNetV3中，作者为了获得更高的精度，在global-avg-pooling后使用了1x1的卷积。该操作大幅提升了参数量但对计算量影响不大，所以如果从存储角度评价模型的优异程度，MobileNetV3优势不是很大，但由于其更小的计算量，使得其有更快的推理速度。


此外，我们模型库中的ssld蒸馏模型表现优异，从各个考量角度下，都刷新了当前轻量级模型的精度。由于MobileNetV3模型结构复杂，分支较多，对GPU并不友好，GPU预测速度不如MobileNetV1[2]

就像之前所说的：只有在更深层次使用h-swish才能得到比较大的好处。所以在上面的网络模型中，不论大小，作者只在模型的后半部分使用h-swish。

用谷歌pixel 1/2/3来对大小V3进行测试的结果。

MobileNetV3定义了两个模型: MobileNetV3-Large和MobileNetV3-Small。V3-Large是针对高资源情况下的使用，相应的，V3-small就是针对低资源情况下的使用。两者都是基于之前的简单讨论的NAS。

有一点值得说一下，训练V3用的是4x4 TPU Pod，batch size 409…(留下了贫穷的泪水)

网络的架构基于NAS实现的MnasNet，神经结构搜索（NAS）[5]
引入MobileNetV1的深度可分离卷积
引入MobileNetV2的具有线性瓶颈的倒残差结构
引入基于squeeze and excitation结构的轻量级注意力模型(SE)
使用了一种新的激活函数h-swish(x)


[1]: https://github.com/d-li14/mobilenetv3.pytorch
[2]: https://paddleclas.readthedocs.io/zh_CN/latest/models/Mobile.html
[3]: https://github.com/pytorch/vision/pull/3182/files
[4]: http://www.tensorinfinity.com/paper_185.html
[5]: https://cygao.xyz/2019/07/12/lightweight/
[6]: https://github.com/xiaolai-sqlai/mobilenetv3/blob/master/mobilenetv3.py
