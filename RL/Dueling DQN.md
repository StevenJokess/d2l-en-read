

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-25 00:28:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 00:29:33
 * @Description:
 * @TODO::
 * @Reference:
-->

## Dueling DQN[1]

用一句话来概括 Dueling DQN 就是. 它将每个动作的 Q 拆分成了 state 的 Value 加上 每个动作的 Advantage.

原来 DQN 神经网络直接输出的是每种动作的 Q值, 而 Dueling DQN 每个动作的 Q值 是有下面的公式确定的.

Q(s, a ; \theta, \alpha, \beta)=V(s ; \theta, \beta)+A(s, a ; \theta, \alpha)

这是开车的游戏, 左边是 state value, 发红的部分证明了 state value 和前面的路线有关, 右边是 advantage, 发红的部分说明了 advantage 很在乎旁边要靠近的车子, 这时的动作会受更多 advantage 的影响. 发红的地方左右了自己车子的移动原则.

## 算法[3]

本算法仅仅改变了Q网络的结构，算法仍然使用DQN算法。 值得注意的是在网络的状态价值与优势值求和时，对于一个Q值，状态价值和优势值可以任意调整。为了解决这种不确定性，作者提出了两种方式来限制优势值的范围。

强制最大的Advantage等于零，即让Advantage层的输出减去其最大值
强制Advantage的均值等于零，即让Advantage层的输出减去其均值
由于均值相对于最大值更加稳定，作者最终选用了后一种方式。


[1]:
