

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 14:28:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 14:30:55
 * @Description:
 * @TODO::
 * @Reference:
-->


虽然生成对抗网络(GANs)在各种任务中表现出了显著的成功，但它们在生成高质量图像方面仍然面临着挑战。在本文中，我们提出堆叠生成对抗网络(StackGAN)，旨在生成高分辨率的真实感图像。首先，我们提出了一个两阶段生成对抗网络架构，StackGAN-v1，用于文本到图像的合成。Stage-I GAN根据给定的文本描述绘制对象的基本形状和颜色，生成低分辨率图像。阶段ii GAN将阶段i的结果和文本描述作为输入，并生成具有逼真细节的高分辨率图像。其次，针对条件生成任务和无条件生成任务，提出了一种先进的多级生成对抗网络结构StackGAN-v2。我们的stackagan -v2树状结构中包含多个发生器和鉴别器;同一场景对应的多尺度图像由树的不同分支生成。通过联合逼近多个分布，StackGAN-v2比StackGAN-v1显示出更稳定的训练行为。大量的实验表明，所提出的堆叠生成对抗网络在生成逼真的图像方面明显优于其他先进的方法。[1]

[1]: https://arxiv.org/abs/1710.10916
