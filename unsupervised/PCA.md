

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 17:09:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 20:12:53
 * @Description:
 * @TODO::
 * @Reference:https://stanford.edu/~shervine/l/zh/teaching/cs-229/cheatsheet-unsupervised-learning
 * https://kangcai.github.io/2019/02/11/ml-supervised-2-nb/
-->

# 主成分分析PCA

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
