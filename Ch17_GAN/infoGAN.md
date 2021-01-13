

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 23:10:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 19:07:25
 * @Description:
 * @TODO::
 * @Reference:https://www.zhihu.com/column/c_1186629504699731968
 * https://github.com/znxlwm/pytorch-generative-model-collections
 * [3]: https://www.leiphone.com/news/201701/Kq6FvnjgbKK8Lh8N.html
 * [4]: http://www.tensorinfinity.com/paper_26.html
-->

# Information Maximizing Generative Adversarial Nets

InfoGAN是伯克利大学和openAI联手在NIPS2016发表的论文，本质上也可以看作是一种cGAN。从出发点看，InfoGAN是基于朴素GAN改进的。它将原先生成器上输入的latent code z按维度进行分解，除了原先的噪声z以外，还分解出一个解耦表示c。InfoGAN的基本思想是，如果这个c能解释生成出来的G(z,c)，那么c应该与G(z,c)由高度的相关性。其在MNIST、3D人脸和椅子、CelebA、SVHN数据集上都取得了不错的实验效果。

其中：

- c除了可以表示类别以外，还可以包含多种变量。以MNIST数据集为例，还可以表示诸如光照方向，字体的倾斜角度，笔画粗细等。
- c仅仅包含原来z中若干个维度，每个维度可以是离散的也可以是连续的，用来表示数据中的解耦变化因子。以MNIST数据集为例，取z中3个维度作为c，1个离散，2个连续，最后习得的c，离散的维度表示不同数字，连续的维度分别表示了数字的旋转和粗细

损失函数改进：通过最大化隐变量与观测数据的互信息，并提出一个可高效优化的互信息的下界，使得GAN有了可解释的特征表征（interpretable representation）。

## 互信息 (Mutual Information)[9]

互信息是两个随机变量依赖程度的量度, 可以表示为:
$$
I(X ; Y)=H(X)-H(X \mid Y)
$$

其中, $I(X ; Y)$ 是当Y被探索了, 关于X的不确定性的减少量, 根据互信息理论, 我们希望得到 $P_{G}(c \mid x)$ 有一个较小的熵，熵代表惊喜度, 较小的熵表示该事件发生可能性较大, 也就是说该概率较大，最终的InfoGAN的定义式如下:
$$
\min _{G} \max _{D} V_{I}(D, G)=V(D, G)-\lambda I(c ; G(z, c))
$$

要去直接优化 $I(c ; G(z, c))$ 是极其困难的, 因为这意味着我们要能够计算后验概率（posterior
probability) $P(c \mid x),$ 但是我们可以用一个辅助分布 (auxiliary distribution) $Q(c \mid x),$ 来近似这一后验
概率。这样我们能够给出互信息的一个下界 (lower bounding) $：$
$$
I(c ; G(z, c)) \geqslant \mathbb{E}_{x \sim G(z, c)}\left[\mathbb{E}_{c^{\prime} \sim P(c \mid x)}\left[\log Q\left(c^{\prime} \mid x\right)\right]\right]+H(c)
$$


## 互信息最大化

要去直接优化 $I(c ; G(z, c))$ 是极其困难的, 因为这意味着我们要能够计算后验概率（posterior
probability) $P(c \mid x),$ 所以论文采用了变分推断的思想，定义一个辅助分布(auxiliary distribution) $Q(c \mid x)$来接近 $P(c \mid x)$
$$
\begin{aligned}
I(c ; G(z, c)) &=H(c)-H(c \mid G(z, c)) \\
&=\mathbb{E}_{x \sim G(z, c)}\left[\mathbb{E}_{c^{\prime} \sim P(c \mid x)}\left[\log P\left(c^{\prime} \mid x\right)\right]\right]+H(c) \\
&=\mathbb{E}_{x \sim G(z, c)}[\underbrace{D_{\mathrm{KL}}(P(\cdot \mid x) \| Q(\cdot \mid x))}_{\geq 0}+\mathbb{E}_{c^{\prime} \sim P(c \mid x)}\left[\log Q\left(c^{\prime} \mid x\right)\right]]+H(c) \\
& \geq \mathbb{E}_{x \sim G(z, c)}\left[\mathbb{E}_{c^{\prime} \sim P(c \mid x)}\left[\log Q\left(c^{\prime} \mid x\right)\right]\right]+H(c)
\end{aligned}
$$
论文将H(c)看做常数，并根据定理：
Lemma 5.1 For random variables $X, Y$ and function $f(x, y)$ under suitable regularity conditions:
$\mathbb{E}_{x \sim X, y \sim Y \mid x}[f(x, y)]=\mathbb{E}_{x \sim X, y \sim Y\left|x, x^{\prime} \sim X\right| y}\left[f\left(x^{\prime}, y\right)\right]$

如此可以定义变分下界

$$
\begin{aligned}
L_{I}(G, Q) &=E_{c \sim P(c), x \sim G(z, c)}[\log Q(c \mid x)]+H(c) \\
&=E_{x \sim G(z, c)}\left[\mathbb{E}_{c^{\prime} \sim P(c \mid x)}\left[\log Q\left(c^{\prime} \mid x\right)\right]\right]+H(c) \\
& \leq I(c ; G(z, c))
\end{aligned}
$$
最终InfoGAN的定义式如下:
$$
\min _{G, Q} \max _{D} V_{\operatorname{InfoGAN}}(D, G, Q)=V(D, G)-\lambda L_{I}(G, Q)
$$

## 解耦表示（disentangled representation）







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

- 原来的GAN G的输出为 G(z) 现在改为 G(z,c)
- c可以包含多种变量，根据不同的分布，比如在MNIST中，c可以一个值来表示类别，一个高斯分布的值来表示手写体的粗细

Q通过与D共享卷积层，计算花销大大减少。此外，Q是一个变分分布，在神经网络中直接最大化，Q也可以视作一个判别器，输出类别c。


InfoGAN的重要意义在于，它通过从噪声z中拆分出结构化的隐含编码c的方法，使得生成过程具有一定程度的可控性，生成结果也具备了一定的可解释性。[8]


[1]: https://www.zhihu.com/column/c_1186629504699731968
[2]: https://github.com/dragen1860/Deep-Learning-with-TensorFlow-book/blob/master/%E3%80%90%E3%80%8ATensorFlow%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E3%80%8B%E3%80%91.pdf 13.4.2
[3]: https://arxiv.org/abs/1606.03657
[4]: https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/infogan/infogan.py
[5]: http://www.c-s-a.org.cn/html/2019/11/7156.html#outline_anchor_12
[6]: https://www.inference.vc/infogan-variational-bound-on-mutual-information-twice/
[7]: https://blog.csdn.net/Layumi1993/article/details/52474554
[8]: http://www.tensorinfinity.com/paper_26.html
[9]: https://www.jiqizhixin.com/articles/2020-09-04-15
[10]: https://blog.csdn.net/qq_31239495/article/details/82862660
