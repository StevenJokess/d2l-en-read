

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 23:10:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 15:20:30
 * @Description:
 * @TODO::
 * @Reference:https://www.zhihu.com/column/c_1186629504699731968
 * https://github.com/znxlwm/pytorch-generative-model-collections
 * [3]: https://www.leiphone.com/news/201701/Kq6FvnjgbKK8Lh8N.html
-->

# InformationMaximizing Generative Adversarial Nets

InfoGAN的作者对损失函数进行了一些小的改进，一定程度上让网络学习到了可解释的特征表示，即作者文中所说的interpretable reptesentation。

InfoGANs通过最大化隐变量与观测数据的互信息，来改进GAN的解释性。

解耦表示（disentangled representation）

InfoGAN，是伯克利大学和openAI联手在NIPS2016发表的论文，提出了用GAN结合互信息来学习变量的解耦表示，并在MNIST、3D人脸和椅子、CelebA、SVHN数据集上都取得了不错的实验效果。

InfoGAN的思想也很简单，GAN的原始噪声z可以看成是数据的一种latent code，但z本身是杂乱无章的，为实现解耦目的，将z按维度拆分成z和解耦表示c两个部分。其中新的z仍然是杂乱无章的，而latent code c仅仅包含原来z中若干个维度，每个维度可以是离散的也可以是连续的，用来表示数据中的解耦变化因子。比如作者在测试MNIST图像时，取z中3个维度作为c，1个离散，2个连续，最后习得的c，离散的维度表示不同数字，连续的维度分别表示了数字的旋转和粗细：





这是总的模型架构，其中值得注意的是，文章直接用判别器作为变分网络 [公式]，最后一层同时输出c的预测和真假的预测。

思考
InfoGAN的互信息项使latent code c尽可能包含更多的关于生成图像的信息，因此能够捕捉不同的变化因子，但是这无法解释c具有解耦的能力。根据近两年的一些文章，可以作出一些猜测：

1.由于c每个维度间是独立的，并且一般假设Q(c|x)维度间独立，因此这样能够促进c的不同维度间的解耦，但根据ICML2019的最佳论文可知，这样并不够。

2.我猜测，为使互信息最大，c的每个维度都应最大限度地捕捉x变化最大且独立的各个方面，而真实的变化因子一般是按照变化方差从大到小排列的，类似PCA，所以这种匹配使解耦成为了可能。

InfoGAN [3]尝试使用无监督的方式去学习输入𝒙的可解释隐向量𝒛的表示方法 (Interpretable Representation)，即希望隐向量𝒛能够对应到数据的语义特征。比如对于 MNIST 手写数字图片，我们可以认为数字的类别、字体大小和书写风格等是图片的隐藏变 量，希望模型能够学习到这些分离的(Disentangled)可解释特征表示方法，从而可以通过人 为控制隐变量来生成指定内容的样本。对于 CelebA 名人照片数据集，希望模型可以把发 型、眼镜佩戴情况、面部表情等特征分隔开，从而生成指定形态的人脸图片。
分离的可解释特征有什么好处呢？它可以让神经网络的可解释性更强，比如𝒛包含了一 些分离的可解释特征，那么我们可以通过仅仅改变这一个位置上面的特征来获得不同语义 的生成数据，如图 13.10 所示，通过将“戴眼镜男士”与“不戴眼镜男士”的隐向量相 减，并与“不戴眼镜女士”的隐向量相加，可以生成“戴眼镜女士”的生成图片。


信息生成对抗网络(InfoGAN) $^{15}$ 是GAN信息理论的一个重要扩展. InfoGAN相比一般的GAN, 引入一个隐码 $c, c$ 表示显著结构化隐层随
机变量与特定语义特征之间的关系. 生成器的输入为呆声 $z$ 和隐码 $c,$ 输出为 $G(z, c),$ 在GAN中, $P_{G}(x \mid c)=P_{G}(x)$. InfoGAN使用互信息 $I(c ; G(z, c))$ 表示两个数据之间的关联性, 而隐码 $c$ 和生成分布 $G(z, c)$ 之间有高的互信息. InfoGAN的目标函数如式(6)所示:[5]

$$
\min _{G} \max _{D} F_{1}(D, G)=F(D, G)-\lambda I(c ; G(z, c))
$$

$\begin{aligned} L_{D, Q}^{i n f o G A N} &=L_{D}^{G A N}-\lambda L_{I}\left(c, c^{\prime}\right) \\ L_{G}^{i n f o G A N} &=L_{G}^{G A N}-\lambda L_{I}\left(c, c^{\prime}\right) \end{aligned}$

When you apply the bound on the first term, you get a lower bound, and you introduce an auxillary distribution that ends up being called the discriminator. This application of the bound is wrong because it bounds the loss function from the wrong side.
When you apply the bound on the second term, you end up upper bounding the loss function, because of the negative sign. This is a good thing.
The combination of a lower bound and an upper bound means that you don't even know which direction you're bounding or approximating the loss function from anymore, it's neither an upper or a lower bound.


潜在编码 latent code c[7]

－ 原来的GAN G的输出为 G(z) 现在改为 G(z,c)

－ c可以包含多种变量，根据不同的分布，比如在MNIST中，c可以一个值来表示类别，一个高斯分布的值来表示手写体的粗细



[1]: https://www.zhihu.com/column/c_1186629504699731968
[2]: https://github.com/dragen1860/Deep-Learning-with-TensorFlow-book/blob/master/%E3%80%90%E3%80%8ATensorFlow%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E3%80%8B%E3%80%91.pdf 13.4.2
[3]: https://arxiv.org/abs/1606.03657
[4]: https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/infogan/infogan.py
[5]: http://www.c-s-a.org.cn/html/2019/11/7156.html#outline_anchor_12
[6]: https://www.inference.vc/infogan-variational-bound-on-mutual-information-twice/
[7]: https://blog.csdn.net/Layumi1993/article/details/52474554
