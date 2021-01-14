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

### 例子[2]

假设校长、教授和研究生通通都是 agent。那今天假设我们只要进入百大就可以得到 reward。假设进入百大的话，校长就要提出愿景告诉其他的 agent 说，现在你要达到什么样的目标。那校长的愿景可能就是说教授每年都要发三篇期刊。然后接下来这些 agent 都是有分层的，所以上面的 agent，他的动作就是提出愿景这样。那他把他的愿景传给下一层的 agent，下一层的 agent 就把这个愿景吃下去。如果他下面还有其他人的话，它就会提出新的愿景。比如说，校长要教授发期刊，但其实教授自己也是不做实验的。所以，教授也只能够叫下面的研究生做实验。所以教授就提出愿景，就做出实验的规划，然后研究生才是真的去执行这个实验的人。然后，真的把实验做出来，最后大家就可以得到reward。那现在是这样子的，在 learn 的时候，其实每一个 agent 都会 learn。那他们的整体的目标就是要达到最后的reward。那前面的这些 agent，他提出来的 actions 就是愿景这样。你如果是玩游戏的话，他提出来的就是，我现在想要产生这样的游戏画面。但是，假设他提出来的愿景是下面的 agent 达不到的，那就会被讨厌。举例来说，教授对研究生都一直逼迫研究生做一些很困难的实验，研究生都做不出来的话，研究生就会跑掉，所以他就会得到一个 penalty。所以如果今天下层的 agent 没有办法达到上层 agent 所提出来的 goal 的话，上层的 agent 就会被讨厌，它就会得到一个 negative reward。所以他要避免提出那些愿景是底下的 agent 所做不到的。那每一个 agent 都是把上层的 agent 所提出来的愿景当作输入，然后决定他自己要产生什么输出。

[1]: https://blog.csdn.net/weixin_42770354/article/details/109849703
[2]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter10/chapter10
