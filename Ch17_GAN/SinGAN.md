

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 18:01:03
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 18:01:21
 * @Description:
 * @TODO::
 * @Reference:2019 年过去了，人工智能领域干了些什么？ - 量子位的回答 - 知乎
https://www.zhihu.com/question/365135309/answer/999770457
-->


# SinGAN：Learning a Generative Model from a Single Natural Image

SinGAN仅在一张图像上进行训练，这张图像既是训练样本也是测试样本，SinGAN是一种非条件（基于随机噪声）的生成对抗模型，利用多尺度金字塔结构的全卷积GAN来提取图像内部分布信息，生成具有相同视觉内容的高质量、多变的样本，每个GAN负责捕捉不同尺度的图像分布，多种图像处理任务都可以应用SinGAN，如图像绘制、编辑、融合，超分辨率重建和动画化。

它能通过单训练样本实现超分辨率、图图转换、Harmonization、图像编辑和单图像动画等功能，有种统一计算机视觉任务的万能算法的感觉。

SinGAN属于“无条件”的生成模型，它能俘获图像块的内部数据分布。SinGAN由全卷积的金字塔GAN网络构成，


强调SinGAN网络的学习目的是：通过无条件生成模型，获得单张训练图像x的内部统计信息。必须将SinGAN和其它的Conditional GAN（CGANs）区分开，因为SinGAN输入是一张图上的图像patch，而CGANs输入是数据库中的整张图像。下面将从多尺度结构和损失函数两个方面进行分析，判别器Dn的功能仅仅为辨别其输入是真实样本还是伪造样本



## 损失函数

SinGAN的训练方式与原始GAN相似，区别仅是多了一个重构损失项：

$\min _{G_{n}} \max _{D_{n}} \mathcal{L}_{\mathrm{adv}}\left(G_{n}, D_{n}\right)+\alpha \mathcal{L}_{\mathrm{rec}}\left(G_{n}\right)$

对抗性损失Ladv用于惩罚生成样本xn~分布和真实样本xn分布之间的距离，

对抗损失是生成器和判别器互相博弈，

Reconstruction loss We want to ensure that there exists a specific set of input noise maps, which generates the original image $x .$ We specifically choose $\left\{z_{N}^{\mathrm{rec}}, z_{N-1}^{\mathrm{rec}} \ldots, z_{0}^{\mathrm{rec}}\right\}=\left\{z^{*}, 0, \ldots, 0\right\},$ where $z^{*}$ is some
fixed noise map (drawn once and kept fixed during training). Denote by $\tilde{x}_{n}^{\text {rec }}$ the generated image at the $n$ th scale when using these noise maps. Then for $n<N$,


$$
\mathcal{L}_{\mathrm{rec}}=\left\|G_{n}\left(0,\left(\tilde{x}_{n+1}^{\mathrm{rec}}\right) \uparrow^{r}\right)-x_{n}\right\|^{2}
$$
and for $n=N,$ we use

Gn输入仅仅是噪声z*，重构损失如下：

其中重构损失Lrec目的是确保噪声图能够产生和xn相近的样本。

$\mathcal{L}_{\mathrm{rec}}=\left\|G_{N}\left(z^{*}\right)-x_{N}\right\|^{2}$.


以色列理工学院和谷歌联合出品，拿下ICCV2019最佳论文的SinGAN：
https://arxiv.org/abs/1905.0116
[2]: ICCV2019最佳论文奖SinGAN（一）原理剖析 - 机器学习入坑者的文章 - 知乎 https://zhuanlan.zhihu.com/p/95070686
