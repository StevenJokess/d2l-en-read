

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-26 21:09:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 19:43:08
 * @Description:
 * @TODO::
 * @Reference:
-->

# Deep Deterministic Policy Gradients (DDPG)

## 离散动作 vs. 连续动作

离散动作与连续动作是相对的概念，一个是可数的，一个是不可数的。

离散动作有如下几个例子：[9]

- 在 CartPole 环境中，可以有向左推小车、向右推小车两个动作。
- 在 Frozen Lake 环境中，小乌龟可以有上下左右四个动作。
- 在 Atari 的 Pong 游戏中，游戏有 6 个按键的动作可以输出。

但在实际情况中，经常会遇到连续动作空间的情况，也就是输出的动作是不可数的。比如：

- 推小车力的大小，
- 选择下一时刻方向盘的转动角度，
- 四轴飞行器的四个螺旋桨给的电压的大小。

## 拆解

在连续控制领域，比较经典的强化学习算法就是 深度确定性策略梯度(Deep Deterministic Policy Gradient，简称 DDPG)。

DDPG 的特点可以从它的名字当中拆解出来，拆解成 Deep、Deterministic 和 Policy Gradient。

- Deep 是因为用了神经网络；
- Deterministic 表示 DDPG 输出的是一个确定性的动作，可以用于连续动作的一个环境；
- Policy Gradient 代表的是它用到的是策略网络。REINFORCE 算法每隔一个 episode 就更新一次，但 DDPG 网络是每个 step 都会更新一次 policy 网络，也就是说它是一个单步更新的 policy 网络。

DDPG是基于actor-critic[1]的无模型确定性策略梯度算法，人工智能就是解决无数据预处理，多维度，敏感输入的多目标任务。DQN只能解决低维度的离散输出动作的任务，不能直接解决连续动作任务，DQN及其衍生算法直接扔掉了动作空间中一些可能有用的信息。

DDPG及其拓展则是DeepMind开发的面向连续控制的off policy算法，相对PPO 更sample efficient。DDPG训练的是一种确定性策略deterministic policy，即每一个state下都只考虑最优的一个动作。DDPG的拓展版D4PG从paper中的结果看取得了非常好的效果，但是并没有开源，目前github上也没有人能够完全复现Deepmind的效果。[6]

DDPG 是 DQN 的一个扩展的版本。

- 在 DDPG 的训练中，它借鉴了 DQN 的技巧：目标网络和经验回放。
- 经验回放这一块跟 DQN 是一样的，但 target network 这一块的更新跟 DQN 有点不一样。

由 DPG 升级为 DDPG，即将 actor 模型和 critic 模型升级为 actor 网络 $\mu\left(s \mid \theta^{\mu}\right)$ 和 critic 网 络 $Q\left(s, a \mid \theta^{Q}\right)$ 。[8]

DQN 的最佳策略是想要学出一个很好的 Q 网络，学好这个网络之后，我们希望选取的那个动作使你的 Q 值最大。

DDPG 的目的也是为了求解让 Q 值最大的那个 action。

- Actor 只是为了迎合评委的打分而已，所以用来优化策略网络的梯度就是要最大化这个 Q 值，所以构造的 loss 函数就是让 Q 取一个负号。
- 我们写代码的时候就是把这个 loss 函数扔到优化器里面，它就会自动最小化 loss，也就是最大化 Q。

这里要注意，除了策略网络要做优化，DDPG 还有一个 Q 网络也要优化。

评委一开始也不知道怎么评分，它也是在一步一步的学习当中，慢慢地去给出准确的打分。

我们优化 Q 网络的方法其实跟 DQN 优化 Q 网络的方法是一样的，我们用真实的 reward rr 和下一步的 Q 即 Q' 来去拟合未来的收益 Q_target。

然后让 Q 网络的输出去逼近这个 Q_target。

所以构造的 loss function 就是直接求这两个值的均方差。
构造好 loss 后，我们就扔进去那个优化器，让它自动去最小化 loss 就好了。


## 伪代码

https://img-blog.csdn.net/20180514210452630?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxMjM5NDk1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70

