

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 16:56:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:40:48
 * @Description:
 * @TODO::
 * @Reference:
-->

## Inception Score (IS)

Proposed by Salimans et al. (2016),the  IS  offers  a  way  to  quantitatively  evaluate  the  qual-ity of generated samples.   Intuitively,  the conditional la-bel distribution of samples containing meaningful objectsshould have low entropy,  and the variability of the sam-ples  should  be  high.   which  can  be  expressed  asIS=exp(Ex∼Q[dKL(p(y|x),p(y))]).  The authors found thatthis score is well-correlated with scores from human anno-tators. Drawbacks include insensitivity to the prior distribu-tion over labels and not being a properdistance.

Inception Score 使用了如下两种评判标准来检验模型的表现：

生成图片的质量
生成图片的多样性


### 两个假设：

越真实的图片，输入预训练的 Inception V3 ，分类的结果越明确。即在1000维的输出向量中，某一维很大，其余维很小。也就是说，输出的概率分布函数图越尖锐。
生成的图片多样性越强，那么类别的边缘分布就越平均，边缘分布的概率函数图像就越平整。

### 最明显的两个问题：

针对第一个假设，是否越真实的图片，分类网络输出的概率分布函数越尖锐？显然是不见得的，如果某一个物体所属的类别在分类网络中并不存在，那么它的分布函数依然尖锐吗？
针对第二个假设，是否输出图片均匀地覆盖每个类别，就意味着生成模型不存在 mode collapse？Inception net 输出 1000 类，假设生成模型在每类上都生成了 50 个图片，那么生成的图片的类别边缘分布是严格均匀分布的，按照 Inception Score 的假设，这种模型不存在 mode collapse，但是，如果各类中的50个图片，都是一模一样的，仍然是 mode collapse。Inception Score 无法检测这种情况。



计算 IS 时只考虑了生成样本，没有考虑真实数据，即 IS 无法反映真实数据和样本之间的距离，IS 判断数据真实性的依据，源于 Inception V3 的训练集： ImageNet，在 Inception V3 的“世界观”下，凡是不像 ImageNet 的数据，都是不真实的，都不能保证输出一个 sharp 的 predition distribution。

## Fréchet Inception Distance (FID)

In this approach pro-posed by Heusel et al. (2017) samples fromPandQarefirst embedded into a feature space (a specific layer of Incep-tionNet). Then, assuming that the embedded data follows amultivariate Gaussian distribution, the mean and covarianceare estimated. Finally, the Fr ́echet distance between thesetwo Gaussians is computed, i.e.FID=||μx−μy||22+ Tr(Σx+ Σy−2(ΣxΣy)12),where(μx,Σx), and(μy,Σy)are the mean and covarianceof the embedded samples fromPandQ, respectively. Theauthors argue that FID is consistent with human judgmentand more robust to noise than IS. Furthermore, the scoreis sensitive to the visual quality of generated samples – in-troducing noise or artifacts in the generated samples willreduce the FID. In contrast to IS, FID can detect intra-classmode dropping – a model that generates only one image perclass will have a good IS, but a bad FID (Lucic et al., 2018).

计算了真实图片和假图片在 feature 层面的距离

$\mathrm{FID}=\left\|\mu_{r}-\mu_{g}\right\|^{2}+T r\left(\Sigma_{r}+\Sigma_{g}-2\left(\Sigma_{r} \Sigma_{g}\right)^{1 / 2}\right)$

众所周知，预训练好的神经网络顶层可以提取图片的高级信息，一定程度能反映图片的本质。因 此, $\mathrm{FID}$ 的提出者通过预训练的 Inception $\mathrm{V} 3$ 来提取全连接层之前的 2048 维向量, 作为图片的特 征。公式 (1) 中:
$\mu_{r} ：$ 真实图片的特征的均值
$\mu_{g} ：$ 生成的图片的特征的均值
$\Sigma_{r}:$ 真实图片的特征的协方差矩阵
$\Sigma_{g}:$ 生成图片的特征的协方差矩阵




https://github.com/mseitzer/pytorch-fid

FID 只是某一层的特征的分布，是否足以衡量真实数据分布与生成数据分布的距离？同时，提出 FID 公式计算的是多元正态分布的距离，显然神经网络提取的特征并不是多元正态分布。
针对同一个生成模型，不同框架下预训练的 Inception V3 算出的 FID 差别是否可以忽略？
FID 无法反映生成模型过拟合的情况，如果某个生成模型只是简单拷贝训练数据，FID 会非常小，认为这是一个完美的生成模型，因此，使用 FID 时同时也要通过别的手段证明生成模型没有过拟合。

## Kernel Inception Distance (KID)

Bi ́nkowski   et   al.(2018) argue that FID has no unbiased estimator and suggestKID as an unbiased alternative. In Appendix B we empir-ically compare KID to FID and observe that both metricsare very strongly correlated (Spearman rank-order correla-tion coefficient of0.994forLSUN-BEDROOMand0.995forCELEBA-HQ-128datasets). As a result we focus on FID asit is likely to result in the same ranking.

[1]: https://arxiv.org/abs/1807.04720
