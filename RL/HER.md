# HER（Hindsight experience replay）

HER（Hindsight experience replay）算法是Open AI 提出的用来解决反馈奖励稀疏的存储样本的数据结构，采用了渐进式的学习方法，通过调整任务难度让模型渐进式的学习，不断增强策略的能力．论文中replay buffer 以序列为单位储存（就是伪代码里面的episode），论文采用future的采样模式．从repaly buffer中采样ｂ个序列，从ｂ个序列中选择某一时刻得到ｂ个样本，每一个样本有一定概率将achieved_goal设置为当前时刻的任一时刻的状态．

## 伪代码：

https://img-blog.csdn.net/20180514214903903?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxMjM5NDk1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70

Given:
$\begin{array}{ll}\text { - an off-policy RL algorithm } \mathbb{A}, & \triangleright \text { e.g. DQN, DDPG, NAF, SDQN }\end{array}$
- a strategy $\mathbb{S}$ for sampling goals for replay, $\triangleright$ e.g. $\mathbb{S}\left(s_{0}, \ldots, s_{T}\right)=m\left(s_{T}\right)$
Initialize $\mathbb{A} \quad \triangleright$ e.g. initialize neural networks Initialize replay buffer $R$ for episode $=1, M$ do Sample a goal $g$ and an initial state $s_{0}$. for $t=0, T-1 \mathbf{d o}$
Sample an action $a_{t}$ using the behavioral policy from $\mathbb{A}$ :
$a_{t} \leftarrow \pi_{b}\left(s_{t} \| g\right)$
$\triangleright \|$ denotes concatenation Execute the action $a_{t}$ and observe a new state $s_{t+1}$ end for for $t=0, T-1 \mathbf{d o}$
$r_{t}:=r\left(s_{t}, a_{t}, g\right)$
Store the transition $\left(s_{t}\left\|g, a_{t}, r_{t}, s_{t+1}\right\| g\right)$ in $R \quad \triangleright$ standard experience replay Sample a set of additional goals for replay $G:=\mathbb{S}($ current episode $)$ for $g^{\prime} \in G$ do
$r^{\prime}:=r\left(s_{t}, a_{t}, g^{\prime}\right)$
Store the transition $\left(s_{t}\left\|g^{\prime}, a_{t}, r^{\prime}, s_{t+1}\right\| g^{\prime}\right)$ in $R$
HER end for end for for $t=1, N$ do Sample a minibatch $B$ from the replay buffer $R$ Perform one step of optimization using $\mathbb{A}$ and minibatch $B$ end for end for
