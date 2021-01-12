# 逆增强学习

我们做增强学习的时候都是对特定任务来手工定义收益函数的思路来完成任务。但是要真正实现稍微智能化的目标，我们更倾向于在不知道具体任务的时候，去观察专家的行为然后推测他想干什么，也就是学习他的收益函数，然后再使用增强学习算法，这也称为逆增强学习。

## 收益函数

自动驾驶等复杂问题在人工设置的收益函数里面也很难刻画。这些的特点是，相对手工来做一个收益函数，由人来介绍怎么做会比较容易。


## VS 模仿学习

模仿学习（行为克隆），也就是直接模仿专家的行为而不需要理解其中原因。这也是实践中的一个备选项，在有些时候也能满足要求，尤其是观测数据很多，且域漂移 (domain shift) 比较小的情况


因为在逆增强学习问题中，我们要尝试去改进收益函数，然而去评估收益函数的时候，我们要求解类似梯度的东西，这其实是正增强学习问题要做的事情，因此有点类似于正增强学习是逆增强学习内循环中的子问题，在样本使用和计算上都很困难。

## 最大熵逆增强学习 (MaxEnt IRL)

1. 给定 $\psi$, 按照上一篇的方法求出对应的 $\beta\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)$ 和 $\alpha\left(\mathbf{s}_{t}\right)$ 。
2. 计算访问概率 $\mu_{t}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \propto \beta_{t}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \alpha_{t}\left(\mathbf{s}_{t}\right)$ 。
3. 求解梯度 $\nabla_{\psi} \mathcal{L}=\frac{1}{N} \sum_{i=1}^{N} \sum_{t=1}^{T} \nabla_{\psi} r_{\psi}\left(\mathbf{s}_{i, t}, \mathbf{a}_{i, t}\right)-\sum_{t=1}^{T} \iint \mu_{t}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \nabla_{\psi} r_{\psi}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \mathrm{d} \mathbf{s}_{t} \mathrm{~d} \mathbf{a}_{t}$
4. 走一个梯度步 $\psi \leftarrow \psi+\eta \nabla_{\psi} \mathcal{L}$ 。

这个是表格形式的最大嫡逆增强学习的算法。该思想由Ziebart et al. (2008) 发表在AAAI上 的"Maximum Entropy Inverse Reinforcement Learning"提出。之所以称为最大嫡, 因为原理 其实与上一篇中的嫡正则化类似。我们可以说明如果我们的 $r_{\psi}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)=\psi^{\top} \mathbf{f}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)$ 是这样的线性形式, 那么其实这样的算法是在最优化 $\max _{\psi} \mathcal{H}\left(\pi^{r} \psi\right)$ s.t. $\mathbf{E}_{\pi^{\prime} \psi}[\mathbf{f}]=\mathbf{E}_{\pi^{*}}[\mathbf{f}],$ 在保证学习的策略的特征和专家策略特征一致的基础上使得策略的嫡最大。。

## Maximum Entropy Deep Inverse Reinforcement Learning

Wulfmeier et al. (2015) 的"Maximum Entropy Deep Inverse Reinforcement Learning"及其应用，Wulfmeier et al. (2016) 发表在IROS上的"Watch This: Scalable Cost-Function Learning for Path Planning in Urban Environments"也使用了类似的方法，还是使用了表格的形式，但是收益函数的设置更复杂，是一个用神经网络来对若干人工特征进行非线性组合的形式，算法本质上和最大熵逆增强学习没有区别，只是需要用神经网络来计算收益，最后需要用梯度去更新的也是神经网络。注意这个问题中状态空间只是一个二维平面，行动空间是离散的方向。该方法的主要局限性是仍然需要迭代求解MDP，而且还需要假设系统动态是已知的。

