大致介绍¶
介绍下课程推进的逻辑：

第一章介绍基础概念，用着重分清楚Reward,value function和q function的区别。

第二章介绍MDP，MDP是对环境的一种建模，即state将以一种什么样的方式推进是已知的。重点理解Bellman Expectation Equation和Bellman Optimality Equation，二者本质上都是递推公式，给动态规划打下基础。

第三章介绍如何处理MDP，分为两步：planning和controlling。planning代表如何评估$v_{\pi}$，controlling代表如何根据评估，找到最优的策略$\pi_*$。解决方案包括policy iteration和value iteration。

第四章介绍环境未知的情况下（model free），如何做planning。有两种方法：MC（Monte-Carlo）和TD（Temporal Difference）。

第五章介绍环境未知的情况下，如何做controlling。又根据实验episode的产生，是不是依据目标policy，引出On-Policy和Off-Policy两种方法。主要的算法有：On-Policy Monte-Carlo Control，On-Policy Sarsa Control，Off-Policy Q-learning。

第六章介绍在MDP表格太大的情况下，如何近似价值函数，主要介绍Q-Learning with Linear Function Approximation，Deep-Q Learning（DQN）。

第七章同样针对第六章的情况，但是采用的方法是直接拟合策略函数，引入Monte-Carlo Policy Gradient (REINFORCE)，再分析纯policy gradient的问题，引入Actor-Critic。

[1]: https://github.com/applenob/rl_learn/blob/master/class_note.ipynb
