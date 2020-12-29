

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 20:04:33
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:08:12
 * @Description:
 * @TODO::
 * @Reference:http://www.tensorinfinity.com/paper_26.html
-->

# Loss-Sensitive GAN

与前文提到的LSGAN（1east square GAN）不同，这里的LS-GAN是指Loss-Sensitive GAN，即损失敏感GAN。一般认为，GAN可以分 为生成器G和判别器D。与之不同的是，针对判别器D，LS-GAN想要学习的是损失函数 $L_{\theta}(x),$ 要求 $L_{\theta}(x)$ 在真实样本上尽可能小，在 生成样本上尽可能大。由此，LS-GAN基于损失函数的目标函数为
$$
\min _{\theta} E_{x \sim P_{r}}\left[L_{\theta}(x)\right]+\lambda E_{x \sim P_{r}, Z_{G} \sim P_{G}\left(Z_{G}\right)}\left[\left(\triangle\left(x, z_{G}\right)+L_{\theta}(x)-L_{\theta}\left(z_{G}\right)\right)_{+}\right]
$$
生成器的目标函数为
$$
\min _{\phi} E_{x \sim P_{r}, z \sim P_{z}(z)}\left[L_{\theta}\left(G_{\phi}(z)\right)\right]
$$
此处 $\triangle\left(x, z_{G}\right)$ 是来自约束假设 $L_{\theta}(x) \leq L_{\theta}\left(z_{G}\right)-\triangle\left(x, z_{G}\right),$ 表示真实的样本要与生成样本间隔 $\triangle\left(x, z_{G}\right)$ 的长度， 如此LS-GAN就可 以将 $L_{\theta}$ 用于提高距离真实样本较远的样本上, 可以更合理的发挥LS-GAN的建模能力。

此外，为了证明LS-GAN的收敘性，还做了一个基本的假设：要求真实分布限定在Lipschitz 密度上，即真实分布的概率密度函数建 立在紧集上，并且它是Lipschitz连续的。通俗地说，就是要求真实分布的概率密度函数不能变化的太快，概率密度的变化不能随 着样本的变化而无限地增大。

## 推广为GLS-GAN(Genera1ized LS-GAN)

所谓的GLS-GAN，就是将损失函数 $L_{\theta}$ 的目标函数 扩展为
$$
\min _{\theta} E_{x \sim P_{r}}\left[L_{\theta}(x)\right]+\lambda E_{x \sim P_{r}, Z_{G} \sim P_{G}\left(Z_{G}\right)}\left[C_{v}\left(\Delta\left(x, z_{G}\right)+L_{\theta}(x)-L_{\theta}\left(z_{G}\right)\right)\right]
$$
此处 $C_{v}(a)=\max \{a, v a\},$ 其中 $v \in[-\infty, 1]$ 。

## GLS-GAN

可以证明，当v=0时，GLS-GAN就是前文的LS-GAN。另外，当v=1时，可以证明，GLS-GAN就是WGAN。所以，Qi认为，LS-GAN与WGAN都是GLS-GAN的一种特例。
