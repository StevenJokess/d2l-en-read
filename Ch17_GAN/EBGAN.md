

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:21:38
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 19:22:40
 * @Description:
 * @TODO::
 * @Reference:
-->

Energy-Based GAN (EBGAN)
https://arxiv.org/pdf/1609.03126.pdf

$L_{D}^{E B G A N}=D_{A E}(x)+\max \left(0, m-D_{A E}(G(z))\right)$
$L_{G}^{E B G A N}=D_{A E}(G(z))+\lambda \cdot P T$

![](img\EBGAN.png)
