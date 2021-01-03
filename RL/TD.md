# Temporal-Difference Learning

## 时序差分（Temporal-Difference）简介

- 时序差分是强化学习的核心观点。
- 时序差分是DP和MC方法的结合。
- MC要等一个完整的序列结束，比如玩21点扑克，直到玩完才能知道是胜是负；相反，时序差分每经历一步，都会更新价值函数，因为每一步都会观察到一个新的Reward，比如Grid World，每走一步都知道reward是什么。
- TD往往比MC高效；TD和MC都使用经验（experience）来解决预测问题。
- 所谓差分就是下一个时刻的估计和当前时刻的估计的差。


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

https://applenob.github.io/rl_note/intro-note-6/

