

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-19 20:01:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 19:51:15
 * @Description:
 * @TODO::
 * @Reference:
-->

强化学习是一种利用试错的方法训练主体在复杂环境中进行决策的过程，主体在训练过程中的典型目标是需要最大化在环境中所获取的奖励信息，而这些奖励则与大量的参数相关，包括速度、好奇心和审美特征等等。然而，由于难以定义或者太过稀疏，为特定的任务设计奖励函数却是十分困难的，所以这一问题很难用强化学习来解决。

模仿学习（Imitation learning，IL）方法为强化学习提供了一种可能的解决方案，从专家的示教中学习如何解决问题。然而前沿的模仿学习方法都依赖于对抗训练，利用最小/最大优化流程进行训练，使得算法在训练时不太稳定也不便于部署。

## 对抗模仿学习

前沿的对抗模仿学习方法与生成对抗网络十分类似，都是利用生成器（策略）来最大化对于判别器（奖励）的混淆，而判别器则会努力区分主体的状态行为与专家间的区别。

对抗模仿学习可以被归结为分布匹配问题，例如在度量空间中最小化概率分布间的距离。然而就像GAN一样，对抗模仿学习仅仅依赖于最小/最大化优化，会使训练过程存在不可避免的稳定性问题。



PWIL的优势在于不仅可以覆盖专家的行为，同时其奖励函数无需与环境进行交互同时易于调节。这为未来模仿学习领域的探索打开了新的方向。PWIL还可以应用于只有试教状态存在的情况下，最终也能用于基于视觉观察的行为操控中去。[1][2]

能模仿人的智能体[4]
这是通过GANs实现模仿学习。不同于传统的奖励机制，某些AI研究人员希望针对自主学习智能体，提出一种全新的方法。

他们将实际的示范数据输入到智能体，然后智能体从中学习并尝试模仿相同的动作。

code[5]

[1]: https://www.zhihu.com/question/376954557/answer/1500668073
[2]: https://ai.googleblog.com/2020/09/imitation-learning-in-low-data-regime.html
[3]: https://github.com/RITCHIEHuang/Awesome-Imitation-Learning
[4]: https://zhuanlan.zhihu.com/p/28504510
[5]: https://github.com/openai/imitation
