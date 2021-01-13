# InfoGAIL

是Stanford的Ermon组发表在NIPS17上的工作，主要是在GAIL框架下加入InfoGAN的思想，建模具有多样性的专家行为。

## 改进

1. 在policy上加入对隐变量c的dependency
1. 优化隐变量和policy产生轨迹的互信息


本文还使用reward augmentation和WGAN来改善训练。

首先我们假设专家策略是许多独立的策略的集合
$$
\pi_{E}=\left\{\pi_{E}^{0}, \pi_{E}^{1}, \ldots\right\}
$$
并且假设专家轨迹的产生过程为(先采样c, 然后再选择具体的策略): : :
$$
s_{0} \sim \rho_{0}, c \sim p(c), \pi \sim p(\pi \mid c), a_{t} \sim \pi\left(a_{t} \mid s_{t}\right), s_{t+1} \sim P\left(s_{t+1} \mid a_{t}, s_{t}\right)
$$
因为 $p(\pi \mid c)$ 和 $\pi\left(a_{t} \mid s_{t}\right)$ 都需要学习, 所以直接学习 $\pi(a \mid s, c)$ 。
文在objective中加入隐变量和生成轨迹的互信息作为regularization:
$$
\begin{aligned}
I(c ; \tau) &=H(c)-H(c \mid \tau) \\
&=H(c)+\int_{c} \int_{\tau} p(c, \tau) \log p(c, \tau) d c d \tau \\
&=H(c)+\int_{c} \int_{\tau} p(c)(\tau \mid c) \log p(c \mid \tau) d c d \tau \\
&=H(c)+\mathbb{E}_{c \sim p(c), a \sim \pi(\cdot \mid s, c)}[\log \hat{m}(c \mid \tau)]
\end{aligned}
$$
由于后验概率 $p(c \mid \tau)$ 无法直接access, 互信息难以直接优化。本文引入一个变分下界：
$$
L_{I}(\pi, Q)=H(c)+\mathbb{E}_{c \sim p(c), \alpha \pi \pi\left(\mid s_{s}\right)}[\log Q(c \mid \tau)] \leq I(c ; \tau)
$$
此时 $Q(c \mid \tau)$ 是 $p(c \mid \tau)$ 的一个近似。。
综上, InfoGAIL的优化目标变成了:

$\min _{\max } \mathbb{E}_{\pi}[\log D(s, a)]+\mathbb{E}_{\pi_{E}}[\log (1 - \quad D(s, a))] \quad \lambda_{1} L_{I}(\pi, Q) \quad \lambda_{2} H(\pi)$

[1]: https://arxiv.org/pdf/1703.08840.pdf
[2]: https://www.zhihu.com/column/c_1131879960117473280
