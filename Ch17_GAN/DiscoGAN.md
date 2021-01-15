

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:21:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-21 22:42:23
 * @Description:
 * @TODO::
 * @Reference:
-->

# DiscoGAN



While humans easily recognize relations between data from different domains without any supervision, learning to automatically discover them is in general very challenging and needs many ground-truth pairs that illustrate the relations. To avoid costly pairing, we address the task of discovering cross-domain relations given unpaired data. We propose a method based on generative adversarial networks that learns to discover relations between different domains (DiscoGAN). Using the discovered relations, our proposed network successfully transfers style from one domain to another while preserving key attributes such as orientation and face identity.

A,B分别是两个域，[公式] 是由 [公式]生成的由A到B的样本，[公式] 是由以 [公式] 为输入生成的由B到A的样本。 [公式] 用于限制 [公式] 和 [公式] 应该尽可能地相似，d可以用MSE,cos等距离函数。



[1]: https://arxiv.org/pdf/1703.05192.pdf
[2]: https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/discogan/discogan.py
