# Sparse Reward

在使用Reinforcement Learning来构造agent时，多数情况下这个agent是得不到任何Reward的。这使得agent的训练变得非常困难。
举例来说，假设我们制作了一个机械手臂，希望让它完成‘用桌上的螺丝刀把螺丝钉栓进去’这个任务，但agent起初是什么都不知道的，它能够完成各种action的原因在于Exploration机制。只有当它随机地将螺丝刀拿起来，再把螺钉栓进去，这个时候它才能得到Reward，但想在随机的情况下完成这一系列的动作就如大海捞针一般困难。
所以说，当环境当中的reward十分稀疏（sparse）时，这个RL的问题就会十分困难。本节课程介绍的就是三种用于解决Sparse Reward的方法。

## Reward Shaping

即人工地设计Reward，刻意地引导agent进行我们想要的action，让环境当中的reward变得不那么稀疏。下面是一些人为设计Reward的方法。

## Curiosity

ICM intrinsic curiosity module

在Q-learning当中，我们根据每一个状态 $s_{t}$ 和在这个状态下采取的action $a_{t}$ 得到了这一个step的 reward $r_{t},$ 期望所有step的reward之和越大越好。在Curiosity的机制下，我们加入了另一个得到 Reward的方式一 $\quad \mathrm{ICM} r_{i}^{t},$ 它由当前状态 $s_{t},$ 采取的action $a_{t}$ 以及下一个状态 $s_{t+1}$ 计算得到。

ICM最原始的具体设计方式如下：有一个network以 $s_{t}$ 和 $a_{t}$ 作为输入，其输出的是machine自己预测的 下一个状态 $\hat{s}_{t+1},$ 然后让它和真实发生的下一个状态 $s_{t+1}$ 做对比, 二者相差越大, ICM得到的reward 就越高，即如果未来得到的state越难被预测到，得到的reward就越高。这就鼓励machine在最开始训 练模型的时候去主动采取那些风险比较大的action。。

## Curriculum Learning

即给机器的学习过程做规划, 从简单到困难。。 准确的来说, 是逐渐提高学习的样本难度，模拟人类的学习过程。 为此，我们需要为机器设计'课程'，即给机器学习的样本做难度上的规划, 一种通用的方法被称作 Reverse Curriculum Generation。它的一般步骤如下:

1. 确定一个目标状态 $s_{g \circ}$
2. 设计一些与目标状态相近的状态 $s_{1}$
3. 以这些 $s_{1}$ 开始与环境互动, 每一个 $s_{1}$ 得到的状态-行动序列 $\tau$ 都有一个Reward $R\left(s_{1}\right)$
4. 删去那些 $R\left(s_{1}\right)$ 过大或过小的样本 $($ 过大代表样本难度过低, 反之则代表过高 $)$, 留下 $R\left(s_{1}\right)$ 适 中的样本
5. 在这些适中的样本周围再Sample出更多的状态 $s_{2},$ 重复步骤3、4。。

## Hierarchical Reinforcement Learning

将所有的agent分层，上层的agent将目标分解为小目标，当目标不能再被分解的时候，最底层的agent就付诸行动，采取action以实现这些小目标。当最底层的agent不能完成这些目标时，上层的agent就会受到一定的惩罚（Penalty），所以上层的agent要避免提出下层agent达不到的目标。另外，当下层的agent达成了一个错误的目标的时候，我们就将上层提出的目标直接修改为下层达成的这个目标（即不浪费下层agent训练过程中的任何成果）[1]

[1]: https://blog.csdn.net/weixin_42770354/article/details/109849703
