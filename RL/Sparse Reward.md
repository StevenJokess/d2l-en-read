

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 20:20:55
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 20:21:10
 * @Description:
 * @TODO::
 * @Reference:
-->

# Sparse Reward

在使用Reinforcement Learning来构造agent时，多数情况下这个agent是得不到任何Reward的。这使得agent的训练变得非常困难。
举例来说，假设我们制作了一个机械手臂，希望让它完成‘用桌上的螺丝刀把螺丝钉栓进去’这个任务，但agent起初是什么都不知道的，它能够完成各种action的原因在于Exploration机制。只有当它随机地将螺丝刀拿起来，再把螺钉栓进去，这个时候它才能得到Reward，但想在随机的情况下完成这一系列的动作就如大海捞针一般困难。

稀疏奖励问题是指agent探索的过程中难以获得正奖励，导致学习缓慢甚至无法进行学习的问题，并且广泛存在于现实中，比如围棋，人们很难去设定中间每步的奖励，并且状态空间巨大，使用全局奖励会有奖励稀疏且滞后的问题。[4]

所以说，当环境当中的reward十分稀疏（sparse）时，这个RL的问题就会十分困难。本节课程介绍的就是三种用于解决Sparse Reward的方法。

## Reward Shaping

即人工地设计Reward，刻意地引导agent进行我们想要的action，让环境当中的reward变得不那么稀疏。下面是一些人为设计Reward的方法。

Reward shaping 的意思是说环境有一个固定的 reward，它是真正的 reward，但是为了让 agent 学出来的结果是我们要的样子，我们刻意地设计了一些 reward 来引导我们的 agent。

举例来说，如果是把小孩当成一个 agent 的话。那一个小孩，他可以 take 两个 actions，一个 action 是他可以出去玩，那他出去玩的话，在下一秒钟它会得到 reward 1。但是他在月考的时候，成绩可能会很差。所以在100 个小时之后呢，他会得到 reward -100。然后，他也可以决定要念书，然后在下一个时间，因为他没有出去玩，所以他觉得很不爽，所以他得到 reward -1。但是在 100 个小时后，他可以得到 reward 100。但对一个小孩来说，他可能就会想要 take play 而不是 take study。我们计算的是 accumulated reward，但也许对小孩来说，他的 discount factor 会很大，所以他就不太在意未来的reward。而且因为他是一个小孩，他还没有很多 experience，所以他的 Q-function estimate 是非常不精准的。所以要他去 estimate 很远以后会得到的 accumulated reward，他其实是预测不出来的。所以这时候大人就要引导他，怎么引导呢？就骗他说，如果你坐下来念书我就给你吃一个棒棒糖。所以，对他来说，下一个时间点会得到的 reward 就变成是positive 的。所以他就觉得说，也许 take 这个 study 是比 play 好的。虽然这并不是真正的 reward，而是其他人骗他的reward，告诉他说你采取这个 action 是好的。Reward shaping 的概念是一样的，简单来说，就是你自己想办法 design 一些 reward，它不是环境真正的 reward。在玩 Atari 游戏里面，真的 reward 是游戏主机给你的 reward，但你自己去设计一些 reward 好引导你的 machine，做你想要它做的事情。

Reward shaping 是有问题的，因为我们需要 domain knowledge，举例来说，机器人想要学会的事情是把蓝色的板子从这个柱子穿过去。机器人很难学会，我们可以做 reward shaping。一个貌似合理的说法是，蓝色的板子离柱子越近，reward 越大。但是 machine 靠近的方式会有问题，它会用蓝色的板子打柱子。而我们要把蓝色板子放在柱子上面去，才能把蓝色板子穿过柱子。 这种 reward shaping 的方式是没有帮助的，那至于什么 reward shaping 有帮助，什么 reward shaping 没帮助，会变成一个 domain knowledge，你要去调的。

## Curiosity

ICM intrinsic curiosity module

在Q-learning当中，我们根据每一个状态 $s_{t}$ 和在这个状态下采取的action $a_{t}$ 得到了这一个step的 reward $r_{t},$ 期望所有step的reward之和越大越好。在Curiosity的机制下，我们加入了另一个得到 Reward的方式一 $\quad \mathrm{ICM} r_{i}^{t},$ 它由当前状态 $s_{t},$ 采取的action $a_{t}$ 以及下一个状态 $s_{t+1}$ 计算得到。

ICM最原始的具体设计方式如下：有一个network以 $s_{t}$ 和 $a_{t}$ 作为输入，其输出的是machine自己预测的 下一个状态 $\hat{s}_{t+1},$ 然后让它和真实发生的下一个状态 $s_{t+1}$ 做对比, 二者相差越大, ICM得到的reward 就越高，即如果未来得到的state越难被预测到，得到的reward就越高。这就鼓励machine在最开始训 练模型的时候去主动采取那些风险比较大的action。。

