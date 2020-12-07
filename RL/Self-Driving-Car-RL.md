

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 19:03:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 19:05:31
 * @Description:
 * @TODO::
 * @Reference:https://github.com/FLHonker/Self-Driving-Car-RL
-->

此无人车AI项目使用的Deep Q-learning算法，是DeepMind在2013年发明的深度强化学习算法，将Q-learning的思想与神经网络算法结合，也算是现代强化学习算法的源头了。研究者用这个算法在2015年让计算机学会了49种Atari游戏，并在大部分游戏中击败了人类。从适用性上来讲，我们不需要告诉AI具体的规则，只要让它不断摸索，它就能慢慢从中找到规律，完成许多之前被认为只有人类能完成的智力活动。

计算出的L值被反馈(back-propagation)以计算每个突触(绿色圈圈)的权重w，使得L值可以尽量小。

需要注意的是，上面的过程我们称之为"学习"(learn)，尽管我们对比了以前的Q值并反馈给输入端，但是这一次计算得到的Q值是不变的。我们接下来要做的是根据这一次计算得到的Q值，做出一个"动作"(act)。

那么*为什么不直接选择最大的Q值所对应的action，而是用Softmax-Function来做决定*？这里就涉及到几种动作选择策略。直接选择最大的Q值并不是不可以，这种就叫做贪心策略，缺点是很容易陷入局部最优解。因为如果执行了某个动作后，最终达到了目标，那么这种策略就会在后续此状态时一直选择这种动作，导致没有机会探索全局最优解。
