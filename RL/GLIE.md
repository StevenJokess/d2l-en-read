GLIE: Greedy in the Limit with Infinite Exploration[1]

- All state-action pairs are explored infinitely many times $\lim _{k \rightarrow \infty} N_{k}(s, a)=\infty$
- The policy converges on a greedy policy
- $\lim _{k \rightarrow \infty} \pi_{k}(a \mid s)=1\left(a=\arg \max _{a^{\prime} \in A} Q_{k}\left(s, a^{\prime}\right)\right.$
- Improve policy based on new action-value function
- $\epsilon \leftarrow 1 / k$
- $\pi \leftarrow \epsilon-$ greedy $(Q)$
- Theorem: GLIE Monte-Carlo control converges to the optimal action-value function

[1]: Temporal Difference Learning - WJP的文章 - 知乎 https://zhuanlan.zhihu.com/p/57836142
