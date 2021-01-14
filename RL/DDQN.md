

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 23:24:08
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 00:31:47
 * @Description:
 * @TODO::
 * @Reference:
-->

# DDQN (Double Deep Q-Network)

主要提出在计算Target Q值的时候，使用当前网络选择贪婪策略，然后使用Target Q网络来评估策略。这样有利于减少由于直接使用max(Target Q)值带来的过度估计(Over Estimation)，所谓过度估计就是最终我们得到的算法模型有很大的偏差(bias)[4]。

是2016年提出的算法，灵感源自2010年的Double Q-learning

注意和Double Q-Learning进行区分(Double Q-Learning是交替交换两个Q的角色进行更新，而Double DQN依然是若干step使用当前网络更新TargetQ网络)[3]

将算法DQN的[2]

$U_{t} \leftarrow R_{t+1}+\gamma \max _{a} Q\left(S_{t+1}, a ; \mathbf{w}_{\text {目标 }}\right)$


而在Double-DQN中，不再是直接从目标 $Q_{tar}$ 网络中选择各个动作中的最大 $Q$ 值, 而是先从当前 $Q$ 网络选择Q值最大对应的动作, 然后代入到目标网络$Q_{tar}$中计算对应的值：


$U_{t} \leftarrow R_{t+1}+\gamma Q_{tar}\left(S_{t+1}, \arg \max _{a} Q\left(S_{t+1}, a ; \mathbf{w}\right) ; \mathbf{w}_{\text {目标}}\right)$

Double-DQN的好处是Nature DQN中使用max虽然可以快速让Q值向可能的优化目标靠拢，但是很容易过犹不及，导致过度估计(Over Estimation)，所谓过度估计就是最终我们得到的算法模型有很大的偏差(bias)。[5]

解决方案：DDQN通过解耦目标Q值动作的选择和目标Q值的计算这两步

每次更新动作价值时用其中的一个网络确定动作，用确定的动作和另外一个网络来估计回报。

而双重Q学习却可以消除最大化偏差。基于查找表的双重Q学习引入了两个动作价值的估计q(0)和q(1)，每次更新动作价值时用其中的一个网络确定动作，用确定的动作和另外一个网络来估计回报。

![Ari](img/DDQN.png)

Deepmind于2015年发表论文《Deep reinforcement learning with double Q-learning》，将双重Q学习用于深度Q网络，得到了双重深度Q网络（DoubleDeep Q Network，Double DQN）

考虑到深度Q网络已经有了评估网络和目标网络两个网络，所以双重深度Q学习在估计回报时只需要用评估网络确定动作，用目标网络确定回报的估计即可。

将算法DQN的[2]

$U_{t} \leftarrow R_{t+1}+\gamma \max _{a} q\left(S_{t+1}, a ; \mathbf{w}_{\text {目标 }}\right)$

换为

$U_{t} \leftarrow R_{t+1}+\gamma q\left(S_{i} \arg \max _{a} Q\left(S_{t+1}, a ; \mathbf{w}\right) ; \mathbf{w}_{\text {目标}}\right)$

## 为什么 Q 值总是被高估了呢？

因为实际上在做的时候，是要让左边这个式子跟右边这个目标越接近越好。你会发现目标的值很容易一不小心就被设得太高。因为在算这个目标的时候，我们实际上在做的事情是，看哪一个 a 可以得到最大的 Q 值，就把它加上去，就变成我们的目标。所以假设有某一个动作得到的值是被高估的。

举例来说， 现在有 4 个动作，本来它们得到的值都是差不多的，它们得到的 reward 都是差不多的。但是在估计的时候，网络是有误差的。

- 假设是第一个动作被高估了，假设绿色的东西代表是 被高估的量, 它被高估了，那这个目标就会选这个动 作, 然后就会选这个高估的 Q 值来加上 $r_{t},$ 来当作你 的目标。
- 如果第四个动作被高估了，那就会选第四个动作来加 上 $\mathrm{r}_{\mathrm{t}}$ 来当作你的目标值。所以你总是会选那个 $\mathrm{Q}$ 值被 高估的, 你总是会选那个 reward 被高估的动作当作这 个 max 的结果去加上 $\mathrm{r}_{\mathrm{t}}$ 当作你的目标, 所以你的目标总是太大。

## 怎么解决目标值总是太大的问题呢?

在 Double DQN 里面，选动作的 Q-function 跟算值的 Q-function 不是同一个。在原来的 DQN 里面, 你穷举所有的
a, 把每一个 a 都带进去, 看哪一个a 可以给你的 Q 值最 高，那你就把那个 Q 值加上 $\mathrm{r}_{\mathrm{t}}$ 。但是在 Double DQN 里
面, 你有两个 Q-network：
- 第一个 Q-network Q 决定哪一个动作的 Q 值最大（你 把所有的 a 带入 Q 中，看看哪一个 Q 值最大) 。
- 你决定你的动作以后, 你的 Q 值是用 $\mathrm{Q}^{\prime}$ 算出来的。
假设我们有两个 Q-function,
- 假设第一个 Q-function 高估了它现在选出来的动作 a, 只要第二个 Q-function $\mathrm{Q}^{\prime}$ 没有高估这个动作 a 的 值，那你算出来的就还是正常的值。
- 假设 $\mathrm{Q}^{\prime}$ 高估了某一个动作的值，那也没差, 因为只 要前面这个 Q 不要选那个动作出来就没事了，这个就 是 Double DQN 神奇的地方。

## 哪来 $\mathrm{Q}$ 跟 $\mathrm{Q}^{\prime}$ 呢? 哪来两个网络呢?

在实现上，你有两个 Q-network：目标的 Q-network 和 你会更新的 Q-network。所以在 Double DQN 里面，你会 拿你会更新参数的那个 Q-network 去选动作，然后你拿目 标网络（固定住不动的网络) 去算值。

Double DQN 相较于原来的 DQN 的更改是最少的, 它几乎没有增加任何的运算量, 连新的网络都不用, 因为原来就 有两个网络了。你唯一要做的事情只有, 本来你在找 Q 值 最大的 a 的时候, 你是用 $\mathrm{Q}^{\prime}$ 来算, 你是用目标网络来 算, 现在改成用另外一个会更新的 Q-network 来算。

假如你今天只选一个 tip 的话, 正常人都是实现 Double DQN, 因为很容易实现。


[1]: https://github.com/zackchase/mxnet-the-straight-dope/blob/master/chapter17_deep-reinforcement-learning/DQN.ipynb
[2]: https://weread.qq.com/web/reader/da832f507192b327da81965kd6432e00228d645920e3401
[3]: https://github.com/shenweichen/ReinforcementLearning
[4]: https://blog.csdn.net/JohnJim0/article/details/111552545
[5]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter7/chapter7
