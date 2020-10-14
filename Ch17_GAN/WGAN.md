

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 21:54:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-14 20:27:38
 * @Description:
 * @TODO::
 * @Reference:
-->

# Wasserstein GAN (WGAN)

WGAN, which uses a modified loss function based on the so-called Wasserstein-1 (or earth mover's) distance between the distributions of real and fake images for improving the training performance.[1]


we talked about the WGAN with GP to maintain the 1-Lipschitz property instead of clipping the weights.[1]


As we've mentioned before, GANs are notoriously hard to train. The opposing objectives of the two networks, the discriminator and the generator, can easily cause training instability. The discriminator attempts to correctly classify the fake data from the real data. Meanwhile, the generator tries its best to trick the discriminator. If the discriminator learns faster than the generator, the generator parameters will fail to optimize. On the other hand, if the discriminator learns more slowly, then the gradients may vanish before reaching the generator. In the worst case, if the discriminator is unable to converge, the generator is not going to be able to get any useful feedback.[2]
...



对抗生成网络的训练不稳定问题的一种有效解决方法是W-GAN[Arjovsky et al.,2017]，通过用Wasserstein距离替代JS散度来进行训练．[3]

Wasserstein距离也称为推土机距离，参见第E.3.4节

和原始GAN相比，W-GAN的评价网络最后一层不使用Sigmoid函数，损失函数不取对数

[1]: https://learning.oreilly.com/library/view/python-machine-learning/9781789955750/Text/Chapter_17.xhtml#_idParaDest-342
[2]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781788629416/ch05.html
[3]: https://nndl.github.io

TODO:https://github.com/uclaacmai/Generative-Adversarial-Network-Tutorial
