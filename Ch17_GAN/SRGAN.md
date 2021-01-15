

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 20:32:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 23:57:26
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch09.html#idm45762347307368
 * A survey of current super-resolution techniques
 * https://arxiv.org/pdf/1902.06068.pdf
-->

# SRGAN

# 分辨率

分辨率极限，无论对于图像重建或是图像后处理算法的研究者，都是一项无法回避的技术指标。

图像分辨率泛指成像或显示系统对细节的分辨能力，代表图像中存储的信息量。 
指图像中存储的信息量，是每英寸图像内有多少个像素点，分辨率的单位为PPI(Pixels Per Inch)，通常叫做：像素每英寸。 
图片的大小由像素的多少决定，分辨率是单位密度，同量像素图片的分辨率越高，面积越小。 
一般情况下，图像分辨率越高，图像中包含的细节越多，信息量也越大。图像分辨率分为空间分辨率和时间分辨率。通常，分辨率被表示成每一个方向上的像素数量，例如64*64的二维图像。但是，分辨率的高低并不等同于像素数量的多少，例如一个通过插值放大了5倍的图像并不表示它包含的细节增加了多少。图像超分辨率重建关注的是恢复图像中丢失的细节，即高频信息。



时间分辨率性能决定了视频输出的帧率，即实时效果；
空间分辨率性能决定了图像的画面清晰度究竟是720P，1080P，还是4K；
色阶分辨率性能决定了图像显示色彩的丰满程度与粒度。

图片压缩与传输，即以较低的码率进行图像编码，在传输过程中可极大节省转发服务器的流量带宽，在客户端解码得到相对低清晰度的图片，最后通过超分辨重建技术处理获得高清晰度图片

## 传统超分辨重建技术

大体上可分为4类：

1. 预测型（prediction-based）
1. 边缘型（edge-based）
1. 统计型（statistical）
1. 图像块型（patch-based/example-based）

## Introduction to Super-Resolution



图像的超分辨率重构技术（Super-Resolution）指的是将给定的低分辨率图像通过算法恢复成相应的高分辨率图像，其主要分为两个大类：一类是使用单张低分辨率图像进行高分辨率图像的重建，一类是使用同一场景的多张低分辨率图像进行高分辨率图像的重建。此篇文章使用的是基于深度学习中的GAN网络对单张图像进行操作的超分辨率重构方法，超分辨重构和去噪、去网格、去模糊等问题是类似的。对于一张低分辨图像，可能会有多张高分辨图像与之对应，因此通常在求解高分辨率图像时会加一个先验信息进行规范化约束。在传统的方法中，通常会通过加入一些先验信息来恢复高分辨率图像，如，插值法、稀疏学习、还有基于回归方法的随机森林等。而基于深度学习的SR方法，则是通过神经网络直接进行从低分辨图像到高分辨图像的端到端的学习。[5]

### 国内研究现状

对SR的质量进行定量评价常用的两个指标是 PSNR(Peak Signal-to-Noise Ratio 峰值信噪比) 和 SSIM（Structure Similarity Index 结构相似性）。这两个值越高代表重建结果的像素值和金标准越接近.

2016年香港中文大学Dong等人将卷积神经网络应用于单张图像超分辨率重建上完成了深度学习在图像超分辨率重建问题的开山之作SRCNN(Super-Resolution Convolutional Neural Network)。SRCNN将深度学习与传统稀疏编码之间的关系作为依据，将3层网络划分为图像块提取(Patch extraction and representation)、非线性映射(Non-linear mapping)以及最终的重建(Reconstruction)。重建效果远远优于其他传统算法，利用SRCNN进行超分辨率图像重建与使用其他方法进行超分辨率重建的效果对比图如下图1所示。


Here’s the first part of a very simple super-resolution model. To start, it’s pretty much exactly the same as any model you’ve seen so far:





class OurFirstSRNet(nn.Module):

  def __init__(self):
      super(OurFirstSRNet, self).__init__()
      self.features = nn.Sequential(
          nn.Conv2d(3, 64, kernel_size=8, stride=4, padding=2),
          nn.ReLU(inplace=True),
          nn.Conv2d(64, 192, kernel_size=2, padding=2),
          nn.ReLU(inplace=True),
          nn.Conv2d(192, 256, kernel_size=2, padding=2),
          nn.ReLU(inplace=True)
      )

  def forward(self, x):
      x = self.features(x)
      return x
