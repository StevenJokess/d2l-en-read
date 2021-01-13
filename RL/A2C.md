

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 21:55:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 22:19:38
 * @Description:
 * @TODO::
 * @Reference:
-->

#  A2C (Advantage Actor-Critic)

## 动机

Actor-Critic有一项缺点就是它需要Estimate两个network (Q-network和V-network)， 成倍增加了 network估测不准的风险。我们可以只估测一个network来降低风险, 主要利用了以下这个式子
$$
Q^{\pi}\left(s_{t}^{n}, a_{t}^{n}\right)=r_{t}^{n}+V^{\pi}\left(s_{t+1}^{n}\right)
$$
(注：严格来说应该在右边加上期望值, 这两端才能完全相等, 这里直接令两端相等, 虽然引入了 $r_{t}^{n}$ 这 个随机变量带来的方差, 但相比于 $G_{t}^{n}$ 这个将所有step的reward加起来得到的随机变量的方差来说是微 不足道的) 基于这些步骤, 我们可以更新一下我们在文章开头用于计算梯度的那个式子：
$$
\nabla \bar{R}_{\theta} \approx \frac{1}{N} \sum_{n=1}^{N} \sum_{t=1}^{T_{n}}\left(r_{t}^{n}+V^{\pi}\left(s_{t+1}^{n}\right)-V_{0}^{\pi}\left(s_{t}^{n}\right)\right) \nabla \log _{\theta_{\theta}}\left(a_{t}^{n} \mid s_{t}^{n}\right)
$$

Tips for Advantage Actor-Critic:
Actor和Critic两个network的参数可以共用:
我们知道A2C当中实际上要更新的是两个network, 一个是策略本身 $\pi(s),$ 另外一个是V-network $V^{\pi}(s),$ 由于这两个network的输入都是状态s, 因而它们在最前面几层layer的处理是可以共用的
$1 \pm$

i)
Original paper: https://arxiv.org/abs/1602.01783
Baselines blog post: https://blog.openai.com/baselines-acktr-a2c/
python -m baselines.run --alg=a2c --env=PongNoFrameskip-v4 runs the algorithm for 40M frames = 10M timesteps on an Atari Pong. See help (-h) for more options
also refer to the repo-wide README.md

[1]: https://github.com/openai/baselines/tree/master/baselines/a2c
[2]: https://github.com/rpatrik96/pytorch-a2c
[3]: https://github.com/bentrevett/pytorch-rl
