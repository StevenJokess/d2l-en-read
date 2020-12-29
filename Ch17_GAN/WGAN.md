

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 21:54:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:00:53
 * @Description:
 * @TODO::
 * @Reference:
-->

# Wasserstein GAN (WGAN)

一篇新鲜出炉的arXiv论文Martin Arjovsky等人《Wasserstein GAN》[8]却在Reddit的Machine Learning频道火了[7]

\begin{array}{l}
\mathbb{E}_{x \sim P_{g}}[\log (1-D(x))] \quad(\text { 公式 } 2) \\
\mathbb{E}_{x \sim P_{g}}[-\log D(x)] \quad \text { (公式3 })
\end{array}

后者在WGAN两篇论文中称为“the - log D alternative”或“the - log D trick”。WGAN前作分别分析了这两种形式的原始GAN各自的问题所在，下面分别说明。


改进DCGAN依靠的是对判别器和生成器的架构进行实验枚举，最终找到一组比较好的网络架构设置，但是实际上是治标不治本，没有彻底解决问题。

今天的主角Wasserstein GAN（下面简称WGAN）成功地做到了以下爆炸性的几点：

- 彻底解决GAN训练不稳定的问题，不再需要小心平衡生成器和判别器的训练程度
- 基本解决了collapse mode的问题，确保了生成样本的多样性
- 训练过程中终于有一个像交叉熵、准确率这样的数值来指示训练的进程，这个数值越小代表GAN训练得越好，代表
- 生成器产生的图像质量越高（如题图所示）


以上一切好处不需要精心设计的网络架构，最简单的多层全连接网络就可以做到

WGAN modified of DCGAN in:
1. remove sigmoid in the last layer of discriminator(classification -> regression)                                       # 回归问题,而不是二分类概率
2. no log Loss (Wasserstein distance)
3. clip param norm to c (Wasserstein distance and Lipschitz continuity) 每次更新判别器的参数之后把它们的绝对值截断到不超过一个固定常数c
4. No momentum-based optimizer, use RMSProp，SGD instead


是什么原因导致了 GAN 训练如此不稳定呢？WGAN 提出是因为 JS 散度在不重叠的分 布𝑝和𝑞上的梯度曲面是恒定为 0 的。如图 13.19 所示，当分布𝑝和𝑞不重叠时，JS 散度的梯 度值始终为 0，从而导致此时 GAN 的训练出现梯度弥散现象，参数长时间得不到更新，网络无法收敛。



## Wasserstein距离[10]

Wasserstein距离是从最优运输理论中的Kantorovich问题衍生而来的，可以如下定义真实分布与生成分布的Wasserstein-1距离：



提出Wasserstein distance距离作为衡量，并将其转换为求解最优的利普希茨连续函数的问题，为此进行参数约束：将过大的参数直接裁剪到一个阈值以下。

假设我们有了两个概率分布p(x),q(x)，那么Wasserstein距离的定义为

$\mathcal{W}[p, q]=\inf _{\gamma \in \Pi[p, q]} \iint \gamma(\boldsymbol{x}, \boldsymbol{y}) d(\boldsymbol{x}, \boldsymbol{y}) d \boldsymbol{x} d \boldsymbol{y}$

事实上，这也算是最优传输理论中最核心的定义了。

d(x,y)不一定是距离，其准确含义应该是一个成本函数，代表着从x运输到y的成本。常用的d是基于l范数衍生出来的



## JS 散度的缺陷

Martin Arjovsky等人先阐述了朴素GAN因生成器梯度消失而训练失败的原因[8]：他们认为，朴素GAN的目标函数在本质上可以等价于优化真实分布与生成分布的Jensen-Shannon散度。而根据Jensen-Shannon散度的特性，当两个分布间互不重叠时，其值会趋向于一个常数，这也就是梯度消失的原因。


## EM 距离

Wasserstein距离也称为Earth-Mover Distanc 推土机距离，简称EM 距离



它 表示了从一个分布变换到另一个分布的最小代价，定义为：

$W(p, q)=\inf _{v \sim \prod(p, q)} \mathbb{E}_{(x, y) \sim \gamma}[\|x-y\|]$



绘制出 JS 散度和 EM 距离的曲线，如图 13.20 所示，可以看到，JS 散度在𝜃 = 0处不连 续，其他位置导数均为 0，而 EM 距离总能够产生有效的导数信息，因此 EM 距离相对于 JS 散度更适合指导 GAN 网络的训练。

𝑊𝑝

![JS 散度和 EM 距离随𝜃变换曲线](img\JS_EM.jpg)

