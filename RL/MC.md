

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 16:49:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 16:49:45
 * @Description:
 * @TODO::
 * @Reference:https://medium.com/@zsalloum/monte-carlo-in-reinforcement-learning-the-easy-way-564c53010511
-->



在蒙特卡洛（MC）中，我们玩游戏的情节直到到达终点，我们从途中获得了奖励然后返回情节的开始。 我们重复此方法至足够的次数，然后平均每个状态的值。

If you recall the formula of the State-Value function from “Math Behind Reinforcement Learning” article:
Image for post
It is not possible to compute the V(s) because p(s’,r|s,a) is now unknown to us.
