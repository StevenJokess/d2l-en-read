

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 20:52:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 21:36:25
 * @Description:
 * @TODO::
 * @Reference:https://yinyoupoet.github.io/2020/02/18/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0%E4%B9%8B%E6%B7%B1%E5%BA%A6Q%E7%BD%91%E7%BB%9CDQN%E8%AF%A6%E8%A7%A3/#%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0
-->



先分别介绍强化学习和Q-学习，然后再引入深度强化学习和DQN。

## 强化学习

讲强化学习先讲其适用的场景。强化学习多用在需要与环境交互的场景下，即给定一个环境的状态（State），程序根据某种策略（Policy）选出一个对应的行为（Action），而执行这个Action后环境又会发生改变，即状态会转换为新的状态S'，且每执行完一个Action后程序会得到一个激励值（Reward），而程序就依据得到的激励值的大小调整其策略，使得在所有步骤执行完后，即状态到达终止状态（Terminal）时，所获得的Reward之和最大。

上面说的可能比较抽象，举个例子，假如我们的程序是一只小狗，现在我们让它坐下（给它一个State），它如果听话（某种Policy）坐下（执行Action），那么我们就给它一个鸡腿（正激励），而如果它不听话（某种Policy）跑开了（执行另一种Action），我们就罚它一顿不许吃饭（负激励），而在它执行完这个行为后，我们可以再次对它提出要求，比如让它站起来（新的State），然后如此往复。小狗对我们给的每一个状态都要给出一个行为，而我们会在它每次给出行为后决定给它一个什么样的激励，且环境的状态在它执行完Action后可能会发生变化，然后它需要对新环境再继续根据某种策略选择执行新的动作，从而得到新的激励。而我们训练的目的，就是使得总的激励值之和最大。

环境观测值/状态 State
动作选择策略 Policy
执行的动作/行为 Action
得到的奖励 Reward
下一个状态 S’

Agent是我们的程序，它观察Environment并获得state，依据它的Policy对state做出action，此时能得到一个reward，且Environment改变了，因此Agent会得到一个新的state，并继续执行下去。


Q-Learning
Q学习算法是强化学习中的一种，更准确的说，是一种关于策略的选择方式。实际上，我们可以发现，强化学习的核心和训练目标就是选择一个合适的策略Policy，使得在每个epoch结束时得到的reward之和最大。

Q学习的思想是：Q(S, A) = 在状态S下，采取动作A后，未来将得到的奖励Reward值之和。


## DQN

DQN属于DRL（深度强化学习）的一种，它是深度学习与Q学习的结合体。前面讲了采用S-A表格的局限性，当状态和行为的组合不可穷尽时，就无法通过查表的方式选取最优的Action了。这时候就该想到深度学习了，想通过深度学习找到最优解在很多情况下确实不太靠谱，但是找到一个无限逼近最优解的次优解，倒是没有问题的。

因此DQN实际上，总体思路还是用的Q学习的思路，不过对于给定状态选取哪个动作所能得到的Q值，却是由一个深度神经网络来计算的了，其流程图如下：

![DQN](img\DQN.png)

![DQN_alg](img\DQN_alg.png)

## Target Network

上面的代码似乎已经能够正常运行了，为什么又冒出一个target network呢？回想下前面那个公式，这里重新搬到下面来，是不是之前说target和θi-都先忽略，现在就该解释一下了。


损失函数

这个公式里θi-和θi肯定是有区别的，不然也犯不着用两个符号了。事实上，我们需要设计两个DNN，它们结构完全一样，但是参数不一样，即神经网络中各层的权重、偏置等，一个的参数是θi-，而另一个是θi。我们每次迭代中，更新的是θi而不更新θi-，且规定每运行C步后让θi- = θi。而其θi-所在的网络就被称为target network。

为什么要弄这么奇怪的东西？

这也是为了防止过拟合。试想如果只有一个神经网络，那么它就在会不停地更新，那么它所追求的目标是在一直改变的，即在θ改变的时候，不止Q(s, a)变了，max *Q(s’, a’)*也变了。这样的好处是使得上面公式中target所标注的部分是暂时固定的，我们不断更新θ追逐的是一个固定的目标，而不是一直改变的目标。

```md
[1]: https://yinyoupoet.github.io/2020/02/18/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0%E4%B9%8B%E6%B7%B1%E5%BA%A6Q%E7%BD%91%E7%BB%9CDQN%E8%AF%A6%E8%A7%A3/#%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0
[2]: https://www.cnblogs.com/wdzeng/p/10860166.html
[3]:



---

```md
TODO:


Ye, Hao, Geoffrey Ye Li, and Biing-Hwang Fred Juang. “Deep reinforcement learning based resource allocation for V2V communications.” IEEE Transactions on Vehicular Technology 68.4 (2019): 3163-3173.
Mnih, Volodymyr, et al. “Human-level control through deep reinforcement learning.” Nature 518.7540 (2015): 529-533.
Welcome to Deep Reinforcement Learning Part 1 : DQN
RL — DQN Deep Q-network
关于强化学习中经验回放（experience replay）的两个问题？ - 宝珠道人的回答 - 知乎
memory replay 是不是就是在DQN中为训练提供训练样本的呢？ - 东林钟声的回答 - 知乎
Using Deep Q-Learning in the Classification of an Imbalanced Dataset
强化学习的Q-learning可以从已经完成的episode学习吗？还是边学习边完成episode的？ - 郭祥昊的回答 - 知乎
Reinforcement learning – Part 1: Introduction to Q-learning
Reinforcement learning – Part 2: Getting started with Deep Q-Networks
Deep Q Learning
Deep Q-Learning
如何用简单例子讲解 Q - learning 的具体过程？ - 牛阿的回答 - 知乎

https://yinyoupoet.github.io/2020/02/29/%E8%AE%BA%E6%96%87%E6%9F%A5%E6%96%B0/#%E5%8F%82%E8%80%83%E8%AE%BA%E6%96%87


如果你也想进入深度强化学习领域，这里有一些资源供你入门时参考：

Andrej Karpathy的 Deep Reinforcement Learning: Pong from Pixels 是一份关于建立动机和直觉方面很好的介绍文章。
想了解更多关于强化学习方面的理论，可以参考 David Silver的演讲 。这篇演讲没有过多关于深度强化学习的内容（ 基于神经网络的强化学习 ），但至少教会了你很多词汇，帮助你理解相关论文。
John Schulman的 Nuts and Bolts of Deep RL talk 有很多实际应用方面的建议，这些问题你在后面都可能遇到。
想了解目前深度强化学习领域发生了什么，可以参考一下这些内容：

Alex Irpan的 Deep Reinforcement Learning Doesn’t Work Yet 对目前的状况有一个很好的概述。
Vlad Mnih的 Recent Advances and Frontiers in Deep RL ，有很多关于实际例子，用以解决 Alex 文章中提到的问题。
Sergey Levine的 Deep Robotic Learning 谈话，聚焦改善机器人的泛化和样本效率问题。
Pieter Abbeel 在2017 NIPS会议上 Deep Learning for Robotics 主题演讲， 提到很多最新的深度强化学习技术。


UCL Course on RL http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html
UC Berkeley RL Bootcamp https://sites.google.com/view/deep-rl-bootcamp/lectures
DQN paper https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
```

