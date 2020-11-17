

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 20:32:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 20:50:09
 * @Description:
 * @TODO::
 * @Reference:
-->
# SRResnet/SRGAN：使用生成对抗网络进行图像超分辨率.

Implementation of Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network.

直接使用MSE损失函数训练的超分辨率模型，在PSNR和SSIM等评价指标上能够得到较高的结果，但图像细节显示依旧较差。作者利用生成对抗网络的方法得到视觉特性较好的结果。



作者提出的生成对抗网络结构如图所示。[3]

生成器结构参考了ResNet，输入低分辨率图像得到高分辨率图像，这一部分可作为SRResNet单独使用。
判别器结构参考了VGG，输入真实图像和生成的高分辨率图像，对二者进行分类。


模型的训练按照生成对抗网络的损失进行：

![生成对抗网络的损失](https://cdn.mathpix.com/snip/images/-5e18_2A6ahiFJw1RaOCvndiHbehUnrTle3tIcJCC-s.original.fullsize.png)

作者提出了感知损失函数(perceptual loss $l^{S R},$ 由内容损失函数(content loss $)_{X}^{S R}$ 和对抗损 失函数(adversarial loss $) l_{G e n}^{S R}$ 组成。
内容损失函数(content $\operatorname{loss}) l_{X}^{S R}$ 基于一个预训练的VGG19网络, 通过比较生成图像和真实图像 的网络中特征差异进行定义。其中 $\Phi_{i, j}$ 表示VGG19网络中第i个池化层之前的第j个卷积层(在激 活函数之后)的特征图。
对抗损失函数(adversarial loss $l_{G e}^{R}$ 试图使判别器无法正确的分类生成器获得的结果


SRGAN
[1]: https://arxiv.org/abs/1609.04802
[2]: https://github.com/eriklindernoren/Keras-GAN/blob/master/srgan/srgan.py
[3]: https://0809zheng.github.io/2020/08/10/srresnet.html
