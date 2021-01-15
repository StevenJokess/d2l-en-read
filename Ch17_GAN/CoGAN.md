# CoGAN

学习联合分配
用面部字符P（金发，女性，微笑，戴眼镜），P（棕色，男性，微笑，没有眼镜）等不同组合创建GAN是很不现实的。维数的诅咒使得GAN的数量呈指数增长。但我们可以学习单个数据分布并将它们组合以形成不同的分布，即不同的属性组合。

CoGAN:Coupled Generative Adversarial Networks

CoGAN会训练两个GAN而不是一个单一的GAN。

当然，GAN研究人员不停止地将此与那些警察和伪造者的博弈理论进行类比。所以这就是CoGAN背后的想法，用作者自己的话说就是：

在游戏中，有两个团队，每个团队有两个成员。生成模型组成一个团队，在两个不同的域中合作共同合成一对图像，用以混淆判别模型。判别模型试图将从各个域中的训练数据分布中绘制的图像与从各个生成模型中绘制的图像区分开。同一团队中，参与者之间的协作是根据权重分配约束建立的。这样就有了一个GAN的多人局域网竞赛

CoupledGAN 通过部分权重共享学习到多个域图像的联合分布。生成器前半部分权重共享，目的在于编码两个域高层的，共有信息，后半部分没有进行共享，则是为了各自编码各自域的数据。判别器前半部分不共享，后半部分用于提取高层特征共享二者权重。对于训练好的网络，输入一个随机噪声，输出两张不同域的图片。

值得注意的是，上述模型学习的是联合分布 P(x,y)，如果使用两个单独的 GAN 分别取训练，那么学习到的就是边际分布 P(x) 和 P(y)。。

在cross domain学习中也常用到多判别器多生成器多结构，分别学习不同的域。而且各个域的判别器和生成器通常会共享一些权重[2]

论文：

https://arxiv.org/abs/1606.07536

代码：

https://github.com/mingyuliutw/CoGAN

博客：

https://wiseodd.github.io/techblog/2017/02/18/coupled_gan/


[1] Liu M, Tuzel O. Coupled Generative Adversarial Networks[J]. neural information processing systems, 2016: 469-477.
https://cloud.tencent.com/developer/article/1473720
[2]: https://www.zhihu.com/search?type=content&q=StackGAN
