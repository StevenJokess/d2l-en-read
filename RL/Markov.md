

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-30 19:53:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 19:57:43
 * @Description:
 * @TODO::
 * @Reference:
-->

# Finite Markov Decision Processes

## 背景

求解强化学习问题可以理解为如何最大化个体在与环境交互过程中获得的累积奖励
当环境状态是完全可观测时，个体可以通过构建马尔科夫决策过程来描述整个强化学习问题。有时候环境状态并不是完全可观测的，此时个体可以结合自身对于环境的历史观测数据来构建一个近似的完全可观测环境的描述
从这个角度来说，几乎所有的强化学习问题都可以被认为或可以被转化为马尔科夫决策过程

## Agent和Environment的交互

- 学习者和决策者称为agent
- agent交互的对象, 外部环境, 称为Environment。
- 在时刻t, agent的所处的环境用状态: $S_{t} \in S$ 表示, $S$ 是可能的状态集。假设agent采用了动作 $A_{t} \in A\left(S_{t}\right)$,
- $A\left(S_{t}\right)$ 代表在状态 $S_{t}$ 下可能的动作集。
- 到了下一个时刻t+1, agent收到了一个奖励: $R_{t+1} \in R,$ 并且发现自己处在一个新的state中: $S_{t+1}$ 。

## Markov Process: 由简单到复杂:

- 包含 $<\mathbf{S}, \mathbf{P}>,$ 即状态集合和状态转移矩阵。 $\mathrm{MRP}:$ 包含 $<\mathbf{S}, \mathbf{P}, \mathbf{R}, \gamma>,$ 即增加了奖励函数和折扣系数
$$
\mathbf{R}_{s}=E\left[\mathbf{R}_{t+1} \mid S_{t}=s\right]
$$
- 引入 $G_{t}=R_{t+1}+\gamma R_{t+2}+\ldots=\sum_{k=0}^{\infty} \gamma^{k} R_{t+k+1},$ 注意Value是期望, G是
针对一个sample, $v(s)=E\left[G_{t} \mid S_{t}=s\right]_{0}$
- MDP:包含<S，A, $\mathbf{P}, \mathbf{R}, \gamma>,$ 增加了A，是有限的动作集合。
$$
\mathbf{P}_{s s}^{a}=P\left[S_{t+1}=s^{\prime} \mid S_{t}=s, A_{t}=a\right], \mathbf{R}_{s}^{a}=E\left[R_{t+1} \mid S_{t}=s, A_{t}=a\right]_{0}
$$

## 什么是有限

有限MDP中的有限意味着：状态空间S、动作空间A和奖励空间R都是离散且有限的。

## 目标和奖励的区别

- 每个时间节点上, agent都会收到一个奖励的数值: $R_{t}$ 。
- 但是, agent的目标应该是：所有时间结点上的奖励的和的最大化。
- 即 $: G_{t}=R_{t+1}+R_{t+2}+\ldots+R_{T}$

## 什么是Episode

一系列的agent和environment交互序列，由一系列(state, action, reward)三元组构成。每个episode之间相互不影响，且都是有一个相同的终止状态（terminate state）。

## Episode和Continuing Tasks的统一规范

在Episode的尾部加入吸收状态（absorbing state），在此状态下，奖励永远是0，且下一个状态永远是当前状态。

这样收益可以统一使用下面的Expected Discounted Return表示。

## Expected Discounted Return

- 回报: $G_{t}=R_{t+1}+\gamma R_{t+2}+\ldots=\sum_{k=0}^{\infty} \gamma^{k} R_{t+k+1}$
- $\gamma$ 是参数, 且 $0 \leq \gamma \leq 1,$ 被称为discount rate
- 含义: 一个奖励, 如果是在k个时间节点以后收到，那么对于当前来说, 它的价值是即时奖励的 $\gamma^{k-1}$ 倍。
- 从 G_{t}$ 的定义 $,$ 很容易获得递推式: $G_{t}=R_{t+1}+\gamma G_{t+1}$

## 马尔科夫性质 (Markov property)

- 核心思想：当前state继承了所有的环境历史信息。也就是说在每次决策的时候，我们只用考虑当前状态就可以了。
- $\operatorname{Pr} S_{t+1}=s^{\prime}, R_{t+1}=r\left|S_{0}, A_{0}, R_{1}, \ldots, S_{t-1}, A_{t_{1}}, R_{t}, S_{t}, A_{t}=\operatorname{Pr} S_{t+1}=s^{\prime}, R_{t+1}=r\right| S_{t}, A_{t}$
- 即便state是非马尔科夫的, 我们也希望近似到马尔科夫。

## 马尔科夫决策过程(Markov decision process, MDP)

