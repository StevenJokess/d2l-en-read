

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:21:21
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 18:47:40
 * @Description:
 * @TODO::
 * @Reference:
-->
# Least Squares Generative Adversarial Networks(最小二乘生成式对抗网络)

虽然WGAN和WGAN-GP已经基本解决了训练失败的问题，但是无论是训练过程还是是收敛速度都要比常规 GAN 更慢。受WGAN理论的启发，Mao 等人提出了最小二乘GAN (least square GAN, LSGAN)

传统GAN中, D网络和G网络都是用简单的交叉熵loss做更新, 最小二乘GAN则用最小二乘(Least Squares) Loss 做更新：

选择最小二乘Loss做更新有两个好处, 1. 更严格地惩罚远离数据集的离群Fake sample, 使得生成图片更接近真实数据(同时图像也更清晰) 2. 最小二乘保证离群sample惩罚更大, 解决了原本GAN训练不充分(不稳定)的问题:

因为生成网络已经完成了我们为它设定的目标——尽可能地混淆判别网络，所以交叉熵损失函数已经很小了。而最小二乘损失函数采取不一样的策略，要想让最小二乘损失函数比较小，在混淆判别网络的前提下还需要让生成网络把距离决策边界比较远的生成数据拉向决策边界。[5]

为什么最小二乘损失函数可以使得原始生成式对抗网络的训练更稳定呢？因为交叉熵损失函数很容易就会达到饱和状态（饱和状态是指梯度为0），而最小二乘损失函数只在一个点上能达到饱和状态。[5]

LSGAN将GAN的目标函数由交叉熵损失替换成最小二乘损失，以此拒绝了标准GAN生成的图片质量不高以及训练过程不稳定这两个缺陷。[8]

但缺点也是明显的, LSGAN对离离群点的过度惩罚, 可能导致样本生成的”多样性”降低, 生成样本很可能只是对真实样本的简单”模仿”和细微改动.[3]

## 目标函数
### 判别器


$$
\underset{\min }{D} E_{x \sim P_{\text {data}}(x)}\left[(D(x)-b)^{2}\right]+E_{z \sim P_{z}(z)}\left[(D(G(Z))-a)^{2}\right]
$$

```py
class discriminator(nn.Module):
    def __init__(self, dim=3):
        super(discriminator, self).__init__()
        self.conv1 = nn.Conv(dim, 64, 5, 2, 2)
        self.conv2 = nn.Conv(64, 128, 5, 2, 2)
        self.conv2_bn = nn.BatchNorm(128)
        self.conv3 = nn.Conv(128, 256, 5, 2, 2)
        self.conv3_bn = nn.BatchNorm(256)
        self.conv4 = nn.Conv(256, 512, 5, 2, 2)
        self.conv4_bn = nn.BatchNorm(512)
        self.fc = nn.Linear(512*7*7, 1)
        self.leaky_relu = nn.Leaky_relu()

    def execute(self, input):
        x = self.leaky_relu(self.conv1(input), 0.2)
        x = self.leaky_relu(self.conv2_bn(self.conv2(x)), 0.2)
        x = self.leaky_relu(self.conv3_bn(self.conv3(x)), 0.2)
        x = self.leaky_relu(self.conv4_bn(self.conv4(x)), 0.2)
        x = x.reshape((x.shape[0], 512*7*7))
        x = self.fc(x)
        return x
```

### 生成器

$$
E_{z \sim P_{z}(z)}\left[(D(G(Z))-c)^{2}\right]
$$

这里a, b, c满足b-c=1和b-a=2。根据[6]，它等价于弄散度中的 $x^{2}$ 散度，也即是说，LSGAN用 $x^{2}$ 散度取代了朴素GAN 的 JensenShannon散度。

