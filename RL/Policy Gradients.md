

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:03:50
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 18:04:25
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/99679223
-->

# Policy Gradients

Policy Gradients的是一种基于策略的强化学习方法，基于策略的意思就是直接根据状态输出动作或者动作的概率。
我们使用神经网络输入当前的状态，网络就可以输出我们在这个状态下采取每个动作的概率。
与之前的DQN和Q-Learmnig这类基于价值的学习方法相比，二者的主要不同为：
1、基于价值的强化学习方法对应的最优策略通常是确定性策略，一般是从众多行为价值中选择一个最大价值的行为，仅有一定的概率会随机选择，而有些问题的最优策略却是随机策略，无法通过基于价值的学习方法求解。此时Policy Gradients可以起到很好的作用。
2、DQN之类的方法一般都是只处理离散动作，无法处理连续动作。
