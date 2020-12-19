

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:21:21
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 22:37:33
 * @Description:
 * @TODO::
 * @Reference:
-->
# Least Squares Generative Adversarial Networks

传统GAN中, D网络和G网络都是用简单的交叉熵loss做更新, 最小二乘GAN则用最小二乘(Least Squares) Loss 做更新:

选择最小二乘Loss做更新有两个好处, 1. 更严格地惩罚远离数据集的离群Fake sample, 使得生成图片更接近真实数据(同时图像也更清晰) 2. 最小二乘保证离群sample惩罚更大, 解决了原本GAN训练不充分(不稳定)的问题:

但缺点也是明显的, LSGAN对离离群点的过度惩罚, 可能导致样本生成的”多样性”降低, 生成样本很可能只是对真实样本的简单”模仿”和细微改动.[3]

## Loss

\begin{aligned}
L_{D} &=E\left[(D(x)-1)^{2}\right]+E\left[D(G(z))^{2}\right] \\
L_{G} &=E\left[(D(G(z))-1)^{2}\right]
\end{aligned}

[4]
#don't use BCE loss!
#criterion = nn.BCELoss()

#now use RMSprop instead of Adam, with lr of 0.00005
G_optimizer = optim.RMSprop(G.parameters(), lr=0.00005)
D_optimizer = optim.RMSprop(D.parameters(), lr=0.00005)


class LSGAN(GAN):
    """
    和原始 GAN 相比，只是修改了 loss function, 但有时在最开始的时候崩掉, 生成空白
    """
    def __init__(self, latent_dim, img_shape, a, b, c):
        super().__init__(latent_dim, img_shape)
        self.a, self.b, self.c = a, b, c
        self.loss_func = keras.losses.MeanSquaredError()

    def step(self, img):
        d_label = self.c * tf.ones((len(img) * 2, 1), tf.float32)
        g_loss, g_img, g_acc = self.train_g(d_label)

        d_label = tf.concat(
            (self.b * tf.ones((len(img), 1), tf.float32),       # real
             self.a * tf.ones((len(g_img)//2, 1), tf.float32)), # fake
            axis=0)
        img = tf.concat((img, g_img[:len(g_img)//2]), axis=0)
        d_loss, d_acc = self.train_d(img, d_label)
        return d_loss, d_acc, g_loss, g_acc


if __name__ == "__main__":
    LATENT_DIM = 100
    # A, B, C = -1, 1, 0
    A, B, C = -1, 1, 1
    IMG_SHAPE = (28, 28, 1)
    BATCH_SIZE = 64
    EPOCH = 20

    set_soft_gpu(True)
    d = get_half_batch_ds(BATCH_SIZE)
    m = LSGAN(LATENT_DIM, IMG_SHAPE, A, B, C)
    train(m, d, EPOCH)

[1]: https://arxiv.org/pdf/1611.04076.pdf
[2]: https://github.com/MorvanZhou/mnistGANs/blob/main/lsgan.py
[3]: http://nooverfit.com/wp/%E7%8B%AC%E5%AE%B6%EF%BD%9Cgan%E5%A4%A7%E7%9B%98%E7%82%B9%EF%BC%8C%E8%81%8A%E8%81%8A%E8%BF%99%E4%BA%9B%E5%B9%B4%E7%9A%84%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C-lsgan-wgan-cgan-info/
[4]: https://github.com/bentrevett/pytorch-generative-models/blob/master/3%20-%20LSGAN.ipynb
