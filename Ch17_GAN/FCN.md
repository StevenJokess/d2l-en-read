

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-09 17:23:58
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-09 17:24:08
 * @Description:
 * @TODO::
 * @Reference:
-->
fcn(fully convolutional natwork)的思想是：修改一个普通的逐层收缩的网络，用上采样(up sampling)(？？反卷积)操作代替网络后部的池化(pooling)操作。因此，这些层增加了输出的分辨率。为了使用局部的信息，在网络收缩过程（路径）中产生的高分辨率特征(high resolution features) ，被连接到了修改后网络的上采样的结果上。在此之后，一个卷积层基于这些信息综合得到更精确的结果。

与fcn(fully convolutional natwork)不同的是，我们的网络在上采样部分依然有大量的特征通道(feature channels)，这使得网络可以将环境信息向更高的分辨率层(higher resolution layers)传播。结果是，扩张路径基本对称于收缩路径。网络不存在任何全连接层(fully connected layers)，并且，只使用每个卷积的有效部分，例如，分割图(segmentation map)只包含这样一些像素点，这些像素点的完整上下文都出现在输入图像中。为了预测图像边界区域的像素点，我们采用镜像图像的方式补全缺失的环境像素。这个tiling方法在使用网络分割大图像时是非常有用的，因为如果不这么做，GPU显存会限制图像分辨率。 我们的训练数据太少，因此我们采用弹性形变的方式增加数据。这可以让模型学习得到形变不变性。这对医学图像分割是非常重要的，因为组织的形变是非常常见的情况，并且计算机可以很有效的模拟真实的形变。在[3]中指出了在无监督特征学习中，增加数据以获取不变性的重要性。

https://github.com/amusi/Deep-Learning-Interview-Book/blob/master/docs/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0.md