

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:42:04
 * @Description:
 * @TODO::
 * @Reference:
-->

# 《Large scale GANtraining for high fidelity natural image synthesis》


在 SAGAN 的基础上，BigGAN [2]尝试将 GAN 的训练扩展到大规模上去，利用正交 正则化等技巧保证训练过程的稳定性。BigGAN 的意义在于启发人们，GAN 网络的训练同 样可以从大数据、大算力等方面受益。BigGAN 图片生成效果达到了前所未有的高度： Inception score 记录提升到 166.5(提高了 52.52)；Frechet Inception Distance 下降到 7.4，降 低了 18.65，如图 13.13 所示，图片的分辨率可达512 × 512，图片细节极其逼真。

网络已经学会了如何表示其训练的图片的许多关键特征，如动物身体的结构、草的纹理以及光影的细节效果（即使是通过肥皂泡折射的）。但仔细观察下面这些图，就不免能发现些许小异常，如白狗明显多了条腿，喷泉其中一个喷嘴的水流呈奇怪的直角状。虽然生成式模型的开发者在努力避免这种不完美，但这些可见的不完美也突显了重建熟悉的数据（如图像）的一个好处，即研究人员可以通过检查样本，推断出模型学到了什么以及没有学到什么。[1]

## 之前的相关工作

近期的研究工作集中在修改初始的GAN算法，使得它更稳定。这些方法中，既有经验性的分析，也有理论性的分析。其中一种思路是修改训练时的目标函数以确保收敛。另外一种思路是通过梯度惩罚或归一化技术对D进行限定，这两种方法都是在抵抗对无界的目标函数的使用，确保对任意的G，D都能提供梯度。


## 用截断技巧在真实性和多样性之间做折中

生成器的随机噪声输入一般使用正态分布或者均匀分布的随机数。本文采用了截断技术，对正态分布的随机数进行截断处理，实验发现这种方法的结果最好。对此的直观解释是，如果网络的随机噪声输入的随机数变动范围越大，生成的样本在标准模板上的变动就越大，因此样本的多样性就越强，但真实性可能会降低。首先用截断的正态分布N(0,1)随机数产生噪声向量Z，具体做法是如果随机数超出一定范围，则重新采样，使得其落在这个区间里。这种做法称为截断技巧：将向量Z进行截断，模超过某一指定阈值的随机数进行重采样，这样可以提高单个样本的质量，但代价是降低了样本的多样性。下图证明了这一点：



## 总结[5]

作者得出的结论是，稳定性不单单来源于G或者D，而是两者在对抗训练过程中相互作用的结果。它们病态条件的症状可以用来跟踪和鉴别不稳定性，确保合理的条件被证明对于训练是必须的但对防止训练崩溃时不充分的，即必要不充分。对D进行严格的限制能确保稳定性，但会严重损失最终生成的数据的质量。以现有的技术，可以放宽这个条件并允许崩溃在训练出一个好的结果之后发生和达到更好的数据生成效果。



[1]: https://www.leiphone.com/news/201904/LhyoY2oy3cC5MzII.html
[2]: https://github.com/huggingface/pytorch-pretrained-BigGAN
[3]: https://github.com/anhtuan85/Generative-Adversarial-Networks-GANs-Specialization/blob/main/Course%202%20-%20Build%20Better%20Generative%20Adversarial%20Networks%20(GANs)/Week%203/BigGAN.ipynb
[4]: https://github.com/ajbrock/BigGAN-PyTorch
[5]: BigGAN论文解读 - SIGAI的文章 - 知乎
https://zhuanlan.zhihu.com/p/51507779
