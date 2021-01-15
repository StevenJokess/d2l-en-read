

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

# Dueling DQN[1]

用一句话来概括 Dueling DQN 就是. 它将每个动作的 Q 拆分成了 state 的 Value 加上 每个动作的 Advantage.



原来 DQN 神经网络直接输出的是每种动作的 Q值, 而 Dueling DQN 每个动作的 Q值 是有下面的公式确定的.

Q(s, a ; \theta, \alpha, \beta)=V(s ; \theta, \beta)+A(s, a ; \theta, \alpha)

这是开车的游戏, 左边是 state value, 发红的部分证明了 state value 和前面的路线有关, 右边是 advantage, 发红的部分说明了 advantage 很在乎旁边要靠近的车子, 这时的动作会受更多 advantage 的影响. 发红的地方左右了自己车子的移动原则.


图中将原有的DQN算法的网络输出分成了两部分：即值函数和优势函数共同组成, 在数学上表示为：[5]
$$
Q(s, a ; \theta, \alpha, \beta)=V(s ; \theta, \beta)+A(s, a ; \theta, \alpha)
$$
其中, $\theta$ 表示网络结构, $\alpha, \beta$ 表示两个全连接层网络的参数, 由图和公式可知, $V$ 仅与状态有关, 而 $A$ 与状态和动作都有关。。 如果仅仅用当前的这个公式更新的话, 其存在一个“unidentifiable”问题（比如V和A分别加上和减去一 个值能够得到同样的Q, 但反过来显然无法由Q得到唯一的V和A) 。作者为了解决它, 作者强制优势 函数估计量在选定的动作处具有零优势。 也就是说让网络的最后一个模块实现前向映射，表示为：
$$
Q(s, a ; \theta, \alpha, \beta)=V(s ; \theta, \beta)+\left(A(s, a ; \theta, \alpha)-\max _{a^{\prime} \in|\mathcal{A}|} A\left(s, a^{\prime} ; \theta, \alpha\right)\right)
$$
怎么理解呢? 对于任意 $a$ 来说
$$
a^{*}=\arg \max _{a^{\prime} \in \mathcal{A}} Q\left(s, a^{\prime} ; \theta, \alpha, \beta\right)=\arg \max _{a^{\prime} \in \mathcal{A}} A\left(s, a^{\prime} ; \theta, \alpha\right)
$$
那么我们可以得到: $Q\left(s, a^{*} ; \theta, \alpha, \beta\right)=V(s ; \theta, \beta),$ 因此, $V(s ; \theta, \beta)$ 提供了价值函数的估计， 而另一个产生了优势函数的估计。在这里作者使用里平均 $\left(\frac{1}{|\mathcal{A}|}\right)$ 代替了最大化操作, 表示为：
$$
Q(s, a ; \theta, \alpha, \beta)=V(s ; \theta, \beta)+\left(A(s, a ; \theta, \alpha)-\frac{1}{|\mathcal{A}|} \sum_{a^{\prime}} A\left(s, a^{\prime} ; \theta, \alpha\right)\right)
$$
采用这种方法, 虽然使得值函数V和优势函数A不再完美的表示值函数和优势函数(在语义上的表示) 但是这种操作提高了稳定性。而且, 并没有改变值函数V和优势函数A的本质表示。。。。

## 模型简介

在传统的DDQN模型中，通过优化目标Q值的计算来优化算法，在Prioritized Replay DQN中，通过优化经验回放池按权重采样来优化算法。

在某些情况下，我们更关注agent所处的state如何，而不是其在该state下做出的action。
主要提出一种duelling结构，将Q网络分解为Value和Advantage,分别学习当前state的价值和在当前状态下各个action的相对价值。最后将两个通道的输出相加得到估计得Q-Value
实现过程中由于Q = V+A,对V和A同时加减一个常量不影响Q值的大小,为了能得到固定的V和A，对A减去所有A的均值。[4]

而在Dueling DQN中，尝试通过优化神经网络的结构来优化算法。具体的操作如下：

Dueling DQN考虑将Q网络分成两部分，第一部分仅仅与状态S有关，这部分叫做价值函数部分，记为V；第二部分同时与状态S和动作A有关，这部分叫做优势函数，记为A，所以最终的Q为：Q=V+A

我们可以直接使用上一节的价值函数的组合公式得到我们的动作价值, 但是这个式子无法辨识最终输出里面 $V(S, w, \alpha)$ 和 $A(S, A, w, \beta)$ 各自的作 为了可以体现这种可辨识性(identifiability),实际使用的组合公式如下：
$$
Q(S, A, w, \alpha, \beta)=V(S, w, \alpha)+\left(A(S, A, w, \beta)-\frac{1}{\mathcal{A}} \sum_{a^{\prime} \in \mathcal{A}} A\left(S, a^{\prime}, w, \beta\right)\right)
$$
其实就是对优势函数部分做了中心化的处理。以上就是Duel DQN的主要算法思路。由于它仅仅涉及神经网络的中间结构的改进, 现有的DQN算法可以

用Duel DQN网络结构的基础上继续使用现有的算法。由于算法主流程和其他算法没有差异，这里就不单独讲Duel DQN的算法流程了。
Dueling DQN网络与DDQN网络结构的区别如下图所示（左边为DDQN，右边为Dueling DQN）：

## 算法[3]

本算法仅仅改变了Q网络的结构，算法仍然使用DQN算法。 值得注意的是在网络的状态价值与优势值求和时，对于一个Q值，状态价值和优势值可以任意调整。为了解决这种不确定性，作者提出了两种方式来限制优势值的范围。

强制最大的Advantage等于零，即让Advantage层的输出减去其最大值
强制Advantage的均值等于零，即让Advantage层的输出减去其均值
由于均值相对于最大值更加稳定，作者最终选用了后一种方式。


DQN系列我花了5篇来讲解，一共5个前后有关联的算法：DQN(NIPS2013), Nature DQN, DDQN, Prioritized Replay DQN和Dueling DQN。目前使用的比较主流的是后面三种算法思路

绝大多数DQN只能处理离散的动作集合，不能处理连续的动作集合。虽然NAF DQN可以解决这个问题，但是方法过于复杂了。而深度强化学习的另一个主流流派Policy-Based而可以较好的解决这个问题，从下一篇我们开始讨论Policy-Based深度强化学习。


[1]:


[4]: https://github.com/shenweichen/ReinforcementLearning
[5]: https://blog.csdn.net/gsww404/article/details/104997834
