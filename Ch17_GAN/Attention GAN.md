

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 21:12:36
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 21:15:11
 * @Description:
 * @TODO::
 * @Reference:https://wangsp.blog.csdn.net/article/details/83792876
-->

受 GAN Progressive Growing 的启发（参见《Progressive Growing of GANs for Improved Quality, Stability, and Variation》）设计出的训练结构。不同之处在于层数保持不变——我只是不断改变输入的尺寸并调整学习率，以确保尺寸之间的转换顺利进行。似乎基本最终结果是相同的——训练更快、更稳定，且泛化效果更好。


