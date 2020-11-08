

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 16:06:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 16:07:44
 * @Description:
 * @TODO::
 * @Reference:
-->
GAN模型是基于Lipschitz连续空间, 且依赖于生成样本是可微的, 一般对离散数据不起作用. Devon等[2]提出一种引入离散数据的GAN训练方法——边界寻找生成对抗网络, 称为BGAN. BGAN使用来自鉴别器的估计差分度量来计算生成的样本的重要性权重, 为训练生成器提供一个基于KL-散度的策略梯度, 且这个策略梯度引入奖励机制, 使用重要权重作为奖励信号. GAN应用于离散数据的另一种方法是Tong等[3]提出的最大似然增强的离散生成对抗网络, 其对GAN的目标没有直接进行优化, 而是使用遵循对数似然的对应的输出推导出了一种全新的、低方差的目标, 主要是为了解决在离散数据上的反向传播困难的问题. 虽然GAN能应用于离散数据空间, 但这几种方法实现的效果不是很好, 不如基于连续空间的效果显著.

[1]: http://www.c-s-a.org.cn/html/2019/11/7156.html#outline_anchor_12
[2]: Hjelm RD, Jacob AP, Che T, et al. Boundary-seeking generative adversarial networks. arXiv preprint arXiv: 1702.08431v4, 2018.
[3]: Che T, Li YR, Zhang RX, et al. Maximum-likelihood augmented discrete generative adversarial networks. arXiv preprint arXiv: 1702.07983, 2017.
