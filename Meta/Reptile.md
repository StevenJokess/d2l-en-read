

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 16:31:05
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 17:37:20
 * @Description:
 * @TODO::
 * @Reference:
-->

Reptile (Nichol, Achiam & Schulman, 2018) is a remarkably simple meta-learning optimization algorithm. It is similar to MAML in many ways, given that both rely on meta-optimization through gradient descent and both are model-agnostic.


Reptile 的训练过程如下：

1. 随机初始化 $\phi$（即得到 $\phi^0$）；
2. 从任务的概率分布中采样得到一批任务；
3. Reptile 在具体任务上的参数更新方式与 MAML 相同，只是不限制在一个训练任务上的参数更新次数，因此我们**多次**更新参数，得到 $\hat{\theta}^m$；
4. 让 $\phi^{0}$ 沿着 $\phi^{0}$ 到 $\hat{\theta}^m$ 的方向更新一次，得到 $\phi^{1}$；
5. 循环第 2～4 步，直到训练结束。

![](https://raw.githubusercontent.com/bighuang624/pic-repo/master/Hung-yi-Lee-Reptile.png)

可以看到，Reptile 的过程与模型预训练有相似之处。为了区分 Reptile、MAML 和模型预训练，我们有下图所示例子：

![](https://raw.githubusercontent.com/bighuang624/pic-repo/master/Hung-yi-Lee-Meta-Learning-comparision.png)

可以看到，当我们要决定初始参数 $\phi$ 的更新方向时，我们先利用采样得到的训练任务进行两次更新，方向分别为 $g\_1$ 和 $g\_2$。那么，模型预训练中的 $\phi$ 更新方向为 $g\_1$，MAML 中的 $\phi$ 更新方向为 $g\_2$，而 Reptile 中的 $\phi$ 更新方向为 $g\_1 + g\_2$（当然，如之前所说，Reptile 没有限制只能走两步，这里只是以两次更新为例）。

Demo of Reptile: [https://openai.com/blog/reptile](https://openai.com/blog/reptile)

作者认为 Reptile 和 MAML 的优化目标都为（5.1 节）：

沿 task 上的损失的平均梯度方向更新模型，使模型在当前任务上的表现更好

最大化同一个 task 中多个 batch 的梯度的内积。因为梯度的内积越大说明它们夹角越小，意味着它们的更新方向越相似，因此在一个 batch 上的更新同时还能提升在另外一个 batch 上的性能，从而使模型在当前任务上具有更好的泛化性。

[1]: https://arxiv.org/pdf/1803.02999.pdf
[2]: https://github.com/bighuang624/Hung-yi-Lee-ML-notes/edit/master/docs/MAML.md
[3]: https://renovamen.ink/post/2020/08/05/meta-learning/#fomaml
[4]: https://lilianweng.github.io/lil-log/2018/11/30/meta-learning.html
