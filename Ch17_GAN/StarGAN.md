

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-28 21:15:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 20:12:38
 * @Description:
 * @TODO::
 * @Reference:[1]: https://github.com/PaddlePaddle/models/tree/develop/PaddleCV/gan
 * https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch07_%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C(GAN)/ch7.md
-->
cycleGAN模型较好的解决了无监督图像转换问题，可是这种单一域的图像转换还存在一些问题：

要针对每一个域训练一个模型，效率太低。举例来说，我希望可以将橘子转换为红苹果和青苹果。对于cycleGAN而言，需要针对红苹果，青苹果分别训练一个模型。

对于每一个域都需要搜集大量数据，太麻烦。还是以橘子转换为红苹果和青苹果为例。不管是红苹果还是青苹果，都是苹果，只是颜色不一样而已。这两个任务信息是可以共享的，没必要分别训练两个模型。而且针对红苹果，青苹果分别取搜集大量数据太费事。

starGAN则提出了一个多领域的无监督图像翻译框架，实现了多个领域的图像转换，且对于不同领域的数据可以混合在一起训练，提高了数据利用率

实现StarGAN时使用了Wasserstein距离，即WGAN-GP。

StarGAN多领域属性迁移，引入辅助分类帮助单个判别器判断多个属性，可用于人脸属性转换。[1]

StarGAN中生成网络的编码部分主要由convolution-instance norm-ReLU组成，解码部分主要由transpose convolution-norm-ReLU组成，判别网络主要由convolution-leaky_ReLU组成，详细网络结构可以查看network/StarGAN_network.py文件。生成网络的损失函数是由WGAN的损失函数，重构损失和分类损失组成，判别网络的损失函数由预测损失，分类损失和梯度惩罚损失组成。

https://github.com/yunjey/stargan
