

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 20:32:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 19:36:08
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch09.html#idm45762347307368
 * A survey of current super-resolution techniques
 * https://arxiv.org/pdf/1902.06068.pdf
-->


# Introduction to Super-Resolution

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
