

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 17:09:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:20:39
 * @Description:
 * @TODO::
 * @Reference:https://stanford.edu/~shervine/l/zh/teaching/cs-229/cheatsheet-unsupervised-learning
 * https://kangcai.github.io/2019/02/11/ml-supervised-2-nb/
 * [3]: https://www.zhihu.com/org/bei-jing-zhang-liang-wu-xian-ke-ji-you-xian-gong-si/posts?page=8
-->

# 主成分分析PCA

## 为什么要有 PCA[3]

如果数据之中的某些维度之间存在较强的线性相关关系，那么样本在这 两个维度上提供的信息有就会一定的重复，所以我们希望数据各个维度之间是不相关的 (也就是正交的)。此外，出于降低处理数据的计算量或去除噪 声等目的，我们也希望能够将数据集中一些不那么重要 (方差小) 的维度剔除掉。

这是一种维度降低的技巧，找到投影数据到能够最大化方差的方向。

特征值，特征向量给定矩阵 A\in\mathbb{R}^{n\times n}A∈R
n×n
 ，\lambdaλ 被称为 AA 的一个特征值当存在一个称为特征向量的向量 z\in\mathbb{R}^n\backslash\{0\}z∈R
n
 \{0}，使得：

这个过程最大化所有 k 维空间的方差

## PCA

相比于LDA，PCA还更常用一些，PCA优势在于它采用无监督（unsupervised）方式，不要求样本带类别信息，PCA的无监督优势很吸引人，因为自然界中任何信息都属于无类别信息，只有被人定义了类别的信息才是带类别信息，所以带类别信息相对于全体信息来说是十分稀有的。由于任何多维特征都可以使用PCA处理，所以PCA更像是一个通用的预处理方法；PCA的主要作用是挖掘主成分和降维；PCA的本质思想是使主成分或者说降维后的特征每个维度之间方差最大，熵，其物理意义是体系混乱程度的度量，所以也可以说PCA是使熵尽可能大。以下是PCA的推导过程

1. 去除均值
1. 计算协方差矩阵
1. 计算协方差矩阵的特征值和特征向量
1. 将特征值排序
1. 保留前N大的特征值对应的特征向量作为新空间的基向量
1. 将数据转换到上面得到的N个特征向量构建的新空间中（实现了特征压缩）

## 应用

PCA 在自然语言处理方面也有比较多的应用，其中之一就是用来计算 词向量。word2vec 是 Google 在 2013 年提出了一个自然语言处理工具包，

## PCA 的缺陷

虽然 PCA 是一种强大的数据分析工具，但是它也存在一定的缺陷。一 方面，PCA 只能对数据进行线性变换，这对于一些线性不可分的数据是不利 的。为了解决 PCA 只能进行线性变换的问题，Schölkopf, Bernhard 在 1998 年提出了 Kernel PCA。Kernel PCA 在计算 M = [公式] 的时候不是直接进行相乘，而是使 [公式] =Φ(xi)TΦ(xj)=K(xi,xj)}。这里的K(xi,xj)是一个与支持向量机中类似的核函数。这样就能够对数据进行非线性变换。另一方面，PCA 的结果容易受到每一维数据的大小的影响，如果我们对每一维数据乘以一个不同的权重因子之后再进行 PCA降维，得到的结果可能与直接进行PCA降维得到的结果相差比较大。对于这个问题，Leznik 等人在论文Estimating Invariant Principal Components Using Diagonal Regression 中给出了一种解决方案。除此之外，PCA 要求数每一维的均值都是0，在将原始数据的每一维的均值都变成0时可能会丢失掉一些信息。虽然PCA有这些缺陷，但是如果合理的利用，PCA 仍然不失为一种优秀的数据分析 和降维的手段。
