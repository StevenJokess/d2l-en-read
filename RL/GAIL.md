# GAIL:Generative Adversarial Imitation Learning 算法

其中discriminator的更新公式为：

$\mathcal{L}_{\text {discriminator }}(\psi)=\mathbb{E}_{\tau \sim p}\left[-\log D_{\psi}(\tau)\right]+\mathbb{E}_{\tau \sim q}\left[-\log \left(1-D_{\psi}(\tau)\right)\right]$

$D(\tau)=$ probability $\tau$ is a demo , 用 $\log D(\tau)$ 作为回报。

[1]: IRL 之小白 - WJP的文章 - 知乎 https://zhuanlan.zhihu.com/p/59649635
