

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-28 21:15:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 19:04:09
 * @Description:
 * @TODO::
 * @Reference:[1]: https://github.com/PaddlePaddle/models/tree/develop/PaddleCV/gan
 * https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch07_%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C(GAN)/ch7.md
 * [3]: http://www.tensorinfinity.com/paper_26.html
-->
cycleGAN模型较好的解决了无监督图像转换问题，可是这种单一域的图像转换还存在一些问题：

要针对每一个域训练一个模型，效率太低。举例来说，我希望可以将橘子转换为红苹果和青苹果。对于cycleGAN而言，需要针对红苹果，青苹果分别训练一个模型。

对于每一个域都需要搜集大量数据，太麻烦。还是以橘子转换为红苹果和青苹果为例。不管是红苹果还是青苹果，都是苹果，只是颜色不一样而已。这两个任务信息是可以共享的，没必要分别训练两个模型。而且针对红苹果，青苹果分别取搜集大量数据太费事。

starGAN则提出了一个多领域的无监督图像翻译框架，实现了多个领域的图像转换，且对于不同领域的数据可以混合在一起训练，提高了数据利用率



StarGAN是CycleGAN的进一步扩展，一个类别与一个类别对应就要训练一次太过麻烦，我们不但需要把笑脸转化为哭脸，还需要把它转化为惊讶，沮丧等多种表情，而StarGAN实现了这种功能。
StarGAN作为CycleGAN的推广，将两两映射变成了多领域之间的映射，是图像翻译领域的又一重大突破。此外，StarGAN还可以通过实现多数据集之间的联合训练（比如将拥有肤色，年龄等标签的CelebA数据集和拥有生气、害怕等表情标签的RaFD数据集），将之训练到同一个模型，完成了模型的压缩，是图像翻译领域的一大突破。[3]

模型中 (a)-(d) 的要求如下:
（a）D学会区分真实图像和生成图像，并将真实图像分类到其对应的域。因此，对D而言， $D: x \rightarrow\left\{D_{s r c}(x) ; D_{c l s}(x)\right\}$
（b）拼接目标标签与输入图片，将之输入G，并生成相应的图像;
（c）在给定原始域标签的情况下，G要尽量能重建原始图像。这与CycleGAN的循环一致性一脉相承;
（d）这一点与一般的GAN相同，G要尽量生成与真实图像相似的图像，但同时又尽量能被D区分出来。
从目标函数上来看，首先判别器的目标函数，要求满足GAN的结构，即
$$
L_{a d v}=E_{x}\left[\log D_{s r c}(x)\right]+E_{x, c}\left[\log \left(1-D_{\operatorname{src}}(G(x, c))\right)\right]
$$
此外，还要就判别器能将真实图像分类到相应的域，
$$
L_{c l s}^{r}=E_{x, c^{\prime}}\left[-\log D_{c l s}\left(c^{\prime} \mid x\right)\right]
$$
针对生成器，除了 $L_{a d v}$ 对应的GAN的结构外，还要求判别器能将生成图像分类到相应的域
$$
L_{c l s}^{f}=E_{x, c}\left[-\log D_{c l s}(c \mid G(x, c))\right]
$$
此外，还要求尽量能重建原始图像
$$
L_{r e c}=E_{x, c, c^{\prime}}\left[x-G\left(G(x, c), c^{\prime}\right)\right]
$$
其中, $c^{\prime}$ 为原始图像x对应的类别。如此，可以得到判别器的目标函数
$$
\min _{D} L_{D}=-L_{a d v}+\lambda_{c l s} L_{c l s}^{r}
$$
以及生成器的目标函数为
$$
\min _{G} L_{G}=L_{a d v}+\lambda_{c l s} L_{c l s}^{f}+\lambda_{r e c} L_{r e c}
$$
其中 $\lambda_{c l s}, \lambda_{r e c}$ 均为常数。

实现StarGAN时使用了Wasserstein距离，即WGAN-GP。

StarGAN多领域属性迁移，引入辅助分类帮助单个判别器判断多个属性，可用于人脸属性转换。[1]

StarGAN中生成网络的编码部分主要由convolution-instance norm-ReLU组成，解码部分主要由transpose convolution-norm-ReLU组成，判别网络主要由convolution-leaky_ReLU组成，详细网络结构可以查看network/StarGAN_network.py文件。生成网络的损失函数是由WGAN的损失函数，重构损失和分类损失组成，判别网络的损失函数由预测损失，分类损失和梯度惩罚损失组成。

https://github.com/yunjey/stargan