Algorithm 1 Maximum Entropy Deep IRL
Input: $\mu_{D}^{a}, f, S, A, T, \gamma$
Output: optimal weights $\theta^{*}$
$1: \theta^{1}=$ initialise_weights ()
Iterative model refinement
2: for $\mathrm{n}=1: \mathrm{N}$ do
3: $\quad r^{n}=$ nn_forward $\left(f, \theta^{n}\right)$
Solution of MDP with current reward
4: $\quad \pi^{n}=$ approx_value_iteration $\left(r^{n}, S, A, T, \gamma\right)$
5: $\quad \mathbb{E}\left[\mu^{n}\right]=$ propagate_policy $\left(\pi^{n}, S, A, T\right)$
Determine Maximum Entropy loss and gradients
6: $\quad \mathcal{L}_{D}^{n}=\log \left(\pi^{n}\right) \times \mu_{D}^{a}$
7: $\quad \frac{\partial \mathcal{L}_{D}^{n}}{\partial r^{n}}=\mu_{D}-\mathbb{E}\left[\mu^{n}\right]$
Compute network gradients
8: $\quad \frac{\partial \mathcal{L}_{D}^{n}}{\partial \theta_{D}^{n}}=$ nn_backprop $\left(f, \theta^{n}, \frac{\partial \mathcal{L}_{D}^{n}}{\partial r^{n}}\right)$
9: $\quad \theta^{n+1}=$ update_weights $\left(\theta^{n}, \frac{\partial \mathcal{L}_{D}^{n}}{\partial \theta_{D}^{n}}\right)$
10: end for

## 深度逆增强学习

要处理深度逆增强学习问题，我们希望能适应离散较大的甚至是连续的状态行动空间，而且我们需要对系统动态未知的情况下做有效的学习。

假设我们不知道系统动态，但可以像普通增强学习一样抽样。

注意到我们前面对数似然函数的梯度 $\nabla_{\psi} \mathcal{L}=\mathbf{E}_{\tau \sim \pi^{*}(\tau)}\left[\nabla_{\psi} r_{\psi}(\tau)\right]-\mathbf{E}_{\tau \sim p\left(\tau \mid \mathcal{O}_{1: T, \psi}\right)}\left[\nabla_{\psi} r_{\psi}(\tau)\right],$ 前者是专家样本数据中得到的, 后者是当前收益函数对应最优策略下的。

要做到后者, 一个比较直接的想法是使用任何最大嫡增强学习方法学习出策略 $p\left(\mathbf{a}_{t} \mid \mathbf{s}_{t}, \mathcal{O}_{1: T}, \psi\right),$ 然后根据这个策略来采集 $\left\{\tau_{j}\right\}$ 。此时，就用专家样本的结果减掉新抽 样本的结果, $\nabla_{\psi} \mathcal{L} \approx \frac{1}{N} \sum_{i=1}^{N} \nabla_{\psi} r_{\psi}\left(\tau_{i}\right)-\frac{1}{M} \sum_{j=1}^{M} \nabla_{\psi} r_{\psi}\left(\tau_{j}\right)$ 来做无偏估计。

然而事实上这种学习的做法是代价很高的, 因为我们不假定有模型, 所以可能要用无模型的增强学习算法, 这将使得每一 步都花掉很多很多时间。这里我们可以采用一些小技巧，我们可以不用完全地把对应的最优策略学 出来，而只是每次把策略改进一点点, 然后用这个不准确的策略去近似估计梯度。然而现在多出来 个问题, 由于我们使用的策略是不正确的 (不是最优的策略)， 因此我们的估计量将不再无偏。

