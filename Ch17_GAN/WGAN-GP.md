

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 17:42:09
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 19:30:20
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



[1]: Gulrajani,  I.,  Ahmed,  F.,  Arjovsky,  M.,  Dumoulin,  V.,  and  Courville,A. C. (2017). Improved training of Wasserstein GANs. InAdvances inNeural Information Processing Systems(pp. 5767-5777).
[2]: https://lanpartis.github.io/deep%20learning/2018/06/24/Use-GANs-to-Generate-Pokemons.html
