

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 21:27:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:30:27
 * @Description:
 * @TODO::
 * @Reference:
-->


# Q-learning

1989年, Watkins将TD学习和最优控制完全融合在一起,发明了Q-learning,这项工作扩展并整合了先前RL研究三条主线的所有工作[10]

Q-Learning是一种value-based算法，即通过判断每一步进行的价值value来进行下一步的动作[11]

- off-policy 不需要重要性采样。
- 下一个动作从behaviour policy中选择: $A_{t+1} \sim \mu\left(\cdot \mid S_{t}\right)$
- 备选的动作从target policy中选择： $A^{\prime} \sim \pi\left(\cdot \mid S_{t}\right),$ 用于下面式子的计算。
- 更新 $Q\left(S_{t}, A_{t}\right) \leftarrow Q\left(S_{t}, A_{t}\right)+\alpha\left(R_{t+1}+\gamma Q\left(S_{t+1}, A^{\prime}\right)-Q\left(S_{t}, A_{t}\right)\right)$
- target policy 是关于 $Q(s, a)$ 的贪妥策略, 有 $\pi\left(S_{t+1}\right)=\underset{a}{\operatorname{argmax}} Q\left(S_{t+1}, a^{\prime}\right)$

$Q(S, A) \leftarrow Q(S, A)+\alpha\left(R+\gamma \max _{a^{\prime}} Q\left(S^{\prime}, a^{\prime}\right)-Q(S, A)\right)$

Q-learning learns the action-value function Q(s, a): how good to take an action at a particular state. For example, for the board position below, how good to move the pawn two steps forward. Literally, we assign a scalar value over the benefit of making such a move.
Q is called the action-value function (or Q-value function in this article).[4]

Q代表某种动作的长期回报价值。 Q学习是通过观察来学习Q值的。[7]

Q 学习（Q- learning）方法。 它自然的包含了两个部分， 一个是通过经历不停的强化对某个状态行为下趋势的认知 ，另一个则是根据这个趋势，每步走出当下最优的选择（这不就是理性人决策吗！）。[5]

Q学习的过程是：[7]

开始时智能体会把每个“状态-动作”组的Q值初始化为0。更精确的描述为对所有的状态s和动作a：Q(s,a)=0。这从本质上说我们不知道关于每个“状态-动作”组的长期回报信息。

在智能体开始学习后，它会在状态s下采取动作a并获得回报r。它的状态会变成状态s’。智能体会用以下公式更新Q(s,a)：

Q(s,a) = (1-学习速率)*Q(s,a)+学习速率*(r+折扣率*max_a(Q(s’,a)))

基于off-policy思想的Q-learning，与Monte Carlo 方法中off-policy的灵魂思路是一致的，除了更新价值的步数不一样之外。[2]

更新Q值时所使用的方法是沿用既定的策略（on-policy）还是使用新策略（off-policy）。[3]

Q-learning虽然具有学习到全局最优的能力，但是其收敛慢。[2]

γ越大，小鸟就会越重视以往经验，越小，小鸟只重视眼前利益（R）。

定义Q value，它就是在理性人（没步下做最优选择）假设下每一步的收益按贴现率加和来的未来收益总期望。这么绕口，其实我还没说下半句， 那就是在此刻某个行为下的期望，太累了，分开讲。 这整个定义，就是充满智慧的Q - value。[5]

然后Q - learning呢？ 刚说过了， 学习，是通过既往的经验， Q - learning的过程就是根据行为做出后得到的真实境遇（可以是奖励或是惩罚，也可以是新的位置的Q值）来更新这个期望的过程， that‘s all。 当Q 值被更新， 你的行为也就被更新了 ，因为我每一次的行为无非选择最大的Q值。[5]


归根结底还是贝尔曼方程，策略是 arg max， $\quad P_{x^{\prime}}$ 用后验概率，所以贝尔曼方程表示为
$$
Q(s, a)=r+\gamma \max Q\left(s^{\prime}, a^{\prime}\right)
$$
因为每次执行和观测都有噪声，所以在更新 Q 函数时，用学习率的方式。（图中的注释并不是很正确，所 谓现实，只不过是新的估计，应该是新做计和旧估计的差值）[6]

## 伪代码

Initialize $Q(s, a), \forall s \in \mathcal{S}, a \in \mathcal{A}(s),$ arbitrarily, and $Q($terminal-state$, \cdot)=0$
Repeat (for each episode):
Initialize $S$ Repeat (for each step of episode):
Choose $A$ from $S$ using policy derived from $Q$ (e.g., $\varepsilon$ -greedy) Take action $A,$ observe $R, S^{\prime}$
$$
\begin{array}{l}
Q(S, A) \leftarrow Q(S, A)+\alpha\left[R+\gamma \max _{a} Q\left(S^{\prime}, a\right)-Q(S, A)\right] \\
S \leftarrow S^{\prime} ;
\end{array}
$$
until $S$ is terminal

```py
#[9]
class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions  # a list
        self.lr = learning_rate # 学习率
        self.gamma = reward_decay   # 奖励衰减
        self.epsilon = e_greedy     # 贪婪度
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)   # 初始 q_table

    def choose_action(self, observation):
        self.check_state_exist(observation)  # 检测本 state 是否在 q_table 中存在(见后面标题内容)

        # 选择 action
        if np.random.uniform() < self.epsilon:  # 选择 Q value 最高的 action
            state_action = self.q_table.loc[observation, :]

            # 同一个 state, 可能会有多个相同的 Q action value, 所以我们乱序一下
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)

        else:  # 随机选择 action
            action = np.random.choice(self.actions)

        return action

    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)  # 检测 q_table 中是否存在 s_ (见后面标题内容)
        # print(s + '  ' + s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()  # 下个 state 不是 终止符
        else:
            q_target = r  # 下个 state 是终止符
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # 更新对应的 state-action 值

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )
```





