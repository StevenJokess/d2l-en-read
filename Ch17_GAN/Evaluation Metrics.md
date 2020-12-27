

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 16:56:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 16:59:23
 * @Description:
 * @TODO::
 * @Reference:
-->

## Inception Score (IS)

Proposed by Salimans et al. (2016),the  IS  offers  a  way  to  quantitatively  evaluate  the  qual-ity of generated samples.   Intuitively,  the conditional la-bel distribution of samples containing meaningful objectsshould have low entropy,  and the variability of the sam-ples  should  be  high.   which  can  be  expressed  asIS=exp(Ex∼Q[dKL(p(y|x),p(y))]).  The authors found thatthis score is well-correlated with scores from human anno-tators. Drawbacks include insensitivity to the prior distribu-tion over labels and not being a properdistance.

## Frechet Inception Distance (FID)

In this approach pro-posed by Heusel et al. (2017) samples fromPandQarefirst embedded into a feature space (a specific layer of Incep-tionNet). Then, assuming that the embedded data follows amultivariate Gaussian distribution, the mean and covarianceare estimated. Finally, the Fr ́echet distance between thesetwo Gaussians is computed, i.e.FID=||μx−μy||22+ Tr(Σx+ Σy−2(ΣxΣy)12),where(μx,Σx), and(μy,Σy)are the mean and covarianceof the embedded samples fromPandQ, respectively. Theauthors argue that FID is consistent with human judgmentand more robust to noise than IS. Furthermore, the scoreis sensitive to the visual quality of generated samples – in-troducing noise or artifacts in the generated samples willreduce the FID. In contrast to IS, FID can detect intra-classmode dropping – a model that generates only one image perclass will have a good IS, but a bad FID (Lucic et al., 2018).

## Kernel Inception Distance (KID)

Bi ́nkowski   et   al.(2018) argue that FID has no unbiased estimator and suggestKID as an unbiased alternative. In Appendix B we empir-ically compare KID to FID and observe that both metricsare very strongly correlated (Spearman rank-order correla-tion coefficient of0.994forLSUN-BEDROOMand0.995forCELEBA-HQ-128datasets). As a result we focus on FID asit is likely to result in the same ranking.

[1]: https://arxiv.org/abs/1807.04720
