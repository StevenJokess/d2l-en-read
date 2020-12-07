

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 19:18:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 17:22:55
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/115049575
-->

# AutoGAN: Neural Architecture Search for Generative Adversarial Networks

来自ICCV2019，这篇论文首次将NAS技术运用到GAN上。

## Introduction

NAS已经成功地运用在了图像分类和图像分割任务的backbone上，但是在GAN上还未提及。因此，作者在本文探索了将NAS运用到GAN上面的方法。

其实在之前，GAN的backbone一直没有受很大的重视，之前许多GAN用的backbone都比较简单，像其他图像任务，作者认为增强GAN的主干设计对进一步改进GAN也很重要。所以作者就想到了NAS。

## NAS算法有3个要点：

the search space. 现在有两种策略，一种是一次搜索出整个网络结构(macro search)；另一种是搜索cell，然后按照预定义的方式堆叠在一起(micro search)；
the optimization algorithm. 现在流行的优化算法有：强化学习、进化算法、贝叶斯优化、随机搜索、基于梯度的优化方法。
the proxy task. 即，如何评估训练过程中搜索出的结构的性能。

作者的方法就是，只用NAS搜索G，待G的结构变得深了以后再用预定义的块堆叠出新的D。搜索方法和最初NAS那篇论文一样，使用一个RNN控制器来选择search space里的一个blocks，方案如下图所示：



## Optimization Method

AutoGAN有两组参数：一是RNN控制器的参数 [公式] ，另一个是生成器(搜索过的)和判别器的参数 [公式] ，训练过程的伪代码如下：






hinge loss:





[1]: https://arxiv.org/abs/1908.03835
[2]: https://github.com/TAMU-VITA/AutoGAN
