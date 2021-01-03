

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 21:34:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:29:27
 * @Description:
 * @TODO::
 * @Reference:
-->

# PPO (proximal policy optimization)

PPO算法是目前最主流的DRL算法，同时面向离散控制和连续控制，在OpenAI Five上取得了巨大成功。但是PPO是一种on-policy的算法，也就是PPO面临着严重的sample inefficiency，需要巨量的采样才能学习，这对于真实的机器人训练来说，是无法接受的。

Minimal implementation of clipped objective Proximal Policy Optimization (PPO) in PyTorch

[1]:https://github.com/nikhilbarhate99/PPO-PyTorch
[2]:https://github.com/bentrevett/pytorch-rl/blob/master/5%20-%20Proximal%20Policy%20Optimization%20(PPO)%20%5BCartPole%5D.ipynb
[3]: https://github.com/higgsfield/RL-Adventure-2/blob/master/3.ppo.ipynb
[4]: https://zhuanlan.zhihu.com/p/70360272
