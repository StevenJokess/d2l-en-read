

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 00:30:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 00:31:07
 * @Description:
 * @TODO::
 * @Reference:https://github.com/bentrevett/pytorch-rl/blob/master/5%20-%20Proximal%20Policy%20Optimization%20(PPO)%20%5BCartPole%5D.ipynb
-->
import torch.distributions as distributions
dist = distributions.Categorical(action_prob)