## Curriculum Learning

通过设置不同难度梯度的课程来加速学习，类似人类学习的过程，从简单的问题学习到的策略能够迁移到复杂的问题中。目前也有一些自动课程学习的研究，推荐这个国外的博客 https://lilianweng.github.io/lil-log/2020/01/29/curriculum-for-reinforcement-learning.html#automatic-goal-generation ，对课程学习的算法讲的很详细。[4]

即给机器的学习过程做规划, 从简单到困难。。 准确的来说, 是逐渐提高学习的样本难度，模拟人类的学习过程。 为此，我们需要为机器设计'课程'，即给机器学习的样本做难度上的规划, 一种通用的方法被称作 Reverse Curriculum Generation。它的一般步骤如下:

1. 确定一个目标状态 $s_{g \circ}$
2. 设计一些与目标状态相近的状态 $s_{1}$
3. 以这些 $s_{1}$ 开始与环境互动, 每一个 $s_{1}$ 得到的状态-行动序列 $\tau$ 都有一个Reward $R\left(s_{1}\right)$
4. 删去那些 $R\left(s_{1}\right)$ 过大或过小的样本 $($ 过大代表样本难度过低, 反之则代表过高 $)$, 留下 $R\left(s_{1}\right)$ 适 中的样本
5. 在这些适中的样本周围再Sample出更多的状态 $s_{2},$ 重复步骤3、4。。

### Reverse Curriculum Generation

什么叫做适中，这个就是你要调的参数，找一些 reward 适中的 case。接下来，再根据这些 reward 适中的 case 去 sample 出更多的 state。假设你一开始，你机械手臂在这边，可以抓的到以后。接下来，就再离远一点，看看能不能够抓得到，又抓的到以后，再离远一点，看看能不能抓得到。这是一个有用的方法，它叫做Reverse Curriculum learning。刚才讲的是 curriculum learning，就是你要为机器规划它学习的顺序。而 reverse curriculum learning 是从 gold state 去反推，就是说你原来的目标是长这个样子，我们从目标去反推，所以这个叫做 reverse。[3]


如何提高模型解决大状态空间大动作空间下复杂问题的能力

## Hierarchical Reinforcement Learning

将所有的agent分层，上层的agent将目标分解为小目标，当目标不能再被分解的时候，最底层的agent就付诸行动，采取action以实现这些小目标。当最底层的agent不能完成这些目标时，上层的agent就会受到一定的惩罚（Penalty），所以上层的agent要避免提出下层agent达不到的目标。另外，当下层的agent达成了一个错误的目标的时候，我们就将上层提出的目标直接修改为下层达成的这个目标（即不浪费下层agent训练过程中的任何成果）[1]

分层强化学习，使用多层次的结构来学习不同层次的策略，提高了解决复杂问题的能力。比较经典的比如 FeUdal networks for hierarchical reinforcement learning、Meta-Learning SharedHierarchies、Learning Multi-Level Hierarchies with Hindsight。[4]

## 数据

一是，利用数据改进 agent 的学习，包括已有数据、外部数据等；二是，改进模型，提升模型在大状态、大动作空间下处理复杂问题的能力。具体的，利用数据改进 agent 学习的方法包括好奇心驱动（Curiosity Driven）、奖励重塑（Reward Shaping）、模仿学习（Imitation Learning）、课程学习（Curriculum Learning）等等。改进模型的方法主要是执行分层强化学习（Hierarchical Reinforcement Learning），使用多层次的结构分别学习不同层次的策略来提高模型解决复杂问题的能力，以及元学习（Meta-Learning）的方法。

举例：我们要完成一个很大的 task 的时候，我们并不是从非常底层的那些 action 开始想起，我们其实是有个 plan。我们先想说，如果要完成这个最大的任务，那接下来要拆解成哪些小任务。每一个小任务要再怎么拆解成小小的任务。举例来说，叫你直接写一本书可能很困难，但叫你先把一本书拆成好几个章节，每个章节拆成好几段，每一段又拆成好几个句子，每一个句子又拆成好几个词汇，这样你可能就比较写得出来，这个就是分层的 reinforcement learning 的概念。[2]

https://www.chainnews.com/articles/832740147057.htm

[1]: https://blog.csdn.net/weixin_42770354/article/details/109849703
[2]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter10/chapter10?id=reward-shaping
[3]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter10/chapter10?id=reward-shaping
[4]: 强化学习稀疏奖励算法总结 - yr15的文章 - 知乎 https://zhuanlan.zhihu.com/p/133334392