## 环境的构建

```py
#[11]
import numpy as np
import pandas as pd
import time

class Env:
    def __init__(self,column,maze_column):
        self.column = column                        #表示地图的长度
        self.maze_column = maze_column - 1          #宝藏所在的位置
        self.x = 0                                  #初始化x
        self.map = np.arange(column)                #给予每个地点一个标号
        self.count = 0                              #用于技术一共走了多少步


    def draw(self):
        a = []
        for j in range(self.column) :               #更新图画
            if j == self.x:
                a.append('o')
            elif j == self.maze_column:
                a.append('m')
            else:
                a.append('_')
        interaction = ''.join(a)
        print('\r{}'.format(interaction),end = '')


    def get_observation(self):
        return self.map[self.x]                     #返回现在在所


    def get_terminal(self):
        if self.x == self.maze_column:              #如果得到了宝藏，则返回已经完成
            done = True
        else:
            done = False
        return done


    def update_place(self,action):
        self.count += 1                              #更新的时候表示已经走了一步
        if action == 'right':
            if self.x < self.column - 1:
                self.x += 1
        elif action == 'left':   #left
            if self.x > 0:
                self.x -= 1

    def get_target(self,action):
        if action == 'right':                        #获得下一步的环境的实际情况
            if self.x + 1 == self.maze_column:
                score = 1
                pre_done = True
            else:
                score = 0
                pre_done = False
            return self.map[self.x + 1],score,pre_done
        elif action == 'left':   #left
            if self.x - 1 == self.maze_column:
                score = 1
                pre_done = Ture
            else:
                score = 0
                pre_done = False
            return self.map[self.x - 1],score,pre_done



    def retry(self):            #初始化
        self.x = 0
        self.count = 0
```

## Test

```py
#[11]
from Env import Env
from QL import QL
import numpy as np
import time

LONG = 6                    #总长度为6
MAZE_PLACE = 6              #宝藏在第六位
TIMES = 15                  #进行15次迭代

people = QL(['left','right'])       #生成QLearn主体的对象，包含left和right
site = Env(LONG,MAZE_PLACE)         #生成测试环境
for episode in range(TIMES):
    state = site.get_observation()  #观察初始环境
    site.draw()                     #生成图像
    time.sleep(0.3)                 #暂停
    while(1):
        done = site.get_terminal()  #判断当前环境是否到达最后
        if done:                    #如果到达，则初始化
            interaction = '\n第%s次世代，共使用步数：%s。'%(episode+1 ,site.count)
            print(interaction)
            site.retry()
            time.sleep(2)
            break
        action = people.choose_action(state)                        #获得下一步方向
        state_after,score,pre_done = site.get_target(action)    #获得下一步的环境的实际情况
        people.learn(state,action,score,state_after,pre_done)       #根据所处的当前环境对各个动作的预测得分和下一步的环境的实际情况更新当前环境的q表
        site.update_place(action)                                   #更新位置
        state = state_after                                         #状态更新
        site.draw()                                                 #更新画布
        time.sleep(0.3)


print(people.q_table)
```

```md
[1]: https://www.zhihu.com/question/26408259
[2]: https://www.zhihu.com/question/26408259/answer/467132543
[3]: https://www.zhihu.com/question/57159315/answer/164323983
[4]: https://medium.com/@jonathan_hui/rl-dqn-deep-q-network-e207751f7ae4
[5]: https://www.zhihu.com/question/26408259/answer/389938864
[6]: 如何用简单例子讲解 Q - learning 的具体过程？ - Michael Jackson的回答 - 知乎 https://www.zhihu.com/question/26408259/answer/540258528
[7]: http://www.oreilly.com.cn/radar/?p=816
[8]: http://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-8.pdf
[9]: https://github.com/0aqz0/path-planning-with-qlearning/blob/master/RL_brain.py
[10]: https://www.hzmedia.com.cn/w/reader.aspx?id=378872d4-69a3-4208-958a-4bc3c48e0287_1
[11]: https://blog.csdn.net/weixin_44791964/article/details/95410737
TODO: https://github.com/iArunava/Q-Learning/blob/master/Q-Learning%20with%20PyTorch.ipynb
```

--

Q-learning suggested readings
• Classic papers • Watkins. (1989). Learning from delayed rewards: introduces Q-learning
• Riedmiller. (2005). Neural fitted Q-iteration: batch-mode Q-learning with neural networks
• Deep reinforcement learning Q-learning papers
• Lange, Riedmiller. (2010). Deep auto-encoder neural networks in reinforcement learning: early image-based Q-learning method using autoencoders to construct embeddings • Mnih et al. (2013). Human-level control through deep reinforcement learning: Qlearning with convolutional networks for playing Atari.
• Van Hasselt, Guez, Silver. (2015).

Deep reinforcement learning with double Q-learning: a very effective trick to improve performance of deep Q-learning.
• Lillicrap et al. (2016). Continuous control with deep reinforcement learning: continuous Q-learning with actor network for approximate maximization.
• Gu, Lillicrap, Stuskever, L. (2016). Continuous deep Q-learning with model-based acceleration: continuous Q-learning with action-quadratic value functions.
• Wang, Schaul, Hessel, van Hasselt, Lanctot, de Freitas (2016). Dueling network architectures for deep reinforcement learning: separates value and advantage estimation in Q-function.
