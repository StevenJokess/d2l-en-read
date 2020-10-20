

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-19 18:30:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 21:45:30
 * @Description:
 * @TODO::
 * @Reference:
-->
生成对抗网络GAN（Generative Adversarial Network）

生成对抗网络（Generative Adversarial Network，简称GAN）是非监督式学习的一种方法，通过让两个神经网络相互博弈的方式进行学习。该方法由伊恩·古德费洛等人于2014年提出。生成对抗网络由一个生成网络与一个判别网络组成。生成网络从潜在空间（latent space）中随机取样作为输入，其输出结果需要尽量模仿训练集中的真实样本。判别网络的输入则为真实样本或生成网络的输出，其目的是将生成网络的输出从真实样本中尽可能分辨出来。而生成网络则要尽可能地欺骗判别网络。两个网络相互对抗、不断调整参数，最终目的是使判别网络无法判断生成网络的输出结果是否真实。

框架中同时训练两个模型：捕获数据分布的生成模型G，和估计样本来自训练数据的概率的判别模型D。G的训练程序是将D错误的概率最大化。这个框架对应一个最大值集下限的双方对抗游戏。可以证明在任意函数G和D的空间中，存在唯一的解决方案，使得G重现训练数据分布，而D=0.5。在G和D由多层感知器定义的情况下，整个系统可以用反向传播进行训练。在训练或生成样本期间，不需要任何马尔科夫链或展开的近似推理网络。实验通过对生成的样品的定性和定量评估证明了本框架的潜力

生成对抗网络常用于生成以假乱真的图片。此外，该方法还被用于生成影片、三维物体模型等。虽然生成对抗网络原先是为了无监督学习提出的，它也被证明对半监督学习、完全监督学习、强化学习是有用的。

GAN的提出者伊恩·古德费洛，曾就读于斯坦福大学，在那里获得了了计算机科学学士和硕士学位，之后在Yoshua Bengio和Aaron Courville 的指导下于蒙特利尔大学获得机器学习博士学位。毕业后，Goodfellow加入Google，成为Google Brain研究小组的成员。2015年他离开了Google，加入了新成立的OpenAI研究所。2017年3月回到Google Research。

Goodfellow最知名的成就就是发明了GAN,被誉为GAN之父。同时他还是 Deep Learning 教材的主要作者。在Google，他开发了一个系统，该系统使Google Maps能够自动转录街景汽车拍摄的照片中的地址，并展示了机器学习系统的安全漏洞。

2017年，Goodfellow被《MIT技术评论》的35位35岁以下的创新者所引用。在2019年，他被列入《外交政策》的100位全球思想家名单。


[1]: https://www.aminer.cn/ai-history
[2]: https://mrt.aminer.cn/5df49f20e8cc00e7af330f6b
