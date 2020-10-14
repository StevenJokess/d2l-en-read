

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 21:54:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-14 22:22:32
 * @Description:
 * @TODO::
 * @Reference:
-->

# Wasserstein GAN (WGAN)

Wasserstein距离也称为推土机距离



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

## 评价网络

然而，要计算公式(13.54)中的上界也并不容易．根据神经网络的通用近似定理，我们可以假设存在一个神经网络使得可以达到这个上界．令𝑓(𝒙;𝜙)为一个神经网络，假设存在参数集合Φ，对于所有的𝜙 ∈ Φ，𝑓(𝒙;𝜙)为K-Lipschitz连续函数，那么公式（13.54）中的上界可以近似转换为

$\max _{\phi \in \Phi}\left(\mathbb{E}_{x \sim p_{r}}[f(\boldsymbol{x} ; \phi)]-\mathbb{E}_{x \sim p_{\theta}}[f(\boldsymbol{x} ; \phi)]\right)$




的偏导数的模$\left\|\frac{\partial f(x ; \phi)}{\partial x}\right\|$小于某个上界．由于这个偏导数的大小一般和参数的取值范围相关，我们可以通过限制参数𝜙的取值范围来近似，令𝜙 ∈ [−𝑐,𝑐]，𝑐为一个比较小的正数，比如0.01

## 生成网络

生成网络的目标是使得评价网络𝑓(𝒙;𝜙)对其生成样本的打分尽可能高，即$\max _{\theta} \mathbb{E}_{z \sim p(z)}[f(G(z ; \theta) ; \phi)]$
因为𝑓(𝒙;𝜙)为不饱和函数，所以生成网络参数𝜃的梯度不会消失，理论上解决了原始GAN训练不稳定的问题．并且W-GAN中生成网络的目标函数不再是两个分布的比率，在一定程度上缓解了模型坍塌问题，使得生成的样本具有多样性


[1]: https://learning.oreilly.com/library/view/python-machine-learning/9781789955750/Text/Chapter_17.xhtml#_idParaDest-342
[2]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781788629416/ch05.html
[3]:https://nndl.github.io/ 13.3
[4]: Arjovsky M, Chintala S, Bottou L, 2017. Wasserstein GAN[J/OL]. CoRR, abs/1701.07875.http://arxiv.org/abs/1701.07875.
