

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-19 18:53:17
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 18:54:29
 * @Description:
 * @TODO::
 * @Reference:
-->



在多任务中训练一个通用模型——slow，用这个通用模型拓展到其他任务进行训练就会快很多，得到新模型——fast。本文中的模型使用RNN作为训练模型。


把先验知识融入到强化学习算法中过去已经被探索了很多次，而且也有几种不同的形式：

1. 自动调超参数，学习率等
1. 使用分层贝叶斯方法在动力学模型上保持后验，并根据后验应用Thompson采样
1. 许多分层强化学习的工作都提出从以前的任务中提取可重用的技能，以加快对新任务的探索


智能体的学习过程看做目标，用标准强化学习算法进行优化。然后使用RNN处理多个MDP问题，提取先验知识到智能体。




[1]: https://stepneverstop.github.io/rl2.html
[2]: https://arxiv.org/pdf/1611.02779.pdf
