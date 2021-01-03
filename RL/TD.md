# Temporal-Difference Learning

## 时序差分（Temporal-Difference）简介

- 时序差分是强化学习的核心观点。
- 时序差分是DP和MC方法的结合。
- MC要等一个完整的序列结束，比如玩21点扑克，直到玩完才能知道是胜是负；相反，时序差分每经历一步，都会使用bootstrapping来更新价值函数，适用于不完整的episode的情形，因为每一步都会观察到一个新的Reward，比如Grid World，每走一步都知道reward是什么。
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

https://applenob.github.io/rl_note/intro-note-6/
https://github.com/applenob/rl_learn/blob/master/class_note.ipynb

