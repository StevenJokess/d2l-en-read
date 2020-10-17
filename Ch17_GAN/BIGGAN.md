

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 16:54:42
 * @Description:
 * @TODO::
 * @Reference:
-->

在 SAGAN 的基础上，BigGAN [9]尝试将 GAN 的训练扩展到大规模上去，利用正交 正则化等技巧保证训练过程的稳定性。BigGAN 的意义在于启发人们，GAN 网络的训练同 样可以从大数据、大算力等方面受益。BigGAN 图片生成效果达到了前所未有的高度： Inception score 记录提升到 166.5(提高了 52.52)；Frechet Inception Distance 下降到 7.4，降 低了 18.65，如图 13.13 所示，图片的分辨率可达512 × 512，图片细节极其逼真。


