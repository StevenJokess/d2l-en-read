

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 21:30:50
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 21:31:05
 * @Description:
 * @TODO::
 * @Reference:
-->
Dynamic Computation
动态计算(Dynamic Computation)是指根据计算环境（如电量）自动调整网络的消耗。

实现方法：

训练多个不同大小的网络，环境好时使用大网络，环境差时使用小网络；
在网络中间层设置一些分类器，环境好时使用深层的分类器，环境差时使用浅层的分类器；


在浅层加分类器训练时会影响深层的分类精度，一种解决方法是Multi-Scale Dense Networks(MSDN).https://arxiv.org/abs/1703.09844
