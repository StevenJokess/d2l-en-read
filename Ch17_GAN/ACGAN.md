

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-26 21:09:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 18:35:29
 * @Description:
 * @TODO::
 * @Reference:https://github.com/MorvanZhou/mnistGANs/blob/main/acgan.py
-->

# Conditional Image Synthesis with Auxiliary Classifier GANs（辅助类别的GAN）


ACGAN在Imagenet上的生成效果令人惊叹，它特意学习了一个类别下的图片结构：

与CGAN不同的是它在判别器D的真实数据x也加入了类别c的信息，这样就进一步告诉G网络该类的样本结构如何，从而生成更好的类别模拟：

在ACGAN中，生成器的输入也附加标签/条件信息，判别器的输出则有两部分，一部分判断真假，一部分输出类别。[3]

[2]
$L_{D, Q}^{A C G A N}=L_{D}^{G A N}+E[P(\operatorname{class}=c \mid x)]+E[P(\operatorname{class}=c \mid G(z))]$
$L_{G}^{A C G A N}=L_{G}^{G A N}+E[P(\operatorname{class}=c \mid G(z))]$



[1]: https://arxiv.org/pdf/1610.09585.pdf
[2]: http://nooverfit.com/wp/%E7%8B%AC%E5%AE%B6%EF%BD%9Cgan%E5%A4%A7%E7%9B%98%E7%82%B9%EF%BC%8C%E8%81%8A%E8%81%8A%E8%BF%99%E4%BA%9B%E5%B9%B4%E7%9A%84%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C-lsgan-wgan-cgan-info/
[3]: https://zhuanlan.zhihu.com/p/94206978


