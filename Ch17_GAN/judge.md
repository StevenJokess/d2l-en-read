

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 16:04:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 20:24:03
 * @Description:
 * @TODO::
 * @Reference:
-->

对于生成效果和质量, 却只能依赖于视觉上的观察, 由人眼去判断生成的质量好坏. 有些评价指标在数值上虽高, 但是实际的生成效果却不好. 因此, GAN很难找到一个比较客观的、可量化的评价指标.[1]

## 7.2 GAN的生成能力评价

### 7.2.1 如何客观评价GAN的生成能力？

​	最常见评价GAN的方法就是主观评价。主观评价需要花费大量人力物力，且存在以下问题：

- 评价带有主管色彩，有些bad case没看到很容易造成误判

- 如果一个GAN过拟合了，那么生成的样本会非常真实，人类主观评价得分会非常高，可是这并不是一个好的GAN。

因此，就有许多学者提出了GAN的客观评价方法。

### 7.2.2 Inception Score

​	对于一个在ImageNet训练良好的GAN，其生成的样本丢给Inception网络进行测试的时候，得到的判别概率应该具有如下特性：
- 对于同一个类别的图片，其输出的概率分布应该趋向于一个脉冲分布。可以保证生成样本的准确性。
- 对于所有类别，其输出的概率分布应该趋向于一个均匀分布，这样才不会出现mode dropping等，可以保证生成样本的多样性。

​	因此，可以设计如下指标：
$$
IS(P_g)=e^{E_{x\sim P_g}[KL(p_M(y|x)\Vert{p_M(y)})]}
根据前面分析，如果是一个训练良好的GAN，$p_M(y|x)​$趋近于脉冲分布，$p_M(y)​$趋近于均匀分布。二者KL散度会很大。Inception Score自然就高。实际实验表明，Inception Score和人的主观判别趋向一致。IS的计算没有用到真实数据，具体值取决于模型M的选择
$$
​	根据前面分析，如果是一个训练良好的GAN，$p_M(y|x)$趋近于脉冲分布，$p_M(y)$趋近于均匀分布。二者KL散度会很大。Inception Score自然就高。实际实验表明，Inception Score和人的主观判别趋向一致。IS的计算没有用到真实数据，具体值取决于模型M的选择。

​	**特点：可以一定程度上衡量生成样本的多样性和准确性，但是无法检测过拟合。Mode Score也是如此。不推荐在和ImageNet数据集差别比较大的数据上使用。**

### 7.2.3 Mode Score

​	Mode Score作为Inception Score的改进版本，添加了关于生成样本和真实样本预测的概率分布相似性度量一项。具体公式如下：
$$
MS(P_g)=e^{E_{x\sim P_g}[KL(p_M(y|x)\Vert{p_M(y)})-KL(p_M(y)\Vert p_M(y^*))]}
$$

### 7.2.4 Kernel MMD (Maximum Mean Discrepancy)

计算公式如下：
$$
MMD^2(P_r,P_g)=E_{x_r\sim{P_r},x_g\sim{P_g}}[\lVert\Sigma_{i=1}^{n1}k(x_r)-\Sigma_{i=1}^{n2}k(x_g)\rVert]
$$
​	对于Kernel MMD值的计算，首先需要选择一个核函数$k$，这个核函数把样本映射到再生希尔伯特空间(Reproducing Kernel Hilbert Space, RKHS) ，RKHS相比于欧几里得空间有许多优点，对于函数内积的计算是完备的。将上述公式展开即可得到下面的计算公式：
$$
MMD^2(P_r,P_g)=E_{x_r,x_r{'}\sim{P_r},x_g,x_g{'}\sim{P_g}}[k(x_r,x_r{'})-2k(x_r,x_g)+k(x_g,x_g{'})]
$$
MMD值越小，两个分布越接近。

**特点：可以一定程度上衡量模型生成图像的优劣性，计算代价小。推荐使用。**

### 7.2.5 Wasserstein distance

​	Wasserstein distance在最优传输问题中通常也叫做推土机距离。这个距离的介绍在WGAN中有详细讨论。公式如下：
$$
WD(P_r,P_g)=min_{\omega\in\mathbb{R}^{m\times n}}\Sigma_{i=1}^n\Sigma_{i=1}^m\omega_{ij}d(x_i^r,x_j^g)
$$

$$
s.t. \Sigma_{i=1}^mw_{i,j}=p_r(x_i^r),  \forall i;\Sigma_{j=1}^nw_{i,j}=p_g(x_j^g),  \forall j
$$

​	Wasserstein distance可以衡量两个分布之间的相似性。距离越小，分布越相似。

**特点：如果特征空间选择合适，会有一定的效果。但是计算复杂度为$O(n^3)​$太高**

### 7.2.6 Fréchet Inception Distance (FID)

​	FID距离计算真实样本，生成样本在特征空间之间的距离。首先利用Inception网络来提取特征，然后使用高斯模型对特征空间进行建模。根据高斯模型的均值和协方差来进行距离计算。具体公式如下：
$$
FID(\mathbb P_r,\mathbb P_g)=\lVert\mu_r-\mu_g\rVert+Tr(C_r+C_g-2(C_rC_g)^{1/2})
$\mu,C$分别代表协方差和均值。
$$
$\mu,C​$分别代表协方差和均值。

​	**特点：尽管只计算了特征空间的前两阶矩，但是鲁棒，且计算高效。**

### 7.2.7 1-Nearest Neighbor classifier

​	使用留一法，结合1-NN分类器（别的也行）计算真实图片，生成图像的精度。如果二者接近，则精度接近50%，否则接近0%。对于GAN的评价问题，作者分别用正样本的分类精度，生成样本的分类精度去衡量生成样本的真实性，多样性。
- 对于真实样本$x_r$，进行1-NN分类的时候，如果生成的样本越真实。则真实样本空间$\mathbb R$将被生成的样本$x_g$包围。那么$x_r$的精度会很低。
- 对于生成的样本$x_g​$，进行1-NN分类的时候，如果生成的样本多样性不足。由于生成的样本聚在几个mode，则$x_g​$很容易就和$x_r​$区分，导致精度会很高。

**特点：理想的度量指标，且可以检测过拟合。**

### 7.2.8 其他评价方法

​	AIS，KDE方法也可以用于评价GAN，但这些方法不是model agnostic metrics。也就是说，这些评价指标的计算无法只利用：生成的样本，真实样本来计算。
[1]: http://www.c-s-a.org.cn/html/2019/11/7156.html#outline_anchor_12
[2]:
