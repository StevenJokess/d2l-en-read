# GAIL:Generative Adversarial Imitation Learning 算法

利用GAN的对抗训练来生成给定的专家数据分布。为什么要用GAN，作者提出，一般Imitation Learning传统的Behavioral Cloning的方法存在状态漂移的问题，一旦遇到没有在专家轨迹中出现的状态将会产生很大的误差以及累计误差；此外，Inverse RL逆强化学习的方法把强化学习的学习过程套在求解cost function的过程中，因此效率很低；然后，逆强化学习只学到的cost function只是解释了专家轨迹，但没有学习到策略，而利用GAIL可以直接显式的得到决策，更高效。[4]



## TRPO算法（Trust Region Policy Optimization）[2]

Algorithm 1 Policy iteration algorithm guaranteeing nondecreasing expected Initialize $\pi_{0}$. for $i=0,1,2, \ldots$ until convergence do Compute all advantage values $A_{\pi_{i}}(s, a) .$
Solve the constrained optimization problem $\pi_{i+1}=\underset{\pi}{\arg \max }\left[L_{\pi_{i}}(\pi)-C D_{\mathrm{KL}}^{\max }\left(\pi_{i}, \pi\right)\right]$
where $C=4 \epsilon \gamma /(1-\gamma)^{2}$
and $L_{\pi_{i}}(\pi)=\eta\left(\pi_{i}\right)+\sum_{s} \rho_{\pi_{i}}(s) \sum_{a} \pi(a \mid s) A_{\pi_{i}}(s, a)$
end for

算法一方面通过抽样，找到更好的policy，这个policy要比旧的policy有优势 $\boldsymbol{A} \pi \boldsymbol{i},$ 即可一定程度保证更新的policy更优。另一方面TRPO要求新的policy $\pi$ 要和旧的policy $\pi \boldsymbol{i}$ 足够相似，即用 $K L$ divergence来约束:
$D_{KL}(\pi, \pi i)$
文章认为，如果不加KL divergence的约束，其实TRPO算法本质上是 policy iteration算法（不保证更新的policy和旧的相似）; 而加了 $KL$
divergence的约束只要对reward函数 $\boldsymbol{L} \pi$ 和 $K L$ 约束稍加修改，其实就是
常见的policy gradient算法。

## 应用到IRL

在IRL逆向强化学习领域中是没有reward（回报）给出的。在这种情况下我们还要去效仿“大师”，就需要假设一个价值函数 。有了这个假设的价值函数，我们就可以直接套用TRPO的RL算法了。但是这个价值函数不能随便假设，这就回到了我们题目说的GAN+增强学习，没错，用GAN的判别器去判断两个“智能体”（agent）的行为是不是底层逻辑属于同一个价值函数，

### 伪代码

Algorithm 1 Generative adversarial imitation learning
1: Input: Expert trajectories $\tau_{E} \sim \pi_{E}$, initial policy and discriminator parameters $\theta_{0}, w_{0}$
2: for $i=0,1,2, \ldots$ do
3: $\quad$ Sample trajectories $\tau_{i} \sim \pi_{\theta_{i}}$
4: Update the discriminator parameters from $w_{i}$ to $w_{i+1}$ with the gradient $\hat{\mathbb{E}}_{\tau_{i}}\left[\nabla_{w} \log \left(D_{w}(s, a)\right)\right]+\hat{\mathbb{E}}_{\tau_{E}}\left[\nabla_{w} \log \left(1-D_{w}(s, a)\right)\right]$ (17)
5: Take a policy step from $\theta_{i}$ to $\theta_{i+1},$ using the TRPO rule with cost function $\log \left(D_{w_{i+1}}(s, a)\right)$ Specifically, take a KL-constrained natural gradient step with $\hat{\mathbb{E}}_{\tau_{i}}\left[\nabla_{\theta} \log \pi_{\theta}(a \mid s) Q(s, a)\right]-\lambda \nabla_{\theta} H\left(\pi_{\theta}\right)$ $Q(\bar{s}, \bar{a})=\hat{\mathbb{E}}_{\tau_{i}}\left[\log \left(D_{w_{i+1}}(s, a)\right) \mid s_{0}=\bar{s}, a_{0}=\bar{a}\right]$ where
6: end for

4. 就是GAN判别器的更新方法
5. 就是用TRPO更新生成器，其实这里的生成器就是学习“大师行为”的学生算法，即，最后模仿出来的近似策略。（只是这里的TRPO算法的优化目标变为了对抗判别器的预测结果Dw+1）

其中discriminator的更新公式为：

$\mathcal{L}_{\text {discriminator }}(\psi)=\mathbb{E}_{\tau \sim p}\left[-\log D_{\psi}(\tau)\right]+\mathbb{E}_{\tau \sim q}\left[-\log \left(1-D_{\psi}(\tau)\right)\right]$

$D(\tau)=$ probability $\tau$ is a demo , 用 $\log D(\tau)$ 作为回报。

### 问题

此处GAIL就产生一个问题，如上图，GAN的判别器D可以判别生成器的策略和被模仿对象（专家策略）之间的区别，但是，当把行为错误δa反向传播时，只能估算一个大概的梯度δHV 给生成器（往往不稳定并且高方差的）。这就导致一个很明显的漏洞，这个判别器D只能根据当前的行为a、被模仿者的状态x1和模仿者的状态x2做判别，如果模仿者和被模仿者像下面这样：




只要判断x1和x2正负就能轻松判别两种策略，那么梯度也没有办法获得，问题就出在：我们没有把模仿者G的趋势也与Expert专家策略的趋势结合起来，使得Expert策略一直往上走，而G的策略一直往下走，判别器D也浑然不知策略出了问题。

## 趋势也能在梯度

如上图,两个重复的模块即串连起来的两个时刻t和t+1,把时序串连起来的是一个新增的网络f(s,a),它的输入是上个状态St-1,以及模仿者G(策略π)的行为抽样a,输出是预测的下个状态St。这样有了模仿者G的预测状态St,模型就知道G的状态趋势。判别器D就能更好地判别模仿者和被模仿者的差异



[1]: IRL 之小白 - WJP的文章 - 知乎 https://zhuanlan.zhihu.com/p/59649635
[2]: https://arxiv.org/pdf/1502.05477.pdf
[3]: https://arxiv.org/abs/1606.03476
[4]: https://zhuanlan.zhihu.com/p/69773693s