# Twin Delayed DDPG(TD3)

## 动机

虽然 DDPG 有时表现很好，但它在超参数和其他类型的调整方面经常很敏感。DDPG 常见的问题是已经学习好的 Q 函数开始显著地高估 Q 值，然后导致策略被破坏了，因为它利用了 Q 函数中的误差。

我们可以拿实际的 Q 值跟这个 Q-network 输出的 Q 值进行对比。实际的 Q 值可以用 MC 来算。根据当前的 policy 采样 1000 条轨迹，得到 G 后取平均，得到实际的 Q 值。

## 关键技巧

- 截断的双 Q 学习(Clipped Dobule Q-learning) 。 TD3 学
习两个 Q-function (因此名字中有“twin”) 。 TD3 通过
最小化均方差来同时学习两个 Q-function：Q $_{\phi_{1}}$ 和 $\mathrm{Q}_{\phi_{2}}$ 两个 $\mathrm{Q}$ -function 都使用一个目标, 两个 $\mathrm{Q}-$ function 中给出较小的值会被作为如下的 Q-target:
$$
\mathrm{y}\left(\mathrm{r}, \mathrm{s}^{\prime}, \mathrm{d}\right)=\mathrm{r}+\gamma(1-\mathrm{d}) \min _{\mathrm{i}=1,2} \mathrm{Q}_{\phi_{\mathrm{i}, \text { targ }}}\left(\mathrm{s}^{\prime}, \mathrm{a}_{\mathrm{TD} 3}\left(\mathrm{~s}^{\prime}\right)\right)
$$
- 延迟的策略更新(“Delayed" Policy Updates) $^{\star \star}$ 。相关 实验结果表明, 同步训练动作网络和评价网络, 却不 使用目标网络, 会导致训练过程不稳定; 但是仅固定
动作网络时，评价网络往往能句收玫到正确的结果。 因此 TD3 算法以较低的频率更新动作网络，较高频率 更新评价网络, 通常每更新两次评价网络就更新一次
策略。
- 目标策略平滑(Target Policy smoothing)  TD3 引入 了 smoothing 的思想。TD3 在目标动作中加入噪音, 通过平滑 Q 沿动作的变化, 使策略更难利用 Q 函数的误差

目标策略平滑化的工作原理如下：
$$
\mathrm{a}_{\mathrm{TD} 3}\left(\mathrm{~s}^{\prime}\right)=\operatorname{clip}\left(\mu_{\theta, \operatorname{targ}}\left(\mathrm{s}^{\prime}\right)+\operatorname{clip}(\epsilon,-\mathrm{c}, \mathrm{c}), \mathrm{a}_{\mathrm{low}}, \mathrm{a}_{\mathrm{high}}\right)
$$
其中 $\epsilon$ 本质上是一个噪声， 是从正态分布中取样得到的, 即 $\epsilon \sim \mathrm{N}(0, \sigma)$



[1]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter12/chapter12?id=exploration-vs-exploitation
