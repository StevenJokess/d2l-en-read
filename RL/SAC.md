

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

## 最大熵

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

## Maximum Entropy Reinforcement Learning的Bellman方程

Dynamic Programming中Bellman backup equation


$$
q_{\pi}(s, a)=r(s, a)+\gamma \sum_{s^{\prime} \in \mathcal{S}} \mathcal{P}_{s s^{\prime}}^{a} \sum_{a^{\prime} \in \mathcal{A}} \pi\left(a^{\prime} \mid s^{\prime}\right) q_{\pi}\left(s^{\prime}, a^{\prime}\right)
$$

### Policy Iteration


SAC基于最大熵强化学习（Maximum Entropy Reinforcement learning） 框架，

其中的熵增目标函数如下所示：[2]

$J(\pi)=\mathbb{E}_{\pi}\left[\sum_{t} r\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)-\alpha \log \left(\pi\left(\mathbf{a}_{t} \mid \mathbf{s}_{t}\right)\right)\right]$
$$
\begin{array}{l}
\text { Algorithm 1 Soft Actor-Critic } \\
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
