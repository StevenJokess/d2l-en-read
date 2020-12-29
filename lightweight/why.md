

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 19:13:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 19:21:49
 * @Description:
 * @TODO::
 * @Reference:http://www.tensorinfinity.com/paper_185.html
-->
为什么MobileNet会这么快？
在写这篇文章的时候看到了一篇文章Why MobileNet and Its Variants (e.g. ShuffleNet) Are Fast？，这也让我有了一样的一个问题，这篇文章主要是从结构方面进行了讨论，从深度可分离卷积到组卷积的参数计算量等，因为之前的文章都有写过，在这里就不赘述了，感兴趣的同学可以翻阅下之前的文章。

在这里换一个的角度。我们直接从用时多少的角度去讨论下这个问题。
下图来自Caffe作者贾扬清的博士论文：



该图是AlexNet网络中不同层的GPU和CPU的时间消耗，我们可以清晰的看到，不管是在GPU还是在CPU运行，最重要的“耗时杀手”就是conv，卷积层。也就是说，想要提高网络的运行速度，就得到提高卷积层的计算效率。

我们以MobileNetV1为主，看看MobileNet的资源分布情况：



可以看到，MobileNet的95%的计算都花费在了1×1的卷积上，那1×1卷积有什么好处吗？

我们都知道，卷积操作就是如下图所示的乘加运算：



在计算机操作时，需要将其存入内存当中再操作（按照“行先序”）：



这样一来，特征图y11,y12,y21,y22的计算如下所示：



按照卷积计算，实线标注出卷积计算中的访存过程（对应数据相乘），我们可以看到这一过程是非常散乱和混乱的。直接用卷积的计算方式是比较愚蠢的。

这时候就要用到im2col操作。

im2col
一句话来介绍im2col操作的话，就是通过牺牲空间的手段（约扩增K×K倍），将特征图转换成庞大的矩阵来进行卷积计算。



其实思路非常简单：

把每一次循环所需要的数据都排列成列向量，然后逐一堆叠起来形成矩阵（按通道顺序在列方向上拼接矩阵）。

比如Ci×Wi×Hi大小的输入特征图，K×K大小的卷积核，输出大小为Co×Wo×Ho，

输入特征图将按需求被转换成(K∗K)×(Ci∗Wo∗Ho)的矩阵，卷积核将被转换成Co×(K∗K)的矩阵，



然后调用GEMM（矩阵乘矩阵）库加速两矩阵相乘也就完成了卷积计算。由于按照计算需求排布了数据顺序，每次计算过程中总是能够依次访问特征图数据，极大地提高了计算卷积的速度。（不光有GEMM，还有FFt（快速傅氏变换））



换一种表示方法能更好地理解，图片来自High Performance Convolutional Neural Networks for Document Processing：



这样可以更清楚的看到卷积的定义进行卷积操作（上图上半部分），内存访问会非常不规律，以至于性能会非常糟糕。而Im2col()以一种内存访问规则的方式排列数据，虽然Im2col操作增加了很多数据冗余，但使用Gemm的性能优势超过了这个数据冗余的劣势。

所以标准卷积运算大概就是这样的一个过程：



那我们现在回到1×1的卷积上来，有点特殊。按照我们之前所说的，1×1的卷积的原始储存结构和进行im2col的结构如下图所示：



可以看到矩阵是完全相同的。标准卷积运算和1×1卷积运算对比如下图：



也就是说，1x1卷积不需要im2col的过程，所以底层可以有更快的实现，拿起来就能直接算，大大节省了数据重排列的时间和空间。

当然，这些也不是那么绝对的，因为毕竟MobileNet速度快不快，与CONV1x1运算的优化程度密切相关。如果使用了定制化的硬件（比如用FPGA直接实现3x3的卷积运算单元），那么im2col就失去了意义而且反而增加了开销。

回到之前的MobileNet的资源分布，95%的1×1卷积和优化的网络结构就是MobileNet能如此快的原因了。

---

im2col的原理和实现
在 Caffe 中如何计算卷积？- 贾扬清的回答 - 知乎
漫谈卷积层
High Performance Convolutional Neural Networks for Document Processing
Why MobileNet and Its Variants (e.g. ShuffleNet) Are Fast
