

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 19:18:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 15:55:25
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/115049575
 * [2]: Auto-GAN论文解读-论文部分 - 科技猛兽的文章 - 知乎
https://zhuanlan.zhihu.com/p/149458578
-->

# AutoGAN: Neural Architecture Search for Generative Adversarial Networks

来自ICCV2019，这篇论文首次将NAS技术运用到GAN上。

## Introduction

NAS已经成功地运用在了图像分类和图像分割任务的backbone上，但是在GAN上还未提及。因此，作者在本文探索了将NAS运用到GAN上面的方法。

首要问题是，即使是手工设计的结构，GAN的训练也是不稳定并且容易发生模式坍缩（mode collapse），再引入NAS无疑会增大训练的难度。另一个重要挑战是，NAS在图像分类中一般选择验证准确率作为奖励，但选择一个好的评价指标来评估和指导GAN网络结构搜索过程并非易事。

其实在之前，GAN的backbone一直没有受很大的重视，之前许多GAN用的backbone都比较简单，像其他图像任务，作者认为增强GAN的主干设计对进一步改进GAN也很重要。所以作者就想到了NAS。

## 创新点总结如下：

（1）定义了GAN网络结构变化的搜索空间，使用RNN控制器来指导结构搜索，结合参数共享和动态重置策略，提高训练速度。

（2）在AutoGAN的优化中，使用IS作为奖励。搜索到的模型在其他GAN指标（如FID）上也能表现出良好的性能。

（3）受Progressive GAN渐进式训练的启发，引入了多级结构搜索（MLAS），MLAS通过beam search以自下而上的顺序方式（in a bottom-up sequential）在多个阶段中进行搜索。

## NAS算法有3个要点：

AutoGAN使用RNN控制器从搜索空间中选择基本单元块来构建G网络，其基本方案如图1所示。AutoGAN同样包括三个关键方面：搜索空间，搜索策略，和性能评估。

the search space. 现在有两种策略，一种是一次搜索出整个网络结构(macro search)；另一种是搜索cell，然后按照预定义的方式堆叠在一起(micro search)；
the optimization algorithm. 现在流行的优化算法有：强化学习、进化算法、贝叶斯优化、随机搜索、基于梯度的优化方法。
the proxy task. 即，如何评估训练过程中搜索出的结构的性能。

作者的方法就是，只用NAS搜索G，待G的结构变得深了以后再用预定义的块堆叠出新的D。搜索方法和最初NAS那篇论文一样，使用一个RNN控制器来选择search space里的一个blocks，方案如下图所示：


## Search Space

AutoGAN基于多级搜索策略，生成器由一系列基本单元组成。用一个(s+5)的元素组 表示第几个单元(Cells)，第0个单元没有 连接，图2说明了AutoGAN生成器的搜索空间：

上图为AutoGAN中生成器单元的搜索空间，各个符号的意思如下：

[skip_i] 是一个二进制值表示当前第s单元是否使用跳转连接把第i-1单元（i=1，…，s）的输出作为输入。每个单元可以从其他先前的单元进行多个跳转连接。
[C] 是基本卷积块的类型，包括预激活和后激活卷积块。
[N] 表示归一化类型，包括BN、实例归一化及不使用归一化。
[U] 表示上采样操作，包括双线性上采样，最近邻上采样和步长为2的反卷积。U还将确定跳转连接特征图的上采样方法。
[SC] 是二进制值表示是否使用cell内部的shortcut。



## Optimization Method

AutoGAN有两组参数：一是RNN控制器的参数 [公式] ，另一个是生成器(搜索过的)和判别器的参数 [公式] ，训练过程的伪代码如下：

![](autoGAN_search.jpg)

搜索算法为：第1阶段固定 [公式] 训练 [公式] ：采样一个结构，训练几轮GAN的参数，一旦训练损失标准差低于阈值, [公式] 将被设置为True，同时训练立即终止，Generator与Discriminator的参数重置。

第2阶段固定 [公式] 训练 [公式] ：先从shared Generator里面采样 [公式] 个子模型，以Inception score为reward，强化学习方法更新RNN controller。迭代 [公式] 次以后，从派生结构中挑选出最好的K个结构，生成器和对应的判别器将对应增长。同时，初始化一个新的controller继续下一阶段的结构搜索：

具体来说，

第1阶段：Training shared GAN

固定RNN controller policy [公式] 并且update shared parameter，


第2阶段：Training the controller

RNN Controller通过Adam optimizer更新。每个step LSTM会输出一个hidden vector，把它解码以后输出对应的操作的编号。

最终架构的确定方法：

使用 [公式] 采样一些子模型并计算Reward，取出Reward最大的K个。从头训练。最后计算它们的IS score，得分最大的作为结果。



## Proxy Task

Inception score和FID是GAN的两个主要评价指标。由于FID的计算非常耗时，因此本文选择每个派生子模型的IS作为通过强化学习更新控制器的奖励。

作者使用Inception score(IS)来作为奖励，通过强化学习来更新控制器。基于NAS中的参数共享技术，作者进一步为AutoGAN引入了参数动态重置(dynamic-resetting)策略，即，设置一个移动窗口来存储训练过程的损失值，当窗口中的损失值得标准差小于一个预定义得阈值时，停止当前迭代次数训练，更新RNN控制器然后再重新初始化GAN。

在当前迭代中更新完控制器后，再重新初始化GAN模型的参数。注意，不需要重新初始化RNN控制器的参数，这样才能继承历史知识来继续指导网络结构搜索。[2]

作者提出这一策略的目的是，使得搜索过程更加有效，依据在于根据经验，作者观察到mode collapse时训练损失(hinge loss)的方差通常变得非常小。



## Training Shared GAN

hinge loss:

\begin{aligned}
\mathcal{L}_{D}=& E_{x \sim q_{d a t a}}[\min (0,-1+D(x)]+\\
& E_{z \sim p(z)}[\min (0,-1-D(G(z))]\\
\mathcal{L}_{G} &=E_{z \sim p(z)}[\min (0, D(G(z))]
\end{aligned}

消融实验：

1. 代理任务的有效性：
代理任务的evaluation与真实的evaluation是相关的：
2. 使用FID score作为Reward：
3. 参数动态重置：
GAN的训练过程极不稳定，经过长时间的训练，很容易出现模式崩溃。继续训练共享崩溃模型可能是浪费时间。因此，我们引入参数动态重置来缓解这个问题。为了比较，作者在CIFAR10上进行了两个AutoGAN实验，分别采用了动态重置和参数共享策略。我们在两个培训过程中进行评估。如下图所示，动态复位的训练过程只需要43小时，而不需要动态复位的训练过程则需要72小时。



AutoGAN无疑还有很大的改进空间：

1. 搜索空间还可以更大。比如说加入一些 attention 的候选 block，还可以加入 Wasserstein loss 等等；
2. 可以换到更大分辨率的数据集，如 ImageNet 。不过在低分辨率的 CIFAR 10 上搜索要 43 个小时，换到大图上肯定要尝试更高效的搜索算法；
3. 本文其实没有怎么搜判别器 D，可以研究怎么得到更好的判别器 D；
4. 如何和 Conditional GAN 结合，在训练的时候引入标签信息。



[1]: https://arxiv.org/abs/1908.03835
[2]: https://github.com/TAMU-VITA/AutoGAN
