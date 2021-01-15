# 确定性策略梯度(Deterministic policy gradient)

## 背景

Atari 游戏所需的动作是离散的，且属于低维（只有少数几个动作），但现实生活中很多问题都是连续的，且维度比较高，比如机器人控制（多个自由度）、汽车方向盘转向角度，油门大小、天气预报推荐指数等。虽然可以对连续性高维度的动作做离散型的处理，但是对于一个经过离散处理的大状态空间，使用DQN训练仍然是仍然是一个比较棘手的问题，因为DQN算法的核心思想是利用随机策略进行探索，对于高维度的来说，第一个问题是：模型很难收敛，第二个问题是需要在探索和利用之间进行协调。[2]

## 从随机策略到确定性策略

从DDPG这个名字看, 它是由D (Deep) +D (Deterministic ) + PG(Policy Gradient)组成。PG(Policy Gradient)我们在强化学习(土三) 策略賺 度(Policy Gradient)里已经讨论过。那什么是确定性策略梯度(Deterministic Policy Gradient, 以下简称DPG)呢?
确定性策略是和随机策略相对而言的, 对于某一些动作集合来说, 它可能是连续值, 或者非常高维的离散值, 这样动作的空间维度极大。如果我们使用
随机策略, 即像DQN一样研究它所有的可能动作的概率, 并计算各个可能的动作的价值的话, 那需要的样本量是非常大才可行的。于是有人就想出使用确定性策
略来简化这个问题。
作为随机策略, 在相同的策略, 在同一个状态处, 采用的动作是基于一个概率分布的, 即是不确定的。而确定性策略则决定简单点, 虽然在同一个状态 处, 采用的动作概率不同, 但是最大概率只有一个, 如果我们只取最大概率的动作, 去掉这个概率分布, 那么就简单多了。即作为确定性策略, 相同的策略, 在 同一个状态处, 动作是唯一确定的, 即策略变成
$$
\pi_{\theta}(s)=a
$$
2
在看确定性策略梯度DPG前，我们看看基于Q值的随机性策略梯度的梯度计算公式:
$$
\nabla_{\theta} J\left(\pi_{\theta}\right)=E_{s \sim \rho^{\pi}, a \sim \pi_{\theta}}\left[\nabla_{\theta} \log \pi_{\theta}(s, a) Q_{\pi}(s, a)\right]
$$
其中状态的采样空间为 $\rho^{\pi}, \nabla_{\theta} \log \pi_{\theta}(s, a)$ 是分值函数, 可见随机性策略梯度需要在整个动作的空间 $\pi_{\theta}$ 进行采样。
而DPG基于Q值的确定性策略梯度的梯度计算公式是:
$$
\nabla_{\theta} J\left(\pi_{\theta}\right)=E_{s \sim \rho^{\pi}}\left[\left.\nabla_{\theta} \pi_{\theta}(s) \nabla_{a} Q_{\pi}(s, a)\right|_{a=\pi_{\theta}(s)}\right]
$$
跟随机策略梯度的式子相比, 少了对动作的积分, 多了回报Q函数对动作的导数。。。。
于现在我们本来就有Actor网络和Critic两个网络, 那么双网络后就变成了4个网络, 分别是: Actor当前网络, Actor目标网络, Critic当前网络, Critic目标区
络。2个Actor网络的结构相同, 2个Critic网络的结构相同。那么这4个网络的功能各自是什么呢?[3]


首先解决一个强化学习问题, 我们想到的就是累计折扣奖励的定义, 即状态满足 $\rho^{\pi}$ 分布上的累计奖 励，如下：
$$
\begin{aligned}
\nabla_{\theta} J\left(\pi_{\theta}\right)=& \int_{S} \rho^{\pi}(s) \int_{A} \pi_{\theta}(a \mid s) r(s, a) d a d s \\
&=E_{s \sim \rho^{\pi}, a \sim \pi_{\theta}}[r(s, a)]
\end{aligned}
$$
那么什么是策略梯度呢? 策略梯度就是沿着使目标函数变大的方向调整策略的参数，它被定义为：
$$
\begin{array}{c}
\nabla_{\theta} J\left(\pi_{\theta}\right)=\int_{S} \rho^{\pi}(s) \int_{A} \nabla_{\theta} \pi_{\theta}(a \mid s) Q^{\pi}(s, a) d a d s \\
=E_{s \sim \rho^{\pi}, a \sim \pi_{\theta}}\left[\nabla_{\theta} \log \pi_{\theta}(a \mid s) Q^{\pi}(s, a)\right]
\end{array}
$$

公式非常直白的告诉我们, J()函数主要与策略梯度和值函数的期望有关, 尽管状态空间分布 $\rho^{\pi}$ 的分布 依赖于策略参数, 但是策略梯度并不依赖于状态分布上的梯度。另外，在DQN中我们使用了评价网络 和target网络，采用了experimence replay的方式打乱了数据之间的相关性而使得满足独立同分布条 件，利用softupdating方式更新target网络，但总结一句话, 它的策略网路和值函数网络使用的是同一 个网络。在DPG的公式表明, $\mathrm{J}($ )和策略梯度与值函数有关， 因此为了解决策略和值函数之间的问题, 采用了一种新的解决思路将两个网络分开，即：Actor-critic异步框架。

## Actor-Critic框架

