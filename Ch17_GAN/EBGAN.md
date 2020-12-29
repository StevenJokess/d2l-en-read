

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:21:38
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:03:46
 * @Description:
 * @TODO::
 * @Reference:
-->

Energy-Based GAN (EBGAN)
https://arxiv.org/pdf/1609.03126.pdf

EBGAN在边缘的生成效果上更流畅, 而且加了特殊的正则项, 在生成的类别上, EBGAN更倾向于生成不同的脸型和人种[2]

朴素GAN提出将二分类器作为判别器以判别真实数据和生成数据，并将生成数据“拉向”生成数据。然而自从WGAN抛弃了二分类器这个观点，取以函数fω代替，并不将之局限在[0,1]之后，很多改进模型也采取了类似的方法，并将之扩展开来。例如LS-GAN以损失函数L−θ(x)作为目标，要求L−θ(x)在真实样本上尽可能小，在生成样本尽可能大。

基于能量的GAN(Energy-based GAN, EBGAN)则将之具体化了。它将能量模型以及其相关理论引入GAN，以“能量”函数在概念上取代了二分类器，表示对真实数据赋予低能量，对生成数据赋予高能量。





$L_{D}^{E B G A N}=D_{A E}(x)+\max \left(0, m-D_{A E}(G(z))\right)$
$L_{G}^{E B G A N}=D_{A E}(G(z))+\lambda \cdot P T$

![](img\EBGAN.png)

首先，EBGAN给出了它的目标函数
$$
\begin{array}{l}
L_{D}(x, z)=D(x)+[m-D(G(z))]^{+} \\
L_{G}(z)=D(G(z))
\end{array}
$$
其中 $[\cdot]^{+}=\max \{0, \cdot\},$ 极大化 $L_{D}$ 的同时极小化 $L_{G}$ 。EBGAN的设计思想是，一方面词少真实数据的重构误差，另一方面，使得生成 数据的重构误差趋近于m, 即当 $D(G(z))<m$ 时，改下为正，对 $L_{D}$ 的极小化产生贡献，反之 $D(G(z)) \geq m,$ 为 $L_{D}$ 为0，会通过极小 化 $L_{G},$ 将 $D(G(z))$ 拉向m。可以证明，当 $D=D^{*}, G=G^{*}$ 到达Nash均衡时，生成数据分布等于真实数据分布，并且此时 $L_{D}$ 的期望即 $V\left(D^{*}, G^{*}\right)=\int_{x, z} L_{D} p_{\text {data}}(x) p_{z}(z) d x d z=m$
此外在EBGAN中，对D的结构也做了改进。不再采用DCGAN 对D的网络框架或者其相似结构，EBGAN对D的架构采用自动编码器的模式, 模型架构如图所示
Zimage.png
图 4 EBGAN模型架构
可以发现，其判别器或者说能量函数D可以写作
$$
D(x)=\|\operatorname{Dec}(\operatorname{Enc}(x))-x\|
$$
其中Enc, Dec是自编码器中的编码与解码操作。
最后，由于自编码器的特殊构造，EBGAN 还针对 $L_{G}$ 做了特殊设计，即增加一个正则项 $f_{P T}$ 来避免模式崩溃 (mode collapse)问题。 设 $S \in R^{S \times N \text { 是一个 }}$ batch的编码器（encoder）输出结果, $f_{P T}$ 可以定义为
$$
f_{P T}(S)=\frac{1}{N(N-1)} \sum_{i} \sum_{j \neq i}\left(\frac{S_{i}^{T} S_{j}}{\left\|S_{i}\right\|\left\|S_{j}\right\|}\right)^{2}
$$


其思想很简单，利用一个批次的编码器输出结果计算余弦距离并求和取均值，若这一项越小，则两两向量越接近正交。从而解决模式崩溃问题，不会出现一样或者极其相似的图片数据。



[2]: https://zhuyinlin.github.io/build/html/algorithm/GAN.html#sgan-stacked-gan
[3]: http://www.tensorinfinity.com/paper_26.html