If we pass a random tensor through the network, we end up with a tensor of shape [1, 256, 62, 62]; the image representation has been compressed into a much smaller vector. Let’s now introduce a new layer type, torch.nn.ConvTranspose2d. You can think of this as a layer that inverts a standard Conv2d transform (with its own learnable parameters). We’ll add a new nn.Sequential layer, upsample, and put in a simple list of these new layers and ReLU activation functions. In the forward() method, we pass input through that consolidated layer after the others:

class OurFirstSRNet(nn.Module):
  def __init__(self):
      super(OurFirstSRNet, self).__init__()
      self.features = nn.Sequential(
          nn.Conv2d(3, 64, kernel_size=8, stride=4, padding=2),
          nn.ReLU(inplace=True),
          nn.Conv2d(64, 192, kernel_size=2, padding=2),
          nn.ReLU(inplace=True),
          nn.Conv2d(192, 256, kernel_size=2, padding=2),
          nn.ReLU(inplace=True)

      )
      self.upsample = nn.Sequential(
          nn.ConvTranspose2d(256,192,kernel_size=2, padding=2),
          nn.ReLU(inplace=True),
          nn.ConvTranspose2d(192,64,kernel_size=2, padding=2),
          nn.ReLU(inplace=True),
          nn.ConvTranspose2d(64,3, kernel_size=8, stride=4,padding=2),
          nn.ReLU(inplace=True)
      )

  def forward(self, x):
      x = self.features(x)
      x = self.upsample(x)
      return x
If you now test the model with a random tensor, you’ll get back a tensor of exactly the same size that went in! What we’ve built here is known as an autoencoder, a type of network that rebuilds its input, usually after compressing it into a smaller dimension. That is what we’ve done here; the features sequential layer is an encoder that transforms an image into a tensor of size [1, 256, 62, 62], and the upsample layer is our decoder that turns it back into the original shape.

Our labels for training the image would, of course, be our input images, but that means we can’t use loss functions like our fairly standard CrossEntropyLoss, because, well, we don’t have classes! What we want is a loss function that tells us how different our output image is from our input image, and for that, taking the mean squared loss or mean absolute loss between the pixels of the image is a common approach.

NOTE
Although calculating the loss in terms of pixels makes a lot of sense, it turns out that a lot of the most successful super-resolution networks use augmented loss functions that try to capture how much a generated image looks like the original, tolerating pixel loss for better performance in areas like texture and content loss. Some of the papers listed in “Further Reading” go into deeper detail.

Now that gets us back to the same size input we entered, but what if we add another transposed convolution to the mix?

self.upsample = nn.Sequential(...
nn.ConvTranspose2d(3,3, kernel_size=2, stride=2)
nn.ReLU(inplace=True))
Try it! You should find that the output tensor is twice as big as the input. If we have access to a set of ground truth images at that size to act as labels, we can train the network to take in images at a size x and produce images for a size 2x. In practice, we tend to perform this upsampling by scaling up twice as much as we need to and then adding a standard convolutional layer, like so:

self.upsample = nn.Sequential(......
nn.ConvTranspose2d(3,3, kernel_size=2, stride=2),
nn.ReLU(inplace=True),
nn.Conv2d(3,3, kernel_size=2, stride=2),
nn.ReLU(inplace=True))
We do this because the transposed convolution has a tendency to add jaggies and moiré patterns as it expands the image. By expanding twice and then scaling back down to our required size, we hopefully provide enough information to the network to smooth those out and make the output look more realistic.

Those are the basics behind super-resolution. Most current high-performing super-resolution networks are trained with a technique called the generative adversarial network, which has stormed the deep learning world in the past few years.


# SRResnet/SRGAN：使用生成对抗网络进行图像超分辨率.

Implementation of Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network.

直接使用MSE损失函数训练的超分辨率模型，在PSNR和SSIM等评价指标上能够得到较高的结果，但图像细节显示依旧较差。作者利用生成对抗网络的方法得到视觉特性较好的结果。

SRGAN不同于普通的GAN是通过噪声来生成一个真实图片，SRGAN的目的在于将一个低分辨率的图片转化为一个高分辨率的图片。利用感知损失(perceptual loss)和对抗损失(adversarial loss)来提升恢复出的图片的真实感。感知损失是利用卷积神经网络（VGG19）提取出的特征，通过比较生成图片与目标图片之间的特征差别，使生成图片和目标图片在语义和风格上更相似。通俗来讲，SRGAN所要完成的工作就是：通过G网络使低分辨率的图像重建出一张高分辨率的图像，再由D网络判断拿到的生成图与原图之间的差别，当G网络的生成图能够很好的骗过D网络，使之相信此生成图即为原数据集中的图像之一，那么超分辨率重构的网络就实现了。[5]


