

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-30 19:53:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 19:57:43
 * @Description:
 * @TODO::
 * @Reference:https://yuancl.github.io/2019/01/21/rl/%E9%A9%AC%E5%B0%94%E7%A7%91%E5%A4%AB%E5%86%B3%E7%AD%96%E8%BF%87%E7%A8%8B/
-->

# 马尔科夫决策过程

## 背景

求解强化学习问题可以理解为如何最大化个体在与环境交互过程中获得的累积奖励
当环境状态是完全可观测时，个体可以通过构建马尔科夫决策过程来描述整 个强化学习问题。有时候环境状态并不是完全可观测的，此时个体可以结合自身对于环境的历史 观测数据来构建一个近似的完全可观测环境的描述
从这个角度来说，几乎所有的强化学习问题 都可以被认为或可以被转化为马尔科夫决策过程

马尔科夫决策过程(Markov decision process, MDP)是 由 ⟨S, A, P, R, γ⟩ 构成的一个元组，其中:

S 是一个有限状态集
A 是一个有限行为集
P 是集合中基于行为的状态转移概率矩阵: $P_{s s^{\prime}}^{a}=E\left[R_{t+1} \mid S_{t}=s, A_{t}=a\right]$
R 是基于状态和行为的奖励函数: $R_{s}^{a}=E\left[R_{t+1} \mid S_{t}=s, A_{t}=a\right]$
γ 是一个衰减因子:γ ∈ [0, 1]

相关概念
策略
个体在给定状 态下从行为集中选择一个行为的依据则称为策略 (policy)，用字母 π 表示。策略 π 是某一状态下基于行为集合的概率分布:

$\circ$ 当给定一个马尔科夫决策过程:M $=\langle\mathrm{S}, \mathrm{A}, \mathrm{P}, \mathrm{R}, \mathrm{Y}\rangle$ 和一个策略 $\pi,$ 那么状态序列 $S_{1}, S_{2}, \ldots$ 是一个符合马尔科夫过程
$\left\langle S, P_{\pi}\right\rangle$ 的采样
$\circ$ 价值函数
价值函数 $v_{\pi}(s)$ 是在马尔科夫决策过程下基于策略 $\pi$ 的状态价值函数, 表示从状态 s开始, 遵循当前策略 $\pi$ 时所获得
的收获的期望: $v_{\pi}(s)=E\left[G_{t} \mid S_{t}=s\right]$
。 行为价值函数(状态行为对价值函数)
一个基于策略 $\pi$ 的行为价值函数 $q_{\pi}(s, a),$ 表示在遵循策略 $\pi$ 时，对当前状态 $s$ 执行某一具体行为 a 所能的到 的收获
的期望: $q_{\pi}(s, a)=E\left[G_{t} \mid S_{t}=s, A_{t}=a\right]$
。贝尔曼方程
同理, 可推导出如下两个方程
$$
\begin{array}{l}
v_{\pi}(s)=E\left[R_{t+1}+\gamma v_{\pi}\left(S_{t+1}\right) \mid S_{t}=s\right] \\
q_{\pi}(s, a)=E\left[R_{t+1}+\gamma q_{\pi}\left(S_{t+1}, A_{t+1}\right) \mid S_{t}=s, A_{t}=a\right]
\end{array}
$$

## 最优价值函数


背景：
是否存在一个基于某一策略的价值函数， 在该策略下每一个状态的价值都比其它策略下该状态的价值高?如果存在如何找到这样的价值 函数?这样的价值函数对应的策略又是什么策略?
最优状态价值函数
是所有策略下产生的众多状态价值函数 中的最大者
最优行为价值函数(optimal action-value function)
是所有策略下产生的众多行为价 值函数中的最大者:
贝尔曼优化方程
最优状态行为价值
