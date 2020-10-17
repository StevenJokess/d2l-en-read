

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 17:42:09
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 16:53:28
 * @Description:
 * @TODO::
 * @Reference:
-->



即使得生成器的分布𝑝𝑔与真实分布𝑝𝑟之间的 EM 距离越小越好。考虑到𝔼𝒙𝑟∼𝑝𝑟[𝐷(𝒙𝑟)]一项 与生成器无关，因此生成器的训练目标简写为

$\min _{\phi} \mathcal{L}(G, D)=-\mathbb{E}_{x_{f} \sim p_{g}}\left[D\left(x_{f}\right)\right]$
$\quad=-\mathbb{E}_{\mathbf{z} \sim p_{z}(\cdot)}[D(G(\mathbf{z}))]$


```py
def d_loss_fn(generator, discriminator, batch_z, batch_x, is_training):
    # 计算 D 的损失函数     fake_image = generator(batch_z, is_training) # 假样本     d_fake_logits = discriminator(fake_image, is_training) # 假样本的输出     d_real_logits = discriminator(batch_x, is_training) # 真样本的输出     # 计算梯度惩罚项     gp = gradient_penalty(discriminator, batch_x, fake_image)
    # WGAN-GP D 损失函数的定义，这里并不是计算交叉熵，而是直接最大化正样本的输出     # 最小化假样本的输出和梯度惩罚项     loss = tf.reduce_mean(d_fake_logits) - tf.reduce_mean(d_real_logits) + 1 0. * gp

    return loss, gp
```
同样没有交叉熵的计算步骤。代码实现如下：
```
def g_loss_fn(generator, discriminator, batch_z, is_training):
    # 生成器的损失函数     fake_image = generator(batch_z, is_training)     d_fake_logits = discriminator(fake_image, is_training)
    # WGAN-GP G 损失函数，最大化假样本的输出值     loss = - tf.reduce_mean(d_fake_logits)

    return loss
```

[1]: Gulrajani,  I.,  Ahmed,  F.,  Arjovsky,  M.,  Dumoulin,  V.,  and  Courville,A. C. (2017). Improved training of Wasserstein GANs. InAdvances inNeural Information Processing Systems(pp. 5767-5777).
