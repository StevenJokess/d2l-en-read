

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-26 20:19:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 21:00:55
 * @Description:
 * @TODO::
 * @Reference:https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch07_%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C(GAN)/ch7.md
-->

# mode collapsing

 什么是mode collapsing?
​ 某个模式(mode)出现大量重复样本，例如： model collapsing​ 上图左侧的蓝色五角星表示真实样本空间，黄色的是生成的。生成样本缺乏多样性，存在大量重复。比如上图右侧中，红框里面人物反复出现。

7.1.8 如何解决mode collapsing？
方法一：针对目标函数的改进方法

​ 为了避免前面提到的由于优化maxmin导致mode跳来跳去的问题，UnrolledGAN采用修改生成器loss来解决。具体而言，UnrolledGAN在更新生成器时更新k次生成器，参考的Loss不是某一次的loss，是判别器后面k次迭代的loss。注意，判别器后面k次迭代不更新自己的参数，只计算loss用于更新生成器。这种方式使得生成器考虑到了后面k次判别器的变化情况，避免在不同mode之间切换导致的模式崩溃问题。此处务必和迭代k次生成器，然后迭代1次判别器区分开[8]。DRAGAN则引入博弈论中的无后悔算法，改造其loss以解决mode collapse问题[9]。前文所述的EBGAN则是加入VAE的重构误差以解决mode collapse。

方法二：针对网络结构的改进方法

​ Multi agent diverse GAN(MAD-GAN)采用多个生成器，一个判别器以保障样本生成的多样性。具体结构如下：



​ 相比于普通GAN，多了几个生成器，且在loss设计的时候，加入一个正则项。正则项使用余弦距离惩罚三个生成器生成样本的一致性。

​ MRGAN则添加了一个判别器来惩罚生成样本的mode collapse问题。具体结构如下：



​ 输入样本$x​$通过一个Encoder编码为隐变量$E(x)​$，然后隐变量被Generator重构，训练时，Loss有三个。$D_M​$和$R​$（重构误差）用于指导生成real-like的样本。而$D_D​$则对$E(x)​$和$z​$生成的样本进行判别，显然二者生成样本都是fake samples，所以这个判别器主要用于判断生成的样本是否具有多样性，即是否出现mode collapse。

方法三：Mini-batch Discrimination

​ Mini-batch discrimination在判别器的中间层建立一个mini-batch layer用于计算基于L1距离的样本统计量，通过建立该统计量，实现了一个batch内某个样本与其他样本有多接近。这个信息可以被判别器利用到，从而甄别出哪些缺乏多样性的样本。对生成器而言，则要试图生成具有多样性的样本。

# GAN为什么容易训练崩溃？

​ 所谓GAN的训练崩溃，指的是训练过程中，生成器和判别器存在一方压倒另一方的情况。 GAN原始判别器的Loss在判别器达到最优的时候，等价于最小化生成分布与真实分布之间的JS散度，由于随机生成分布很难与真实分布有不可忽略的重叠以及JS散度的突变特性，使得生成器面临梯度消失的问题；�可是如果不把判别器训练到最优，那么生成器优化的目标就失去了意义。因此需要我们小心的平衡二者，要把判别器训练的不好也不坏才行。否则就会出现训练崩溃，得不到想要的结果

## 如何尽量避免GAN的训练崩溃问题？

归一化图像输入到（-1，1）之间；Generator最后一层使用tanh激活函数
生成器的Loss采用：min (log 1-D)。因为原始的生成器Loss存在梯度消失问题；训练生成器的时候，考虑反转标签，real=fake, fake=real
不要在均匀分布上采样，应该在高斯分布上采样
一个Mini-batch里面必须只有正样本，或者负样本。不要混在一起；如果用不了Batch Norm，可以用Instance Norm
避免稀疏梯度，即少用ReLU，MaxPool。可以用LeakyReLU替代ReLU，下采样可以用Average Pooling或者Convolution + stride替代。上采样可以用PixelShuffle, ConvTranspose2d + stride
平滑标签或者给标签加噪声；平滑标签，即对于正样本，可以使用0.7-1.2的随机数替代；对于负样本，可以使用0-0.3的随机数替代。 给标签加噪声：即训练判别器的时候，随机翻转部分样本的标签。
如果可以，请用DCGAN或者混合模型：KL+GAN，VAE+GAN。
使用LSGAN，WGAN-GP
Generator使用Adam，Discriminator使用SGD
尽快发现错误；比如：判别器Loss为0，说明训练失败了；如果生成器Loss稳步下降，说明判别器没发挥作用
不要试着通过比较生成器，判别器Loss的大小来解决训练过程中的模型坍塌问题。比如： While Loss D > Loss A: Train D While Loss A > Loss D: Train A
如果有标签，请尽量利用标签信息来训练
给判别器的输入加一些噪声，给G的每一层加一些人工噪声。
多训练判别器，尤其是加了噪声的时候
对于生成器，在训练，测试的时候使用Dropout
