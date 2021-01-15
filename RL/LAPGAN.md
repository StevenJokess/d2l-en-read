

# LAPGAN(Laplacian Generative Adversarial Networks)

## 动机

早期以DCGAN为代表的网络生成的图片分辨率太低，质量不够好，都不超过100×100，在32×32或者64×64左右。这是因为难以一次性学习到生成高分辨率的样本，收敛过程容易不稳定。

类似的问题在图像分割，目标检测中都存在。在目标检测中，级联网络被广泛使用，即采用从粗到精的方法依次改进检测器的性能。在图像分割中进行上采样时也采用学习小倍率的放大而不是大倍率的方法，如利用两个2倍上采样替换一个4倍的上采样，不仅可以增强网络的表达能力，还降低了学习难度。

基于此，金字塔GAN结构被提出并广泛使用，它参考图像领域里面的金字塔结构由粗到精一步一步生成图像，并添加残差进行学习。

## 高斯金字塔与拉普拉斯金字塔[2]

LAPGAN将条件生成对抗网络CGAN集成到它的拉普拉斯金字塔结构中, 符号约定如下:

(1) G0. G1.....Gk表示k个卷积网络 (即生成器Generator)
(2) z表示噪声数据, 符合某种分布, 如高斯分布;
下式表示高斯金字塔的重建过程:
$$
\tilde{I}_{k}=u\left(\tilde{I}_{k+1}\right)+\tilde{h}_{k}=u\left(\tilde{I}_{k+1}\right)+G_{k}\left(z_{k}, u\left(\tilde{I}_{k+1}\right)\right)
$$
高斯金字塔的第k层重建需要用它的第k+ 1 层上采样(即u(Ik+1))加上拉普拉斯金字塔第k层 (即 hk)，其中hk是第k个生成器Gk通过zk和u(Ik+1)生成的。其中Ik+1初始值为0, 最高级的Gk仅 仅使用噪声矢量Z作为输入生成Ik, 因为它没有上一级:
$$
\tilde{I}_{K}=G_{K}\left(z_{K}\right)
$$
除了最高级以外, 其余的生成器G0、G1.....Gk-1都采用上一级的上采样u(Ik)和噪声zk作为联合输 $\lambda,$ 其中上采样u(Ik)就是“条件变量"。。


[1]: http://papers.nips.cc/paper/5773-deep-generative-image-models-using-a-laplacian-pyramid-of-adversarial-networks.pdf
[2]: https://zhuanlan.zhihu.com/p/94153155
