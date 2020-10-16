

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:18:40
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-16 20:19:04
 * @Description:
 * @TODO::
 * @Reference:
-->
将全模糊图像与打码图像拼接交由生成器的U型网络处理生成图像，再通过判别器判别生成图像是否真实以及是否与打码图像匹配，这样就构成了相应的GAN网络，训练这个GAN网络获得的模型就可以对图像去除马赛克了。值得一提的是，马赛克的算法简单来说是随机无序且不可逆地抹除像素中的色彩信息，从而实现图像模糊的效果。去除马赛克的GAN并不是逆向运算的马赛克算法，而是直接“想象”出合理的色彩信息并将其填充上去而已，并没有做算法的逆向运算，所以去除马赛克后的图像并不一定是原本的图像，只是很相似而已。[1]

[1]: https://weread.qq.com/web/reader/4653238071e86dd54654969k17e328b022b17e62166fad4
