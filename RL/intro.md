

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 22:08:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-11 21:10:21
 * @Description:
 * @TODO::
 * @Reference:https://spinningup.readthedocs.io/zh_CN/latest/spinningup/rl_intro.html#bellman-equations
 * https://nndl.github.io/ ch14
-->

即使是专家也很难给出“正确”的动 作，二是获取大量数据的成本往往比较高．对于下棋这类任务，虽然我们很难知 道每一步的“正确”动作，但是其最后的结果（即赢输）却很容易判断．因此，如果 可以通过大量的模拟数据，通过最后的结果（奖励）来倒推每一步棋的好坏，从 而学习出“最佳”的下棋策略，这就是强化学习．

强化学习（ReinforcementLearning，RL），也叫增强学习，是指一类从（与 环境）交互中不断学习的问题以及解决这类问题的方法．强化学习问题可以描 述为一个智能体从与环境的交互中不断学习以完成特定目标（比如取得最大奖 励值）．和深度学习类似，强化学习中的关键问题也是贡献度分配问题[Minsky, 1961]，每一个动作并不能直接得到监督信息，需要通过整个模型的最终监督信 息（奖励）得到，并且有一定的延时性

## VS ML

Standard (supervised) machine learning:
Usually assumes:
• i.i.d. data
• known ground truth outputs in training

Reinforcement learning:
• Data is not i.i.d.: previous outputs influence future inputs! • Ground truth answer is not known, only know if we succeeded or failed • more generally, we know the reward

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

策略 智能体的策略（Policy）就是智能体如何根据环境状态𝑠来决定下一步的 动作𝑎，通常可以分为确定性策略（Deterministic Policy）和随机性策略（StochasticPolicy）两种[2]

贝尔曼方程

𝑉𝜋(𝑠) = 𝔼𝜏0∶𝑇∼𝑝(𝜏)[𝑟1+ 𝛾𝑇−1∑𝑡=1𝛾𝑡−1𝑟𝑡+1|𝜏𝑠0= 𝑠](14.15)
= 𝔼𝑎∼𝜋(𝑎|𝑠)𝔼𝑠′∼𝑝(𝑠′|𝑠,𝑎)𝔼𝜏1∶𝑇∼𝑝(𝜏)[𝑟(𝑠,𝑎,𝑠′) + 𝛾𝑇−1∑𝑡=1𝛾𝑡−1𝑟𝑡+1|𝜏𝑠1= 𝑠′](14.16)
= 𝔼𝑎∼𝜋(𝑎|𝑠)𝔼𝑠′∼𝑝(𝑠′|𝑠,𝑎)[𝑟(𝑠,𝑎,𝑠′) + 𝛾𝔼𝜏1∶𝑇∼𝑝(𝜏)[𝑇−1∑𝑡=1𝛾𝑡−1𝑟𝑡+1|𝜏𝑠1= 𝑠′]](14.17)
= 𝔼𝑎∼𝜋(𝑎|𝑠)𝔼𝑠′∼𝑝(𝑠′|𝑠,𝑎)[𝑟(𝑠,𝑎,𝑠′) + 𝛾𝑉𝜋(𝑠′)].(14.18)

表示当前状态的值函数可以通过下个状态的值函数来计算．贝尔曼方程因其提出者、美国国家科学院院士、动态规划创始人理查德·贝尔曼（RichardBellman，1920～1984）而得名，也叫作“动态规划方程”．如果给定策略𝜋(𝑎|𝑠)，状态转移概率𝑝(𝑠′|𝑠,𝑎)和奖励𝑟(𝑠,𝑎,𝑠′)，我们就可以通过迭代的方式来计算𝑉𝜋(𝑠)．由于存在折扣率，迭代一定步数后，每个状态的值函数就会固定不变．



## 优势函数（Advantage Functions）

强化学习中，有些时候我们不需要描述一个行动的绝对好坏，而只需要知道它相对于平均水平的优势。也就是说，我们只想知道一个行动的相对 优势 。这就是优势函数的概念。

一个服从策略 \pi 的优势函数，描述的是它在状态 s 下采取行为 a 比随机选择一个行为好多少（假设之后一直服从策略 \pi ）。数学角度上，优势函数的定义为：



马尔科夫决策过程指的是服从 马尔科夫性 的系统： 状态转移只依赖与最近的状态和行动，而不依赖之前的历史数据。

是一个序列化过程，在时刻t，智能体基于当前状态St发出动作At，环境做出回应，生成新的状态St+1和对应的奖励值Rt+1，这里需要强调一点，状态S和奖励值R是成对出现的。智能体的目标就是，通过更加明智地执行动作，从而最大化接下来的累计奖励Gt，公式表示如

T=t+k+1表示最后的时间步，也就意味着在时刻智能体同环境的交互过程结束，这个开始到结束的过程称作一个“轮回（episode）”。当前轮回结束后，智能体的状态会被重置，从而开始一个新的轮回，因此，所有的轮回之间是相互独立

强化学习的主流算法[3]

免模型学习（Model-Free） vs 有模型学习（Model-Based）

在介绍详细算法之前，我们先来了解一下强化学习算法的2大分类。这2个分类的重要差异是：智能体是否能完整了解或学习到所在环境的模型

有模型学习（Model-Based）对环境有提前的认知，可以提前考虑规划，但是缺点是如果模型跟真实世界不一致，那么在实际使用场景下会表现的不好。

免模型学习（Model-Free）放弃了模型学习，在效率上不如前者，但是这种方式更加容易实现，也容易在真实场景下调整到很好的状态。所以免模型学习方法更受欢迎，得到更加广泛的开发和测试。
主流的分类


## challenge[4]

• Humans can learn incredibly quickly
• Deep RL methods are usually slow • Humans can reuse past knowledge
• Transfer learning in deep RL is an open problem
• Not clear what the reward function should be
• Not clear what the role of prediction should be

![主流的分类](img/fenlei.jpg)
[2]: https://weread.qq.com/web/reader/62332d007190b92f62371aek92c3210025c92cc22753209
[3]: https://easyai.tech/ai-definition/reinforcement-learning/
[4]: http://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-1.pdf