- 满足马尔科夫性质的强化学习任务称为MDP。
- 如果state和action空间有限, 则称为有限MDP (涵盖了现代强化学习90\%的问题) 。
- 用 $p\left(s^{\prime}, r \mid s, a\right)$ 表示 $P r S_{t+1}=s^{\prime}, R_{t+1}=r \mid S_{t}, A_{t},$ 这个条件概率是描绘了整个MDP的动态 (Dynamics) $。$ state-action期望奖励: $r(s, a)=\mathbb{E}\left[R_{t+1} \mid S_{t}=s, A_{t}=a\right]=\sum_{r \in R} r \sum_{s^{\prime} \in S} p\left(s^{\prime}, r \mid s, a\right)$
- 状态转移概率: $p\left(s^{\prime} \mid s, a\right)=\operatorname{Pr} S_{t+1}=s^{\prime} \mid S_{t}=s, A_{t}=a=\sum_{r \in R} p\left(s^{\prime}, r \mid s, a\right)$
- state-action-nextstate期望奖励: $r\left(s, a, s^{\prime}\right)=\mathbb{E}\left[R_{t+1} \mid S_{t}=s, A_{t}=a, S_{t+1}=s^{\prime}\right]=\sum_{r \in R} r \frac{p\left(s^{\prime}, r \mid s, a\right)}{p\left(s^{\prime} \mid s, a\right)}$

它是 由 ⟨S, A, P, R, γ⟩ 构成的一个元组，其中:

- S 是一个有限状态集
- A 是一个有限行为集
- P 是集合中基于行为的状态转移概率矩阵: $P_{s s^{\prime}}^{a}=E\left[R_{t+1} \mid S_{t}=s, A_{t}=a\right]$
- R 是基于状态和行为的奖励函数: $R_{s}^{a}=E\left[R_{t+1} \mid S_{t}=s, A_{t}=a\right]$
- γ 是一个衰减因子:γ ∈ [0, 1]

## 价值函数

关于策略 $\pi$ 的state-value函数
$$
v_{\pi}(s)=\mathbb{E}_{\pi}\left[G_{t} \mid S_{t}=s\right]=\mathbb{E}_{\pi}\left[\sum_{k} \gamma^{k} R_{t+k+1} \mid S_{t}=s\right]
$$

$$
q_{\pi}(a, s)=\mathbb{E}_{\pi}\left[G_{t} \mid S_{t}=s, A_{t}=a\right]=\mathbb{E}_{\pi}\left[\sum_{k=0}^{\infty} \gamma^{k} R_{t+k+1} \mid S_{t}=s, A_{t}=a\right]
$$
即，在使用策略 $\pi$ 的前提下，衡量处于某个state下，执行某个action有多好。
Bellman Euqation
Bellman Expectation Euqation for $v_{\pi}$
$$
v_{\pi}(s)=\sum_{a} \pi(a \mid s) \sum_{s^{\prime}, r} p\left(s^{\prime}, r \mid s, a\right)\left[r+\gamma v_{\pi}\left(s^{\prime}\right)\right] ; ; \forall s \in S
$$
理解：
1.方括号中是根据后继状态的价值重新估计的价值函数，再在动作空间、后继状态空间和动作空间用相应的概率做加权求
和。
2.表达的是某个状态的价值和其后继状态的价值之间的关系。
backup: 是强化学习方法的核心, 以时序意义上的回退, 用下一个时刻的值去评估当前时刻的值。

## 相关概念

### 策略

个体在给定状态下从行为集中选择一个行为的依据则称为策略 (policy)，用字母 π 表示。策略 π 是某一状态下基于行为集合的概率分布:

- 当给定一个马尔科夫决策过程:M $=\langle\mathrm{S}, \mathrm{A}, \mathrm{P}, \mathrm{R}, \mathrm{Y}\rangle$ 和一个策略 $\pi,$ 那么状态序列 $S_{1}, S_{2}, \ldots$ 是一个符合马尔科夫过程
$\left\langle S, P_{\pi}\right\rangle$ 的采样
- 价值函数
价值函数 $v_{\pi}(s)$ 是在马尔科夫决策过程下基于策略 $\pi$ 的状态价值函数, 表示从状态 s开始, 遵循当前策略 $\pi$ 时所获得的收获的期望: $v_{\pi}(s)=E\left[G_{t} \mid S_{t}=s\right]$
。
- 行为价值函数(状态行为对价值函数)
一个基于策略 $\pi$ 的行为价值函数 $q_{\pi}(s, a),$ 表示在遵循策略 $\pi$ 时，对当前状态 $s$ 执行某一具体行为 a 所能的到的收获的期望: $q_{\pi}(s, a)=E\left[G_{t} \mid S_{t}=s, A_{t}=a\right]$
。

## 贝尔曼方程(Bellman euqation)

同理, 可推导出如下两个方程
$$
\begin{array}{l}
v_{\pi}(s)=E\left[R_{t+1}+\gamma v_{\pi}\left(S_{t+1}\right) \mid S_{t}=s\right] \\
q_{\pi}(s, a)=E\left[R_{t+1}+\gamma q_{\pi}\left(S_{t+1}, A_{t+1}\right) \mid S_{t}=s, A_{t}=a\right]
\end{array}
$$

