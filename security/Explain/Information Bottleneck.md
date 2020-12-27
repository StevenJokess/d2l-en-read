

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 14:53:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 14:54:47
 * @Description:
 * @TODO::
 * @Reference:https://mp.weixin.qq.com/s/cesmzbpzX8vVqsAmYFKrMg
-->

耶路撒冷希伯来大学的计算机与神经科学家 Naftali Tishby 提出了一项名为「信息瓶颈」（Information Bottleneck）的新理论


这一想法是指神经网络就像把信息挤进瓶颈一样，只留下与一般概念最为相关的特征，去掉大量无关的噪音数据。

由 Tishby 及其学生 Ravid Shwartz-Ziv 联合进行的引人注目的实验揭示了发生在深度学习之中的挤压过程，

在 2015 年，他和他的学生提出假设，（https://arxiv.org/abs/1503.02406）深度学习是一个信息瓶颈程序，尽可能的压缩数据噪声，保留数据想表达的信息。Tishby 和 Shwartz-Ziv 的新的深度神经网络实验揭示了瓶颈程序是如何工作的。在一个案例中，研究员训练小型网络使其将数据标记为 1 或 0（比如「狗」或「非狗」），网络一共有 282 个神经连接并随机初始化连接强度，然后他们使用 3000 个样本的输入数据集追踪网络究竟在做什么。
