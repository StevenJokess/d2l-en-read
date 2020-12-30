

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 15:22:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 19:42:37
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/245566551
 * https://kexue.fm/archives/6016
 * https://mp.weixin.qq.com/s/iqCMA7E_vtdymVxxz7bpRA
-->

# f-GAN

## f-散度

GAN 的核心本质是通过对抗训练将随机噪声的分布拉近到真实的数据分布，那么就需要一个度量概率分布的指标—散度。我们熟知的散度有 KL 散度公式如下（KL 散度有一个缺点就是距离不对称性，所以说它不是传统真正意义上的距离度量方法）。

$$
D_{K L}(p \| q):=\int_{\mathbb{R}^{n}} \log \left(\frac{p(x)}{q(x)}\right) p(x) d x
$$
和 JS 散度公式如下 (JS 散度是改进了 KL 散度的距离不对称性)：
$$
D_{J S}(p \| q):=\frac{1}{2} D_{K L}(p \| M)+\frac{1}{2} D_{K L}(q \| M)
$$

但是其实能将所有我们熟知散度归结到一个大类那就是 $f$ - 散度, 具体的定义如下所示
定义1: 设 $p(x)$ 和 $q(x)$ 是 $\mathbb{R}^{n}$ 上的两个概率密度函数。则 $p$ 和 $q$ 的 $f$ - 散度定义为:

$$
D_{f}(p \| q):=\mathbb{E}_{\mathbf{x} \sim q}\left[f\left(\frac{p(\mathbf{x})}{q(\mathbf{x})}\right)\right]=\int_{\mathbb{R}^{n}} f\left(\frac{p(x)}{q(x)}\right) q(x) d x
$$

其中, 如果 $q(x)=0$ 时, 会有 $f\left(\frac{p(x)}{q(x)}\right) q(x)=0_{\circ}$
需要搞清楚一点事的 f- 散度依据所选函数不一样, 距离的不对称也不一样。

命题3：设 $f(x)$ 是域 $I \subseteq \mathbb{R}$ 上的严格凸函数, 使得 $f(1)=0_{\text {假设supp }(p)} \subseteq \operatorname{supp}(q)$ (相
当于 $p \ll q$ 或 $f(t)>0,$ 其中 $t \in[0,1)$ 。则有 $D_{f}(p \| q) \geq 0, \quad D_{f}(p \| q)=0$ 当且仅当
$p(x)=q(x)$


通过f散度去构建一般的GAN模型，  散度是KL散度的一般化

对于给定的概率分布 ，f-GAN 的目标是最小化相对于概率分布  的 f- 散度 。在样本空间中，f-GAN 解决了下面的极大极小问题：

$\min _{\nu} \sup _{T}\left(\mathbb{E}_{\mathbf{x} \sim \nu}[T(\mathbf{x})]-\mathbb{E}_{\mathbf{x} \sim \mu}\left[f^{*}(T(\mathbf{x}))\right]\right)$

可以将如上的优化问题称为变分散度最小化（VDM）。注意 VDM 看起来类似于 GAN 中的极大极小值问题，其中 Borel 函数$T$被称为评判函数。


Algorithm 2 f-GAN Algorithm Input: 随机噪声 $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{m}\right\}$ in $\mathbb{R}^{d} ;$ 真实样本 $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{m}\right\} \subset \mathcal{X}$.
Output:生成样本 $X_{\text {fake }}$
1: for $t=0$ to $T-1$ do
2: $\quad$ 从高斯噪声分布 $\gamma$ 中随机采样出m个样本，即 $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{m}\right\}$ in $\mathbb{R}^{d}$;
3: $\quad$ 从真实数据分布 $\mathcal{X}$ 中随机采样出m个样本，即 $\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{m}\right\} \subset \mathcal{X}$;
4: $\quad$ 通过小批量随机梯度下降法来更新判别器 $S_{\omega}$ 的参数 $\omega,$ 具体公式 为:
$$
\nabla_{\omega} \frac{1}{m} \sum_{i=1}^{m}\left[g_{f}\left(S_{\omega}\left(G_{\theta}\left(\mathbf{z}_{i}\right)\right)\right)-f^{*}\left(g_{f}\left(S_{\omega}\left(\mathbf{x}_{i}\right)\right)\right)\right]
$$
$5: \quad$ 再从高斯噪声分布 $\gamma$ 中随机采样出另外的m个样本，即 $\left\{\mathbf{z}_{1}, \ldots, \mathbf{z}_{m}\right\}$ in $\mathbb{R}^{d}$;
6: $\quad$ 通过小批量随机梯度下降法来更新判别器 $G_{\theta}$ 的参数，具体公式为:
$$
\nabla_{\theta} \frac{1}{m} \sum_{i=1}^{m} g_{f}\left(S_{\omega}\left(G_{\theta}\left(\mathbf{z}_{i}\right)\right)\right)
$$
7: return $X_{\text {fake}}$


