

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-29 18:53:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 20:40:47
 * @Description:
 * @TODO::
 * @Reference:
-->
在ShuffleNetV2的论文中，作者提出了设计轻量级网络的四大准则，并且根据四大准则与ShuffleNetV1的不足，设计了ShuffleNetV2网络。[2]


ShuﬄeNet V2虽然提出减少计算量的四个原则，基本卷积单元仍采用Depthwise和Pointwise降低计算量，但是没有提出如何实现提高准确率，推断延迟等评价指标。

对比MobileNet V1&V2，ShuﬄeNet V1&V2模型（图17），手工设计轻量化模型主要得益于depth-wise convolution减少计算量，而解决信息不流畅的问题，MobileNet 系列采用了 point-wise convolution，ShuffleNet 采用的是 channel shuffle。[4]

channel split，通道分割将输入的feature maps分为两部分：一个分支为shortcut流，另一个分支含三个卷积（且三个分支的通道数一样）。分支合并采用拼接（concat），让前后的channel数相同，最后进行Channel Shuffle（完成和ShuffleNet V1一样的功能）。元素级的三个运算channel split、concat、Channel Shuffle合并一个Element-wise，显著降低计算复杂度。
仍采用Depthwise和Pointwise降低计算量。[5]

ShuffleNet和MobileNet系列的异同
手工设计轻量化模型主要得益于depth-wise convolution减少计算量，而解决信息不流畅的问题，MobileNet 系列采用了 point-wise convolution，ShuffleNet 采用的是 channel shuffle。[5]
[1]: https://github.com/pytorch/vision/blob/master/torchvision/models/shufflenetv2.py
[2]: https://paddleclas.readthedocs.io/zh_CN/latest/models/Mobile.html
[3]: https://github.com/ericsun99/Shufflenet-v2-Pytorch/blob/master/ShuffleNetV2.py
[4]: https://zhuanlan.zhihu.com/p/45496826
[5]: https://cygao.xyz/2019/07/12/lightweight/
