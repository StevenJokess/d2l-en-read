

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 22:08:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 22:11:51
 * @Description:
 * @TODO::
 * @Reference:https://spinningup.readthedocs.io/zh_CN/latest/spinningup/rl_intro.html#bellman-equations
-->

术语：

状态和观察(states and observations)
动作空间(action spaces)
策略(policies)
行动轨迹(trajectories)
不同的回报公式(formulations of return)
强化学习优化问题(the RL optimization problem)
值函数(value functions)

机性策略
深度强化学习中最常见的两种随机策略是 绝对策略 (Categorical Policies) 和 对角高斯策略 (Diagonal Gaussian Policies)。


贝尔曼方程




## 优势函数（Advantage Functions）

强化学习中，有些时候我们不需要描述一个行动的绝对好坏，而只需要知道它相对于平均水平的优势。也就是说，我们只想知道一个行动的相对 优势 。这就是优势函数的概念。

一个服从策略 \pi 的优势函数，描述的是它在状态 s 下采取行为 a 比随机选择一个行为好多少（假设之后一直服从策略 \pi ）。数学角度上，优势函数的定义为：



马尔科夫决策过程指的是服从 马尔科夫性 的系统： 状态转移只依赖与最近的状态和行动，而不依赖之前的历史数据。
