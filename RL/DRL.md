

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 21:49:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-11 21:12:34
 * @Description:
 * @TODO::
 * @Reference:https://nndl.github.io/
-->

# 深度强化学习[1]

在强化学习中，一般需要建模策略𝜋(𝑎|𝑠)和值函数𝑉𝜋(𝑠),𝑄𝜋(𝑠,𝑎)．早期的强化学习算法主要关注状态和动作都是离散且有限的问题，可以使用表格来记录这些概率．但在很多实际问题中，有些任务的状态和动作的数量非常多．比如围棋的棋局有3361≈ 10170种状态，动作（即落子位置）数量为361．还有些任务的状态和动作是连续的．比如在自动驾驶中，智能体感知到的环境状态是各种传感器数据，一般都是连续的．动作是操作方向盘的方向（−90度∼ 90度）和速度控制（0 ∼ 300公里/小时），也是连续的．


## Why deep reinforcement learning?[3]

• Deep = can process complex sensory input ▪ …and also compute really complex functions • Reinforcement learning = can choose complex actions

为了有效地解决这些问题，我们可以设计一个更强的策略函数（比如深度神经网络），使得智能体可以应对复杂的环境，学习更优的策略，并具有更好的泛化能力．深度强化学习（Deep Reinforcement Learning）是将强化学习和深度学习结合在一起，用强化学习来定义问题和优化目标，用深度学习来解决策略和值函数的建模问题，然后使用误差反向传播算法来优化目标函数．深度强化学习在一定程度上具备解决复杂问题的通用智能，并在很多任务上都取得了很大的成功．[2]

[1]: https://nndl.github.io/
[2]: https://mrt.aminer.cn/5e05b8176438ae128ad73227
[3]: http://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-1.pdf