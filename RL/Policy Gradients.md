

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:03:50
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 01:58:51
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/99679223
 * https://github.com/bentrevett/pytorch-rl
 * https://github.com/dalmia/David-Silver-Reinforcement-learning/tree/master/Week%207%20-%20Policy%20Gradient%20Methods
 * https://github.com/applenob/rl_learn/blob/master/class_note.ipynb
-->

# Policy Gradients

Policy Gradients的是一种基于策略的强化学习方法，基于策略的意思就是直接根据状态输出动作或者动作的概率。



我们使用神经网络输入当前的状态，网络就可以输出我们在这个状态下采取每个动作的概率。
与之前的DQN和Q-Learning这类基于价值的学习方法相比，二者的主要不同为：
1、基于价值的强化学习方法对应的最优策略通常是确定性策略，一般是从众多行为价值中选择一个最大价值的行为，仅有一定的概率会随机选择，而有些问题的最优策略却是随机策略，无法通过基于价值的学习方法求解。此时Policy Gradients可以起到很好的作用。
2、DQN之类的方法一般都是只处理离散动作，无法处理连续动作。

优点：

- 更好的收敛性。
- 在高维空间和连续的动作空间更有效。
- 可以学习随机的policy。

缺点：

- 通常收敛到局部最优。
- 评估一个policy通常是低效且高方差的。


继续从目标函数说起, 由于要用神经网络来计算策略梯度，需要用一个网络结构去逼近策略, 在此处 我们假设神经网络的结构参数为 $\theta$,将目标函数由公式-1变为：
$$
J(\theta)=E_{\tau \sim \pi_{\theta}(\tau)}[r(\tau)]=\int_{\tau \sim \pi_{\theta}(\tau)} \pi_{\theta}(\tau) r(\tau) d \tau
$$
推导原因： $f(x)$ 关于某分布 $P(x)$ 的期望, 对于连续性变量, 期望通过积分求得：
$$
E_{x \sim P}[f(x)]=\int p(x) f(x) d x
$$
在数学中梯度的含义就是对函数求取导数，在监督学习中，我们求取损失函数的时候经常求取目标函 数的梯度。同理, 对于策略的目标函数, 我们同样对目标函数 $J(\cdot)$ 公式(2)求取梯度：
$$
\nabla_{\theta} J(\theta)=\int_{\tau \sim \pi_{\theta}(\tau)} \nabla_{\theta} \pi_{\theta}(\tau) r(\tau) d \tau
$$
到这里，我们发现并没有方法直接计算, 通过导数求导变换得到：
$$
\nabla_{\theta} \pi_{\theta}(\tau)=\pi_{\theta}(\tau) \nabla_{\theta} \log \pi_{\theta}(\tau)
$$
将公式(5)代入(4)得到策略梯度：
$$
\begin{array}{l}
\nabla_{\theta} J(\theta)=E_{\tau \sim \pi_{\theta}(\tau)}\left[\nabla_{\theta} \log \pi_{\theta}(\tau) r \tau\right] \\
=\int_{\tau \sim \pi_{\theta}(\tau)} \pi_{\theta}(\tau) \nabla_{\theta} \log \pi_{\theta}(\tau) r(\tau) d \tau
\end{array}
$$

终于通过变化计算得到了策略梯度的计算方法, 但是发现 $\nabla_{\theta} \log \pi_{\theta}(\tau)$ 并没法直接求取。那么该怎 样计算呢? 通过前面我们知道对于序列 $\tau,$ 策略 $\pi(\tau)=\pi\left(s_{0}, a_{0}, s_{1}, a_{1}, \ldots, s_{T}, a_{T}\right)$,我们将 $\pi(\tau)$ 通过最原始的 方法展开得到
$$
\pi(\tau)=p\left(s_{0}\right) \prod_{t=0}^{T} \pi_{\theta}\left(a_{t} \mid s_{t}\right) p\left(s_{t+1} \mid s_{t}, a_{t}\right)
$$
$$
\begin{aligned}
\nabla_{\theta} \log \pi_{\theta}(\tau)=& \nabla_{\theta} \log \left(p\left(s_{0}\right) \prod_{t=0}^{T} \pi_{\theta}\left(a_{t} \mid s_{t}\right) p\left(s_{t+1} \mid s_{t}, a_{t}\right)\right) \\
=\nabla_{\theta}\left(\log p\left(s_{0}\right)+\right.&\left.\sum_{t=0}^{T} \log \pi_{\theta}\left(a_{t} \mid s_{t}\right)+\sum_{t=0}^{T} \log p\left(s_{t+1} \mid s_{t}, a_{t}\right)\right) \\
&=\sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}\left(a_{t} \mid s_{t}\right)
\end{aligned}
$$
这样公式已经和监督学习中的最大似然有相同点了，因此我们对其进行蒙特卡洛处理，最终将公式(6)
(7)(8)组合, 并对公式(6)中的期望用蒙特卡洛进行替换, 得到最终策略梯度：
$$
\begin{aligned}
\nabla_{\theta} J(\theta) &=E_{\tau \sim \pi_{\theta}(\tau)}\left[\sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}\left(a_{t} \mid s_{t}\right)\left(\sum_{t}^{T} r\left(s_{t}, a_{t}\right)\right)\right] \\
&=\frac{1}{N} \sum_{t=0}^{N}\left[\sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}\left(a_{t} \mid s_{t}\right)\left(\sum_{t=0}^{T} r\left(s_{t} \mid a_{t}\right)\right)\right]
\end{aligned}
$$
终于我们得到了策略梯度的计算公式, 接下来就是更新了梯度，和监督学习是一个方式
$$
\hat{\theta}=\theta+\alpha \nabla_{\theta} J(\theta)
$$

