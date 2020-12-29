

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 15:59:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 19:11:42
 * @Description:
 * @TODO::
 * @Reference:
-->

Radford 等[2]提出了深度卷积生成对抗网络(DCGAN), 将卷积神经网络(CNN)应用到生成对抗网络中, 通过对GAN的体系结构更改, 提高了GAN的训练的稳定性. 在DCGAN中, 对GAN的体系结构进行了一些修改: 将空间池化层函数替换为跨卷积; 去除了完全连接层, 能提高模型的稳定性; 除了生成器的输出层和判别器的输入层之外, 对每个单元的输入进行批归一化操作; 在生成器中使用ReLU激活函数, 在其输出层使用Tanh函数; 在判别器中使用LeakyReLU激活函数. DCGAN具有更强大的生成能力, 训练也更稳定, 生成的样本具有更多的多样性, 因此, 很多对于GAN的改进都是基于DCGAN的结构. DCGAN只是对GAN模型的结构进行了改进, 对生成器和判别器进一步的细化, 并没有对优化方法进行改进.[1]

DCGAN虽然没有带来理论上以及GAN上的解释性，但是其强大的图片生成效果吸引了更多的研究者关注GAN，证明了其可行性并提供了经验，给后来的研究者提供了神经网络结构的参考。此外，DCGAN的网络结构也可以作为基础架构，用以评价不同目标函数的GAN，让不同的GAN得以进行优劣比较。DCGAN的出现极大增强了GAN的数据生成质量。而如何提高生成数据的质量（如生成图片的质量）也是如今GAN研究的热门话题。[3]

DCGAN是在GAN的基础上提出了一种训练架构，并对其做了训练指导，比如几乎完全用卷积层取代了全连接层，去掉池化层，采用批标准化(Batch Normalization, BN)等技术，将判别模型的发展成果引入到了生成模型中。此外，还并强调了隐藏层分析和可视化计数对GAN训练的重要性和指导作用。[3]

[1]: http://www.c-s-a.org.cn/html/2019/11/7156.html#outline_anchor_12
[2]: Radford A, Metz L, Chintala S. Unsupervised representation learning with deep convolutional generative adversarial networks. arXiv preprint arXiv: 1511.06434, 2016.
[3]: http://www.tensorinfinity.com/paper_26.html
