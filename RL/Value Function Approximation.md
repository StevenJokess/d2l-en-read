# Value Function Approximation

对于大型的MDP:

- 之前我们通过一张大表, 表格上有 $V(s)$ 或者 $Q(s, a)$ 。
- 对于大型的MDP问题, 表格不再适用, 于是可以估计价值函数。
- $\hat{v}(s, w) \approx v_{\pi}(s)$
- $\bullet \hat{q}(s, a, w) \approx q_{\pi}(s, a)$
- 使用MC或者TD来更新 $w$ 。


## 随机梯度下降：

・先假设有个已知的 $v_{\pi}(S)$
・目标: $J(w)=E_{\pi}\left[\left(v_{\pi}(S)-\hat{v}(S, w)\right)^{2}\right]$
$\bullet$ 梯度下降: $\Delta w=-\frac{1}{2} \alpha \nabla_{w} J(w)=\alpha E_{\pi}\left[\left(v_{\pi}(S)-\hat{v}(S, w)\right) \nabla_{w} \hat{v}(S, w)\right]$
・随机梯度下降只用sample其中一个: $\Delta w=\alpha\left(v_{\pi}(S)-\hat{v}(S, w)\right) \nabla_{w} \hat{v}(S, w)$

## 特征向量 (Feature Vector) :

- 用来表示一个state。
- $$x(S)=\left(\begin{array}{c}
x_{1}(S) \\
\cdots \\
x_{n}(S)
\end{array}\right)$$

## 线性特征组合

- 用特征的线性组合去表示value function。
$\bullet \hat{v}(S, w)=x(S)^{T} w=\sum_{j=1}^{n} x_{j}(S) w_{j}$
$\cdot \Delta w=\alpha\left(v_{\pi}(S)-\hat{v}(S, w)\right) x(S)$
也就是 update = 步长\times预测误差x特征值

## 增量预测算法 (Incremental Prediction Algorithms)

- 回到“ $v_{\pi}(S)$ 是未知的”这个事实。
- 我们使用以下的方法, 不同的方法使用不同的量去替代 $v_{\pi}(S),$ 称为“TD-Target"。
- M C:$ 使用 $G_{t}, \quad \Delta w=\alpha\left(G_{t}-\hat{v}\left(S_{t}, w\right)\right) \nabla_{w} \hat{v}\left(S_{t}, w\right)$
$\cdot T D(0):$ 使用 $R_{t+1}+\gamma \hat{v}\left(S_{t+1}, w\right)$
$$
\Delta w=\alpha\left(R_{t+1}+\gamma \hat{v}\left(S_{t+1}, w\right)-\hat{v}\left(S_{t}, w\right)\right) \nabla_{w} \hat{v}\left(S_{t}, w\right)
$$
$T D(\lambda):$ 使用 $G_{t}^{\lambda}, \Delta w=\alpha\left(G_{t} t^{\lambda}-\hat{v}\left(S_{t}, w\right)\right) \nabla_{w} \hat{v}\left(S_{t}, w\right)$

## Action-Value Function Approximation: 和Value Function Approximation类似。

## Control with Value Function Approximation:

### 更详细的迭代步骤：

在每个episode的每一步:
- 使用policy选择下一步的action。
- 使用approximate function计算Q函数, greedy选择让Q最大的state作为后继。
- 使用Q函数计算TD-Target
- 使用TD-Target, 利用梯度下降, 更新Q函数。
Batch Reinforcement Learning: 思想：从经验中学习最多的知识, 而不仅仅是碰到一个事件, 改变一下想法。

## Least Squares Prediction:

- 给定近似v函数： $\hat{v}(s, w) \approx v_{\pi}(s)$
- 给定经验数据 $D,$ 由<state, value>对构成: $D=\left\{<s_{1}, v_{1}^{\pi}>, \ldots,<s_{T}, v_{T}^{\pi}>\right\}$
$\cdot L S(w)=\sum_{t=1}^{T}\left(v_{t}^{\pi}-\hat{v}\left(s_{t}, w\right)\right)^{2}$

## 带经验回放的随机梯度下降 (Stochastic Gradient Descent with Experience Replay) :
- $\cdot \Delta w=\alpha\left(v^{\pi}-\hat{v}(s, w)\right) \nabla_{w} \hat{v}(s, w)$
- 最终收立到最小平方差: $w^{\pi}=\underset{w}{\operatorname{argmin} L S(w)}$

## 带经验回放的DQN (Experience Replay in Deep Q-Networks) :

- 1.使用 $\epsilon-$ greed $y$ 在policy中选择动作 $a_{t_{0}}$ 2.保存 $\left(s_{t}, a_{t}, r_{t+1}, s_{t+1}\right)$ 到回放记忆 $\angle D_{\circ}$
- 3.从 $D$ 中抽一个mini-batch: $\left(s, a, r, s^{\prime}\right)_{\circ}$
- 4.使用老参数 $w^{-}$ 计算Q-learning target (fixed Q-learning target)
- 5.优化Q-network和Q-learning之间的MSE:
$$
L_{i}(w)=E_{s, a, r, s^{\prime}} \sim D_{i}\left[\left(r+\gamma \max _{a} \alpha\left(s^{\prime}, a^{\prime} ; w_{i}^{-}\right)\right)^{2}\right]
$$
- 两个Trick：经验回放Experience Replay, fixed Q-learning target
