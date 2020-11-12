

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 21:30:37
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-12 21:55:41
 * @Description:
 * @TODO::
 * @Reference:https://tianshou.readthedocs.io/zh/latest/
 * https://github.com/thu-ml/tianshou/edit/master/README.md
-->

天授 是一个基于PyTorch的深度强化学习平台，目前实现的算法有：

策略梯度 PGPolicy Policy Gradient

深度Q网络 DQNPolicy Deep Q-Network

双网络深度Q学习 DQNPolicy Double DQN

优势动作评价 A2CPolicy Advantage Actor-Critic

深度确定性策略梯度 DDPGPolicy Deep Deterministic Policy Gradient

近端策略优化 PPOPolicy Proximal Policy Optimization

双延迟深度确定性策略梯度 TD3Policy Twin Delayed DDPG

软动作评价 SACPolicy Soft Actor-Critic

离散软动作评价 DiscreteSACPolicy Discrete Soft Actor-Critic

后验采样强化学习 PSRLPolicy Posterior Sampling Reinforcement Learning

模仿学习 ImitationPolicy Imitation Learning
优先级经验重放 PrioritizedReplayBuffer Prioritized Experience Replay
广义优势函数估计器 compute_episodic_return() Generalized Advantage Estimator

- [Policy Gradient (PG)](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf)
- [Deep Q-Network (DQN)](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)
- [Double DQN](https://arxiv.org/pdf/1509.06461.pdf)
- [Dueling DQN](https://arxiv.org/pdf/1511.06581.pdf)
- [Advantage Actor-Critic (A2C)](https://openai.com/blog/baselines-acktr-a2c/)
- [Deep Deterministic Policy Gradient (DDPG)](https://arxiv.org/pdf/1509.02971.pdf)
- [Proximal Policy Optimization (PPO)](https://arxiv.org/pdf/1707.06347.pdf)
- [Twin Delayed DDPG (TD3)](https://arxiv.org/pdf/1802.09477.pdf)
- [Soft Actor-Critic (SAC)](https://arxiv.org/pdf/1812.05905.pdf)
- [Discrete Soft Actor-Critic (SAC-Discrete)](https://arxiv.org/pdf/1910.07207.pdf)
- Vanilla Imitation Learning
- [Prioritized Experience Replay (PER)](https://arxiv.org/pdf/1511.05952.pdf)
- [Generalized Advantage Estimator (GAE)](https://arxiv.org/pdf/1506.02438.pdf)
- [Posterior Sampling Reinforcement Learning (PSRL)](https://www.ece.uvic.ca/~bctill/papers/learning/Strens_2000.pdf)
