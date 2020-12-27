

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 21:49:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 20:26:26
 * @Description:
 * @TODO::
 * @Reference:https://nndl.github.io/
 * [2]: https://www.sohu.com/a/336264132_99979179s
-->

# 深度强化学习[1]

深度强化学习是把深度学习和强化学习结合起来，用深度学习学习强化学习模型，所以深度强化学习本质上还是强化学习。

李航表示，当智能系统学习做一些相对简单任务时，可以使用监督学习，监督学习技术已经比较成熟和实用，但代价是要用很多标注数据。相比，强化学习可以适用于让智能系统学习做更加复杂的任务。所以，从这种意义上来说，强化学习未来很有前景。

强化学习未来发展前景广大，但当前却面临着一个巨大的挑战，即强化学习从某种意义上比监督学习更需要大数据，数据成为当前强化学习发展的最大瓶颈。可以想象，未来5G、物联网等技术的发展会带来更多的数据，可能强化学习之后会获得更大的发展。所以，强化学习是大家都很看好的一个方向。[2]

在强化学习中，一般需要建模策略𝜋(𝑎|𝑠)和值函数𝑉𝜋(𝑠),𝑄𝜋(𝑠,𝑎)．早期的强化学习算法主要关注状态和动作都是离散且有限的问题，可以使用表格来记录这些概率．但在很多实际问题中，有些任务的状态和动作的数量非常多．比如围棋的棋局有3361≈ 10170种状态，动作（即落子位置）数量为361．还有些任务的状态和动作是连续的．比如在自动驾驶中，智能体感知到的环境状态是各种传感器数据，一般都是连续的．动作是操作方向盘的方向（−90度∼ 90度）和速度控制（0 ∼ 300公里/小时），也是连续的．


## Why deep reinforcement learning?[3]

• Deep = can process complex sensory input ▪ …and also compute really complex functions • Reinforcement learning = can choose complex actions

为了有效地解决这些问题，我们可以设计一个更强的策略函数（比如深度神经网络），使得智能体可以应对复杂的环境，学习更优的策略，并具有更好的泛化能力．深度强化学习（Deep Reinforcement Learning）是将强化学习和深度学习结合在一起，用强化学习来定义问题和优化目标，用深度学习来解决策略和值函数的建模问题，然后使用误差反向传播算法来优化目标函数．深度强化学习在一定程度上具备解决复杂问题的通用智能，并在很多任务上都取得了很大的成功．[2]

把DRL的算法视为智能体的大脑,那么这个大脑包含两个部分: actor行动模块和 critic评判模块。当然,这两个模块都是由深度神经网络构成的,也正是DRL中“深度”一词的由来。其中 actor行动模块是大脑的动作执行机构,输入外部的环境状态5,然后输出动作a。而 critIc评判模块则可被认为是大脑的价值观,根据历史信息及回馈进行自我调整,然后对整个 actor行动模块进行相关的更新指导。这种基于 actor- critic框架的方法非常类似于人类自身的行为方式。[5]

[1]: https://nndl.github.io/
[2]: https://mrt.aminer.cn/5e05b8176438ae128ad73227
[3]: http://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-1.pdf
[4]: https://github.com/udacity/deep-reinforcement-learning/blob/master/finance/DRL.ipynb
[5]: https://www.hzmedia.com.cn/w/reader.aspx?id=378872d4-69a3-4208-958a-4bc3c48e0287_1
