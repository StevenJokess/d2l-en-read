

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-19 18:30:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 19:44:36
 * @Description:
 * @TODO::
 * @Reference:
-->
# 生成对抗网络GAN（Generative Adversarial Network）

生成对抗网络（Generative Adversarial Network，简称GAN）是非监督式学习的一种方法，通过让两个神经网络相互博弈对抗的方式进行学习。该方法由伊恩·古德费洛等人于2014年提出。生成对抗网络由一个生成网络与一个判别网络组成。

生成网络要做的，是找到一种映射关系：从**潜在空间（latent space）中随机取样**作为输入，其输出结果需要尽量**模仿训练集中的真实样本**。

判别网络的输入则为真实样本或生成网络的输出，输出置信度（1 表示是真实数据，0 表示为 G 伪造的数据），其目的是**将生成网络的输出从真实样本中尽可能分辨出来。**而生成网络则要尽可能地**欺骗判别网络。**两个网络相互对抗、不断调整参数，最终目的是使判别网络无法判断生成网络的输出结果是否真实。

框架中同时训练两个模型：捕获数据分布的生成模型G，和估计样本来自训练数据的概率的判别模型D。G的训练程序是**将D错误的概率最大化。**这个框架对应一个最大值集下限的双方对抗游戏。可以证明在任意函数G和D的空间中，存在唯一的解决方案，使得G重现训练数据分布，而D=0.5。在G和D由多层感知器定义的情况下，整个系统可以用反向传播进行训练。在训练或生成样本期间，不需要任何马尔科夫链或展开的近似推理网络。实验通过对生成的样品的定性和定量评估证明了本框架的潜力

常用于生成以假乱真的图片。此外，该方法还被用于生成影片、三维物体模型等。虽然生成对抗网络原先是为了无监督学习提出的，它也被证明对半监督学习、完全监督学习、强化学习是有用的。

目标函数及流程：
value function $V(G, D)$
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$

- max 部分的含义是，D 要尽可能正确地识别出真实数据和 G 伪造的数据。
- min 部分的含义是，G 要尽可能缩小自己生成的数据与真实数据的差别，让 D 真假难别。

## 伊恩·古德费洛介绍

GAN的提出者伊恩·古德费洛，曾就读于斯坦福大学，在那里获得了了计算机科学学士和硕士学位，之后在Yoshua Bengio和Aaron Courville 的指导下于蒙特利尔大学获得机器学习博士学位。毕业后，Goodfellow加入Google，成为Google Brain研究小组的成员。2015年他离开了Google，加入了新成立的OpenAI研究所。2017年3月回到Google Research。

Goodfellow最知名的成就就是发明了GAN,被誉为GAN之父。同时他还是 Deep Learning 教材的主要作者。在Google，他开发了一个系统，该系统使Google Maps能够自动转录街景汽车拍摄的照片中的地址，并展示了机器学习系统的安全漏洞。

2017年，Goodfellow被《MIT技术评论》的35位35岁以下的创新者所引用。在2019年，他被列入《外交政策》的100位全球思想家名单。

---


有监督学习方法又分生成方法（Generative approach）和判别方法（Discriminative approach），所学到的模型分别称为生成模型（Generative Model）和判别模型（Discriminative Model）。


从概率分布的角度考虑，对于一堆样本数据，每个均有特征Xi对应分类标记yi。

生成模型：学习得到联合概率分布P(x,y)，即特征x和标记y共同出现的概率，然后求条件概率分布。能够学习到数据生成的机制。

判别模型：学习得到条件概率分布P(y|x)，即在特征x出现的情况下标记y出现的概率。

数据要求：生成模型需要的数据量比较大，能够较好地估计概率密度；而判别模型对数据样本量的要求没有那么多。
由生成模型可以得到判别模型，但由判别模型得不到生成模型。

- 典型的生成模型有：朴素贝叶斯法和隐马尔可夫模型，将在后面章节进行相关讲述。
- 典型的判别模型包括：K近邻法、感知机、决策树、逻辑斯谛回归模型、最大熵模型、支持向量机、提升方法和条件随机场等。[11]

网络的最终目标是在D很强大的同时，G生成的假样本送给D后其输出值变为0.5，说明G已经完全骗过了D，即D已经区分不出来输入的样本到底是还是，从而得到一个生成效果很好的G。[3]

mode collapse的意思就是生成的样本大量集中于部分真实样本，那么就是很严重的mode collapse。以生成动漫头像图片为例，从下图中能够明显的看出，红框标记的图像重复出现了很多次，即存在一定的mode collapse。[3]

## 算法[10]