WGAN, which uses a modified loss function based on the so-called Wasserstein-1 (or earth mover's) distance between the distributions of real and fake images for improving the training performance.[1]

$\boldsymbol{W}^{1}\left(p_{\boldsymbol{r}}, p_{\theta}\right)=\inf _{\gamma \sim \Gamma\left(p_{r}, p_{\theta}\right)} \mathbb{E}_{(\boldsymbol{x}, \boldsymbol{y}) \sim \gamma}[\|\boldsymbol{x}-\boldsymbol{y}\|]$

其中Γ(𝑝𝑟,𝑝𝜃)是边际分布为𝑝𝑟和𝑝𝜃的所有可能的联合分布集合

梯度截断?

和原始GAN相比，W-GAN的评价网络最后一层不使用Sigmoid函数，损失函数不取对数

当两个分布没有重叠或者重叠非常少时，它们之间的KL散度为+∞，JS散度为log2，并不随着两个分布之间的距离而变化．而1st-Wasserstein距离依然可以衡量两个没有重叠分布之间的距离

两个分布𝑝𝑟和𝑝𝜃的1st-Wasserstein距离通常难以直接计算，但是两个分布的1st-Wasserstein距离有一个对偶形式

$\boldsymbol{W}^{1}\left(p_{\boldsymbol{r}}, p_{\theta}\right)=\sup _{\|f\|_{L} \leq 1}\left(\mathbb{E}_{\boldsymbol{x} \sim p_{r}}[f(\boldsymbol{x})]-\mathbb{E}_{\boldsymbol{x} \sim p_{\theta}}[f(\boldsymbol{x})]\right),$

we talked about the WGAN with GP to maintain the 1-Lipschitz property instead of clipping the weights.[1]


As we've mentioned before, GANs are notoriously hard to train. The opposing objectives of the two networks, the discriminator and the generator, can easily cause training instability. The discriminator attempts to correctly classify the fake data from the real data. Meanwhile, the generator tries its best to trick the discriminator. If the discriminator learns faster than the generator, the generator parameters will fail to optimize. On the other hand, if the discriminator learns more slowly, then the gradients may vanish before reaching the generator. In the worst case, if the discriminator is unable to converge, the generator is not going to be able to get any useful feedback.[2]
...

## 判别器

然而，要计算公式(13.54)中的上界也并不容易．根据神经网络的通用近似定理，我们可以假设存在一个神经网络使得可以达到这个上界．令𝑓(𝒙;𝜙)为一个神经网络，假设存在参数集合Φ，对于所有的𝜙 ∈ Φ，𝑓(𝒙;𝜙)为K-Lipschitz连续函数，那么公式（13.54）中的上界可以近似转换为

$\max _{\phi \in \Phi}\left(\mathbb{E}_{x \sim p_{r}}[f(\boldsymbol{x} ; \phi)]-\mathbb{E}_{x \sim p_{\theta}}[f(\boldsymbol{x} ; \phi)]\right)$




的偏导数的模$\left\|\frac{\partial f(x ; \phi)}{\partial x}\right\|$小于某个上界．由于这个偏导数的大小一般和参数的取值范围相关，我们可以通过限制参数𝜙的取值范围来近似，令𝜙 ∈ [−𝑐,𝑐]，𝑐为一个比较小的正数，比如0.01

WGAN 判别器的损失函数计算与 GAN 不一样，WGAN 是直接最大化真实样本的输出 值，最小化生成样本的输出值，并没有交叉熵计算的过程。

WGAN与原始GAN第一种形式相比，只改了四点：
1. 判别器最后一层去掉sigmoid             #no sigmoid!            #nn.Sigmoid(),[9]
1. 生成器和判别器的loss不取log
1. 每次更新判别器的参数之后把它们的绝对值截断到不超过一个固定常数c
1. 不要用基于动量的优化算法（包括momentum和Adam），推荐RMSProp，SGD也行

```
Discriminator(
  (main): Sequential(
    (0): Conv2d(3, 64, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (1): LeakyReLU(negative_slope=0.2, inplace)
    (2): Conv2d(64, 128, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (3): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (4): LeakyReLU(negative_slope=0.2, inplace)
    (5): Conv2d(128, 256, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (6): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (7): LeakyReLU(negative_slope=0.2, inplace)
    (8): Conv2d(256, 512, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (9): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (10): LeakyReLU(negative_slope=0.2, inplace)
    (11): Conv2d(512, 1, kernel_size=(4, 4), stride=(1, 1), bias=False)
  )
)
```

## 生成器

生成网络的目标是使得评价网络𝑓(𝒙;𝜙)对其生成样本的打分尽可能高，即$\max _{\theta} \mathbb{E}_{z \sim p(z)}[f(G(z ; \theta) ; \phi)]$

```
Generator(
  (main): Sequential(
    (0): ConvTranspose2d(100, 512, kernel_size=(4, 4), stride=(1, 1), bias=False)
    (1): BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (2): ReLU(inplace)
    (3): ConvTranspose2d(512, 256, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (4): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (5): ReLU(inplace)
    (6): ConvTranspose2d(256, 128, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (7): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (8): ReLU(inplace)
    (9): ConvTranspose2d(128, 64, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (10): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
    (11): ReLU(inplace)
    (12): ConvTranspose2d(64, 3, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)
    (13): Tanh()
  )
)
```

因为𝑓(𝒙;𝜙)为不饱和函数，所以生成网络参数𝜃的梯度不会消失，理论上解决了原始GAN训练不稳定的问题．并且W-GAN中生成网络的目标函数不再是两个分布的比率，在一定程度上缓解了模型坍塌问题，使得生成的样本具有多样性

## 损失函数[9]

生成器的损失函数为

$\min _{G}-E_{z \sim P_{z}}\left[f_{w}(G(z))\right]$

#don't use BCE loss!
#criterion = nn.BCELoss()

#now use RMSprop instead of Adam, with lr of 0.00005
G_optimizer = optim.RMSprop(G.parameters(), lr=0.00005)
D_optimizer = optim.RMSprop(D.parameters(), lr=0.00005)
## 优化器

在误差函数计算时，WGAN 也没 有 log 函数存在。在训练 WGAN 时，WGAN 作者推荐使用 RMSProp 或 SGD 等不带动量 的优化器。




WGAN 还在一定程度上缓解了模 式崩塌的问题，使用 WGAN 的模型不容易出现模式崩塌的现象。需要注意的是，WGAN 一般并不能提升模型的生成效果，仅仅是保证了模型训练的稳定性。当然，保证模型能够 稳定地训练也是取得良好效果的前提。如图 13.21 所示，原始版本的 DCGAN 在不使用 BN 层等设定时出现了训练不稳定的现象，在同样设定下，使用 WGAN 来训练判别器可以 避免此现象

WGAN本作引入了Wasserstein距离，由于它相对KL散度与JS散度具有优越的平滑特性，理论上可以解决梯度消失问题。接着通过数学变换将Wasserstein距离写成可求解的形式，利用一个参数数值范围受限的判别器神经网络来最大化这个形式，就可以近似Wasserstein距离。在此近似最优判别器下优化生成器使得Wasserstein距离缩小，就能有效拉近生成分布与真实分布。WGAN既解决了训练不稳定的问题，也提供了一个可靠的训练进程指标，而且该指标确实与生成样本的质量高度相关。作者对WGAN进行了实验验证。[6]

WGAN的贡献在于，从理论上阐述了因生成器梯度消失而导致训练不稳定的原因，并用Wasserstein距离替代了Jensen-Shannon散度，在理论上解决了梯度消失问题。此外，WGAN还从理论上给出了朴素GAN发生模式坍塌(mode collapse)的原因，并从实验角度说明了WGAN在这一点上的优越性。最后，针对生成分布与真实分布的距离和相关理论以及从Wasserstein距离推导而出的Lipschitz约束，也给了后来者更深层次的启发，如基于Lipschitz密度的 损失敏感GAN(loss sensitive GAN, LS-GAN)。[11]


[1]: https://learning.oreilly.com/library/view/python-machine-learning/9781789955750/Text/Chapter_17.xhtml#_idParaDest-342
[2]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781788629416/ch05.html
[3]: https://nndl.github.io/ 13.3
[4]: Arjovsky M, Chintala S, Bottou L, 2017. Wasserstein GAN[J/OL]. CoRR, abs/1701.07875.http://arxiv.org/abs/1701.07875.
[5]: https://github.com/dragen1860/Deep-Learning-with-TensorFlow-book/blob/master/%E3%80%90%E3%80%8ATensorFlow%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E3%80%8B%E3%80%91.pdf 13.7
[6]: https://zhuanlan.zhihu.com/p/25071913
[7]: https://github.com/chenyuntc/pytorch-GAN/blob/master/WGAN.ipynb
[8]: https://arxiv.org/abs/1701.07875
[9]: https://github.com/bentrevett/pytorch-generative-models/blob/master/4%20-%20WGAN.ipynb
[10]: https://kexue.fm/archives/6280
[11]: http://www.tensorinfinity.com/paper_26.html
