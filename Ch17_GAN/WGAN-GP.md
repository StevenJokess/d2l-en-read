

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 17:42:09
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 20:58:46
 * @Description:
 * @TODO::
 * @Reference:
-->

# WassersteinGAN with Gradient Penality

WGAN没有那么好用，主要原因在于WAGN进行梯度截断。梯度截断将导致判别网络趋向于一个二值网络，造成模型容量的下降。[9]

在提出了WGAN后，作者继续在WGAN上进行优化，又给出了一种新的损失函数，抛弃weight clipping，也就不再需要经验常数c了，取而代之的是gradient penality（梯度惩罚），因此取名为WGAN_GP，也叫Improved_WGAN。[8]

Gradient penality是指：对D的每一个输入样本x, 使得 $\left\|\nabla_{\hat{x}} D(\hat{x})\right\|_{2} \leq 1$ 。意思是对于任意一个
输入样本x, 用D的输出结果D(x)对求梯度后的值的 L2范数 不大于1。

上面的解释可能有些拗口，我们从一维空间中的函数f(x)来进行阐述：一维函数f(x)，对于任意输入 $x,$ 该函数满足: $\quad\left(\frac{d f(x)}{d x}\right)^{2} \leq 1 ，$ 即任意一点的斜率的平方不大于1，进而可以推出:
$\left(f\left(x_{1}\right)-f\left(x_{2}\right)\right)^{2} \leq\left(x_{1}-x_{2}\right)^{2},$ 可想而知 $f(x)$ 的函数曲线是比较平滑的, 所以称为梯度惩罚。那为

什么是 L2范数 呢而不是 L1范数 呢？原因很简单, L1范数会破坏一个函数的可微性呀, 所以 L2范
数 是非常合理的!

注意前面我说的是针对于D的每一个输入样本, 都让它满足 || $\nabla_{x} D(x) \|_{2} \leq 1 ，$ 实际上这是不现实
的, 所以作者又想了一个办法来解决这个问题：假设从真实数据中采样出来的一个点称为x（这个点
是高维空间中的点 $）,$ G利用采样得到的噪声向量所生成的假数据称为 $\hat{\chi},$ 在这两点之间的某一个位
置采样一个点记为, 即对于每一个 $\hat{\chi},,$ 尽量让 $\left\|\nabla_{\hat{x}} D(\hat{x})\right\|_{2} \leq 1$ 。那么最常见的满足上述要求
的采样方法就是线性采样方法了，即在x与 $\tilde{x}$ 所形成的超平面上任意选取一个点 $\hat{x},$, 换句话说就是
在生成样本和真实样本间做一个线性插值, 所以存在 $t \in[0,1],$ 使得 $\hat{x}=t x+(1-t) \tilde{x}$ 。
在新的 损失函数 闪亮登场之前, 我们还有一个小小的优化! 因为作者最后发现, 其实让
$\left\|\nabla_{\hat{x}} D(\hat{x})\right\|_{2} \approx 1$ 是最好的方案, 而不是把1作为上、下限, 别问我为什么, 作者也不知道！因为是通过大量的实验总结出来的。

即使得生成器的分布𝑝𝑔与真实分布𝑝𝑟之间的 EM 距离越小越好。考虑到𝔼𝒙𝑟∼𝑝𝑟[𝐷(𝒙𝑟)]一项 与生成器无关，因此生成器的训练目标简写为

$\min _{\phi} \mathcal{L}(G, D)=-\mathbb{E}_{x_{f} \sim p_{g}}\left[D\left(x_{f}\right)\right]$
$\quad=-\mathbb{E}_{\mathbf{z} \sim p_{z}(\cdot)}[D(G(\mathbf{z}))]$



目标函数：

$L=\underbrace{\underset{\tilde{\boldsymbol{x}} \sim \mathbb{P}_{g}}{\mathbb{E}}[D(\tilde{\boldsymbol{x}})]-\underset{\boldsymbol{x} \sim \mathbb{P}_{r}}{\mathbb{E}}[D(\boldsymbol{x})]}_{\text {Original critic loss }}+\underbrace{\lambda \underset{\hat{\boldsymbol{x}} \sim \mathbb{P}_{\hat{\boldsymbol{x}}}}{\mathbb{E}}\left[\left(\left\|\nabla_{\hat{\boldsymbol{x}}} D(\hat{\boldsymbol{x}})\right\|_{2}-1\right)^{2}\right]}_{\text {Our gradient penalty }} .$

