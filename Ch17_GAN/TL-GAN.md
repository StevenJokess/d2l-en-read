

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 20:57:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 20:59:17
 * @Description:
 * @TODO::
 * @Reference:https://wangsp.blog.csdn.net/article/details/83477553
-->

Transparent Latent-space GAN 模型
TL-GAN：一种新型高效的可控合成和编辑方法。它允许用户使用单个网络逐渐调整单个或多个特征。除此之外，添加新的可调特征可以在一个小时之内非常高效地完成。

通过用预训练的 pg-GAN 进行实验，我发现潜在空间具有两个良好的特性：

它很稠密，这意味着空间汇总的大多数点能够生成合理的图像；
它相当连续，意味着潜在空间中两点之间的插值通常会导致相应图像的平滑过渡。
考虑到这两点，我觉得可以在潜在空间中找到能够预测我们关心的特征（如，女性-男性）的方向。如果是这样的话，我们可以把这些方向的单位向量用作控制生成过程（更男性化或更女性化）的特征轴。


