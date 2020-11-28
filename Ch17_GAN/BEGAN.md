

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 14:01:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-28 20:30:03
 * @Description:
 * @TODO::
 * @Reference:https://weread.qq.com/web/reader/1503267072043961150720ck861322a025a8613985ec87a
 * https://weread.qq.com/web/reader/1503267072043961150720c
-->



从批判性思维的角度来说，BEGAN的目标函数中并没有对抗性质，生成器G 和判别器D 各自为政［5]，这是BEGAN 的问题所在。

与DCGAN不同，BEGAN并不追求生成数据分布与帧数据分布相同或相近，而追求生成数据的残差分布与真数据的残差分布相近。



BEGAN 编码模块的神经网络一共包含5层结构，输入图像的Height、Width、Channel 分别为64像素、64像素、3通道，第1层中使用3次卷积核为3像素×3像素的卷积，第2～4层均使用下采样和两次卷积操作，在每次卷积操作后，均采用ELU 激活函数作用于卷积层的输出，最后是1个全连接层，最终得到1个长度为h 的向量，这就完成了图像的编码过程。

第1层首先使用了1次全连接，然后将1维向量调整为Height、Width、Channel分别为8像素、8像素、n 通道的图像数据，第2～4层均使用步长为2的最近邻上采样和2次卷积核均为3像素×3像素的卷积。每次卷积后，同样采用ELU 激活函数作用于卷积层的输出，最后一层采用1次3像素×3像素的卷积操作，最终得到一张64像素×64像素×3像素的图像数据。


[1]:Radford A， Metz L， Chintala S.Unsupervised representation learning withdeep convolutional generative adversarialnetworks[J]. arXiv preprint， 2015:1511.06434.
[2]Transposed Convolution， Deconvolution[EB/OL]. 2020-03-01.https://buptldy.github.io/2016/10/29/2016-10-29-deconv/.
[3]Alec Radford， Luke Metz， SoumithChintala. Unsupervised RepresentationLearning with Deep Convolutional GenerativeAdversarial Networks[C].ICLR （Poster），2016. https://github.com/darr/DCGAN.
[4]Berthelot D， Schumm T， Metz L.BEGAN: Boundary Equilibrium GenerativeAdversarial Networks[J]. arXiv preprint，2017: 1703.10717.
[5]David Berthelot， Tom Schumm， LukeMetz. BEGAN: Boundary EquilibriumGenerative Adversarial Networks[J]. arXivpreprint， 2017: 1703.10717.https://github.com/anantzoid/BEGAN-PyTorch.
[6]BEGAN 学习笔记[EB/OL]. 2020-03-01.https://zhuanlan.zhihu.com/p/26394806.

[7]: https://github.com/lanpa/BEGAN-pytorch
