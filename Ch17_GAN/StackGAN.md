

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-12 18:56:47
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-16 13:31:24
 * @Description:
 * @TODO::
 * @Reference:
-->

StackGAN: Text to Photo-Realistic Image Synthesis with Stacked Generative Adversarial Networks[2]



Han Zhang, Tao Xu, Hongsheng Li, Shaoting Zhang, Xiaolei Huang, Xiaogang Wang, Dimitris Metaxas. “StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks”. arXiv preprint 2016. 第三篇这方面的工作[20]可以粗略认为是 LAPGAN[16] 和 matching-aware[18] 的结合。他们提出的 StackGAN[20] 做的事情从标题生成鸟类，但是生成的过程则是像 LAPGAN 一样层次化的，从而实现了 256X256 分辨率的图片生成过程。StackGAN 将图片生成分成两个阶段，阶段一去捕捉大体的轮廓和色调，阶段二加入一些细节上的限制从而实现精修。这个过程效果很好，甚至在某些数据集上以及可以做到以假乱真：

## 提出 StackGAN 分段式结构

本文提出了 Stacked Generative Adversarial Networks (StackGAN) 结构，用于根据文字描述，生成对应的 256 * 256 的真实图像（首次这么高的分辨率）。我们将该问题分解为可处理的子问题。

首先是 Stage-I，根据给定的文字描述，勾勒初始的形状和色彩，生成低分辨率的图像，如图一 (a) 所示。

然后 Stage-II 根据 Stage-I 生成的低分辨率图像以及原始文字描述，生成具有更多细节的高分辨率图像。这个阶段可以重新捕获被 Stage-I 忽略的文字描述细节，修正 Stage-I 的的结果的缺陷，并添加改良的细节，如图一 (b) 所示。

从低分辨率图像生成的模型分布与自然图像分布相交叠的概率更好。这就是 Stage-II 能够生成高分辨率图像的根本原因。

## 提出 Conditioning Augmentation 技术

对于 text-to-image 生成任务，text-image 训练数据对（image + text）数量有限，这将导致文本条件多样性的稀疏性(sparsity in the text conditioning manifold)，而这种稀疏性使得 GAN 很难训练。

因此，我们提出了一种新颖的条件增强技术(Conditioning Augmentation technique) 来改善生成图像的多样性，并稳定 conditional-GAN 的训练过程，这使得隐含条件分布更加平滑 (encourages smoothness in the latent conditioning manifold)。



典型的使用多对 GAN 的模型有 StackGAN[3]

StackGAN 首先输出分辨率为 64×64 的图像，然后将其作为先验信息生成一个 256×256 分辨率的图像。[4]


一个StackGAN由一对网络组成，当提供文本描述时，可以生成逼真的图像。

正如上图所看到的，提供文本描述时，StackGAN生成了逼真的鸟类图像。最重要的是生成的图像正类似于所提供的文本。文本到图像合成有许多实际应用，例如从一段文本描述中生成图像，将文本形式的故事转换为漫画，创建文本描述的内部表现。[5]

## Stage-I

### 理论基础

Stage-I 阶段主要用于生成粗略的形状和颜色等。先从 $\mathcal{N}\left(\mu_{0}\left(\varphi_{t}\right), \Sigma_{0}\left(\varphi_{t}\right)\right)$ 中随机采样出 $\hat{c}_{0}$,
器 $D_{0}$ 和 $D_{0},$ 分别对应如下目标函数:
$\max \quad \mathcal{L}_{D_{0}}=\mathbb{E}_{\left(I_{0}, t\right) \sim p_{\text {data }}}\left[\log \left(D_{0}\left(I_{0}, \varphi_{t}\right)\right)\right]+\mathbb{E}_{z \sim p_{z}, t \sim p_{\text {data }}}\left[\log \left(1-D_{0}\left(G_{0}\left(z, \hat{c}_{0}\right), \varphi_{t}\right)\right)\right]$
$$
\min \quad \mathcal{L}_{G_{0}}=\mathbb{E}_{z \sim p_{z}, t \sim p_{\text {data }}}\left[\log \left(1-D_{0}\left(G_{0}\left(z, \hat{c}_{0}\right), \varphi_{t}\right)\right)\right]+\lambda D_{K L}\left(\mathcal{N}\left(\mu_{0}\left(\varphi_{t}\right), \Sigma_{0}\left(\varphi_{t}\right)\right) \| \mathcal{N}(0, I)\right)
$$
其中，真实图像 $I_{0}$ 和文本描述 $\mathrm{t}$ 源自于实际数据分布 $p_{\text {data }}$ 。 $\quad$ z 表示从高斯分布分布 $p_{\text {data }}$ 中 随机提取的噪声向量。 $\quad \lambda$ 为正则化参数， 用于平衡公式
(3) 中的两项。
我们的实验中，设置为 $\lambda=1$ 。其中, $\quad \mu_{0}\left(\varphi_{t}\right), \Sigma_{0}\left(\varphi_{t}\right)$ 是与网络剩余部分一起学习。

### 模型结构