Algorithm 1 GAN Algorithm Input: 随机噪声 $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{m}\right\}$ in $\mathbb{R}^{d} ;$ 真实样本 $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{m}\right\} \subset \mathcal{X} .$
Output:生成样本 $X_{\text {fake }}$
1: for $t=0$ to $T-1$ do
2: $\quad$ 从高斯噪声分布 $\gamma$ 中随机采样出m个样本, 即 $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{m}\right\}$ in $\mathbb{R}^{d}$;
3: $\quad$ 从真实数据分布 $\mathcal{X}$ 中随机采样出m个样本，即 $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{m}\right\} \subset \mathcal{X}$;
4: $\quad$ 通过小批量随机梯度下降法来更新判别器 $D_{\omega}$ 的参数，具体公式为:
$$
\nabla_{\omega} \frac{1}{m} \sum_{i=1}^{m}\left[\log D_{\omega}\left(\mathbf{x}_{i}\right)+\log \left(1-D_{\omega}\left(G_{\theta}\left(\mathbf{z}_{i}\right)\right)\right)\right]
$$
5: $\quad$ 再从高斯噪声分布 $\gamma$ 中随机采样出另外的m个样本, 即 $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{m}\right\}$ in $\mathbb{R}^{d}$;
6: $\quad$ 通过小批量随机梯度下降法来更新判别器 $G_{\theta}$ 的参数，具体公式为:
$$
\nabla_{\theta} \frac{1}{m} \sum_{i=1}^{m} \log \left(1-D_{\omega}\left(G_{\theta}\left(\mathbf{z}_{i}\right)\right)\right)
$$
7: return $X_{\text {fake}}$


## 数学[4]

GAN的全局最优解 首先可以证明，对于任意的G，D的最优解有如下形式（这里来自p_data的数据的标签为1，来 自 $\mathrm{p}_{9}$ 的数据的标签为0 $)$ :
因此目标函数可重写为：
$$
D_{G}^{*}(\boldsymbol{x})=\frac{p_{\text {data}}(\boldsymbol{x})}{p_{\text {data}}(\boldsymbol{x})+p_{g}(\boldsymbol{x})}
$$
最后可以证明当且仅当 $p_{g}=p_{\text {data }},$ 即G完全重现数据生成过程时，C(G)有全局最小值，即达 到训练示意图中(d)的状态。
GAN的收敛性
可以证明，如果G和D有足够的学习能力，那么给定G，D可以达到其最优解，并且 $p_{g}$ 可以更新 来优化
使得p $_{g}$ 收敘于 $\mathrm{p}_{\text {data }}$ 。

$f(D)=a \log (D)+b \log (1-D)$
$\frac{d f(D)}{d D}=a \times \frac{1}{D}+b \times \frac{1}{1-D} \times(-1)=0$
$a \times \frac{1}{D^{*}}=b \times \frac{1}{1-D^{*}}$
$\Leftrightarrow a \times\left(1-D^{*}\right)=b \times D^{*}$
$D^{*}(x)=\frac{P_{data}(x)}{P_{\text {data}}(x)+P_{G}(x)}$




最大化V(G,D)实际上就能导出KL散度的衡量形式，这个[max V（G,D）]就是真图像和假图像之间的距离，为了让它们看上去一样，以假乱真，只要让距离最小也就是min[maxV（G,D）]即可！

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


训练一个 GAN 可能很困难，它经常会遇到各种问题，其中最主要的问题有以下三点：[10]

消失梯度：这种情况经常发生，特别是当判别器太好时，这会阻碍生辰器的改进。使用最佳的判别器时，由于梯度的消失，训练可能失败，因此无法提供足够的信息给生成器改进。
模式塌缩：这是指生成器开始反复产生相同的输出（或一小组输出）的现象。如果判别器陷入局部最小值，那么下一个生成器迭代就很容易找到判别器最合理的输出。判别器永远无法学会走出陷阱。
收敛失败：由于许多因素（已知和未知），GANs 经常无法收敛。

原论文中 G 的训练是希望减小 log(1-D(G(z))，而代码中是使用二值交叉熵BCE(G(z), 1)，即希望提高-log(D(G(x)))，虽然都是希望让 D(G(x)) 趋近于1 ，但数值上还是有细微的不同，后者的梯度更大，不易出现梯度消失的问题。[8]


Define a prior oninput noise variablepz(z).Gis a differentiable function andD(x)outputs a scalar as the probabilitythatxcomes from the training data rather thanpg, the generative distribution we want to learn[6]

video[7]

大部分GAN都有一个特点：训练完成后，判别器都是没有用的。因为理论上越训练，判别器越退化（比如趋于一个常数）。
GAN的判别器和生成器两个网络的复杂度是相当的（如果还有编码器，那么复杂度也跟它们相当），训练完GAN后判别器就不要了，那实在是对判别器这个庞大网络的严重浪费！[9]

[1]: https://www.aminer.cn/ai-history
[2]: https://mrt.aminer.cn/5df49f20e8cc00e7af330f6b
[3]: https://www.jiqizhixin.com/articles/2019-06-13-11
[4]: https://easyai.tech/blog/understanding-generative-adversarial-networks-gans/
[5]: https://ccc013.github.io/2018/12/10/GAN%E5%AD%A6%E4%B9%A0%E7%B3%BB%E5%88%97-%E5%88%9D%E8%AF%86GAN/
[6]: https://arxiv.org/pdf/1702.07800
[7]: https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Generative-Adversarial-Networks
[8]: https://www.zhihu.com/column/c_1257831643526172672
[9]: https://kexue.fm/archives/6409
[10]: https://mp.weixin.qq.com/s/iqCMA7E_vtdymVxxz7bpRA
[11]: https://yulinzhao.wordpress.com/2019/01/17/3-%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95-ch1%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95%E6%A6%82%E8%AE%BA/


TODO:
http://jiangsiyuan.com/2018/04/10/GAN/
