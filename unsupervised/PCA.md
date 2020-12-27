

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 17:09:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 17:10:46
 * @Description:
 * @TODO::
 * @Reference:https://stanford.edu/~shervine/l/zh/teaching/cs-229/cheatsheet-unsupervised-learning
-->

# 主成分分析

这是一种维度降低的技巧，找到投影数据到能够最大化方差的方向。

特征值，特征向量给定矩阵 A\in\mathbb{R}^{n\times n}A∈R
n×n
 ，\lambdaλ 被称为 AA 的一个特征值当存在一个称为特征向量的向量 z\in\mathbb{R}^n\backslash\{0\}z∈R
n
 \{0}，使得：

这个过程最大化所有 k 维空间的方差
