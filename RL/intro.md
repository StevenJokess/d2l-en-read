

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 22:08:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-08 19:50:28
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

是一个序列化过程，在时刻t，智能体基于当前状态St发出动作At，环境做出回应，生成新的状态St+1和对应的奖励值Rt+1，这里需要强调一点，状态S和奖励值R是成对出现的。智能体的目标就是，通过更加明智地执行动作，从而最大化接下来的累计奖励Gt，公式表示如

T=t+k+1表示最后的时间步，也就意味着在时刻智能体同环境的交互过程结束，这个开始到结束的过程称作一个“轮回（episode）”。当前轮回结束后，智能体的状态会被重置，从而开始一个新的轮回，因此，所有的轮回之间是相互独立

[2]: https://weread.qq.com/web/reader/62332d007190b92f62371aek92c3210025c92cc22753209
