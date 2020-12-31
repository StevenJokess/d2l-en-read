

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-11 21:47:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-31 20:18:44
 * @Description:
 * @TODO::
 * @Reference:
-->

# 模型压缩及移动端部署[2]

在取得巨大成功的同时，这些深度神经网络需要巨大的计算开销和内存开销，严重阻碍了资源受限下的使用。本章总结了模型压缩、加速一般原理和方法，以及在移动端如何部署。

## 模型成本[18]

模型参数在一定程度上代表了模型的复杂度, 也在一定程度上决定着模型所占据的空间大小.人为设定的参数数量往往是在实验室经过重复实验调出来的, 这种局部最优的超参数并不代表网络的“真正需求”:它们既存在一定程度上的冗余, 也没有权衡成本和效果之间的关系.

模型的运算时间成本并不仅仅依赖模型的参数数量, 也依赖于模型的深度.以残差网络[10]为例, 尽管在何凯明经典论文中, 1 000多层的残差网络参数数量不到AlexNet的1/10, 但其训练以及测试耗时都明显大于AlexNet.

## 模型压缩

### 模型压缩定义

模型压缩是指利用数据集对已经训练好的深度模型进行精简，进而得到一个轻量且准确率相当的网络，压缩后的网络具有更小的结构和更少的参数，可以有效降低计算和存储开销，便于部署再受限的硬件环境中。

### Why

1. 希望用，表示复杂工作
2. 在线学习和增量学习等实时应用
3. 模型参数作用有限、表达冗余：如，如VGG-16网络，参数数量1亿3千多万，占用500MB空间，需要进行309亿次浮点运算
4. 硬件能力弱、资源受限

Goal: 最大程度的减小模型复杂度，减少模型存储需要的空间，也致力于加速模型的训练和推测

### 主流压缩法

更精细化模型设计、模型裁剪、核的稀疏化、量化、低秩分解、迁移学习等方法，而这些方法又可分为前端压缩和后端压缩。

#### 前端压缩和后端压缩对比

|  对比项目  |                    前端压缩                    |                   后端压缩                   |
| :--------: | :--------------------------------------------: | :------------------------------------------: |
|    含义    |         不会改变原始网络结构的压缩技术         |     会大程度上改变原始网络结构的压缩技术     |
|  主要方法  | 知识蒸馏、紧凑的模型结构设计、滤波器层面的剪枝 | 低秩近似、未加限制的剪枝、参数量化、二值网络 |
|  实现难度  |                     较简单                     |                     较难                     |
|  是否可逆  |                      可逆                      |                    不可逆                    |
|  成熟应用  |                      剪枝                      |              低秩近似、参数量化              |
| 待发展应用 |                    知识蒸馏                    |                   二值网络                   |

## 压缩法

包括网络剪枝、网络精馏和网络分解这3个方向的压缩方法

### 网络剪枝(network pruning)

早期指删除网络中冗余参数, 提高网络泛化能力.

参数的选择，相对比较简单。参数的绝对值越接近零，它对结果的贡献就越小。这一点和稀疏矩阵有些类似。[21]

在CNN出现之后, 网络剪枝主要指减少冗余的浮点计算(floating point operations, 简称FLOP)[17], 从而提高网络运行效率.

网络剪枝按剪枝粒度(pruning granularities)可分为4类, 如图 1所示, 从粗到细为:TODO:中间隐层(layer)剪枝、通道(feature map/channel/filter)剪枝、卷积核(kernel)剪枝、核内权重(intra kernel weight)剪枝、单个权重(weight)剪枝.其中, Feature Map/Channel都指网络中一层产生的特征图张量的一个通道.Filter是网络中的权重参数, Feature Map是网络输出, 在网络剪枝中两者等价, 因为减去一个Filter会导致少产生一个Feature Map.

