

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 20:28:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:29:14
 * @Description:
 * @TODO::
 * @Reference:
-->

相比有监督学习和无监督学习，强化学习在机器学习领域的起步更晚。虽然早在1980年代就出现了时序差分算法[42-44]，但对于很多实际问题，我们无法用表格的形式列举出所有的状态和动作，因此这些抽象的算法无法大规模实用。






神经网络与强化学习的结合，即深度强化学习46-50]，才为强化学习带来了真正的机会。在这里，深度神经网络被用于拟合动作价值函数即Q函数，或者直接拟合策略函数，这使得我们可以处理各种复杂的状态和环境，在围棋、游戏、机器人控制等问题上真正得到应用。神经网络可以直接根据游戏画面，自动驾驶汽车的摄像机传来的图像，当前的围棋棋局，预测出需要执行的动作。其典型的代表是DQN[46]这样的用深度神经网络拟合动作价值函数的算法，以及直接优化策略函数的算法[47-50]。


[46]Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou. Playing Atari with Deep Reinforcement Learning. NIPS 2013.

[47]Mnih, V., Badia, A. P., Mirza, M., Graves, A., Harley, T., Lillicrap, T. P., Silver, D., and Kavukcuoglu, K. (2016). Asynchronous methods for deep reinforcement learning. In the International Conference on Machine Learning (ICML).

[48]Williams, R. J. (1992). Simple statistical gradient-following algorithms for connectionist reinforcement learning. Machine Learning, 8(3):229–256.

[49]Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., and Riedmiller, M. (2014). Deterministic

policy gradient algorithms. In the International Conference on Machine Learning (ICML).

[50]Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., and Wierstra, D.

(2016). Continuous control with deep reinforcement learning. In the International Conference on

Learning Representations (ICLR).



[51]S. Hochreiter, J. Schmidhuber. Long short-term memory. Neural computation, 9(8): 1735-1780, 1997.

[52] David Silver, et al. Mastering the Game of Go with Deep Neural Networks and Tree Search. Nature, 2016.

