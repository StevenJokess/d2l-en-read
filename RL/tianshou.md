

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 21:30:37
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-12 22:13:06
 * @Description:
 * @TODO::
 * @Reference:https://tianshou.readthedocs.io/zh/latest/
 * https://github.com/thu-ml/tianshou/edit/master/README.md
 * https://github.com/thu-ml/tianshou
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


---


Quick Start
This is an example of Deep Q Network. You can also run the full script at test/discrete/test_dqn.py.

First, import some relevant packages:

import gym, torch, numpy as np, torch.nn as nn
from torch.utils.tensorboard import SummaryWriter
import tianshou as ts

Define some hyper-parameters:

task = 'CartPole-v0'
lr, epoch, batch_size = 1e-3, 10, 64
train_num, test_num = 8, 100
gamma, n_step, target_freq = 0.9, 3, 320
buffer_size = 20000
eps_train, eps_test = 0.1, 0.05
step_per_epoch, collect_per_step = 1000, 10
writer = SummaryWriter('log/dqn')  # tensorboard is also supported!

Make environments:


```py
# you can also try with SubprocVectorEnv
train_envs = ts.env.DummyVectorEnv([lambda: gym.make(task) for _ in range(train_num)])
test_envs = ts.env.DummyVectorEnv([lambda: gym.make(task) for _ in range(test_num)])
```

Setup policy and collectors:

```py
policy = ts.policy.DQNPolicy(net, optim, gamma, n_step, target_update_freq=target_freq)
train_collector = ts.data.Collector(policy, train_envs, ts.data.ReplayBuffer(buffer_size))
test_collector = ts.data.Collector(policy, test_envs)
```



Save / load the trained policy (it's exactly the same as PyTorch nn.module):

torch.save(policy.state_dict(), 'dqn.pth')
policy.load_state_dict(torch.load('dqn.pth'))


Watch the performance with 35 FPS:

policy.eval()
policy.set_eps(eps_test)
collector = ts.data.Collector(policy, env)
collector.collect(n_episode=1, render=1 / 35)



Look at the result saved in tensorboard: (with bash script in your terminal)

$ tensorboard --logdir log/dqn
You can check out the documentation for advanced usage.
