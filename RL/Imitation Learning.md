

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-19 20:01:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 19:51:15
 * @Description:
 * @TODO::
 * @Reference:
-->

# Imitation learning

强化学习是一种利用试错的方法训练主体在复杂环境中进行决策的过程，主体在训练过程中的典型目标是需要最大化在环境中所获取的奖励信息，而这些奖励则与大量的参数相关，包括速度、好奇心和审美特征等等。然而，由于难以定义或者太过稀疏，为特定的任务设计奖励函数却是十分困难的，所以这一问题很难用强化学习来解决。

Imitation learning 讨论的问题是：假设我们连 reward 都没有，那要怎么办呢？Imitation learning 又叫做 learning from demonstration(示范学习) ，apprenticeship learning(学徒学习)，learning by watching(观察学习)[7]

在多步决策（sequential decision）中，学习器不能频繁地得到奖励，且这种基于累积奖赏及学习方式存在非常巨大的搜索空间。而模仿学习（Imitation Learning）的方法经过多年的发展，已经能够很好地解决多步决策问题。

模仿学习（Imitation learning，IL）方法为强化学习提供了一种可能的解决方案，从专家的示教中学习如何解决问题。然而前沿的模仿学习方法都依赖于对抗训练，利用最小/最大优化流程进行训练，使得算法在训练时不太稳定也不便于部署。

## 适用范围

假设你不知道该怎么定义 reward，你就可以收集到 expert 的 demonstration。如果你可以收集到一些范例的话，你可以收集到一些很厉害的 agent(比如人)跟环境实际上的互动的话，那你就可以考虑 imitation learning 这个技术。[7]


### 分类

Imitation Learning有两种具体的方法：Behavior Cloning和Inverse Reinforcement Learning（Inverse Optimal Control）

## 对抗模仿学习(GAIL)

前沿的对抗模仿学习方法与生成对抗网络十分类似，都是利用生成器（策略）来最大化对于判别器（奖励）的混淆，而判别器则会努力区分主体的状态行为与专家间的区别。

对抗模仿学习可以被归结为分布匹配问题，例如在度量空间中最小化概率分布间的距离。然而就像GAN一样，对抗模仿学习仅仅依赖于最小/最大化优化，会使训练过程存在不可避免的稳定性问题。
\

PWIL的优势在于不仅可以覆盖专家的行为，同时其奖励函数无需与环境进行交互同时易于调节。这为未来模仿学习领域的探索打开了新的方向。PWIL还可以应用于只有试教状态存在的情况下，最终也能用于基于视觉观察的行为操控中去。[1][2]

能模仿人的智能体[4]
这是通过GANs实现模仿学习。不同于传统的奖励机制，某些AI研究人员希望针对自主学习智能体，提出一种全新的方法。

他们将实际的示范数据输入到智能体，然后智能体从中学习并尝试模仿相同的动作。

code[5]

### Third Person lmitation Learning


其实还有很多相关的研究，举例来说，你在教机械手臂的时候，要注意就是也许机器看到的视野跟人看到的视野是不太一样的。在刚才那个例子里面，人跟机器的动作是一样的。但是在未来的世界里面，也许机器是看着人的行为学的。刚才是人拉着，假设你要让机器学会打高尔夫球，在刚才的例子里面就是人拉着机器人手臂去打高尔夫球，但是在未来有没有可能机器就是看着人打高尔夫球，它自己就学会打高尔夫球了呢？但这个时候，要注意的事情是机器的视野跟它真正去采取这个行为的时候的视野是不一样的。机器必须了解到当它是第三人的视角的时候，看到另外一个人在打高尔夫球，跟它实际上自己去打高尔夫球的时候，看到的视野显然是不一样的。但它怎么把它是第三人的时间所观察到的经验把它 generalize 到它是第一人称视角的时候所采取的行为，这就需要用到Third Person Imitation Learning的技术。[7]

[1]: https://www.zhihu.com/question/376954557/answer/1500668073
[2]: https://ai.googleblog.com/2020/09/imitation-learning-in-low-data-regime.html
[3]: https://github.com/RITCHIEHuang/Awesome-Imitation-Learning
[4]: https://zhuanlan.zhihu.com/p/28504510
[5]: https://github.com/openai/imitation
[6]: https://blog.csdn.net/weixin_42770354/article/details/109853524
[7]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter11/chapter11
