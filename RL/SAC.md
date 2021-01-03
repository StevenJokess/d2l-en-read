

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 23:08:08
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 00:39:53
 * @Description:
 * @TODO::
 * @Reference:https://spinningup.openai.com/en/latest/algorithms/sac.html
-->

# Soft Actor-Critic

是一种基于off-policy和最大熵的深度强化学习算法，并使用的是随机策略stochastic policy，其由伯克利和谷歌大脑的研究人员提出。作为目前高效的model-free算法，SAC是深度强化学习中对于连续动作控制的又一经典algorithm，十分适用于真实世界中的机器人任务学习。

和DDPG相比，Soft Actor-Critic使用的是随机策略stochastic policy，相比确定性策略具有一定的优势（具体后面分析）

## Energy-Based Model(EBM)

对于∀x,p(x)>0这样的假设，EBM表示为：

$\tilde{p}(\mathbf{x})=\exp (-E(\mathbf{x}))$

E(x)被称作是能量函数（energy function）。对所有的z，exp(z)都是正的，这保证了没有一个能量函数会使得某一个状态x的概率为0。基于EBM的策略正是利用这种特性来定义新的策略：

我们可以将能量函数定义为Q函数的负数：

$$
E(X)=-\frac{1}{\alpha} Q_{\text {soft}}^{\pi}\left(s_{t}, a_{t}\right)
$$
其中 $\alpha$ 为用于控制探索程度的参数，策略表示为：
$$
\pi\left(a_{t} \mid s_{t}\right) \propto \exp \left(\frac{1}{\alpha} Q_{\text {soft}}^{\pi}\left(s_{t}, a_{t}\right)\right)
$$
具体的：
$$
\pi\left(a_{t} \mid s_{t}\right)=\frac{\exp \left(\frac{1}{\alpha} Q_{\text {soft}}^{\pi}\left(s_{t}, a_{t}\right)\right)}{\int \exp \left(\frac{1}{\alpha} Q_{\text {soft}}^{\pi}\left(s_{t}, a\right)\right) d a}
$$
其中：
$$
\int \exp \left(\frac{1}{\alpha} Q_{\text {soft}}^{\pi}\left(s_{t}, a\right)\right) d a
$$
我们称作配分函数 $Z^{\pi}\left(s_{t}\right),$ 它是仅与状态s有关的常数。
所以:
$$
\pi\left(s_{t} \mid a_{t}\right)=\exp \left(\frac{1}{\alpha} Q_{\text {soft}}^{\pi}\left(s_{t}, a_{t}\right)-\log Z^{\pi}\left(s_{t}\right)\right)
$$


推到这一步，我们发现，Energy-Based策略的基于KL散度的优化方向实际上就是在优化最大熵RL的目标（

是仅和状态有关的常数，与优化目标无关）——使得每个状态的奖励和该状态下动作的熵最大化。那什么是最大熵RL？最大熵RL起什么作用？


## 最大熵


$P_{w}(y \mid x)=\frac{1}{Z_{w}(x)} \exp \left(\sum_{i=1}^{n} w_{i} \cdot f_{i}(x, y)\right)$[5]

### 目的

对于一般的DRL，学习目标很直接，就是学习一个policy使得累加的reward期望值最大：

$$
\pi^{*}=\arg \max _{\pi} \mathbb{E}_{\left(s_{t}, a_{t}\right) \sim \rho_{\pi}}\left[\sum_{t} R\left(s_{t}, a_{t}\right)\right]
$$

而最大熵RL，除了上面的基本目标，还要求policy的每一次输出的action 熵entropy最大：

$$
\pi^{*}=\arg \max _{\pi} \mathbb{E}_{\left(s_{t}, a_{t}\right) \sim \rho_{\pi}}[\sum_{t} \underbrace{R\left(s_{t}, a_{t}\right)}_{\text {reward }}+\alpha \underbrace{H\left(\pi\left(\cdot \mid s_{t}\right)\right)}_{\text {entropy }}]
$$

### Stochastic policy随机策略

我们知道DDPG训练得到的是一个deterministic policy确定性策略，也就是说这个策略对于一种状态state只考虑一个最优的动作。所以，stochastic policy相对deterministic policy有什么优势呢？

基本目的是什么呢？让策略随机化，即输出的每一个action的概率尽可能分散，而不是集中在一个action上。

最大熵maximum entropy的核心思想就是不遗落到任意一个有用的action，有用的trajectory。

### 基于最大熵的RL算法有什么优势？

以前用deterministic policy的算法，我们找到了一条最优路径，学习过程也就结束了。现在，我们还要求熵最大，就意味着神经网络需要去explore探索所有可能的最优路径，这可以产生以下多种优势：

