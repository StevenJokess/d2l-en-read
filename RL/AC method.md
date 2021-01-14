

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 20:06:23
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 18:02:42
 * @Description:
 * @TODO::
 * @Reference:
-->

## Actor-Critic Methods

 policy-based 的方法 PPO 和 value-based 的方法 Q-learning，这两者其实是可以结合在一起的， 也就是 Actor-Critic 的方法。[6]

变化所驱动的字习规则。虽然1孛习的阜則研允受到了Kopf和动物学习理论的强烈影响,但是,1981年,人们开发了一种在试错学习过程中使用TD学习的方法,称为ator- critic架构,也有人叫作行动者-评论者架构,其中aCtor是行动者,负责动作的选择和执行, critic是评判者负责评价 actor所选动作的好坏。[4]

对于DRL来说,目前的算法都可以包含在 actor-critic框架下。 actor- critic)属于TD学习方法,其用独立的内存结构来明确地表示独立于值函数的策略。策略结构被称为actor,因为它用于选择动作;而估计值函数被称为 critic,因为它评价 actor所做的动作。

In reinforcement learning, an agent makes observations and takes actions within an environment, and in return it receives rewards. Its objective is to learn to act in a way that will maximize its expected long-term rewards.

There are several types of RL algorithms, and they can be divided into three groups:

- Critic-Only: Critic-Only methods, also known as Value-Based methods, first find the optimal value function and then derive an optimal policy from it.
- Actor-Only: Actor-Only methods, also known as Policy-Based methods, search directly for the optimal policy in policy space. This is typically done by using a parameterized family of policies over which optimization procedures can be used directly.
- Actor-Critic: Actor-Critic methods combine the advantages of actor-only and critic-only methods. In this method, the critic learns the value function and uses it to determine how the actor's policy parramerters should be changed. In this case, the actor brings the advantage of computing continuous actions without the need for optimization procedures on a value function, while the critic supplies the actor with knowledge of the performance. Actor-critic methods usually have good convergence properties, in contrast to critic-only methods.

## Actor-Critic methods

Actor-Critic methods are temporal difference (TD) learning methods that represent the policy function independent of the value function.

A policy function (or policy) returns a probability distribution over actions that the agent can take based on the given state. A value function determines the expected return for an agent starting at a given state and acting according to a particular policy forever after.

In the Actor-Critic method, the policy is referred to as the actor that proposes a set of possible actions given a state, and the estimated value function is referred to as the critic, which evaluates actions taken by the actor based on the given policy.

Actor Critic的中文名字是演员&评论家，它的主体可以分为两个部分，分别是演员和评论家。
actor（演员）的作用与其policy gradient类似，其可以通过输入环境的观测量利用神经网络得到每个动作的概率，并通过每个观测状态的得分更新当前的神经网络。它就好像一个被指定动作的演员一般。

Critic（评论家）的作用与其前身DQN类似，其可以通过输入环境的观测量预测每个环境的价值，并通过实际价值与预测价值更新当前的神经网络，它的价值输出可以对actor的动作选择进行动作指导，就好像评论演员的评论家，有助于演员做更好的动作。

actor的前身是policy gradient，policy gradient可以轻松地在完成连续空间的动作，Actor Critic也有同样的特性，但是由于policy gradien是基于回合更新的，所以学习效率比较慢，这时候我们使用前身为DQN的value-based算法为Actor提供算法的参数支持，有助于算法的快速更新。


In this tutorial, both the Actor and Critic will be represented using one neural network with two outputs.

https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic

The actor-critic loss
Since we are using a hybrid actor-critic model, we will use loss function that is a combination of actor and critic losses for training, as shown below:


https://www.tensorflow.org/agents/overview

```py
#[3]
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    lim = 1. / np.sqrt(fan_in)
    return (-lim, lim)

class Actor(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=24, fc2_units=48):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units, action_size)
        self.reset_parameters()

    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)

    def forward(self, state):
        """Build an actor (policy) network that maps states -> actions."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        return F.tanh(self.fc3(x))


class Critic(nn.Module):
    """Critic (Value) Model."""

    def __init__(self, state_size, action_size, seed, fcs1_units=24, fc2_units=48):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fcs1_units (int): Number of nodes in the first hidden layer
            fc2_units (int): Number of nodes in the second hidden layer
        """
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fcs1 = nn.Linear(state_size, fcs1_units)
        self.fc2 = nn.Linear(fcs1_units+action_size, fc2_units)
        self.fc3 = nn.Linear(fc2_units, 1)
        self.reset_parameters()

    def reset_parameters(self):
        self.fcs1.weight.data.uniform_(*hidden_init(self.fcs1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)

    def forward(self, state, action):
        """Build a critic (value) network that maps (state, action) pairs -> Q-values."""
        xs = F.relu(self.fcs1(state))
        x = torch.cat((xs, action), dim=1)
        x = F.relu(self.fc2(x))
        return self.fc3(x)
```

## Actor[5]

Actor神经网络的学习过程是这样的，得到Critic评出的得分，并通过该得分进行训练。
以下代码为Critic评出的得分：

self.td_error = self.r + GAMMA * self.v_ - self.v

通过所有的状态得到所有状态下每个动作的概率，利用：

neg_log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=l2, labels=label)
self.exp_v = tf.reduce_mean(neg_log_prob * self.td_error)

计算每个动作的概率和实际动作的交叉熵，乘上实际得分，得到损失函数值。

[1]: https://github.com/pytorch/examples/blob/master/reinforcement_learning/actor_critic.py
[2]: https://github.com/udacity/deep-reinforcement-learning/blob/master/finance/DRL.ipynb
[3]: https://github.com/udacity/deep-reinforcement-learning/blob/master/finance/model.py
[4]: https://www.hzmedia.com.cn/w/reader.aspx?id=378872d4-69a3-4208-958a-4bc3c48e0287_1
[5]: https://blog.csdn.net/weixin_44791964/article/details/99698318
[6]: https://datawhalechina.github.io/leedeeprl-notes/#/chapter8/chapter8
