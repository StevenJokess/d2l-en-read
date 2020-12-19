

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 23:08:08
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 00:39:53
 * @Description:
 * @TODO::
 * @Reference:https://spinningup.openai.com/en/latest/algorithms/sac.html
-->

Soft Actor-Critic

SAC concurrently learns a policy \pi_{\theta} and two Q-functions Q_{\phi_1}, Q_{\phi_2}. There are two variants of SAC that are currently standard: one that uses a fixed entropy regularization coefficient \alpha, and another that enforces an entropy constraint by varying \alpha over the course of training. For simplicity, Spinning Up makes use of the version with a fixed entropy regularization coefficient, but the entropy-constrained variant is generally preferred by practitioners.


The SAC algorithm has changed a little bit over time. An older version of SAC also learns a value function V_{\psi} in addition to the Q-functions; this page will focus on the modern version that omits the extra value function.


[MinitaurBulletEnv with SAC (Soft-Actor-Critic).](https://www.youtube.com/watch?v=uEAqyEwvi54)
Considered solved if the achieved score exceeds 15 in 100 consecutive episodes. Solved in 1745 episodes (trained for 20 hours).

https://github.com/higgsfield/RL-Adventure-2/blob/master/7.soft%20actor-critic.ipynb
