

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 21:52:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 22:04:29
 * @Description:
 * @TODO::
 * @Reference:
-->


![rl_alg](rl_alg.svg)

免模型学习（Model-Free） vs 有模型学习（Model-Based）
不同强化学习算法最重要的区分点之一就是 智能体是否能完整了解或学习到所在环境的模型。 环境的模型是指一个预测状态转换和奖励的函数。

## 免模型学习



## 有模型学习

优势在于智能体能够 提前考虑来进行规划，走到每一步的时候，都提前尝试未来可能的选择，然后明确地从这些候选项中进行选择。智能体可以把预先规划的结果提取为学习策略。这其中最著名的例子就是 AlphaZero。这个方法起作用的时候，可以大幅度提升采样效率 —— 相对于那些没有模型的方法。

缺点就是智能体往往不能获得环境的真实模型。如果智能体想在一个场景下使用模型，那它必须完全从经验中学习，这会带来很多挑战。最大的挑战就是，智能体探索出来的模型和真实模型之间存在误差，而这种误差会导致智能体在学习到的模型中表现很好，但在真实的环境中表现得不好（甚至很差）。基于模型的学习从根本上讲是非常困难的，即使你愿意花费大量的时间和计算力，最终的结果也可能达不到预期的效果。




[1]: https://spinningup.readthedocs.io/zh_CN/latest/spinningup/rl_intro2.html#model-free-vs-model-based
[2]	A2C / A3C (Asynchronous Advantage Actor-Critic): Mnih et al, 2016 https://arxiv.org/abs/1602.01783
[3]	PPO (Proximal Policy Optimization): Schulman et al, 2017 https://arxiv.org/abs/1707.06347
[4]	TRPO (Trust Region Policy Optimization): Schulman et al, 2015 https://arxiv.org/abs/1502.05477
[5]	DDPG (Deep Deterministic Policy Gradient): Lillicrap et al, 2015 https://arxiv.org/abs/1509.02971
[6]	TD3 (Twin Delayed DDPG): Fujimoto et al, 2018 https://arxiv.org/abs/1802.09477
[7]	SAC (Soft Actor-Critic): Haarnoja et al, 2018 https://arxiv.org/abs/1801.01290
[8]	DQN (Deep Q-Networks): Mnih et al, 2013 https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
[9]	C51 (Categorical 51-Atom DQN): Bellemare et al, 2017 https://arxiv.org/abs/1707.06887
[10] QR-DQN (Quantile Regression DQN): Dabney et al, 2017 https://arxiv.org/abs/1710.10044
[11] HER (Hindsight Experience Replay): Andrychowicz et al, 2017 https://arxiv.org/abs/1707.01495
[12] world Models: Ha and Schmidhuber, 2018
[13] I2A (Imagination-Augmented Agents): Weber et al, 2017 https://arxiv.org/abs/1707.06203
[14] MBMF (Model-Based RL with Model-Free Fine-Tuning): Nagabandi et al, 2017 https://sites.google.com/view/mbmf
[15] MBVE (Model-Based Value Expansion): Feinberg et al, 2018 https://arxiv.org/abs/1803.00101
[16] AlphaZero: Silver et al, 2017 https://arxiv.org/abs/1712.01815
[17] https://spinningup.openai.com/en/latest/