```py
def d_loss_fn(generator, discriminator, batch_z, batch_x, is_training):
    # 计算 D 的损失函数     fake_image = generator(batch_z, is_training) # 假样本     d_fake_logits = discriminator(fake_image, is_training) # 假样本的输出     d_real_logits = discriminator(batch_x, is_training) # 真样本的输出     # 计算梯度惩罚项     gp = gradient_penalty(discriminator, batch_x, fake_image)
    # WGAN-GP D 损失函数的定义，这里并不是计算交叉熵，而是直接最大化正样本的输出     # 最小化假样本的输出和梯度惩罚项     loss = tf.reduce_mean(d_fake_logits) - tf.reduce_mean(d_real_logits) + 1 0. * gp

    return loss, gp
```

```py
# [5]

def gradient_penalty_loss(y_pred, y_average):
    gradients = tf.gradients(y_pred, y_average)[0]
    gradients_sqr = tf.square(gradients)
    gradients_sqr_sum = tf.reduce_sum(gradients_sqr, axis=np.arange(1, len(gradients_sqr.shape)))
    gradients_l2_norm = tf.sqrt(gradients_sqr_sum)

    gradient_penalty = tf.square(gradients_l2_norm)

    return tf.reduce_mean(gradient_penalty)

def discriminator_loss(real_output, generated_output, validity_interpolated, interpolated_img, lambda_=10):

    real_loss = -tf.reduce_mean(real_output)
    fake_loss = tf.reduce_mean(generated_output)
    gp_loss = gradient_penalty_loss(validity_interpolated, interpolated_img)

    return real_loss + fake_loss + gp_loss * lambda_
```

同样没有交叉熵的计算步骤。代码实现如下：

```py
def g_loss_fn(generator, discriminator, batch_z, is_training):
    # 生成器的损失函数     fake_image = generator(batch_z, is_training)     d_fake_logits = discriminator(fake_image, is_training)
    # WGAN-GP G 损失函数，最大化假样本的输出值     loss = - tf.reduce_mean(d_fake_logits)

    return loss
```

```py
# [5]
def generator_loss(generated_output):
    return -tf.reduce_mean(generated_output)
```


its stablity during training.[2]

## Generator

For G I use 4 transposed convolutional layer to rebuild a 3*128*128 RGB image.

```python
class G_net(nn.Module):
    def __init__(self,in_dim=latent_dim):
        super(G_net,self).__init__()
        self.fc1= nn.Sequential(
            nn.Linear(in_dim,units[4]),
            nn.ReLU(),
            nn.Linear(units[4],units[3]*fs[0]*fs[1]),
            nn.ReLU(),
            nn.BatchNorm1d(units[3]*fs[0]*fs[1])
        )
        self.ct1 = nn.Sequential(
            nn.ConvTranspose2d(units[3],units[2],k_size[3],stride=strides[3],padding=padding[3],output_padding=strides[3]/2),
            nn.BatchNorm2d(units[2]),
            nn.ReLU()
        )#[64,12,12]
        self.ct2 = nn.Sequential(
            nn.ConvTranspose2d(units[2],units[1],k_size[2],stride=strides[2],padding=padding[2],output_padding=strides[2]/2),
            nn.BatchNorm2d(units[1]),
            nn.ReLU()
        )#[32,27,27]
        self.ct3 = nn.Sequential(
            nn.ConvTranspose2d(units[1],units[0],k_size[1],stride=strides[1],padding=padding[1],output_padding=strides[1]/2),
            nn.BatchNorm2d(units[0]),
            nn.ReLU()
        )#[3,57,57]
        self.ct4 = nn.Sequential(
            nn.ConvTranspose2d(units[0],small_image_size[0],k_size[0],stride=strides[0],padding=padding[0],output_padding=strides[0]/2),
            nn.Tanh()
        )#[3,289,289]
    def forward(self,X):
        X = self.fc1(X)
        X = self.ct1(X.view(-1,units[3],fs[0],fs[1]))
        X = self.ct2(X)
        X = self.ct3(X)
        return self.ct4(X)
```

## Discriminator