[2]

策略梯度的理论和公式部分计算讲完了，
其实说了这么多，最终只是服务于策略网络的逼近和参数更新



Vanilla Policy Gradient (REINFORCE)

This tutorial covers the workflow of a reinforcement learning project. We'll learn how to: create an environment, initialize a model to act as our policy, create a state/action/reward loop and update our policy. We update our policy with the vanilla policy gradient algorithm, also known as REINFORCE.

In Policy Gradient (PG) methods, we optimize the policy directly. Here, we use a parameterized policy with parameters, ϴ. The main motivation remains to be able to do large-scale RL.

- PG methods have the following characteristics:
  - No value function.
  - Policy learnt directly.
  - Gradient (of the policy) ascent used to maximize the reward.

- Advantages:
  - Policy representation can be a more compact representation. Value function might be complicated and it might be much simpler to say what action to take at a particular time-step.
  - Better convergence properties
  - Effective in Continuous spaces
  - Can learn stochastic policies

  Disadvantages:
  - Inefficient, high variance, slow learning
  - Policy might converge to local optimum.

- Why Stochastic Policy?
  - Deterministic policy can be easily exploitable
  - In the case of state aliasing where we don't have access to the full MDP (maybe features giving some information about the states), stochastic policy works better than deterministic.

- **Policy Objective Functions** (J(ϴ)) types:
  - Based on the start state value
  - Based on the average value from a state onwards
  - Based on the average value per time step from a state onwards

  We have an advantage that the same PG method works for all, with some changes to the state distribution function. We need to find the ϴ that maximizes J(ϴ).

- **Finite-difference PG**: The idea is to use gradient ascent on J(ϴ) and search for a local maxima. For each dimension, perturb the parameters slightly and take the difference between the values after and before perturbation. It is noisy, inefficient and collapses for high dimensions. However, it works for arbitrary policy.

- Assume that the policy is differentiable (like Gaussian or softmax policy) with known gradient. The goal is to compute the graident analytically using the **Likelihood Ratios** trick, where the policy gradient can be written in terms of gradient of the **score (or likelihood) function**. This gradient tends to follow the form: `Actual Value` - `Usual (or mean) Value`.

- **One-step MDP**: Starting from a state `s`, take an action `a` and terminate. The gradient of the cost function turns out to be the expectation of the score function multiplied by the reward, which indicates that to get a higher reward, simply move towards the direction given by the score function.

- For extending to multi-step MDP, just replace the immediate reward with the value function which, according to the Policy Gradient Theorem, gives the actual gradient of any of the policy objective funcitons. In **Monte Carlo PG**, we sample the expectation and update the parameters with SGD (REINFORCE). However, it is slow.

- **Actor-Critic Methods (AC)**: The problem of MCPG was that of high variance. Hence, we use a VFA with parameters *w*, for the value function. Here, the *critic* updates *w* and the *actor* updates the policy parameters, ϴ.

- The value function should be a *Compatible* Value function to avoid any bias. For compatible value functions, the score function represents the feature and the optimal parameter *w* of the VFA minimizes the mean-square error between the VF approximation and the true value function. In such a case, the gradient is exact.

- A trick to reduce the variance is to subtract a baseline (dependent only on state), `B(s)` from the value function. This doesn't change the mean, only reduces the variance. A good baseline is the value function `V`, and after subtracting `V` from `Q`, we get the **Advantage Function** `A(s, a)`, which again represents how much better than usual is `Q`.

- `A` can be estimated by taking the TD-error between the TD target value function `V(s')` and the current value function `V(s)`. This TD-error is an unbiased estimate of `A`. Thus, we can sample the `A` in this way, just by using a single set of parameters for `V`.

- Instead of the TD(0) estimate above, we can use the MC estimate or the TD(λ) estimate as well, for the critic. The same idea can be applied to the actor, in which case the backward view equation changes slightly.

- Stochastic policies can be very noisy to sample and we end up estimating noise. **Natural PG** is parameterization independent and finds the ascent direction close to the vanilla gradient by changing the policy slightly. **Deterministic PG** directly takes the expectation of the gradient of the value function as the update to get a deterministic PG, which turns out to be the limiting case of the stochastic PG.

[2]: https://blog.csdn.net/gsww404/article/details/80705950