1. 学到policy可以作为更复杂具体任务的初始化。因为通过最大熵，policy不仅仅学到一种解决任务的方法，而是所有all。因此这样的policy就更有利于去学习新的任务。比如我们一开始是学走，然后之后要学朝某一个特定方向走。
2. 更强的exploration能力，这是显而易见的，能够更容易的在多模态reward （multimodal reward）下找到更好的模式。比如既要求机器人走的好，又要求机器人节约能源
3. 更robust鲁棒，更强的generalization。因为要从不同的方式来探索各种最优的可能性，也因此面对干扰的时候能够更容易做出调整。（干扰会是神经网络学习过程中看到的一种state，既然已经探索到了，学到了就可以更好的做出反应，继续获取高reward）

### 例子

传统的基于Q-learning 的强化学习的策略比如DDPG等会选择Q值最大的action，再加上exploration noise构成一个高斯分布，如图A2的红色曲线部分。这样的策略是single modal
，而原来的Q函数的分布是multimodal。传统Q-learning对应的策略无法表达这种multimodal ，进而在测试中如果遇到B1图所示的障碍时候，智能体会一直选择向上的那条路径，无法到达目的

![引入](img\SAC_yin.png)

## Maximum Entropy Reinforcement Learning的Bellman方程

Dynamic Programming中Bellman backup equation


$$
q_{\pi}(s, a)=r(s, a)+\gamma \sum_{s^{\prime} \in \mathcal{S}} \mathcal{P}_{s s^{\prime}}^{a} \sum_{a^{\prime} \in \mathcal{A}} \pi\left(a^{\prime} \mid s^{\prime}\right) q_{\pi}\left(s^{\prime}, a^{\prime}\right)
$$

### Policy Iteration


SAC基于最大熵强化学习（Maximum Entropy Reinforcement learning） 框架，

其中的熵增目标函数如下所示：[2]

$J(\pi)=\mathbb{E}_{\pi}\left[\sum_{t} r\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)-\alpha \log \left(\pi\left(\mathbf{a}_{t} \mid \mathbf{s}_{t}\right)\right)\right]$

## 简介

SAC同样基于最大嫡框架，策略基于EBM。
$$
\pi^{*}=\arg \max _{\pi} \sum \mathbb{E}_{\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \sim \rho_{\pi}}\left[r\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)+\alpha \mathcal{H}\left(\pi\left(\cdot \mid \mathbf{s}_{t}\right)\right)\right]
$$
最大嫡框架是在奖励中加入了entropy项，传统的V函数可以据此改为：
$$
\begin{aligned}
V_{s_{t}} &=E_{a_{t} \sim \pi}\left[Q\left(s_{t}, a_{t}\right)\right]+\alpha H\left(\pi\left(\bullet \mid s_{t}\right)\right.\\
&=E_{a_{i} \sim \pi}\left[Q\left(s_{t}, a_{t}\right)-\alpha \log \left(\pi\left(a_{t} \mid s_{t}\right)\right)\right]
\end{aligned}
$$
依据贝尔曼期望方程, $Q$ 函数为：
$$
Q\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \triangleq r\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)+\gamma \mathbb{E}_{\mathbf{s}_{t+1} \sim p}\left[V\left(\mathbf{s}_{t+1}\right)\right]
$$


## 优化

SAC用含参函数 $Q(\theta)$ 和 $\pi(\varphi)$ 来分别近似近似 $Q$ 函数和策略。特别的对于 $Q$ 函数，采用了双 重Q学习类似的技术以及目标网络, 引入两套更新的参数 $\theta_{1}, \theta_{2},$ 以及 $\theta_{1}, \theta_{2}$ 对应的目标网
络参数 $\overline{\theta_{1}}, \overline{\theta_{2}}$ 。为了消除 最大偏差，在估计目标是选取 $Q$ 值中较小的那个，即 $\min _{i=0,1} Q\left(s, a ; \theta_{i}\right)$
在学习 $Q\left(s, a ; \theta_{i}\right)(i=0,1)$ 时，试图最小化：
$$
J_{Q}(\theta)=\mathbb{E}_{\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \sim \mathcal{D}}\left[\frac{1}{2}\left(Q_{\theta}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)-\left(r\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)+\gamma \mathbb{E}_{\mathbf{s}_{t+1} \sim p}\left[V_{\bar{\theta}}\left(\mathbf{s}_{t+1}\right)\right]\right)\right)^{2}\right]
$$
在学习 $\pi(\varphi)$ 时， 试图最小化:
$$
J_{\pi}(\varphi)=E_{s_{t} \sim D}\left[E_{a_{t} \sim \pi_{\varphi}}\left[\alpha \log \left(\pi_{\varphi}\left(a_{t} \mid s_{t}\right)\right)-Q_{\theta}\left(s_{t}, a_{t}\right)\right]\right]
$$
值得一提的是，在策略优化时采用的是reparameterize技巧，即：
$$
\mathbf{a}_{t}=f_{\phi}\left(\epsilon_{t} ; \mathbf{s}_{t}\right)
$$
其中 $\epsilon_{t}$ 是噪声，可以自标准正态分布采样得到。
而这篇工作最大的创新点来自自动化调节 $\alpha,$ 在学习时试图优化： $J\left(\alpha_{t}\right)=E_{a_{t} \sim \pi}\left[-\alpha_{t} \log \left(\pi_{t}\left(a_{t} \mid s_{t} ; \alpha_{t}\right)\right)-\alpha_{t} \bar{H}\right]$
其中 $\bar{H}=-\operatorname{dim}(A)$