Conditioning Augmentation
对于生成器 $G_{0}$, 为了获取文本条件变量 $\hat{c}_{0},$ 词嵌入向量 $\varphi_{t}$ 首先通过全连接层来生成高斯分布 $\mathcal{N}\left(\mu_{0}\left(\varphi_{t}\right), \Sigma_{0}\left(\varphi_{t}\right)\right.$ 中的 $\mu_{0}, \sigma_{0}$
然后, 从中随机采样出 $\hat{c}_{0}=\mu_{0}+\sigma_{0} \odot \epsilon$ 。其中,
( $)$ 表示对应元素相乘, 且 $\epsilon \sim \mathcal{N}(0, I)$ 。
$G_{0}$
随后将获取的 $\hat{c}_{0}$ 与 $N_{z}$ 维噪声向量进行拼接（concatenate $）,$ 作为 $G_{0}$ 的输入, 通过一组上 采样 up-sampling 生成 $W_{0} \times H_{0}$ 的图像。
$D_{0}$
对于判别器 $D_{0}$ ，首先用全连接层将词向量 $\varphi_{t}$ 压缩到 $N_{d},$ 随后进行空间性重复, 得到 $M_{d} \times M_{d} \times N_{d}$ 。同时，将图像输入到一系列下采样 down-sampling , 从而得到 $M_{d} \times M_{d} \times N_{d}$ 尺寸的 tensor
随后, 将文本 tensor 和图像 tensor 进行拼接, 然后输入到一个 $1 \times 1$ 的卷积层, 从而同时综 合文本和图像的信息。最后，用一个只有一个节点的全连接层来生成置信度得分。。

## Stage-II

Stage-I 阶段生成的低分辨率图像通常缺之鲜明的目标特征，并且可能包含一些变形。同时, 文本 描述中的部分信息可能也未体现出来。所以, 通过 Stage-II 可以在 Stage-I 生成的低分辨率图 像和文本描述的基础上，生成高分辨率图片，其修正了 Stage-I 的缺陷，并完善了被忽略的文本信 息细节。

Stage-II 以高斯隐含变量 $\hat{c}$ 以及 'Stage-I' 的生成器的输出 $s_{0}=G_{0}\left(z, \hat{c}_{0}\right)$ 为输入, 来训练生 $\begin{array}{lll}\text { 成器 } & \text { G 和判别器 } & \text { D } & \text { 其目标函数分别为： }\end{array}$ :
$\max \quad \mathcal{L}_{D}=\mathbb{E}_{(I, t) \sim p_{\text {data }}}\left[\log \left(D\left(I, \varphi_{t}\right)\right)\right]+\mathbb{E}_{s_{0} \sim p_{G_{0}}, t \sim p_{\text {data }}}\left[\log \left(1-D\left(G\left(s_{0}, \hat{c}\right), \varphi_{t}\right)\right)\right]$
$\min \quad \mathcal{L}_{G}=\mathbb{E}_{s_{0} \sim p_{G_{0}}, t \sim p_{\text {data }}}\left[\log \left(1-D\left(G\left(s_{0}, \hat{c}\right), \varphi_{t}\right)\right)\right]+\lambda D_{K L}\left(\mathcal{N}\left(\mu\left(\varphi_{t}\right), \Sigma\left(\varphi_{t}\right)\right) \| \mathcal{N}(0, I)\right)$
模型结构
Conditioning Augmentation
首先就是通过词向量 $\varphi_{t}$ 来获取 $\hat{c},$ 其过程与 Stage-I 一样。。。。。
G
首先 $\hat{c}$ 通过空间重复, 变成 $M_{g} \times M_{g} \times N_{g}$ 的 tensor $\quad$ (这里的空间上雷复使之，将原来的 $1 \times 1 \times N_{g}$ 在 $1 \times 1$ 的维度上，进行重复, 得到 $M_{g} \times M_{g}$ )
同时, 将 Stage-I 的输出通过下采样网络，变成尺寸为 $1 \times 1$ 的 tensor, 并与上面的文本 $1 \times 1$ 的 tensor 在通道的维度上进行拼接。。
接着，将上面的 tensor 送入一系列的残差块, 从而习得综合文本描述和图像信息的特征。。。。。。
最后，用上采样网络进行处理, 从而生成 $W \times H$ 的图像。。
$\mathbf{D}$
判别器部分与 Stage-I 别无二致，除了输入尺寸的变化导致的下采样层不同。
此外，在训练阶段, 判别器的输入中，正类样本为真实图像及其对应的文本描述; 而负类样本包含

https://github.com/hanzhanggit/StackGAN-Pytorch



[1]: https://blog.csdn.net/u014625530/article/details/82964796
[2]: https://mrt.aminer.cn/5f324b8b647095ce48741f64
[3]: https://github.com/OUCMachineLearning/OUCML/blob/master/GAN/%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C%E7%BB%BC%E8%BF%B0.md
[4]: https://www.infoq.cn/article/gcgibopiftpbe9deqf3m
[5]: https://www.shuzhiduo.com/A/gAJG4R6o5Z/
[6]: StackGAN - 会飞的闲鱼的文章 - 知乎 https://zhuanlan.zhihu.com/p/78102953
