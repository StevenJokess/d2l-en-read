

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 22:49:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 22:52:35
 * @Description:
 * @TODO::
 * @Reference:
-->

## tradeoff

有两种选择，第一种，按照以前的方法（其中之一）来完成这件事（Exploitation）；或者，你可以尝试另一种方法，一种全新的方法（Exploration）；前者可以获得稳定的效果，但是不一定是最优的，后者可能会得到更优的方法，但是也可能得到一个不如以前方法的效果。

同样的情况在强化学习中会一直伴随我们，两种action，选择其中一个是困难的。在下棋的过程中，针对当前的environment，我们的agent以前有类似的经历，是按照过去的经验完成，还是创新一下，采用一种以前没有经验的方法，这个问题dilemma的，而且这两种方法都没有办法保证自己不会失效（fail）

## Goal-Direct & Uncertain Environment

在一个未知的environment里agent要做出他认为正确的action，并且对interaction做出后续的反应。




[1]: Sutton R S, Barto A G. Reinforcement learning: An introduction[J]. 2011.
[2]: https://face2ai.com/RL-RSAB-1-1-2-Reinforcement-Learning/
