

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 15:59:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 16:00:30
 * @Description:
 * @TODO::
 * @Reference:
-->

Radford 等[2]提出了深度卷积生成对抗网络(DCGAN), 将卷积神经网络(CNN)应用到生成对抗网络中, 通过对GAN的体系结构更改, 提高了GAN的训练的稳定性. 在DCGAN中, 对GAN的体系结构进行了一些修改: 将空间池化层函数替换为跨卷积; 去除了完全连接层, 能提高模型的稳定性; 除了生成器的输出层和判别器的输入层之外, 对每个单元的输入进行批归一化操作; 在生成器中使用ReLU激活函数, 在其输出层使用Tanh函数; 在判别器中使用LeakyReLU激活函数. DCGAN具有更强大的生成能力, 训练也更稳定, 生成的样本具有更多的多样性, 因此, 很多对于GAN的改进都是基于DCGAN的结构. DCGAN只是对GAN模型的结构进行了改进, 对生成器和判别器进一步的细化, 并没有对优化方法进行改进.[1]

[1]: http://www.c-s-a.org.cn/html/2019/11/7156.html#outline_anchor_12
[2]: Radford A, Metz L, Chintala S. Unsupervised representation learning with deep convolutional generative adversarial networks. arXiv preprint arXiv: 1511.06434, 2016.