```python
class D_net(nn.Module):
    def __init__(self):
        super(D_net,self).__init__()
        self.conv1=nn.Sequential(
            nn.Conv2d(image_size[0],units[0],k_size[0],strides[0],padding=padding[0]),
            nn.BatchNorm2d(units[0]),
            nn.LeakyReLU(0.2)
        )
        self.conv2=nn.Sequential(
            nn.Conv2d(units[0],units[1],k_size[1],strides[1],padding=padding[1]),
            nn.BatchNorm2d(units[1]),
            nn.LeakyReLU(0.2)
        )
        self.conv3=nn.Sequential(
            nn.Conv2d(units[1],units[2],k_size[2],strides[2],padding=padding[2]),
            nn.BatchNorm2d(units[2]),
            nn.LeakyReLU(0.2)
        )
        self.conv4=nn.Sequential(
            nn.Conv2d(units[2],units[3],k_size[3],strides[3],padding=padding[3]),
            nn.BatchNorm2d(units[3]),
            nn.LeakyReLU(0.2)
        )
        self.fc1 = nn.Linear(units[3]*fs[0]*fs[1],units[4])
        self.dp = nn.Dropout(0.5)
        self.d_out = nn.Linear(units[4],1)
    def forward(self,X):
        X = self.conv1(X)
        X = self.conv2(X)
        X = self.conv3(X)
        X = self.conv4(X)
        X = X.view((-1,units[3]*fs[0]*fs[1]))
        X = self.dp(F.leaky_relu(self.fc1(X)))
        out = self.d_out(X)
        return out
```

## Train

```python
d_iter = 1
g_iter = 1
epoch = 3000
for e in range(epoch):
    for data in Pk_dataloader:

        for i in range(d_iter):
            #real data
            for p in d_model.parameters():
                p.requires_grad = True
            d_model.zero_grad()
            true_data = Variable(data)
            if use_GPU:
                true_data=true_data.cuda(device)
            d_true_score = d_model(true_data)
            true_loss = -d_true_score.mean()
            #fake data
            noise = get_noise(true_data.size()[0])
            if use_GPU:
                noise = noise.cuda(device)
            fake_data = g_model(noise)
            d_fake_score = d_model(fake_data)
            fake_loss = d_fake_score.mean()
            w_loss = loss_with_penalty(d_model,true_data.data,fake_data.data)
            loss =true_loss+fake_loss+w_loss
            loss.backward()
            d_optimizer.step()
        for i in range(g_iter):
            #train G
            g_model.zero_grad()
            for p in d_model.parameters():
                p.requires_grad = False
            noise = get_noise()
            if use_GPU:
                noise = noise.cuda(device)
            fake_data = g_model(noise)
            g_score = d_model(fake_data)
            g_loss = -g_score.mean()
            g_loss.backward()
            g_optimizer.step()
    if e%10==0:
        fake_imgs=fake_data.cpu().data*0.5 +0.5
        img = ToPILImage()(fake_imgs[3])
        img.save('result/%s/G_result/iter_%d.png'%(code,e))
        torch.save(d_model,'result/%s/D_checkpoint/iter_d_%d.pt'%(code,e))
        torch.save(g_model,'result/%s/G_checkpoint/iter_g_%d.pt'%(code,e))
```

Paper:[3]
Code: [4]




[1]: Gulrajani,  I.,  Ahmed,  F.,  Arjovsky,  M.,  Dumoulin,  V.,  and  Courville,A. C. (2017). Improved training of Wasserstein GANs. InAdvances inNeural Information Processing Systems(pp. 5767-5777).
[2]: https://lanpartis.github.io/deep%20learning/2018/06/24/Use-GANs-to-Generate-Pokemons.html
[3]: https://arxiv.org/abs/1704.00028
[4]: https://github.com/eriklindernoren/Keras-GAN/blob/master/wgan_gp/wgan_gp.py
[5]: https://github.com/thisisiron/TF2-GAN/blob/master/wgan-gp/utils.py

TODO:
[6]: https://github.com/lilianweng/unified-gan-tensorflow
[7]: https://github.com/igul222/improved_wgan_training
[8]: https://www.jiqizhixin.com/articles/2019-06-13-11
[9]: https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch07_%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C(GAN)/ch7.md
https://github.com/caogang/wgan-gp
https://github.com/igul222/improved_wgan_training
