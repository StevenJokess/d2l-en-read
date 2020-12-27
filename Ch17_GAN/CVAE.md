

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 14:58:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 15:01:58
 * @Description:
 * @TODO::
 * @Reference:
-->

# 条件VAE

VAE是无监督训练的，因此很自然想到：如果有标签数据，那么能不能把标签信息加进去辅助生成样本呢？这个问题的意图，往往是希望能够实现控制某个变量来实现生成某一类图像。当然，这是肯定可以的，我们把这种情况叫做Conditional VAE，或者叫CVAE。

我们希望X经过编码后，Z的分布都具有零均值和单位方差，这个“希望”是通过加入了KL loss来实现的。如果现在多了类别信息Y，我们可以希望同一个类的样本都有一个专属的均值μY（方差不变，还是单位方差），这个μY让模型自己训练出来。

在VAE的基础上加入最少的代码来实现CVAE的方案了，因为这个“新希望”也只需通过修改KL loss实现：

$\mathcal{L}_{\mu, \sigma^{2}}=\frac{1}{2} \sum_{i=1}^{d}\left[\left(\mu_{(i)}-\mu_{(i)}^{Y}\right)^{2}+\sigma_{(i)}^{2}-\log \sigma_{(i)}^{2}-1\right]$

CVAE与GAN结合的工作[CVAE-GAN](https://arxiv.org/abs/1703.10155)
