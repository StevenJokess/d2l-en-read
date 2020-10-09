

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-09 15:19:47
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-09 15:21:50
 * @Description:
 * @TODO::
 * @Reference:https://www.nowcoder.com/tutorial/95/a785d36cf4264dfa93c3de133d0bb339
-->

## SGD,Momentum,Adagard,Adam原理

SGD为随机梯度下降,每一次迭代计算数据集的mini-batch的梯度,然后对参数进行跟新。

Momentum参考了物理中动量的概念,前几次的梯度也会参与到当前的计算中,但是前几轮的梯度叠加在当前计算中会有一定的衰减。

Adagard在训练的过程中可以自动变更学习的速率,设置一个全局的学习率,而实际的学习率与以往的参数模和的开方成反比。

Adam利用梯度的一阶矩估计和二阶矩估计动态调整每个参数的学习率,在经过偏置的校正后,每一次迭代后的学习率都有个确定的范围,使得参数较为平稳。

## L1不可导的时候该怎么办

当损失函数不可导,梯度下降不再有效,可以使用坐标轴下降法,梯度下降是沿着当前点的负梯度方向进行参数更新,而坐标轴下降法是沿着坐标轴的方向,假设有m个特征个数,坐标轴下降法进参数更新的时候,先固定m-1个值,然后再求另外一个的局部最优解,从而避免损失函数不可导问题。
使用Proximal Algorithm对L1进行求解,此方法是去优化损失函数上界结果。
