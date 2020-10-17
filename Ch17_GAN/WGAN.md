

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 21:54:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 16:53:20
 * @Description:
 * @TODO::
 * @Reference:
-->

# Wasserstein GAN (WGAN)



是什么原因导致了 GAN 训练如此不稳定呢？WGAN 提出是因为 JS 散度在不重叠的分 布𝑝和𝑞上的梯度曲面是恒定为 0 的。如图 13.19 所示，当分布𝑝和𝑞不重叠时，JS 散度的梯 度值始终为 0，从而导致此时 GAN 的训练出现梯度弥散现象，参数长时间得不到更新，网络无法收敛。

## JS 散度的缺陷



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




## 生成器

生成网络的目标是使得评价网络𝑓(𝒙;𝜙)对其生成样本的打分尽可能高，即$\max _{\theta} \mathbb{E}_{z \sim p(z)}[f(G(z ; \theta) ; \phi)]$


因为𝑓(𝒙;𝜙)为不饱和函数，所以生成网络参数𝜃的梯度不会消失，理论上解决了原始GAN训练不稳定的问题．并且W-GAN中生成网络的目标函数不再是两个分布的比率，在一定程度上缓解了模型坍塌问题，使得生成的样本具有多样性

## 损失函数

## 优化器

在误差函数计算时，WGAN 也没 有 log 函数存在。在训练 WGAN 时，WGAN 作者推荐使用 RMSProp 或 SGD 等不带动量 的优化器。



WGAN 还在一定程度上缓解了模 式崩塌的问题，使用 WGAN 的模型不容易出现模式崩塌的现象。需要注意的是，WGAN 一般并不能提升模型的生成效果，仅仅是保证了模型训练的稳定性。当然，保证模型能够 稳定地训练也是取得良好效果的前提。如图 13.21 所示，原始版本的 DCGAN 在不使用 BN 层等设定时出现了训练不稳定的现象，在同样设定下，使用 WGAN 来训练判别器可以 避免此现象





[1]: https://learning.oreilly.com/library/view/python-machine-learning/9781789955750/Text/Chapter_17.xhtml#_idParaDest-342
[2]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781788629416/ch05.html
[3]: https://nndl.github.io/ 13.3
[4]: Arjovsky M, Chintala S, Bottou L, 2017. Wasserstein GAN[J/OL]. CoRR, abs/1701.07875.http://arxiv.org/abs/1701.07875.
[5]: https://github.com/dragen1860/Deep-Learning-with-TensorFlow-book/blob/master/%E3%80%90%E3%80%8ATensorFlow%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E3%80%8B%E3%80%91.pdf 13.7
