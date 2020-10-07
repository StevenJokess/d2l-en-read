

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 22:02:12
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-07 15:44:26
 * @Description:
 * @TODO::
 * @Reference:
-->

# Variational Autoencoders (VAEs)

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


[1]: https://learning.oreilly.com/library/view/hands-on-artificial-intelligence/9781788836067/de965259-e07e-461a-8d0f-717745273397.xhtml
[2]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781788629416/ch08.html
[3]: https://github.com/AntixK/PyTorch-VAE
[4]: https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73
[5]: https://keras.io/examples/generative/vae/
