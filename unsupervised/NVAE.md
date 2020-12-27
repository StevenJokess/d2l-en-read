

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 16:35:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 16:38:22
 * @Description:
 * @TODO::
 * @Reference:
-->

NVAE全称是Nouveau VAE（难道不是Nvidia VAE？），它包含了很多当前CV领域的新成果，其中包括多尺度架构、可分离卷积、swish激活函数、flow模型等，可谓融百家之所长，遂成当前最强VAE～

NVAE带来的思想冲击主要有两个。

第一，就是自回归的高斯模型可以很有力地拟合复杂的连续型分布。以前笔者以为只有离散分布才能用自回归模型来拟合，所以笔者觉得在编码时，也需要保持编码空间的离散型，也就是VQ-VAE那一条路。而NVAE证明了，哪怕隐变量是连续型的，自回归高斯分布也能很好地拟合，所以不一定要走VQ-VAE的离散化道路了，毕竟连续的隐变量比离散的隐变量更容易训练。

第二，VAE的隐变量可以不止一个，可以有多个的、分层次的。我们再次留意上表，比如FFHQ那一列，关于隐变量z的几个数据，他一共有4+4+4+8+16=36组，每组隐变量大小还不一样，分别是{82,162,322,642,1282}×20，如此算来，要生成一个256×256的FFHQ图像，需要一个总大小有

NVAE通过自回归形式的隐变量分布提升了理论上限，设计了巧妙的编码-解码结构
