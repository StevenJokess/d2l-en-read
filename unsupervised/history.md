

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 20:30:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:32:10
 * @Description:
 * @TODO::
 * @Reference:https://www.zhihu.com/org/bei-jing-zhang-liang-wu-xian-ke-ji-you-xian-gong-si/posts?page=6
-->

# 无监督学习

相比于有监督学习，无监督学习的发展一直和缓慢，至今仍未取得大的突破。下面我们按照聚类和数据降维两类问题对这些无监督学习算法进行介绍。

## 聚类

聚类算法的历史与有监督学习一样悠久。层次聚类算法出现于1963年[26]，这是非常符合人的直观思维的算法，现在还在使用。它的一些实现方式，包括SLINK[27]，CLINK[28]则诞生于1970年代

k均值算法[25]可谓所有聚类算法中知名度最高的，其历史可以追溯到1967年，此后出现了大量的改进算法，也有大量成功的应用，是所有聚类算法中变种和改进型最多的。

大名鼎鼎的EM算法[29]诞生于1977年，它不光被用于聚类问题，还被用于求解机器学习中带有缺数数据的各种极大似然估计问题。

Mean Shift算法[32]早在1995年就被用于聚类问题，和DBSCAN算法[30]，OPTICS算法[31]一样，同属于基于密度的聚类算法。

谱聚类算法[33]是聚类算法家族中年轻的小伙伴，诞生于2000年左右，它将聚类问题转化为图切割问题，这一思想提出之后，出现了大量的改进算法。

## 数据降维

下面来说数据降维算法。经典的PCA算法[14]诞生于1901年，这比第一台真正的计算机的诞生早了40多年。LDA在有监督学习中已经介绍，在这里不再重复。

此后的近100年里，数据降维在机器学习领域没有出现太多重量级的成果。直到1998年，核PCA[15]作为非线性降维算法的出现。这是核技术的又一次登台，与PCA的结合将PCA改造成了非线性的降维算法。

从2000年开始，机器学习领域刮起了一阵流形学习的旋风，这种非线性方法是当时机器学习中炙手可热的方向，这股浪潮起始于局部线性嵌入LLL[16]。此后，拉普拉斯特征映射，局部保持投影，等距映射等算法相继提出[17-19]。流形学习在数学上非常优美，但遗憾的是没有多少公开报道的成功的应用。

t-SNE是降维算法中年轻的成员，诞生于2008年，虽然想法很简单，效果却非常好。

[14] Pearson, K. (1901). On Lines and Planes of Closest Fit to Systems of Points in Space. Philosophical Magazine. 2 (11): 559–572.

[15] Schölkopf, Bernhard (1998). "Nonlinear Component Analysis as a Kernel Eigenvalue Problem". Neural Computation. 10: 1299–1319.

[16] Roweis, Sam T and Saul, Lawrence K. Nonlinear dimensionality reduction by locally linear embedding. Science, 290(5500). 2000: 2323-2326.

[17] Belkin, Mikhail and Niyogi, Partha. Laplacian eigenmaps for dimensionality reduction and data representation. Neural computation. 15(6). 2003:1373-1396.

[18] He Xiaofei and Niyogi, Partha. Locality preserving projections. NIPS. 2003:234-241.

[19] Tenenbaum, Joshua B and De Silva, Vin and Langford, John C. A global geometric framework for nonlinear dimensionality reduction. Science, 290(5500). 2000: 2319-2323.

[20] Laurens Van Der Maaten, Geoffrey E Hinton. Visualizing Data using t-SNE. 2008, Journal of Machine Learning Research.

[21] Stratonovich, R.L. (1960). "Conditional Markov Processes". Theory of Probability and its Applications. 5 (2): 156–178.

[22] Pearl J (1985). Bayesian Networks: A Model of Self-Activated Memory for Evidential Reasoning (UCLA Technical Report CSD-850017). Proceedings of the 7th Conference of the Cognitive Science Society, University of California, Irvine, CA. pp. 329–334. Retrieved 2009-05-01.

[23] Moussouris, John (1974). "Gibbs and Markov random systems with constraints". Journal of Statistical Physics. 10 (1): 11–33.

[24] Lafferty, J., McCallum, A., Pereira, F. (2001). "Conditional random fields: Probabilistic models for segmenting and labeling sequence data". Proc. 18th International Conf. on Machine Learning. Morgan Kaufmann. pp. 282–289.

[25] MacQueen, J. B. (1967). Some Methods for classification and Analysis of Multivariate Observations. Proceedings of 5th Berkeley Symposium on Mathematical Statistics and Probability. 1. University of California Press. pp. 281–297. MR 0214227. Zbl 0214.46201. Retrieved 2009-04-07.

[26] Ward, Joe H. (1963). "Hierarchical Grouping to Optimize an Objective Function". Journal of the American Statistical Association. 58 (301): 236–244. doi:10.2307/2282967. JSTOR 2282967. MR 0148188.

[27] R. Sibson (1973). "SLINK: an optimally efficient algorithm for the single-link cluster method" (PDF). The Computer Journal. British Computer Society. 16 (1): 30–34. doi:10.1093/comjnl/16.1.30.

[28] D. Defays (1977). "An efficient algorithm for a complete-link method". The Computer Journal. British Computer Society. 20 (4): 364–366. doi:10.1093/comjnl/20.4.364.

[29] Dempster, A.P.; Laird, N.M.; Rubin, D.B. (1977). "Maximum Likelihood from Incomplete Data via the EM Algorithm". Journal of the Royal Statistical Society, Series B. 39 (1): 1–38. JSTOR 2984875. MR 0501537.

[30] Ester, Martin; Kriegel, Hans-Peter; Sander, Jörg; Xu, Xiaowei (1996). Simoudis, Evangelos; Han, Jiawei; Fayyad, Usama M., eds. A density-based algorithm for discovering clusters in large spatial databases with noise. Proceedings of the Second International Conference on Knowledge Discovery and Data Mining (KDD-96). AAAI Press. pp. 226–231.

[31] Mihael Ankerst, Markus M. Breunig, Hans-Peter Kriegel, Jörg Sander (1999). OPTICS: Ordering Points To Identify the Clustering Structure. ACM SIGMOD international conference on Management of data. ACM Press. pp. 49–60.

[32] Yizong Cheng. Mean Shift, Mode Seeking, and Clustering. IEEE Transactions on Pattern Analysis and Machine Intelligence, 1995.

[33] Jianbo Shi and Jitendra Malik, "Normalized Cuts and Image Segmentation", IEEE Transactions on PAMI, Vol. 22, No. 8, Aug 2000.