对于分布错误的问题, 一个有力武器是重要性抽样（我们在策略梯度法部分有过介绍 $) ，$ 用其他分 布下抽样结果来得到正确分布下的无偏估计： $\nabla_{\psi} \mathcal{L} \approx \frac{1}{N} \sum_{i=1}^{N} \nabla_{\psi} r_{\psi}\left(\tau_{i}\right)-\frac{1}{\sum_{j} w_{j}} \sum_{j=1}^{M} w_{j} \nabla_{\psi} r_{\psi}\left(\tau_{j}\right)$
其中权重为 $w_{j}=\frac{p\left(\tau_{j}\right) \exp \left(r_{\psi}\left(\tau_{j}\right)\right)}{\pi\left(\tau_{j}\right)},$ 分子正比于收益的指数（我觉得Levine教授原文
$w_{j}=\frac{\exp \left(r_{\psi}\left(\tau_{j}\right)\right)}{\pi\left(\tau_{j}\right)}$ 少了一个概率, 无法推导成下面的形式, 或者是可能它的定义和我上面说的不同了，请评论区大神帮忙研究下)， 分母是现在分布的概率。

因为我们前面会除以权重之和, 就不需要关注 $w_{j}$ 归一化的问题。使用之前策略梯度法一样的展开，对同一条 $\tau_{j},$ 我们得到 $w_{j}=\frac{p\left(\mathbf{s}_{1}\right) \prod_{t} p\left(\mathbf{s}_{t+1} \mid \mathbf{s}_{t}, \mathbf{a}_{t}\right) \exp \left(r_{\psi}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)\right)}{p\left(\mathbf{s}_{1}\right) \prod_{t} p\left(\mathbf{s}_{t-1} \mid \mathbf{s}_{t}, \mathbf{a}_{t}\right) \pi\left(\mathbf{a}_{t} \mid \mathbf{s}_{t}\right)}=\frac{\exp \left(\sum_{t} r_{\psi}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)\right)}{\prod_{t} \pi\left(\mathbf{a}_{t} \mid \mathbf{s}_{t}\right)}$ 这样比较简单的形式。

进一步，最优下 $\pi(\tau) \propto p(\tau) \exp \left(r_{\psi}(\tau)\right),$ 无需做IS。每一步策略迭代都使我们更接近最优分布，因此事实 上是在逐步改进的。。


### 引导代价学习 (guided cost learning)

Finn et al. (2016) 发表在ICML上的文章"Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization" 提出了引导代价学习 (guided cost learning) 算法。需要给定一些人工的示范，然后算法从一个随机的策略[公式] 开始，通过运行策略[公式]去生成随机样本，然后使用重要性抽样和人工示范的方式来更新收益函数，根据收益函数稍微更新一下分布，然后下一阶段的分布更好。最后，我们得到了最终的类似于专家的收益函数和对应的策略。事实上，这个文章中使用了基于模型的算法中的GPS算法来做策略更新，然而事实上任何改进策略的方法应当都是适用的。她们的文章中使用这样的方法来“教”机器人完成人工动手的操作如摆放盘子和往目标杯子里倒水。这项工作相对更早期的逆增强学习算法，如Kalakrishnan et al. (2013) "Learning Objective Functions for Manipulation" 的路径积分IRL (path integral IRL) 和Boularias et al. (2011) "Relative Entropy Inverse Reinforcement Learning" 的相对熵IRL (relative entropy IRL) 的思路的改进主要在于，早期的算法虽然使用了重要性抽样，但是没有下面的那个箭头，没有对策略进行更新，也因此只得到收益函数而不产生最终的策略。但是早期算法如果在初始分布不错的情况下（要求可能较高），也是可以得到一些不错效果的。她们比较了手工设计的收益函数，相对熵IRL和GCL算法的效果。

事实上，很可能我们得到的收益函数不是一个很好的收益函数，但是往往这个策略函数反倒还可以。

## 与生成对抗网络 (GAN) 的联系

IRL是从专家示范中推断出未知收益函数的手段， 一类比较好用的IRL算法是最大熵IRL，相对类似超平面分割的方法来说可以消除歧义，也解决了人类示范可能不是最优这种情况。

Finn et al. (2016) 发表于NIPS的文章 "A Connection between Generative Adversarial Networks, Inverse Reinforcement Learning, and Energy-Based Models" 进行一个对比，IRL中的轨迹对应着GAN中的样本，IRL中的策略对应着GAN中的生成器（生成轨迹和样本），而IRL收益函数则对应了GAN中的判别器。