## 损失函数

论文中还给出了生成器和判别器的损失函数的形式：

### 生成器的损失函数为：

$$
\hat{\theta}_{G}=\operatorname{argmin}_{\theta_{G}} \frac{1}{N} \sum_{n=1}^{N} l^{S R}\left(G_{\theta_{G}}\left(I_{n}^{L R}\right), I_{n}^{H R}\right)
$$

其中, $\quad l^{s R}()$ 为本文所提出的感知损失函数, $ \quad l^{s R}=l_{V G G}^{S R}+10^{-3} l_{C e n}^{S R}$。

内容损失：
$$
l_{V G G}^{I R}=\frac{1}{w H} \sum_{x=1}^{W} \sum_{y=1}^{H}\left(\phi\left(I^{H R}\right)_{x, y}-\phi\left(G_{\theta_{G}}\left(I^{L R}\right)\right)_{x, y}\right)^{2}
$$
训练网络时使用均方差损失可以获得较高的峰值信噪比，一般的超分辨率重建方法中，内容损失都选择使用生成图像和目标图像的均方差损失（MSELoss），但是使用均方差损失恢复的图像会丢失很多高频细节。因此，本文先将生成图像和目标图像分别输入到VGG网络中，然后对他们经过VGG后得到的feature map求欧式距离，并将其作为VGG loss。

### 对抗损失：

$$
l_{G e n}^{S R}=\sum_{n=1}^{N}\left(-\log D_{\theta_{D}}\left(G_{\theta_{G}}\left(I^{L R}\right)\right)\right)
$$

为了避免当判别器训练较好时生成器出现梯度消失，本文将生成器的损失函数进行了修改。
判别器的损失函数为：
与普通的生成对抗网络判别器的的损失函数类似。

传统的方法使用的代价函数一般是最小均方差（MSE），即：

$l_{M S E}^{S R}=\frac{1}{r^{2} W H} \sum_{x=1}^{r W} \sum_{y=1}^{r H}\left(I_{x, y}^{H R}-G_{\theta_{G}}\left(I^{L R}\right)_{x, y}\right)^{2}$


该代价函数使重建结果有较高的信噪比，但是缺少了高频信息，出现过度平滑的纹理。SRGAN认为，应当使重建的高分辨率图像与真实的高分辨率图像无论是低层次的像素值上，还是高层次的抽象特征上，和整体概念和风格上，都应当接近。



作者提出的生成对抗网络结构如图所示。[3]

生成器结构参考了ResNet，输入低分辨率图像得到高分辨率图像，这一部分可作为SRResNet单独使用。
判别器结构参考了VGG，输入真实图像和生成的高分辨率图像，对二者进行分类。


模型的训练按照生成对抗网络的损失进行：

![生成对抗网络的损失](https://cdn.mathpix.com/snip/images/-5e18_2A6ahiFJw1RaOCvndiHbehUnrTle3tIcJCC-s.original.fullsize.png)

作者提出了感知损失函数(perceptual loss $l^{S R},$ 由内容损失函数(content loss $)_{X}^{S R}$ 和对抗损 失函数(adversarial loss $) l_{G e n}^{S R}$ 组成。
内容损失函数(content $\operatorname{loss}) l_{X}^{S R}$ 基于一个预训练的VGG19网络, 通过比较生成图像和真实图像 的网络中特征差异进行定义。其中 $\Phi_{i, j}$ 表示VGG19网络中第i个池化层之前的第j个卷积层(在激 活函数之后)的特征图。
对抗损失函数(adversarial loss $l_{G e}^{R}$ 试图使判别器无法正确的分类生成器获得的结果


SRGAN
[1]: https://arxiv.org/abs/1609.04802
[2]: https://github.com/eriklindernoren/Keras-GAN/blob/master/srgan/srgan.py
[3]: https://0809zheng.github.io/2020/08/10/srresnet.html
[4]: https://nbviewer.jupyter.org/github/cedrickchee/fastai-course-v3/blob/master/nbs/dl1/lesson7-superres-gan_20190110.ipynb
[5]: https://www.jiqizhixin.com/articles/2020-10-30-3
https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Super-Resolution
https://github.com/aitorzip/PyTorch-SRGAN
