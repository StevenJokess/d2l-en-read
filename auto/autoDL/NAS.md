

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-09 14:33:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 15:51:07
 * @Description:
 * @TODO::
 * @Reference:https://machine-learning-from-scratch.readthedocs.io/zh_CN/latest/%E6%A8%A1%E5%9E%8B%E8%AF%84%E4%BC%B0%E4%B8%8E%E6%A8%A1%E5%9E%8B%E8%B0%83%E4%BC%98.html#header-n4
-->



# 超参数调节/超参数优化

机器学习算法中，有两类参数：从训练数据学习得到的参数（例如，线性回归模型中每一项自变量的权重 ），和在开始学习过程之前设置好的参数，即超参数（例如神经网络训练时的学习率/隐藏层层数，或者决策树的最大深度）。超参数往往定义了关于模型的更高层次的概念，例如模型复杂程度或学习能力。

大多数学习算法都有些超参数需要设定。超参数配置不同，学得的模型性能往往有显著差别，这就是参数调节(parameter tuning)：对每种超参数配置下都训练出一个模型，然后把对应最好模型的超参数作为最优结果。

由于很多超参数是在实数范围内取值，因此现实中常用做法是对每个超参数选定一个范围和变化步长。如在[0,1)范围内以 0.2为步长。这样选出的超参数可能不是最佳的，但是这是在计算开销和性能之间取折中的结果。

当模型选择完成后，学习算法和超参数配置已经选定，此时应该用所有训练数据重新训练模型，这才是最终提交的模型。

8.1 搜索策略

超参数搜索有三种常见的策略：
手动搜索：手动选择超参数。
网格搜索：当超参数的数据相对较少时，这个方法很实用。
随机搜索：通常推荐这种方式。
8.1.1 手动搜索
手动选择超参数需要十分清楚超参数的作用，它们是如何影响模型表现的，以及如何调整能达到预期的效果。这需要建模人员对模型和数据有非常大的把控能力。

8.1.2 网格搜索
最传统的超参数优化方法就是网格搜索（Grid search），即对一个指定范围内的超参数集合进行搜索。网格搜索的做法是：

对于每个超参数，选择一个较小的有限值集合去搜索。
然后这些超参数笛卡尔乘积得到多组超参数。
网格搜索使用每一组超参数训练模型，挑选验证集误差最小的超参数作为最好的超参数。
如何确定搜索集合的范围？

如果超参数是数值，则搜索集合的最小、最大元素可以基于先前相似实验的经验保守地挑选出来。
如果超参数是离散的，则直接使用离散值。
通常会根据实验的结果反复尝试并调整超参数的选择范围。假设在集合 {-1,0,1}上网格搜索超参数a ：

如果找到的最佳值是 1，那么说明可能低估了 a 的取值范围。此时重新在 {1,2,3} 上搜索。
如果找到的最佳值是 0，那么可以细化搜索范围以改进估计。此时重新在 {-0.1,0,0.1} 上搜索。
网格搜索的一个缺点是计算代价随着超参数数量呈指数级增长。如果有 m 个超参数，每个最多取 n 个值，那么所需的试验数将是 n的m次方 。



8.1.3 随机搜索
随机搜索是一种可以替代网格搜索的方法，它编程简单、使用方便、能更快收敛到超参数的良好取值。

首先为每个超参数定义一个边缘分布，如伯努利分布（对应着二元超参数）或者对数尺度上的均匀分布（对应着正实值超参数）。
然后假设超参数之间相互独立，从各分布中抽样出一组超参数。
使用这组超参数训练模型。
经过多次抽样 -> 训练过程，挑选验证集误差最小的超参数作为最好的超参数。
随机搜索的优点：

不需要离散化超参数的值，也不需要限定超参数的取值范围。这允许我们在一个更大的集合上进行搜索。
当某些超参数对于性能没有显著影响时，随机搜索相比于网格搜索指数级地高效，它能更快的减小验证集误差。
与网格搜索一样，通常会基于前一次运行结果来重复运行下一个版本的随机搜索。

随机搜索比网格搜索更快的找到良好超参数的原因是：没有浪费的实验。

在网格搜索中，两次实验之间只会改变一个超参数的值，而其他超参数的值保持不变。

如果这个超参数的值对于验证集误差没有明显区别，那么网格搜索相当于进行了两个重复的实验。

在随机搜索中，两次实验之间，所有的超参数值都不会相等，因为每个超参数的值都是从它们的分布函数中随机采样而来。因此不大可能会出现两个重复的实验。

如果该超参数与泛化误差无关，那么：

在网格搜索中，不同该超参数的值、相同的其他超参数值，会导致大量的重复实验。
在随机搜索中，其他超参数值每次也都不同，因此不大可能出现两个重复的实验（除非所有的超参数都与泛化误差无关）。
8.2 调整原则
通常先对超参数进行粗调，然后在粗调中表现良好的超参数区域进行精调。

超参数随机搜索，并不意味着是在有效范围内随机均匀取值。需要选择合适的缩放来进行随机选取。

对于学习率，假设其取值范围为0.000001~1。

如果进行均匀取值，取10个，那么有 90% 的随机值都位于区间[0.1,1]。则[0.000001,0.1] 之间没有足够的探索。这种做法明显不合理。

此时需要使用对数缩放，在对数轴上均匀随机取点。

对于指数加权移动平均的超参数 1/(1-b) 。假设其取值范围为0.9~0.9999。

由于 1/(1-b) 刻画了结果使用过去多少个周期的数据来加权平均。因此如果进行均匀取值，则：

在0.9~0.9005 之间取值时，1/(1-b) 变化不大。
在0.9990~0.9995 之间取值时，1/(1-b) 变化非常大。
b 越接近 1，1/(1-b) 对于它的变化越敏感。此时，需要对 (1-b) 使用对数缩放，在对数轴上均匀随机取点。

如果选择了错误的缩放，如果取值的总量足够大，也可以得到不错的结果。尤其当配合了粗调 -> 精调 策略时，最终还是会聚焦到合适的超参数范围上。

通常情况下，建议至少每隔几个月重新评估或者修改超参数。因为随着时间的变化，真实场景的数据会逐渐发生改变。由于这些变化，原来设定的超参数可能不再适用。

---

神经架构搜索（Neural Architecture Search，NAS）[Zoph et al.,2017]是一个新的比较有前景的研究方向，通过神经网络来自动实现网络架构的设计．一个神经网络的架构可以用一个变长的字符串来描述．利用元学习的思想，神经架构搜索利用一个控制器来生成另一个子网络的架构描述．控制器可以由一个循环神经网络来实现．控制器的训练可以通过强化学习来完成，其奖励信号为生成的子网络在开发集上的准确率．

NAS分为单目标算法与多目标算法。前者的目标是设计出一个神经网络，使得精度等单个指标最大化。后者则要考虑多个指标，如精度与速度，保证设计出来的网络既有很高的准确率，又有很快速度，是多目标优化问题。NAS的综述可阅读之前的文章“神经结构搜索（NAS）综述”。[2]

[2]: https://www.tensorinfinity.com/paper_158.html