## 基于能量的模型 (energy-based models, EBM) 的联系

事实上它和GCL是差不多的，只是GCL的D是一个给定的函数形式，而这边D是一个二分类器（因此该算法不是IRL，但是非常像），总体来说两个算法都是GAN的变种。

## 总结

IRL是从专家示范中推断出未知收益函数的手段， 一类比较好用的IRL算法是最大熵IRL，相对类似超平面分割的方法来说可以消除歧义，也解决了人类示范可能不是最优这种情况。这类算法可以用表格动态规划来实现，比较简单有效，但是只有在状态行动空间较小，动态已知的情况下才能应用。有一类微分最大熵IRL这边没有涉及，它适合于大而连续的空间，但需要知道系统动态。我们这里讲的深度IRL使用的是基于样本的最大熵IRL，可以用于连续空间，可以不假设有模型存在，较广泛。它的实现可以用GCL算法，该算法与GAN也有很深的渊源，和它紧密相关的还有生成对抗模仿学习算法（但不是IRL，不推测收益函数）。


[1]: https://zhuanlan.zhihu.com/p/33663492

事实上, 可以令GAN的判别器取决于收益的方式来完成类似的目标。假设一个轨迹在专家（数据）分布下的概率是 $p(\tau),$ 当前策略下的概率是 $q(\tau),$ 最优判别器应该为 $D^{*}(\tau)=\frac{p(\tau)}{p(\tau)+q(\tau)}$ 。 在IRL中，我们假设专家分布下的概率是 $\frac{1}{Z} \exp \left(R_{\psi}\right),$ 从而 $D_{\psi}(\tau)=\frac{\frac{1}{Z} \exp \left(R_{\psi}\right)}{\frac{1}{Z} \exp \left(R_{\psi}\right)+q(\tau)}$ 。我们的判
别器要最小化损失函数 (reward/discriminator optimizaion) $\mathcal{L}_{\text {discriminator }}(\psi)=\mathbf{E}_{\tau \sim p}\left[-\log D_{\psi}(\tau)\right]+\mathbf{E}_{\tau \sim q}\left[-\log \left(1-D_{\psi}(\tau)\right)\right],$ 简单说就是使得对应分布下的似然最大，这也是IRL的目标函数。

我们的生成器要最小化损失函数 (policy/generator optimization) $\mathcal{L}_{\text {generator }}(\theta)=\mathbf{E}_{\tau \sim q}\left[\log \left(1-D_{\psi}(\tau)\right)-\log D_{\psi}(\tau)\right]=\mathbf{E}_{\tau \sim q}\left[\log q(\tau)+\log Z-R_{\psi}(\tau)\right]$
使得在当前分布下判别器尽可能分不清, 这个结论和上篇中的嫡正则化的增强学习的结论是很相 似的。对于未知的系统动态，我们交替进行策略更新来最大化收益函数，然后进行收益更新来提高 样本收益且降低当前策略收益, 也是类似这样的过程。GCL算法中，机器人尝试的收益函数是要去 最小化的, 人类示范的收益函数是要去最大化的，去尝试学习最大嫡模型的分布 $p(\tau) \propto \exp (r(\tau))$ 此外, 一个有趣的交汇是, IRL也和基于能量的模型 (energy-based models, EBM) 很有关系。
Ho and Ermon (2016) 发表在NIPS上的 "Generative adversarial imitation learning" 一文将
一个二分类器来表示轨迹是一个正样本的概率, 并使用 $\log D(\tau)$ 作为收益函数。事实上它和GCL是 差不多的, 只是GCL的D是一个给定的函数形式, 而这边D是一个二分类器（因此该算法不是IRL, 但是非常像 $) ，$ 总体来说两个算法都是GAN的变种。。
