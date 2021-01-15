# Temporal-Difference Learning

## 时序差分（Temporal-Difference）简介

- 时序差分是强化学习的核心观点。
- 时序差分是DP和MC方法的结合。
- MC要走完完整episode才能更新Q值，比如玩21点扑克，直到玩完才能知道是胜是负；相反，时序差分只需要后面一步的单个即时收益 $R_{t+1}$ 和下一个状态的 $Q\left(S_{t+1}, A_{t+1}\right)$ 估计值通过差分思想来更新当前状态的 $Q\left(S_{t+1}, A_{t+1}\right)$ (由于只看1步, 也称onestep TD learning)，适用于不完整的episode的情形，因为每一步都会观察到一个新的Reward，比如Grid World，每走一步都知道reward是什么。
- TD往往比MC高效，通过猜测来更新猜测；TD和MC都使用经验（experience）来解决预测问题。
- 所谓差分就是下一个时刻的估计和当前时刻的估计的差。

## MC vs. TD：

- 用通俗的语言描述就是，对于某个state的value更新，MC会把这个state后面所有的state都计算R，用来计算G；而TD只会计算当前下一个状态的R，其他后面的R不算，采用当前估计的value来替代。
- MC有高方差，0偏差，对初始值不敏感，使用sample，不使用bootstrapping。
- TD往往更高效，且对初始值敏感，使用sample，使用bootstrapping。



## 什么是stationary？

stationary：环境不随时间变化而变化；
non-stationary：环境会随时间变化而变化。

## TD(0)

因为直接使用现有的估计取更新估计，因此这种方法被称为自举（bootstrap）

$$
\begin{array}{l}
\text { Algorithm TD(0) } \\
\hline
\text { Input: the policy $\pi$ to be evaluated}\\
 \text { Initialize $V(s)$ arbitrarily $\left(\right.$ e.g., $\left.V(s)=0, \forall s \in \mathcal{S}^{+}\right)$} \\
\text { Repeat (for each episode): } \\
\qquad \begin{array}{l}
\text { Initialize $S$ } \\
\text { Repeat (for each step of episode): } \\
\qquad \begin{array}{l}
\text { $A \leftarrow$ action given by $\pi$ for $S$ }\\
\text { Take action $A,$ observe $R, S^{\prime}$}\\
\text { $V(S) \leftarrow V(S)+\alpha\left[R+\gamma V\left(S^{\prime}\right)-V(S)\right]$}\\
\text { $S \leftarrow S^{\prime}$}\\
\end{array} \\
\end{array} \\
\text { until $S$ is terminal } \\
\end{array}
$$

$\text { TD error: } \delta_{t}=R_{t+1}+\gamma V\left(S_{t+1}\right)-V\left(S_{t}\right)$



```py
def temporal_difference(values, alpha=0.1, batch=False):
    state = 3
    trajectory = [state]
    rewards = [0]
    while True:
        ...
        # TD update
        if not batch:
            values[old_state] += alpha * (reward + values[state] - values[old_state])
        ...
        rewards.append(reward)
    return trajectory, rewards
```

## n-step TD：

TODO:

n-step TD learning是这两种 算法的折中，它不是固定的只向采样1步或是全采样，它可以通过可调节的步长n来决定向后采样 几步来更新。n-step TD思想虽然很好理解，但书中算法公式的下标还是有点绕，以下我们先简 述n-step Bootstrapping的思想, 然后从火车过桥模型的例子来理解算法中的下标。[3]

## TD($\lambda$)：

- Forward-view：

- 每个n-step的 $G_{t}$ 加权求和 $,$ 权重: $(1-\lambda) \lambda^{n-1}, G_{t}^{\lambda}=(1-\lambda) \sum_{n=1}^{\infty} \lambda^{n-1} G_{t}^{n}$
- V\left(S_{t}\right) \leftarrow V\left(S_{t}\right)+\alpha\left(G_{t}^{\lambda}-V\left(S_{t}\right)\right)$



## Forward-view和Backward-view:

- Forward-view只能计算完整的episodes。 Backward-view可以计算不完整的episodes。
- Forward-view提供了理论。
- Backward-view提供了机制。 Forward-view倾向于最高频的状态。

## Eligibility Traces:

- Eligibility Traces结合了高频的倾向和最近的倾向。
- $E_{0}(s)=0$
- $E_{t}(s)=\gamma \lambda E_{t-1}(s)+\mathbf{1}\left(S_{t}=s\right),$ 累加代表了高频倾向; 但之前的时刻会衰减代表了最近的倾向。

## Backward-view TD( $\lambda$ ) :

- \delta_{t}=R_{t+1}+\gamma V\left(S_{t+1}-V\left(S_{t}\right)\right)$
- V(s) \leftarrow V(s)+\alpha \delta_{t} E_{t}(s)$

## 单步更新与回合更新（Monte-carlo update&Temporal-Difference update）

单步更新，顾名思义，也就是每次执行一次action后，进行一次更新；而回合更新，就是在一次训练的epoch中，结束后才进行更新。
用我现在在研究的量化交易与人工智能来举个例子，就好比每次执行一次买或卖的action后，更新一下模型中的参数，这就是单步更新；而从开盘到结束作为一次的训练epoch，从开始到结束的这一回合训练过程中，所有动作都是根据目前的参数进行选择，直到结束这一回合的训练后，才进行更新参数。
个人目前觉得，单步更新容易陷入局部最小，而回合更新则更全局一些，但是回合更新要等到这一回合的训练结束才进行参数更新，所以学习的效率不高。

https://applenob.github.io/rl_note/intro-note-6/
https://github.com/applenob/rl_learn/blob/master/class_note.ipynb
[3]: [强化学习]从火车过桥模型理解n-step TD Learning - 阿亮算法的文章 - 知乎
https://zhuanlan.zhihu.com/p/295098730s
[6]: https://blog.csdn.net/FrankieHello/article/details/78821488?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-11.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-11.control
