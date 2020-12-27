

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-19 18:30:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 15:33:44
 * @Description:
 * @TODO::
 * @Reference:
-->
# 生成对抗网络GAN（Generative Adversarial Network）

生成对抗网络（Generative Adversarial Network，简称GAN）是非监督式学习的一种方法，通过让两个神经网络相互博弈对抗的方式进行学习。该方法由伊恩·古德费洛等人于2014年提出。生成对抗网络由一个生成网络与一个判别网络组成。
生成网络要做的，是找到一种映射关系：从潜在空间（latent space）中随机取样作为输入，其输出结果需要尽量模仿训练集中的真实样本。
判别网络的输入则为真实样本或生成网络的输出，输出置信度（1 表示是真实数据，0 表示为 G 伪造的数据），其目的是将生成网络的输出从真实样本中尽可能分辨出来。而生成网络则要尽可能地欺骗判别网络。两个网络相互对抗、不断调整参数，最终目的是使判别网络无法判断生成网络的输出结果是否真实。

框架中同时训练两个模型：捕获数据分布的生成模型G，和估计样本来自训练数据的概率的判别模型D。G的训练程序是将D错误的概率最大化。这个框架对应一个最大值集下限的双方对抗游戏。可以证明在任意函数G和D的空间中，存在唯一的解决方案，使得G重现训练数据分布，而D=0.5。在G和D由多层感知器定义的情况下，整个系统可以用反向传播进行训练。在训练或生成样本期间，不需要任何马尔科夫链或展开的近似推理网络。实验通过对生成的样品的定性和定量评估证明了本框架的潜力

常用于生成以假乱真的图片。此外，该方法还被用于生成影片、三维物体模型等。虽然生成对抗网络原先是为了无监督学习提出的，它也被证明对半监督学习、完全监督学习、强化学习是有用的。

目标函数及流程：
value function $V(G, D)$
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$

max 部分的含义是，D 要尽可能正确地识别出真实数据和 G 伪造的数据。
min 部分的含义是，G 要尽可能缩小自己生成的数据与真实数据的差别，让 D 真假难别。

GAN的提出者伊恩·古德费洛，曾就读于斯坦福大学，在那里获得了了计算机科学学士和硕士学位，之后在Yoshua Bengio和Aaron Courville 的指导下于蒙特利尔大学获得机器学习博士学位。毕业后，Goodfellow加入Google，成为Google Brain研究小组的成员。2015年他离开了Google，加入了新成立的OpenAI研究所。2017年3月回到Google Research。

Goodfellow最知名的成就就是发明了GAN,被誉为GAN之父。同时他还是 Deep Learning 教材的主要作者。在Google，他开发了一个系统，该系统使Google Maps能够自动转录街景汽车拍摄的照片中的地址，并展示了机器学习系统的安全漏洞。

2017年，Goodfellow被《MIT技术评论》的35位35岁以下的创新者所引用。在2019年，他被列入《外交政策》的100位全球思想家名单。


网络的最终目标是在D很强大的同时，G生成的假样本送给D后其输出值变为0.5，说明G已经完全骗过了D，即D已经区分不出来输入的样本到底是还是，从而得到一个生成效果很好的G。[3]

mode collapse的意思就是生成的样本大量集中于部分真实样本，那么就是很严重的mode collapse。以生成动漫头像图片为例，从下图中能够明显的看出，红框标记的图像重复出现了很多次，即存在一定的mode collapse。[3]

## 数学[4]


2. 优点[5]
(以下优点和缺点主要来自 Ian Goodfellow 在 Quora 上的回答，以及知乎上的回答)

GAN 模型只用到了反向传播,而不需要马尔科夫链
训练时不需要对隐变量做推断
理论上,只要是可微分函数都可以用于构建 D 和 G ,因为能够与深度神经网络结合做深度生成式模型
G 的参数更新不是直接来自数据样本,而是使用来自 D 的反向传播
相比其他生成模型（VAE、玻尔兹曼机），可以生成更好的生成样本
GAN 是一种半监督学习模型，对训练集不需要太多有标签的数据；
没有必要遵循任何种类的因子分解去设计模型,所有的生成器和鉴别器都可以正常工作(概率密度不可计算时也可以，由于引入了一个非常聪明的内部对抗的训练机制，可以逼近一些不是很容易计算的目标函数。)
各种类型的损失函数都可以整合到GAN模型中

1. 缺点

可解释性差,生成模型的分布 Pg(G)没有显式的表达
比较难训练, D 与 G 之间需要很好的同步,例如 D 更新 k 次而 G 更新一次
训练 GAN 需要达到纳什均衡,有时候可以用梯度下降法做到,有时候做不到.我们还没有找到很好的达到纳什均衡的方法,所以训练 GAN 相比 VAE 或者 PixelRNN 是不稳定的,但我认为在实践中它还是比训练玻尔兹曼机稳定的多.
它很难去学习生成离散的数据,就像文本
相比玻尔兹曼机,GANs 很难根据一个像素值去猜测另外一个像素值,GANs 天生就是做一件事的,那就是一次产生所有像素,你可以用 BiGAN 来修正这个特性,它能让你像使用玻尔兹曼机一样去使用 Gibbs 采样来猜测缺失值
训练不稳定，G 和 D 很难收敛；
训练还会遭遇梯度消失、模式崩溃的问题
缺乏比较有效的直接可观的评估模型生成效果的方法

原论文中 G 的训练是希望减小 log(1-D(G(z))，而代码中是使用二值交叉熵BCE(G(z), 1)，即希望提高-log(D(G(x)))，虽然都是希望让 D(G(x)) 趋近于1 ，但数值上还是有细微的不同，后者的梯度更大，不易出现梯度消失的问题。[8]


Define a prior oninput noise variablepz(z).Gis a differentiable function andD(x)outputs a scalar as the probabilitythatxcomes from the training data rather thanpg, the generative distribution we want to learn[6]

video[7]

[1]: https://www.aminer.cn/ai-history
[2]: https://mrt.aminer.cn/5df49f20e8cc00e7af330f6b
[3]: https://www.jiqizhixin.com/articles/2019-06-13-11
[4]: https://easyai.tech/blog/understanding-generative-adversarial-networks-gans/
[5]: https://ccc013.github.io/2018/12/10/GAN%E5%AD%A6%E4%B9%A0%E7%B3%BB%E5%88%97-%E5%88%9D%E8%AF%86GAN/
[6]: https://arxiv.org/pdf/1702.07800
[7]: https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Generative-Adversarial-Networks
[8]: https://www.zhihu.com/column/c_1257831643526172672
TODO:
http://jiangsiyuan.com/2018/04/10/GAN/