从框架的 名字我们就可以知道一些信息：Actor(演员)-Critic(评论家)框架，相当于演员和评论家共同来提升表演，演员跳舞的姿态可能动作不到位，于是评论家告诉演员，你这样跳舞不好，它会建议演员修改一下舞姿了，当演员在某个舞姿上表演的比较好，那评论家就会告诉演员, 不错，你可以加大力度往这个方向发展，是不是明白其中的意思了？
那么对应到RL中，Actor就是策略网络，来做动作选择(空间探索)。Critic就是值函数，对策略函数进行评估， 具体的流程如图：

![](img\A+C_env.png)


简单描述一下图：其中的TD-error就是Critic告诉Actor的偏差。。
具体的更新过程：
$$
\begin{array}{c}
\delta_{t}=r_{t}+\gamma Q^{w}\left(s_{t+1}, \mu_{\theta}\left(s_{t+1}\right)\right)-Q^{w}\left(s_{t}, a_{t}\right) \\
w_{t+1}=w_{t}+\alpha_{w} \delta_{t} \nabla_{w} Q^{w}\left(s_{t}, a_{t}\right) \\
\theta_{t+1}=\theta_{t}+\left.\alpha_{\theta} \mu_{\theta}\left(s_{t}\right) \nabla Q^{w}\left(s_{t}, a_{t}\right)\right|_{a=\mu_{\theta}(s)}
\end{array}{c}
$$
我们现在考虑如何将策略梯度框架扩展到确定性政策。我们的主要结果是一个确定性的策略梯度定理, 类似于上一节中介绍的随机政策梯度定理。 我们在确定性政策梯度的形式背后提供一种非正式的 直觉。 然后，我们从第一原则给出确定性政策梯度定理的形式证明。最后，我们证明确定性政策梯 度定理实际上是随机政策梯度定理的一个极限情况（具体的证明见论文附录）)
那么极限情况是舍呢？ 就是当概率策略的方差趋近于0的时候, 就是确定性策略,即
$$
\begin{aligned}
\nabla_{\theta} J\left(\mu_{\theta}\right) &=\left.\int_{S} \rho^{\mu}(s) \nabla_{\theta} \mu_{\theta}(s) \nabla_{a} Q^{\mu}(s, a)\right|_{a=\mu_{\theta}(s)} d s \\
=& E_{s \sim \rho^{\mu}}\left[\left.\nabla_{\theta} \mu_{\theta}(s) \nabla Q^{\mu}(s, a)\right|_{a=\mu_{\theta}(s)}\right]
\end{aligned}
$$

公式推到依据： 对于连续性变量, 期望通过积分求得：
$$
E_{x \sim P}[f(x)]=\int p(x) f(x) d x
$$

## 兼容函数近似

一般而言, 将近似$Q^{w}(s, a)$ 代入确定性政策梯度并不一定会遵循真正的梯度 $($ 事实上它也不一定是上 升方向) 。 类似于随机情况, 我们现在找到一类兼容函数逼近器 $Q^{w}(s, a)$ 使得真正的梯度被保留。 换句话说, 我们找到了 critic $Q^{w}\left(s, a,\right.$ 使得梯度 $\nabla_{a} Q^{\mu}(s, a)$ 可以用 $\nabla_{a} Q^{w}(s, a)$ 替代, 而不会影响 确定性政策梯度。 以下定理适用于on-policy $E[\cdot]=E_{s \sim \rho^{\mu}}[\cdot]$ 和off-policy政策, $E[\cdot]=E_{s \sim \rho^{\beta}}[\cdot]$,

Theorem 3. A function approximator $Q^{w}(s, a)$ is compatible with a deterministic policy $\mu_{\theta}(s), \nabla_{\theta} J_{\beta}(\theta)=$ $\mathbb{E}\left[\left.\nabla_{\theta} \mu_{\theta}(s) \nabla_{a} Q^{w}(s, a)\right|_{a=\mu_{\theta}(s)}\right],$ if
1. $\left.\nabla_{a} Q^{w}(s, a)\right|_{a=\mu_{\theta}(s)}=\nabla_{\theta} \mu_{\theta}(s)^{\top} w \quad$ and
2. $w$ minimises the mean-squared error, $\operatorname{MSE}(\theta, w)=$ $\mathbb{E}\left[\epsilon(s ; \theta, w)^{\top} \epsilon(s ; \theta, w)\right] \quad$ where $\quad \epsilon(s ; \theta, w) \quad=$
$$
\left.\nabla_{a} Q^{w}(s, a)\right|_{a=\mu_{\theta}(s)}-\left.\nabla_{a} Q^{\mu}(s, a)\right|_{a=\mu_{\theta}(s)}
$$
总结一下:
回顾前文的内容, 我们知道广义的值函数求解包括策略评估和策略改善, 当值函数最优的俄时候, 策 略也是最优的 (此处的策略是贪妥策略)，而策略搜索是将策略参数化, 即 $\pi_{\theta}(s),$ 因此, 我们可以使 用参数化或者非参数化(神经网路) 逼近策略, 找到最优的 $\theta$, 使得累计折扣奖励最大化。确定性策略梯 度就是在确定的梯度策略方向上进行学习。。。

[2]: https://blog.csdn.net/gsww404/article/details/80403150
[3]: https://www.cnblogs.com/pinard/p/10345762.html
