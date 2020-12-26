

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:21:38
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 20:30:16
 * @Description:
 * @TODO::
 * @Reference:
-->

Energy-Based GAN (EBGAN)
https://arxiv.org/pdf/1609.03126.pdf

EBGAN在边缘的生成效果上更流畅, 而且加了特殊的正则项, 在生成的类别上, EBGAN更倾向于生成不同的脸型和人种[2]

$L_{D}^{E B G A N}=D_{A E}(x)+\max \left(0, m-D_{A E}(G(z))\right)$
$L_{G}^{E B G A N}=D_{A E}(G(z))+\lambda \cdot P T$

![](img\EBGAN.png)

[2]: https://zhuyinlin.github.io/build/html/algorithm/GAN.html#sgan-stacked-gan