![图1](http://www.jos.org.cn/html/2018/2/PIC/rjxb-29-2-251-1.jpg)

####

从剪枝目标上分类, 可分为减少参数/网络复杂度、减小过拟合/增加泛化能力/提高准确率、减小部署运行时间(test run-time)/提高网络效率以及减小训练时间等.不同的剪枝方法侧重也会有所不同, 有的剪枝方法完全依赖网络参数, 剪枝后不需要调优恢复准确率; 有的剪枝方法则只适用于全连接层剪枝.下面按照剪枝粒度的分类从细到粗加以叙述.





非结构化剪枝: 通常是连接级、细粒度的剪枝方法，精度相对较高，但依赖于特定算法库或硬件平台的支持	Deep Compression , Sparse-Winograd 算法等；

Anwar等人[19]提出了结构化剪枝的概念, 可以很方便地使用现有的硬件和BLAS等软件库进行矩阵相乘, 利用剪枝后网络的稀疏性来加速网络效率.粗粒度剪枝, 如通道粒度和卷积核粒度本身就是结构化的, Anwar的创新之处在于提出了核内定步长粒度(intra kernel strided sparsity), 将细粒度剪枝转化为结构化剪枝.


结构化剪枝	是filter级或layer级、粗粒度的剪枝方法，精度相对较低，但剪枝策略更为有效，不需要特定算法库或硬件平台的支持，能够直接在成熟深度学习框架上运行。	如局部方式的、通过layer by layer方式的、最小化输出FM重建误差的Channel Pruning , ThiNet , Discrimination-aware Channel Pruning ；全局方式的、通过训练期间对BN层Gamma系数施加L1正则约束的Network Slimming ；全局方式的、按Taylor准则对Filter作重要性排序的Neuron Pruning ；全局方式的、可动态重新更新pruned filters参数的剪枝方法 ;
https://blog.csdn.net/baidu_31437863/article/details/84474847


#### 网络分解

网络分解的目的是将矩阵二维张量的奇异值分解(singular value decomposition, 简称SVD)推广到三维卷积核, 并且减小前向传播的时间.

#### 网络精馏

网络精馏是指利用大量未标记的迁移数据(transfer data), 让小模型去拟合大模型, 从而让小模型学到与大模型相似的函数映射.网络精馏可以看成在同一个域上迁移学习[34]的一种特例, 目的是获得一个比原模型更为精简的网络, 整体的框架图如图 4所示.





大模型作为教师模型(teacher model)是预先训练好的, 小模型作为学生模型(student model), 由教师模型指导, 步骤①首先由数据生成器生成大量的迁移数据(transfer data), 分别送入教师模型和学生模型中.步骤②将教师模型的输出作为真实值, 衡量学生模型的输出与它之间的损失.步骤③通过梯度下降等方法更新学生模型的权重, 使得学生模型的输出和教师模型的输出更加接近, 从而达到利用小模型拟合大模型的效果.

#### 总体压缩效用评价指[18]

网络压缩评价指标包括运行效率、参数压缩率、准确率.与基准模型比较衡量性能提升时, 可以使用提升倍数(speedup)或提升比例(ratio), 两者可以相互转换, 本文统一使用提升比例.

目前, 大部分研究工作均会测量Top-1准确率, 只有在ImageNet这类大型数据集上才会只用Top-5准确率.为方便比较, 本文在后续的效果对比表中使用Top-1准确率.









# “好、快、省”[1]

具体要求就是软件平台“

### 高accuracy，

### 低latency，

Single stream任务，主要用latency，也有用fps（frame per second）的，latency和fps可以直接换算；

Offline任务，可以用throughput。



高energy efficiency，

低memory size，

高flexibility”。


## 编译优化技术[1]

如著名的TVM，“TVM An Automated End-to-End Optimizing Compiler for Deep Learning”。TVM提供了Computational Graphs和code generation两个层级的优化。Computational Graphs在计算执行和数据存储方面提供了Operator Fusion和Data Layout Transformation。Operator Fusion合并几个算子为融合算子，有利于减少算子调度和各算子存储访问的成本。





## 常用的轻量级网络

SequeezeNet
MobileNet
MobileNet-v2
Xception
ShuffleNet-v1
ShuffleNet-v2

### 对比

|     网络结构      | TOP1 准确率/% | 参数量/M | CPU运行时间/ms |
| :---------------: | :-----------: | :------: | :------------: |
|   MobileNet V1    |     70.6      |   4.2    |      123       |
|  ShuffleNet(1.5)  |     69.0      |   2.9    |       -        |
|  ShuffleNet(x2)   |     70.9      |   4.4    |       -        |
|   MobileNet V2    |     71.7      |   3.4    |       80       |
| MobileNet V2(1.4) |     74.7      |   6.9    |      149       |

### 未来

深度网络压缩本质目的上,即提取网络中的有用信息

1. 任务或使用场景层面的压缩：具体场景，不需要那么ImageNet 1000类复杂的识别预测
2. 压缩评价标准需要更加泛化：现在只侧重于和被压缩的大型网络在参数量和运行时间上的比较；未来一方面平衡运行速度和模型大小在不同应用场景下的影响;另一方面,可以从模型本身的结构性出发,对压缩后的模型进行评价.
3. 学生网络结构的构造：如何根据教师网络结构设计合理的网络结构在精简模型的条件下获取较高的模型性能
4.。。





### 现有移动端开源框架及其特点

pytorch[14][16],facebook
djl[15],amazon
NCNN[5],tencent
QNNPACK[6],facebook
Prestissimo[7],九言科技
MDL[8],baidu
Paddle-Mobile[9],baidu
MACE[10],xiaomi
FeatherCNN[11],tencent
TensorFlow Lite[12],google
PocketFlow[13],tencent

More[4]

#### 移动端开源框架部署

PaddleMobile[2]
NCNN[3][20]


[1]: https://blog.csdn.net/zxf_zjf/article/details/106444531
[2]: https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch17_%E6%A8%A1%E5%9E%8B%E5%8E%8B%E7%BC%A9%E3%80%81%E5%8A%A0%E9%80%9F%E5%8F%8A%E7%A7%BB%E5%8A%A8%E7%AB%AF%E9%83%A8%E7%BD%B2/%E7%AC%AC%E5%8D%81%E4%B8%83%E7%AB%A0_%E6%A8%A1%E5%9E%8B%E5%8E%8B%E7%BC%A9%E3%80%81%E5%8A%A0%E9%80%9F%E5%8F%8A%E7%A7%BB%E5%8A%A8%E7%AB%AF%E9%83%A8%E7%BD%B2.md#1783-%E5%9C%A8android%E6%89%8B%E6%9C%BA%E4%B8%8A%E4%BD%BF%E7%94%A8paddlemobile%E5%AE%9E%E7%8E%B0%E5%9B%BE%E5%83%8F%E5%88%86%E7%B1%BB
[3]: https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch17_%E6%A8%A1%E5%9E%8B%E5%8E%8B%E7%BC%A9%E3%80%81%E5%8A%A0%E9%80%9F%E5%8F%8A%E7%A7%BB%E5%8A%A8%E7%AB%AF%E9%83%A8%E7%BD%B2/17.8.1%20NCNN%E9%83%A8%E7%BD%B2.md
[4]: https://blog.csdn.net/zchang81/article/details/74280019
[5]: https://github.com/Tencent/ncnn
[6]: https://github.com/pytorch/QNNPACK%E3%80%80%E3%80%80%E3%80%80%E3%80%80
[7]: https://github.com/in66-dev/In-Prestissimo%E3%80%80%E3%80%80
[8]: https://github.com/allonli/mobile-deep-learning
[9]: https://github.com/PaddlePaddle/paddle-mobile%E3%80%80
[10]: https://github.com/XiaoMi/mace
[11]: https://github.com/Tencent/FeatherCNN
[12]: https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/lite
[13]: https://github.com/Tencent/PocketFlow
[14]: https://github.com/StevenJokess/pytorch-andriod-greatdemo
[15]: https://github.com/StevenJokess/djl-android-demo
[16]: https://github.com/StevenJokess/Pytorch-Kotlin-Demo
[17]: Oberman SF, Flynn MJ. Design issues in division and other floating-point operations. IEEE Trans. on Computers, 1997, 46(2): 154–161. [doi:10.1109/12.565590]
[18]: http://www.jos.org.cn/html/2018/2/5428.htm
[19]: Anwar S, Hwang K, Sung W. Structured pruning of deep convolutional neural networks. ACM Journal on Emerging Technologies in Computing Systems (JETC), 2017, 13(3): Article No.32. [doi:10.1145/3005348]
[20]: 安卓端深度学习模型部署-以NCNN为例 - 带萝卜的文章 - 知乎 https://zhuanlan.zhihu.com/p/137453394
