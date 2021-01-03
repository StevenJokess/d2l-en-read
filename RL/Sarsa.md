# Sarsa

On-Policy Sarsa Control：

![Sarsa](img\Sarsa.png)


Initialize $Q(s, a), \forall s \in \mathcal{S}, a \in \mathcal{A}(s),$ arbitrarily, and $Q($terminal-state$, \cdot)=0$
Repeat (for each episode):
Initialize $S$ Choose $A$ from $S$ using policy derived from $Q$ (e.g., $\varepsilon$ -greedy) Repeat (for each step of episode):
Take action $A,$ observe $R, S^{\prime}$ Choose $A^{\prime}$ from $S^{\prime}$ using policy derived from $Q$ (e.g., $\varepsilon$ -greedy)
$$
Q(S, A) \leftarrow Q(S, A)+\alpha\left[R+\gamma Q\left(S^{\prime}, A^{\prime}\right)-Q(S, A)\right]
$$
$S \leftarrow S^{\prime} ; A \leftarrow A^{\prime} ;$
until $S$ is terminal

所谓sarsa即，1.使用$\epsilon$-greedy，根据$s$，选择$a$；2.获得奖励$r$，和新的状态$s'$；3.再使用$\epsilon$-greedy，选择$a'$

## Forward View Sarsa($\lambda$):

- $q_{t}^{\lambda}=(1-\lambda) \sum_{n=1}^{\infty} \lambda^{n-1} q_{t}^{(n)}$
- $Q\left(S_{t}, A_{t}\right) \leftarrow Q\left(S_{t}, A_{t}\right)+\alpha\left(q_{t}^{\lambda}-Q\left(S_{t}, A_{t}\right)\right)$

## Backward View Sarsa($\lambda$):

- $E_{0}(s, a)=0$
- $E_{t}(s, a)=\gamma \lambda E_{t-1}(s, a)+\mathbf{1}\left(S_{t}=s, A_{t}=a\right)$
- $\delta_{t}=R_{t+1}+\gamma Q\left(S_{t+1}, A_{t+1}\right)-Q\left(S_{t}, A_{t}\right)$
- $Q(s, a) \leftarrow Q(s, a)+\alpha \delta_{t} E_{t}(s, a)$

### 伪代码

Initialize $Q(s, a)$ arbitrarily, for all $s \in \mathcal{S}, a \in \mathcal{A}(s)$ Repeat (for each episode):
$E(s, a)=0,$ for all $s \in \mathcal{S}, a \in \mathcal{A}(s)$
Initialize $S, A$ Repeat (for each step of episode):
Take action $A,$ observe $R, S^{\prime}$ Choose $A^{\prime}$ from $S^{\prime}$ using policy derived from $Q$ (e.g., $\varepsilon$ -greedy)
$$
\begin{array}{l}
\delta \leftarrow R+\gamma Q\left(S^{\prime}, A^{\prime}\right)-Q(S, A) \\
E(S, A) \leftarrow E(S, A)+1
\end{array}
$$
For all $s \in \mathcal{S}, a \in \mathcal{A}(s)$
$$
\begin{aligned}
Q(s, a) & \leftarrow Q(s, a)+\alpha \delta E(s, a) \\
E(s, a) & \leftarrow \gamma \lambda E(s, a) \\
S \leftarrow S^{\prime} ; A & \leftarrow A^{\prime}
\end{aligned}
$$
until $S$ is terminal


Off-Policy Learning: behaviour policy: $\mu(a \mid s),$ 已知的, 可以用来指导的策略。
Importance Sampling for Off-Policy Monte-Carlo:

## 重要性采样 (估计期望)：

$$
\begin{array}{l}
E_{x \sim P}[f(X)]=\sum P(X) f(X)=\sum Q(x) \frac{P(X)}{Q(X)} f(X)=E_{X} \sim Q\left[\frac{P(X)}{Q(X)} f(X)\right] \\
G_{t}^{\pi / \mu}=\frac{\pi\left(A_{t} \mid S_{t}\right)}{\mu\left(A_{t} S_{t}\right)} \frac{\pi\left(A_{t} S_{t}\right)}{\mu\left(A_{t} S_{t}\right)} \frac{\pi\left(A_{t+1} \mid S_{t+1}\right)}{\mu\left(A_{T} \mid S_{T}\right)} G_{t}
\end{array}
$$
