

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 21:28:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 14:34:51
 * @Description:
 * @TODO::
 * @Reference:
-->

# Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks


We introduce a class of CNNs called deep convolutional generative adversarial networks (DCGANs), that have certain architectural constraints, and demonstrate that they are a strong candidate for unsupervised learning. Training on various image datasets, we show convincing evidence that our deep convolutional adversarial pair learns a hierarchy of representations from object parts to scenes in both the generator and discriminator.

Generated bedrooms.

DCGAN我们的总结

使用一些架构约束来稳定生成的对抗网络

用条带式卷积(鉴别器)和分数条带式卷积(生成器)替换任何池化层。

在发生器和鉴别器中都使用批范数

为更深层次的架构移除完全连接的隐藏层。最后使用平均池。

除了输出使用Tanh之外，在生成器中对所有层使用ReLU激活。

在鉴别器中对所有层使用LeakyReLU激活。

使用discriminator作为预训练的网络进行CIFAR-10分类，并显示相当不错的结果。

生成非常酷的卧室图像，看起来超级真实

为了让你相信网络没有作弊:

展示内插的潜在空间，过渡非常流畅，潜在空间中的每一幅图像都是卧室。

经过一段时间的训练(以0.0002的学习率)，在这个阶段上网络真的不能背。

为了探究网络学习到的表征，

显示过滤器上的反褶积，以显示最大的激活发生在窗口和床等对象上

找出一种方法来识别和删除在生成中绘制窗口的过滤器。

现在您可以控制生成器不输出某些对象。

因为我们要绊倒了

微笑的女人-中性女人+中性男人=微笑的男人。Whuttttt !

戴眼镜的男士-不戴眼镜的男士+不戴眼镜的女士=戴眼镜的女士。Omg ! !

以一种完全无监督的方式学习了一个潜在空间在这个潜在空间中旋转是线性的。WHHHAAATT ????!!!!!!

图11，在imagenet上训练的飞机有鸟腿。所以cooool。

[1]: https://arxiv.org/abs/1511.06434v2
[2]: https://github.com/Newmu/dcgan_code