## 伪代码

$$
\begin{array}{l}
\text { Algorithm:  Soft Actor-Critic } \\
\hline \text { Initialize parameter vectors } \psi, \bar{\psi}, \theta, \phi . \\
\text { for each iteration do } \\
\qquad \begin{array}{l}
\text { for each environment step do } \\
\qquad \begin{array}{l}
\mathbf{a}_{t} \sim \pi_{\phi}\left(\mathbf{a}_{t} \mid \mathbf{s}_{t}\right) \\
\mathbf{s}_{t+1} \sim p\left(\mathbf{s}_{t+1} \mid \mathbf{s}_{t}, \mathbf{a}_{t}\right) \\
\mathcal{D} \leftarrow \mathcal{D} \cup\left\{\left(\mathbf{s}_{t}, \mathbf{a}_{t}, r\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right), \mathbf{s}(+1)\right\}\right. \\
\end{array} \\
\text { end for } \\
\end{array} \\
\qquad \begin{array}{l}
\text { for each gradient step do } \\
\qquad \begin{array}{l}
\psi \leftarrow \psi-\lambda_{V} \hat{\nabla}_{\psi} J_{V}(\psi)\text { (更新V值函数) }
 \\
\theta_{i} \leftarrow \theta_{i}-\lambda_{Q} \hat{\nabla}_{\theta_{i}} J_{Q}\left(\theta_{i}\right) \text { for } i \in\{1,2\} \text { (更新Q值函数) } \\
\phi \leftarrow \phi-\lambda_{\pi} \hat{\nabla}_{\phi} J_{\pi}(\phi) \text { (更新策略) } \\
\bar{\psi} \leftarrow \tau \psi+(1-\tau) \bar{\psi} \text { (目标网络软更新) }\\
\end{array} \\
\text { end for } \\
\end{array} \\
\text { end for } \\
\end{array}
$$

SAC模型同时学习action value Q、state value V和policy π。V中引入Target V，供Q学习时使用；Target Network使学习有章可循、效率更高。Q有两个单独的网络，选取最小值供V和π学习时使用，希望减弱Q的过高估计。π学习的是分布的参数：均值和标准差；这与DDPG不同，DDPG的π是Deterministic的，输出直接就是action，而SAC学习的是个分布，学习时action需要从分布中采样，是Stochastic的。

SAC concurrently learns a policy $\pi_{\theta}$ and two Q-functions $Q_{\phi_1}$, $Q_{\phi_2}$. There are two variants of SAC that are currently standard: one that uses a fixed entropy regularization coefficient \alpha, and another that enforces an entropy constraint by varying \alpha over the course of training. For simplicity, Spinning Up makes use of the version with a fixed entropy regularization coefficient, but the entropy-constrained variant is generally preferred by practitioners.





The SAC algorithm has changed a little bit over time. An older version of SAC also learns a value function V_{\psi} in addition to the Q-functions; this page will focus on the modern version that omits the extra value function.

构建首先是神经网络化，我们用神经网络来表示Q和Policy：  和  。Q网络比较简单，几层的MLP最后输出一个单值表示Q就可以了，Policy网络需要输出一个分布，一般是输出一个Gaussian 包含mean和covariance。[3]

SAC的关键是引入最大熵，优化soft value。最大熵会使action探索能力很强，模型效果更平稳，但注意需要场景也是接受较强的探索。从结构上讲，SAC模型冗余，在学习π和soft Q的情况下，又学习了soft V。由于面临的是连续动作空间，求期望的地方，采取了采样近似，需要批次处理的数据集更加完整。优化技巧比较晦涩，感觉很难通用。




[MinitaurBulletEnv with SAC (Soft-Actor-Critic).](https://www.youtube.com/watch?v=uEAqyEwvi54)
Considered solved if the achieved score exceeds 15 in 100 consecutive episodes. Solved in 1745 episodes (trained for 20 hours).

https://github.com/higgsfield/RL-Adventure-2/blob/master/7.soft%20actor-critic.ipynb



[2]: https://www.huaweicloud.com/articles/1d0333fd58123a05695ddcc8b4532c86.html#
[3]: https://zhuanlan.zhihu.com/p/70360272
[4]: https://github.com/AIfeng333/Soft-Reinforcement-learning
[5]: https://github.com/applenob/machine_learning_basic/blob/master/13_graph.ipynb
