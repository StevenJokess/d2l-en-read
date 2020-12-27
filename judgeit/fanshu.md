

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 19:05:47
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 19:07:37
 * @Description:
 * @TODO::
 * @Reference:
-->
范数	表达式	参数先验知识	作用
L1		拉普拉斯分布	1）产生稀疏模型，可以用于特征选择
2）一定程度上可以防止过拟合（overfitting）
L2		高斯分布	主要作用是防止模型过拟合

$\left\|\theta_{f}\right\|_{1}=\sum_{i=0}^{M}\left|\theta_{i}\right|$

$\left\|\theta_{f}\right\|_{2}=\sum_{i=0}^{M} \theta_{i}^{2}$
