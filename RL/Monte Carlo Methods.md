

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 17:07:37
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 17:40:57
 * @Description:
 * @TODO::
 * @Reference:
-->

# Monte Carlo Methods

## 蒙特卡洛方法简介

使用蒙特卡洛方法不需要像DP一样，对环境要有完整的知识（model free），而是通过经验去学习。所谓经验就是对状态、动作、奖励的采样（sample sequence）。

用sample的均值去近似期望。

使用蒙特卡洛通常需要完整的episode，因此蒙特卡洛的更新方式更像是episode-by-episode，而不是像DP的step-by-step。适用于所有的episode都会结束的情形。

优点：

1. 可以从实际经验中学习；
2. 可以从模拟的经验中学习；
3. 可以直接从感兴趣的state开始采样episode。

## 蒙特卡洛预测（评估）

- 在一个episode中状态s可能出现多次，每一次出现称为一次对状态s的访问（visit）。
- first-visit MC method:只是用每个episode中第一次对状态s的访问评估状态s的价值函数。
- every-visit MC method:用每个episode中每次对状态s的访问评估状态s的价值函数。

### first-visit MC method

- 评估某个状态 $s$ 。
- 在某一个episode中，第一次发生状态 $s$ 的是时间 $t_{t}$
- 计数器自增: $N(s) \leftarrow N(s)+1$
- $S(s) \leftarrow S(s)+G_{t}$
- 计算价值函数： $V(s) \leftarrow S(s) / N(s)$

### every-visit MC method

类似于上面，只不过是每次出现状态$s$，都要纳入计算。


增量计算均值: $\mu=\frac{1}{k} \sum_{j=1}^{k} x_{j}=\frac{1}{k}\left(x_{k}+(k-1) \mu_{k-1}\right)=\mu_{k-1}+\frac{1}{k}\left(x_{k}-\mu_{k-1}\right)$

增量式的Monte-Carlo更新：
- 对于每个Episode: $S_{1}, A_{1}, R_{2}, \ldots, S_{T}$ 结束完以后，增量地更新 $V(s)_{\circ}$ $N\left(S_{t}\right) \leftarrow N\left(S_{t}\right)+1$
$V\left(S_{t}\right) \leftarrow V\left(S_{t}\right)+\frac{1}{N\left(S_{t}\right)}\left(G_{t}-V\left(S_{t}\right)\right)$
- 可以写成 $V\left(S_{t}\right) \leftarrow V\left(S_{t}\right)+\alpha\left(G_{t}-V\left(S_{t}\right)\right)$

## 蒙特卡洛评估动作价值函数（Action Values）

- 注意：如果我们的问题中，没有对环境建模，那么单纯评估状态价值函数是不够的。我们必须要评估动作价值函数。
- 主体思想：从评估state到评估state-action对。
- 可能存在的问题：某些state-action对可能不会被访问（稀疏性问题）。


## 蒙特卡洛控制

控制（control）的目的是找到最优策略。

其中，E代表策略的evaluation，I代表策略的improvement。


## 不使用Exploring Starts

- 如何才能不使用Exploring Starts？保证所有被选择的动作被持续地选择。
- 使用on-policy和off-policy。

## on-policy vs off-policy

- on-policy只有一套policy，更简单，是首选。
- off-policy使用两套policy，更复杂、更难收敛；但也更通用、更强大。
- on-policy和off-policy本质依然是Exploit vs Explore的权衡。

### on-policy

去评估和提高生成episode时采用的policy。全过程只有一种策略，MC ES属于on-policy。

### off-policy

- 所有的MC控制方法都面临一个困境：它们都想找到一个最优的策略，但却必须采用非最优的策略去尽可能多地探索（explore）数据。
- 直接使用两套策略：采样用的policy称为behavior policy，即行为策略；最终的目标policy：target policy，即目标策略。这就是off-policy。
- 假设目标策略是π，行为策略是b，那么对于所有的$π(a|s)>0$必然有$b(a|s)>0$，这称为“覆盖”（coverage）。一个常见的例子是：行为策略使用价值函数的greedy policy，而目标策略使用ε-greedy policy。




Follow the instructions in Monte_Carlo.ipynb to write your own implementations of many Monte Carlo methods! The corresponding solutions can be found in Monte_Carlo_Solution.ipynb.[1]

## Monte Carlo Policy Gradients[2]

```py
#[2]
class Policy(nn.Module):
    def __init__(self, s_size=4, h_size=16, a_size=2):
        super(Policy, self).__init__()
        self.fc1 = nn.Linear(s_size, h_size)
        self.fc2 = nn.Linear(h_size, a_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.softmax(x, dim=1)

    def act(self, state):
        state = torch.from_numpy(state).float().unsqueeze(0).to(device)
        probs = self.forward(state).cpu()
        m = Categorical(probs)
        action = m.sample()
        return action.item(), m.log_prob(action)
```


[1]: https://github.com/udacity/deep-reinforcement-learning/blob/master/monte-carlo/Monte_Carlo.ipynbs
[2]: https://github.com/udacity/deep-reinforcement-learning/blob/master/reinforce/REINFORCE.ipynb
