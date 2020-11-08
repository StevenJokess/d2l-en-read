

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 00:31:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 00:32:38
 * @Description:
 * @TODO::
 * @Reference:https://github.com/MorvanZhou/mnistGANs/blob/main/wgan_div.py
-->

# Wasserstein Divergence for GANs


```py
# modified from WGANgp
class WGANdiv(WGANgp):
    """
    WGAN clip weights 方案比较粗暴,
    用 gradient penalty 替代 clip 有助于 D 的能力提升, 间接提升 G. 不过WGAN-GP中判别器的优化目标已经不再是散度
    提出了Wasserstein散度的概念，摆脱了WGAN需要 [公式] 满足Lipschitz条件的限制。
    """
    def __init__(self, latent_dim, p, lambda_, img_shape):
        super().__init__(latent_dim, lambda_, img_shape)
        self.p = p

    # Wasserstein Divergence
    def gp(self, real_img, fake_img):
        e = tf.random.uniform((len(real_img), 1, 1, 1), 0, 1)
        noise_img = e * real_img + (1.-e)*fake_img      # extend distribution space
        with tf.GradientTape() as tape:
            tape.watch(noise_img)
            o = self.d(noise_img)
        g = tape.gradient(o, noise_img)         # image gradients
        # the following is different from WGANgp
        gp = tf.pow(tf.reduce_sum(tf.square(g), axis=[1, 2, 3]), self.p)
        return tf.reduce_mean(gp)
```

[1]: https://github.com/MorvanZhou/mnistGANs/blob/main/wgan_div.py
