

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 22:08:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 23:34:25
 * @Description:
 * @TODO::
 * @Reference:https://spinningup.readthedocs.io/zh_CN/latest/spinningup/rl_intro.html#bellman-equations
 * https://nndl.github.io/ ch14
 * https://anesck.github.io/M-D-R_learning_notes/RLTPI/notes_html/1.chapter_one.html
-->

即使是专家也很难给出“正确”的动 作，二是获取大量数据的成本往往比较高．对于下棋这类任务，虽然我们很难知 道每一步的“正确”动作，但是其最后的结果（即赢输）却很容易判断．因此，如果 可以通过大量的模拟数据，通过最后的结果（奖励）来倒推每一步棋的好坏，从 而学习出“最佳”的下棋策略，这就是强化学习．

强化学习（ReinforcementLearning，RL），也叫增强学习，是指一类从（与 环境）交互中不断学习的问题以及解决这类问题的方法．强化学习问题可以描 述为一个智能体从与环境的交互中不断学习以完成特定目标（比如取得最大奖 励值）．和深度学习类似，强化学习中的关键问题也是贡献度分配问题[Minsky, 1961]，每一个动作并不能直接得到监督信息，需要通过整个模型的最终监督信 息（奖励）得到，并且有一定的延时性

强化学习的基本概念[3]

奖励（reward）：奖励是强化学习系统的学习目标。智能体在采取行动后会收到环境发来的奖励，而强化学习的目标就是要最大化长时间里的总奖励。
策略（policy）：策略为强化学习的学习对象。策略会指导智能体根据当前环境来采取动作，策略可以是确定性的，也可以是不确定性的（概率分布），强化学习通过改进策略来最大化总奖励。
智能体（agent）：强化学习系统中的行动者和学习者，它可以做出决策和接受奖励信号，我们并不需要对智能体本身进行建模，只需了解它在不同环境下可以做出的动作，并接受奖励信号。
环境（environment）：强化学习系统中除智能体以外的所有事物，它是智能体交互的对象。环境可以是已知的，也可以是未知的，因此可以对环境建模，也可以不对环境建模。
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


注：同策学习（on-policy）是边决策边学习，学习者同时也是决策者。异策学习（off-policy）则是通过之前的历史（可是自己的也可以是别人的）进行学习，学习者和决策者不需要相同。[3]

强化学习和监督学习、无监督学习的区别[5]

1. 监督式学习就好比你在学习的时候，有一个导师在旁边指点，他知道怎么是对的怎么是错的。

   强化学习会在没有任何标签的情况下，通过先尝试做出一些行为得到一个结果，通过这个结果是对还是错的反馈，调整之前的行为，就这样不断的调整，算法能够学习到在什么样的情况下选择什么样的行为可以得到最好的结果。

2. 监督式学习出的是之间的关系，可以告诉算法什么样的输入对应着什么样的输出。监督学习做了比较坏的选择会立刻反馈给算法。

   强化学习出的是给机器的反馈 reward function，即用来判断这个行为是好是坏。 另外强化学习的结果反馈有延时，有时候可能需要走了很多步以后才知道以前的某一步的选择是好还是坏。

3. 监督学习的输入是独立同分布的。

   强化学习面对的输入总是在变化，每当算法做出一个行为，它影响下一次决策的输入。

4. 监督学习算法不考虑这种平衡，就只是 exploitative。

   强化学习，一个 agent 可以在探索和开发（exploration and exploitation）之间做权衡，并且选择一个最大的回报。

5. 非监督式不是学习输入到输出的映射，而是模式(自动映射)。

   对强化学习来说，它通过对没有概念标记、但与一个延迟奖赏或效用（可视为延迟的概念标记）相关联的训练例进行学习，以获得某种从状态到行动的映射。

**强化学习和前二者的本质区别**:没有前两者具有的明确数据概念，它不知道结果，只有目标。数据概念就是大量的数据，有监督学习、无监督学习需要大量数据去训练优化你建立的模型。

|      | 监督学习         | 非监督学习     | 强化学习                                                     |
| ---- | ---------------- | -------------- | ------------------------------------------------------------ |
| 标签 | 正确且严格的标签 | 没有标签       | 没有标签，通过结果反馈调整                                   |
| 输入 | 独立同分布       | 独立同分布     | 输入总是在变化，每当算法做出一个行为，它影响下一次决策的输入。 |
| 输出 | 输入对应输出     | 自学习映射关系 | reward function，即结果用来判断这个行为是好是坏              |
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
[5]: https://github.com/NLP-LOVE/ML-NLP/tree/master/Deep%20Learning/14.%20Reinforcement%20Learning
