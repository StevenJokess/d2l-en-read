# Model Free Control

## On-policy learning vs. Off-policy learning：

on代表在任务中学习，从采样的$\pi$中学习$\pi$。（自学）
off代表在某种基础上学习，从采样的$\mu$中学习$\pi$。（有人示范）
On-Policy Monte-Carlo Control：

policy evaluation：Monte-Carlo policy evaluation，$Q≈q_{\pi}$。
policy improvement：$\epsilon$-greedy policy improvement

为什么使用Q？：V的greedy policy improvement依赖于MDP，而Q的则不需要。



## Greedy in the Limit with Infinite Exploration (GLIE)：

希望上面提到的$\epsilon$是衰减的，即到最后的时候，直接采用贪婪选择。