### Bellman Expectation Euqation for $q_{\pi}$

$$
q_{\pi}(s, a) =\sum_{s^{\prime}} p\left(s^{\prime}, r \mid s, a\right)\left[r+\gamma \sum_{a^{\prime}} q\left(s^{\prime}, a^{\prime}\right)\right]
$$

## 最优价值函数[2]

### 背景：

是否存在一个基于某一策略的价值函数， 在该策略下每一个状态的价值都比其它策略下该状态的价值高?如果存在如何找到这样的价值 函数?这样的价值函数对应的策略又是什么策略?

### 最优

最优状态价值函数是所有策略下产生的众多状态价值函数中的最大者
最优行为价值函数(optimal action-value function)
是所有策略下产生的众多行为价值函数中的最大者:

$$
\begin{array}{c}
v_{*}(s)=\max _{\pi} v_{\pi}(s) \\
q_{*}(s, a)=\max _{\pi} q_{\pi}(s, a)
\end{array}
$$

### 贝尔曼优化方程

### Bellman Optimality Euqation for $v_{*}(s):$

$$
\max _{a \in A(s)} \sum_{s^{\prime}, r} p\left(s^{\prime}, r \mid s, a\right)\left[r+\gamma v_{*}\left(s^{\prime}\right)\right]
$$

### Bellman Optimality Euqation for $q_{*}(s, a)$ :

$$
\sum_{s^{\prime}, r} p\left(s^{\prime}, r \mid s, a\right)\left[r+\gamma \max _{a^{\prime}} x q_{*}\left(s^{\prime}, a^{\prime}\right)\right]
$$

### 解决Bellman Optimality Equation的方法：

Bellman Optimality Equation是非线性的，不能直接计算；
迭代求解的方法：

- MDP：
    - Value Iteration
    - Policy Iteration
- Model Free：
    - Q-learning
    - Sarsa

## Bellman Equation总结：

Bellman Equation可以理解成某一时刻在某一状态下的value可以拆分成即时奖励和一下一个时刻开始所有可能的状态的价值的期望。
二者本质上都是递推公式，其中蕴含的“backup”思路，也就是从后一个状态的价值，逆推回前一个状态的价值。
Bellman Equation表达的是某个状态的价值和其后继状态的价值之间的关系。

## 如何解决MDP的问题

解决MDP的问题的三种基本方法：

动态规划（Dynamic Programming）：理论上完美，但需要很强的算力和准确的环境model。
蒙特卡洛（Monte Carlo Methods）：不需要模型，可操作性强，但不太适合一步一步的增量计算。
差分学习（Temporal-Difference Learning）：不需要模型，也是增量式的，但分析起来很复杂。

继续使用机器人炒股票的例子去理解：

1. 动态规划必须保证有环境模型，也就是给定一个状态和动作，我们可以预测下一个状态和奖励；
2. 蒙特卡洛的方法好比，机器人参与了好几个系列的买卖决策操作，然后根据最终的收益，去更新之前的每个状态的价值和策略。
3. 差分学习的方法好比，机器人每一次买卖操作，都会有一个收益，根据这个收益直接更新状态的价值和策略。
需要注意的是，动态规划因为有环境模型，所以总是可以知道某一个状态和动作对应的奖励是什么，因此没有“实验”的概念；后面两种方案，都需要用实验中实际产生的奖励作为反馈。

三种基本方法之间又可以相互结合：

- 蒙特卡洛+差分学习，使用多步bootstrap。
- 差分学习+模型学习。

### 近似函数：[3]

- 近似价值函数：目标$J(w) = E_{\\pi}[(v_{\\pi}(S)-\\hat v(S,w))^2]$，使近似的价值函数接近实际的价值函数。
    - `Q-Learning with Linear Function Approximation`
    - `Deep-Q Learning（DQN）`：使用了`Experience Replay`和`fixed Q-learning target`。
- 拟合策略函数：目标$J_1(\\theta)=V^{\\pi_{\\theta}}(s_1) = E_{\\pi_{\\theta}}[v_1]$，使找到的策略函数可以使价值函数最大化。
    - `Monte-Carlo Policy Gradient (REINFORCE)`
- 近似价值函数 + 拟合策略函数
    - ` Actor-Critic`：Critic：更新价值函数的参数$w$ 。Actor：更新策略的参数 $θ$ ，使用critic建议的方向。"

[1]: https://yuancl.github.io/2019/01/21/rl/%E9%A9%AC%E5%B0%94%E7%A7%91%E5%A4%AB%E5%86%B3%E7%AD%96%E8%BF%87%E7%A8%8B/
[2]: https://applenob.github.io/rl_note/intro-note-3/
[3]: https://github.com/applenob/rl_learn/blob/master/learning_route.ipynb
