

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 22:31:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 22:31:08
 * @Description:
 * @TODO::
 * @Reference:https://github.com/bentrevett/pytorch-rl/blob/master/3%20-%20Advantage%20Actor%20Critic%20(A2C)%20%5BCartPole%5D.ipynb
-->
SEED = 1234

train_env.seed(SEED);
test_env.seed(SEED+1)
np.random.seed(SEED);
torch.manual_seed(SEED);
