

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 17:13:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 17:13:38
 * @Description:
 * @TODO::
 * @Reference:https://lilianweng.github.io/lil-log/2017/08/20/from-GAN-to-WGAN.html
-->
## Kullback–Leibler and Jensen–Shannon Divergence

Before we start examining GANs closely, let us first review two metrics for quantifying the similarity between two probability distributions.

(1) KL (Kullback–Leibler) divergence measures how one probability distribution p diverges from a second expected probability distribution q.

DKL(p∥q)=∫xp(x)logp(x)q(x)dx
DKL achieves the minimum zero when p(x) == q(x) everywhere.

It is noticeable according to the formula that KL divergence is asymmetric. In cases where p(x) is close to zero, but q(x) is significantly non-zero, the q’s effect is disregarded. It could cause buggy results when we just want to measure the similarity between two equally important distributions.

(2) Jensen–Shannon Divergence is another measure of similarity between two probability distributions, bounded by [0,1]. JS divergence is symmetric (yay!) and more smooth. Check this Quora post if you are interested in reading more about the comparison between KL divergence and JS divergence.

DJS(p∥q)=12DKL(p∥p+q2)+12DKL(q∥p+q2)
KL and JS divergence

Fig. 1. Given two Gaussian distribution, p with mean=0 and std=1 and q with mean=1 and std=1. The average of two distributions is labelled as m=(p+q)/2. KL divergence DKL is asymmetric but JS divergence DJS is symmetric.

Some believe (Huszar, 2015) that one reason behind GANs’ big success is switching the loss function from asymmetric KL divergence in traditional maximum-likelihood approach to symmetric JS divergence. We will discuss more on this point in the next section.
