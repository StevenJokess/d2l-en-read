

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:33:30
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-16 20:42:53
 * @Description:
 * @TODO::
 * @Reference:
-->

VAE-GAN是结合了VAE与GAN的一种结构

## AutoEncoder(AE)

从VAE角度来看，VAE产生的图像比较模糊，很大一部分原因是，它并不知道怎么才能比较好地定义生成图像与真实图像之间的损失，传统的VAE会通过比较生成图像与真实图像像素之间的差，取均值定义出损失，这种方式就导致生成的图像比较模糊。为了解决这个问题，我们可以给VAE加上一个判别器，此时VAE的解码器生成图像时，不仅要让生成的图像与原始图像之间的损失较小，还需要让生成的图像骗过判别器。加上判别器结构后，判别器就会强迫VAE的解码器生成清晰的图像。

从GAN角度来看，传统GAN的生成器在生成图像时，它会接受判别器的指导，从而随着训练的进行逐步生成逼真的图像。但在单纯的GAN结构中，因为生成器与判别器的能力难以均衡，容易造成训练的不稳定，一个原因就是对GAN而言，生成器从未见过真实的图像，不清楚真实图像的样子，直接尝试从一堆随机数据中生成图像，此时生成器的能力难以与判别器抗衡，实现对抗，这种情况下，我们通常需要多次调整生成器的参数或经过较长时间的训练，模型才有可能收敛。而给GAN加上VAE的编码器的作用就是为生成器增加一个损失，即生成图像与真实图像之间的损失，这相当于告诉生成器真实图像的模样，生成器多了一个损失作为指导，在训练时会更加稳定。


VAE-GAN而言，它有3个主要部分，分别是编码器、生成器（解码器）以及判别器。对每个部分而言，其对应的损失都是不相同的

VAE的目标函数

$\mathcal{L}(\theta, \phi ; x)=E_{Q_{\phi}(z \mid x)}\left[\log P_{\theta}(x \mid z)\right]-D_{\mathrm{KL}}\left(Q_{\phi}(z \mid x)|| P_{\theta}(z)\right)$

## 损失函数

### 生成器

是 $\quad$ mathcalL $_{\text {lilike }}^{\text {Dis }}$ 、 $\log (1-\operatorname{Dis}(\operatorname{Dec}(z)))$ 与

$\log (1-\operatorname{Dis}(\operatorname{Dec}(\operatorname{Enc}(x)))), \quad \mathcal{L}_{\text {llike }}^{\text {Dis }}$


表示生成器同样希望最小化通过隐变量生成的数据与真实数据之间的损失，其次生成器还需要接收判别器传递的对抗损失，它希望自己通过随机噪声生成的图像与通过隐变量生成的图像可以获得更高的分数。

### 判别器

$\mathscr{L}_{\mathrm{GAN}}=\log (\operatorname{Dis}(x))+\log (1-\operatorname{Dis}(\operatorname{Dec}(z)))+\log (1-\operatorname{Dis}(\operatorname{Dec}(\operatorname{Enc}(x))))$




用self.gamma作为权重参数，其目的是平衡对抗损失与学习相似性损失，学习相似性损失会让生成器生成与原始图像相近的规则图像，减缓了生成器生成崩塌的图像问题，而对抗损失会让生成器生成的图像保持多样性。
