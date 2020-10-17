

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 22:02:12
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 14:47:54
 * @Description:
 * @TODO::
 * @Reference:
-->

# Variational Autoencoders (VAEs)

假设一个生成模型（如图13.3所示）中包含隐变量，即有部分变量是不可观测的，其中观测变量𝑿是一个高维空间𝒳中的随机向量，隐变量𝒁是一个相对低维的空间𝒵中的随机向量．



In a nutshell, a VAE is an autoencoder whose encodings distribution is regularised during the training in order to ensure that its latent space has good properties allowing us to generate some new data. Moreover, the term “variational” comes from the close relation there is between the regularisation and the variational inference method in statistics.

autoencoders are neural networks architectures composed of both an encoder and a decoder that create a bottleneck to go through for data and that are trained to lose a minimal quantity of information during the encoding-decoding process (training by gradient descent iterations with the goal to reduce the reconstruction error)[4]

Auto-Encoding Variational Bayes by Diederik P Kingma and Max Welling, presented at ICLR 2014 (https://arxiv.org/abs/1312.6114).

```python
#[5]
class VAE(keras.Model):
    def __init__(self, encoder, decoder, **kwargs):
        super(VAE, self).__init__(**kwargs)
        self.encoder = encoder
        self.decoder = decoder

    def train_step(self, data):
        if isinstance(data, tuple):
            data = data[0]
        with tf.GradientTape() as tape:
            z_mean, z_log_var, z = encoder(data)
            reconstruction = decoder(z)
            reconstruction_loss = tf.reduce_mean(
                keras.losses.binary_crossentropy(data, reconstruction)
            )
            reconstruction_loss *= 28 * 28
            kl_loss = 1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var)
            kl_loss = tf.reduce_mean(kl_loss)
            kl_loss *= -0.5
            total_loss = reconstruction_loss + kl_loss
        grads = tape.gradient(total_loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))
        return {
            "loss": total_loss,
            "reconstruction_loss": reconstruction_loss,
            "kl_loss": kl_loss,
        }
```

A collection of Variational AutoEncoders (VAEs) implemented in pytorch with focus on reproducibility. [3]

variational autoencoders (VAEs) are autoencoders that tackle the problem of the latent space irregularity by making the encoder return a distribution over the latent space instead of a single point and by adding in the loss function a regularisation term over that returned distribution in order to ensure a better organisation of the latent space[4]


![VAE_Encoder](img\VAE_Encoder.png)[5]

![VAE_Decoder](img\VAE_Decoder.png)[5]

![VAE](img\autoencoder_loss.png)[5]

变分自编码器（Variational AutoEncoder，VAE）[Kingma et al.,2014]是一种深度生成模型，其思想是利用神经网络来分别建模两个复杂的条件概率密度函数．（1）用神经网络来估计变分分布𝑞(𝒛;𝜙)，称为推断网络．理论上𝑞(𝒛;𝜙)可以不依赖𝒙．但由于𝑞(𝒛;𝜙)的目标是近似后验分布𝑝(𝒛|𝒙;𝜃)，其和𝒙相关，因此变分密度函数一般写为𝑞(𝒛|𝒙;𝜙)．推断网络的输入为𝒙，输出为变分分布𝑞(𝒛|𝒙;𝜙)．（2）用神经网络来估计概率分布𝑝(𝒙|𝒛;𝜃)，称为生成网络．生成网络的输入为𝒛，输出为概率分布𝑝(𝒙|𝒛;𝜃)．将推断网络和生成网络合并就得到了变分自编码器的整个网络结构，如图13.4所示，其中实线表示网络计算操作，虚线表示采样操作．



深度生成模型，比如变分自编码器、深度信念网络等，都是显示地构建出样本的密度函数𝑝(𝒙;𝜃)，并通过最大似然估计来求解参数，称为显式密度模型（Explicit Density Model）．比如，变分自编码器的密度函数为𝑝(𝒙,𝒛;𝜃) = 𝑝(𝒙|𝒛;𝜃)𝑝(𝒛;𝜃)．虽然使用了神经网络来估计𝑝(𝒙|𝒛;𝜃)，但是我们依然假设𝑝(𝒙|𝒛;𝜃)为一个参数分布族，而神经网络只是用来预测这个参数分布族的参数．这在某种程度上限制了神经网络的能力．[6]

变分自编码器是一个非常典型的深度生成模型，利用神经网络的拟合能力来有效地解决含隐变量的概率模型中后验分布难以估计的问题[Kingma et al.,2014;Rezende et al.,2014]．变分自编码器的详尽介绍可以参考文献[Doersch,2016]．[Bowman et al.,2016]进一步将变分自编码器应用于序列生成问题．再参数化是变分自编码器的重要技巧．对于离散变量的再参数化，可以使用Gumbel-Softmax方法[Jang et al.,2017][6]

[1]: https://learning.oreilly.com/library/view/hands-on-artificial-intelligence/9781788836067/de965259-e07e-461a-8d0f-717745273397.xhtml
[2]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781788629416/ch08.html
[3]: https://github.com/AntixK/PyTorch-VAE
[4]: https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73
[5]: https://keras.io/examples/generative/vae/
[6]: https://nndl.github.io/
[7]: Doersch C, 2016. Tutorial on variational autoencoders[J/OL]. CoRR, abs/1606.05908.http://arxiv.org/abs/1606.05908.
TODO:
[8]: https://github.com/dragen1860/Deep-Learning-with-TensorFlow-book/blob/master/ch12-%E8%87%AA%E7%BC%96%E7%A0%81%E5%99%A8/vae.py
