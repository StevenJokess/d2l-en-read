

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 21:27:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 21:45:31
 * @Description:
 * @TODO::
 * @Reference:
-->

Q-learning（off-policy）

Q-learning learns the action-value function Q(s, a): how good to take an action at a particular state. For example, for the board position below, how good to move the pawn two steps forward. Literally, we assign a scalar value over the benefit of making such a move.
Q is called the action-value function (or Q-value function in this article).[4]

Q 学习（Q- learning）方法。 它自然的包含了两个部分， 一个是通过经历不停的强化对某个状态行为下趋势的认知 ，另一个则是根据这个趋势，每步走出当下最优的选择（这不就是理性人决策吗！）。[5]

基于off-policy思想的Q-learning，与Monte Carlo 方法中off-policy的灵魂思路是一致的，除了更新价值的步数不一样之外。[2]

更新Q值时所使用的方法是沿用既定的策略（on-policy）还是使用新策略（off-policy）。[3]

Q-learning虽然具有学习到全局最优的能力，但是其收敛慢。[2]

γ越大，小鸟就会越重视以往经验，越小，小鸟只重视眼前利益（R）。

定义Q value，它就是在理性人（没步下做最优选择）假设下每一步的收益按贴现率加和来的未来收益总期望。这么绕口，其实我还没说下半句， 那就是在此刻某个行为下的期望，太累了，分开讲。 这整个定义，就是充满智慧的Q - value。[5]

然后Q - learning呢？ 刚说过了， 学习，是通过既往的经验， Q - learning的过程就是根据行为做出后得到的真实境遇（可以是奖励或是惩罚，也可以是新的位置的Q值）来更新这个期望的过程， that‘s all。 当Q 值被更新， 你的行为也就被更新了 ，因为我每一次的行为无非选择最大的Q值。[5]


归根结底还是贝尔曼方程，策略是 arg max， $\quad P_{x^{\prime}}$ 用后验概率，所以贝尔曼方程表示为
$$
Q(s, a)=r+\gamma \max Q\left(s^{\prime}, a^{\prime}\right)
$$
因为每次执行和观测都有噪声，所以在更新 Q 函数时，用学习率的方式。（图中的注释并不是很正确，所 谓现实，只不过是新的估计，应该是新做计和旧估计的差值）[6]


```md


[1]: https://www.zhihu.com/question/26408259
[2]: https://www.zhihu.com/question/26408259/answer/467132543
[3]: https://www.zhihu.com/question/57159315/answer/164323983
[4]: https://medium.com/@jonathan_hui/rl-dqn-deep-q-network-e207751f7ae4
[5]: https://www.zhihu.com/question/26408259/answer/389938864
[6]: 如何用简单例子讲解 Q - learning 的具体过程？ - Michael Jackson的回答 - 知乎
https://www.zhihu.com/question/26408259/answer/540258528
```