Algorithm 1 DDPG algorithm
Randomly initialize critic network $Q\left(s, a \mid \theta^{Q}\right)$ and actor $\mu\left(s \mid \theta^{\mu}\right)$ with weights $\theta^{Q}$ and $\theta^{\mu}$. Initialize target network $Q^{\prime}$ and $\mu^{\prime}$ with weights $\theta^{Q^{\prime}} \leftarrow \theta^{Q}, \theta^{\mu^{\prime}} \leftarrow \theta^{\mu}$
Initialize replay buffer $R$ for episode $=1, \mathrm{M}$ do a random process $\mathcal{N}$ for action exploration Receive initial observation state $s_{1}$ Select action $a_{t}=\mu\left(s_{t} \mid \theta^{\mu}\right)+\mathcal{N}_{t}$ according to the current policy and exploration noise Execute action $a_{t}$ and observe reward $r_{t}$ and observe new state $s_{t+1}$ state $s_{t+1}$ Store from $R$ Sample a random minibatch of $N$ transitions $\left(s_{i}, a_{i}, r_{i}, s_{i+1}\right)$ from $R$
Set $y_{i}=r_{i}+\gamma Q^{\prime}\left(s_{i+1}, \mu^{\prime}\left(s_{i+1} \mid \theta^{\mu^{\prime}}\right) \mid \theta^{Q^{\prime}}\right)$
Update critic by minimizing the loss: $L=\frac{1}{N} \sum_{i}\left(y_{i}-Q\left(s_{i}, a_{i} \mid \theta^{Q}\right)\right)^{2}$ Update the actor policy using the sampled policy gradient:
$\left.\left.\nabla_{\theta^{\mu}} J \approx \frac{1}{N} \sum_{i} \nabla_{a} Q\left(s, a \mid \theta^{Q}\right)\right|_{s=s_{i}, a=\mu\left(s_{i}\right)} \nabla_{\theta^{\mu}} \mu\left(s \mid \theta^{\mu}\right)\right|_{s_{i}}$
Update the target networks:
$\theta^{Q^{\prime}} \leftarrow \tau \theta^{Q}+(1-\tau) \theta^{Q^{\prime}}$ $\theta^{\mu^{\prime}} \leftarrow \tau \theta^{\mu}+(1-\tau) \theta^{\mu^{\prime}}$
end for
end for

```py
class Actor(nn.Module):
	def __init__(self, state_dim, action_dim, max_action):
		super(Actor, self).__init__()

		self.l1 = nn.Linear(state_dim, 400)
		self.l2 = nn.Linear(400, 300)
		self.l3 = nn.Linear(300, action_dim)

		self.max_action = max_action


	def forward(self, state):
		a = F.relu(self.l1(state))
		a = F.relu(self.l2(a))
		return self.max_action * torch.tanh(self.l3(a))
```

```py
class Critic(nn.Module):
	def __init__(self, state_dim, action_dim):
		super(Critic, self).__init__()

		self.l1 = nn.Linear(state_dim, 400)
		self.l2 = nn.Linear(400 + action_dim, 300)
		self.l3 = nn.Linear(300, 1)


	def forward(self, state, action):
		q = F.relu(self.l1(state))
		q = F.relu(self.l2(torch.cat([q, action], 1)))
		return self.l3(q)
```


```py
#[3]
def ddpg(n_episodes=2000, max_t=700):
    scores_deque = deque(maxlen=100)
    scores = []
    max_score = -np.Inf
    for i_episode in range(1, n_episodes+1):
        state = env.reset()
        agent.reset()
        score = 0
        for t in range(max_t):
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += reward
            if done:
                break
        scores_deque.append(score)
        scores.append(score)
        print('\rEpisode {}\tAverage Score: {:.2f}\tScore: {:.2f}'.format(i_episode, np.mean(scores_deque), score), end="")
        if i_episode % 100 == 0:
            torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
            torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
    return scores

Paper[5]
```

## Exploration vs. Exploitation

DDPG 通过 off-policy 的方式来训练一个确定性策略。因为策略是确定的，如果 agent 使用同策略来探索，在一开始的时候，它会很可能不会尝试足够多的 action 来找到有用的学习信号。为了让 DDPG 的策略更好地探索，我们在训练的时候给它们的 action 加了噪音。DDPG 的原作者推荐使用时间相关的 OU noise，但最近的结果表明不相关的、均值为 0 的 Gaussian noise 的效果非常好。由于后者更简单，因此我们更喜欢使用它。为了便于获得更高质量的训练数据，你可以在训练过程中把噪声变小。

在测试的时候，为了查看策略利用它学到的东西的表现，我们不会在 action 中加噪音。

[1]: https://github.com/udacity/deep-reinforcement-learning/blob/master/finance/DRL.ipynb
[2]: https://github.com/udacity/deep-reinforcement-learning/blob/master/finance/DRL.ipynb
[3]: https://github.com/udacity/deep-reinforcement-learning/blob/master/ddpg-bipedal/DDPG.ipynb
[4]: https://github.com/sfujim/TD3/blob/master/DDPG.py
[5]: https://arxiv.org/abs/1509.02971
[6]: https://zhuanlan.zhihu.com/p/70360272
[7]: https://blog.csdn.net/qq_31239495/article/details/80313803
[8]: https://github.com/CharmyZ/note-book-blog/blob/master/%E3%80%8A%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0%E5%9C%A8%E9%98%BF%E9%87%8C%E7%9A%84%E6%8A%80%E6%9C%AF%E6%BC%94%E8%BF%9B%E4%B8%8E%E4%B8%9A%E5%8A%A1%E5%88%9B%E6%96%B0%E3%80%8B.pdf
[9]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter12/chapter12