```py
class generator(Module):
    def __init__(self, dim=3):
        super(generator, self).__init__()
        self.fc = nn.Linear(1024, 7*7*256)
        self.fc_bn = nn.BatchNorm(256)
        self.deconv1 = nn.ConvTranspose(256, 256, 3, 2, 1, 1)
        self.deconv1_bn = nn.BatchNorm(256)
        self.deconv2 = nn.ConvTranspose(256, 256, 3, 1, 1)
        self.deconv2_bn = nn.BatchNorm(256)
        self.deconv3 = nn.ConvTranspose(256, 256, 3, 2, 1, 1)
        self.deconv3_bn = nn.BatchNorm(256)
        self.deconv4 = nn.ConvTranspose(256, 256, 3, 1, 1)
        self.deconv4_bn = nn.BatchNorm(256)
        self.deconv5 = nn.ConvTranspose(256, 128, 3, 2, 1, 1)
        self.deconv5_bn = nn.BatchNorm(128)
        self.deconv6 = nn.ConvTranspose(128, 64, 3, 2, 1, 1)
        self.deconv6_bn = nn.BatchNorm(64)
        self.deconv7 = nn.ConvTranspose(64 , dim, 3, 1, 1)
        self.relu = nn.ReLU()
        self.tanh = nn.Tanh()

    def execute(self, input):
        x = self.fc(input).reshape((input.shape[0], 256, 7, 7))
        x = self.relu(self.fc_bn(x))
        x = self.relu(self.deconv1_bn(self.deconv1(x)))
        x = self.relu(self.deconv2_bn(self.deconv2(x)))
        x = self.relu(self.deconv3_bn(self.deconv3(x)))
        x = self.relu(self.deconv4_bn(self.deconv4(x)))
        x = self.relu(self.deconv5_bn(self.deconv5(x)))
        x = self.relu(self.deconv6_bn(self.deconv6(x)))
        x = self.tanh(self.deconv7(x))
        return x
```

## Loss

推广都建立在 Lipschitz 约束之上，只不过微调了 Loss[7]


\begin{aligned}
L_{D} &=E\left[(D(x)-1)^{2}\right]+E\left[D(G(z))^{2}\right] \\
L_{G} &=E\left[(D(G(z))-1)^{2}\right]
\end{aligned}

```py
def ls_loss(x, b):
    mini_batch = x.shape[0]
    y_real_ = jt.ones((mini_batch,))
    y_fake_ = jt.zeros((mini_batch,))
    if b:
        return (x-y_real_).sqr().mean()
    else:
        return (x-y_fake_).sqr().mean()
```

优化目标为[5]


$\min _{D} J(D)=\min _{D}\left(\frac{1}{2} E_{x \sim p_{r}(x)}[D(x)-a]^{2}+\frac{1}{2} E_{z \sim p_{z}(z)}[D(G(z))-b]^{2}\right)$
$\min _{G} J(G)=\min _{G} \frac{1}{2}\left(E_{z \sim p_{z}(z)}[D(G(z))-c]^{2}\right)$

其中，随机变量z服从标准正态分布。常数a、b分别表示真实数据和生成数据的标记；c是生成网络为了让判别网络认为生成数据是真实数据而设定的值。

其中, 设定 a = 0, b = c = 1, 且 a, b, c 分别代表伪 造图的标签、真实图的标签和生成器期望判别器对 伪造图判定的标签. 与原始的生成式对抗网络一致, 在 pdata(x) = pg(x) 时, 达到网络内部的纳什均衡.

最后一层去掉sigmoid，并且计算Loss的时候用平方误差即可。[6]

```py
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
```



最后，LSGAN的优越性在于，它缓解了GAN训练时的不稳定，提高了生成数据的质量和多样性，也为后面的泛化模型f-GAN提供了思路。

[1]: https://arxiv.org/pdf/1611.04076.pdf
[2]: https://github.com/MorvanZhou/mnistGANs/blob/main/lsgan.py
[3]: http://nooverfit.com/wp/%E7%8B%AC%E5%AE%B6%EF%BD%9Cgan%E5%A4%A7%E7%9B%98%E7%82%B9%EF%BC%8C%E8%81%8A%E8%81%8A%E8%BF%99%E4%BA%9B%E5%B9%B4%E7%9A%84%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C-lsgan-wgan-cgan-info/
[4]: https://github.com/bentrevett/pytorch-generative-models/blob/master/3%20-%20LSGAN.ipynb
[5]: https://weread.qq.com/web/reader/d7032cd072021a59d7038afk28d32de024d28dd2c795c7f
[6]: https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch07_%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C(GAN)/ch7.md
[7]: https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247484880&idx=1&sn=4b2e976cc715c9fe2d022ff6923879a8&chksm=96e9da50a19e5346307b54f5ce172e355ccaba890aa157ce50fda68eeaccba6ea05425f6ad76&scene=21#wechat_redirect
[8]: https://github.com/Jittor/jittor/blob/master/notebook/LSGAN.src.md
