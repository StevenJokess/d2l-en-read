

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 23:24:08
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 19:47:46
 * @Description:
 * @TODO::
 * @Reference:
-->

# DDQN (Double-Deep Q-Network)

而双重Q学习却可以消除最大化偏差。基于查找表的双重Q学习引入了两个动作价值的估计q(0)和q(1)，每次更新动作价值时用其中的一个网络确定动作，用确定的动作和另外一个网络来估计回报。

![Ari](img/DDQN.png)

Deepmind于2015年发表论文《Deep reinforcement learning with double Q-learning》，将双重Q学习用于深度Q网络，得到了双重深度Q网络（DoubleDeep Q Network，Double DQN）

考虑到深度Q网络已经有了评估网络和目标网络两个网络，所以双重深度Q学习在估计回报时只需要用评估网络确定动作，用目标网络确定回报的估计即可。

将算法DQN的[2]

$U_{i} \leftarrow R_{i}+\gamma \max _{a} q\left(S_{i}^{\prime}, a ; \mathbf{w}_{\text {目标 }}\right)$

换为

$U_{i} \leftarrow R_{i}+\gamma q\left(S_{i}^{\prime}, \arg \max _{a} q\left(S_{i}^{\prime}, a ; \mathbf{w}\right) ; \mathbf{w}_{\text {目标 }}\right)$

## 算法[3]

本算法仅仅改变了Q网络的结构，算法仍然使用DQN算法。 值得注意的是在网络的状态价值与优势值求和时，对于一个Q值，状态价值和优势值可以任意调整。为了解决这种不确定性，作者提出了两种方式来限制优势值的范围。

强制最大的Advantage等于零，即让Advantage层的输出减去其最大值
强制Advantage的均值等于零，即让Advantage层的输出减去其均值
由于均值相对于最大值更加稳定，作者最终选用了后一种方式。


[1]: https://github.com/zackchase/mxnet-the-straight-dope/blob/master/chapter17_deep-reinforcement-learning/DQN.ipynb
[2]: https://weread.qq.com/web/reader/da832f507192b327da81965kd6432e00228d645920e3401
[3]: https://lanpartis.github.io/reinforcement%20learning/2020/08/21/Dueling-DQN.html
