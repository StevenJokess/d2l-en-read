

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 15:23:03
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 16:47:12
 * @Description:
 * @TODO::
 * @Reference:
-->
Model-Agnostic Meta Learning（MAML）

假设你去逛一座城市，酒店租在市中心要比远郊好很多一个道理吧，你很方便就可以到达任意景点[2]

MAML 和 Reptile，它们不改变深度神经网络的结构，只改变网络的初始化参数。[3]

Few-Shot Learning

MetaNMT与multilingual transfer的方法最根本的不同在于后者并没有考虑对于low-resource的pairs的学习过程，而前者显式地利用上面提到的损失函数不断地对其学习过程进行模拟，而这样的模拟过程对于新的任务的fine-tune过程大有裨益。

## 损失函数的奥妙：初始化参数掌控全场，分任务参数各自为营

$L(\phi)=\sum_{n=1}^{N} l^{n}\left(\hat{\theta}^{n}\right)$
$L(\phi)=\sum_{n=1}^{N} l^{n}(\phi)$


反例

![init](img\MAML_init.jpg)

左图为普通训练，右图代表 MAML 初始化。图片来源：李宏毅老师的 PPT

上图中横坐标代表网络参数，纵坐标代表损失函数。浅绿和墨绿两条曲线代表两个 task 的损失函数随参数变化曲线。我们发现如果用公式 (2)，我们将得到左图的效果：在靠近墨绿色曲线的附近，找到可以使两个任务损失函数之和最小的参数$\phi$。但是如果用它作为初始化参数，在 task 2 上训练，我们最终将收敛到 task 2 左侧的 local minima，而不是其右侧更小的 global minima。而使用公式 (1) 时，$\phi$会掌控全场，它不太在意训练集上的损失，而是着眼于最大化网络的学习能力。如右图所示，这个$\phi$就是很好的初始化参数，往左往右，皆可到达不同任务的 global minima。即：左侧图片得到的全局最优解，并不是模型学习能力最强的地方，也就是说，用这个全局最优解初始化网络参数，再在新任务上做 fine-tuning，最终得到的模型可能不会收敛到新任务的最优解。这就是 MAML 优于 fine-tuning 的地方。



和 fine-tuning 预训练网络的技术的区别，个人认为最明显的是：预训练神经网络时，往往有它自己的任务，并没有考虑到将来别人拿这个网络做别的用途。所以它一心一意把自己的 task 搞好就万事大吉了，至于它能用在别的任务中，纯粹是无心插柳。而 Meta Learning 从一开始，就不以降低训练 task 损失函数为唯一目标，它的目标是各个 task 都学一点，然后学一组有潜力的初始化参数，以备将来新的训练任务。[3]

fine-tuning 之所以能 work，是因为预训练的神经网络本身就有很强的特征提取能力，能够提取很多有含义的特征，例如毛皮，耳朵，鼻子，眼睛，分辨猫狗，只需要知道这些特征是如何组合的就好了，这比从头开始学习如何提取毛皮、耳朵、鼻子等特征要高效得多。

MAML 方法的可解释性和通用性成就了它的经典，不拘泥于具体模型结构，不限制其使用任务范围，通过提取模型在多任务上的学习经验，使模型随时“待命”在一个良好的初始状态。当有新任务 “召唤” 它时，它便能凭借极少的训练数据和快速的模型微调迅速对新任务进行适应。[4]

所谓的历史信息也就是之前的transitions(state,action,reward,next_state)。把历史信息输入进去，原来的reinforcement learning就分分钟变成meta reinforcement learning啦。

二次梯度了，这意味着MAML的训练会很慢，那么就很难hold住大网络了。实际上MAML目前对于大的网络结构比如Resnet效果并不好。然后MAML是使用D_train的Loss来更新整个网络，对比HyperNetwork缺少灵活性。这个Loss就是最好的吗？不见得。如果D_train是无监督数据，那怎么办？所以MAML是有局限性的。

其实运用了k-means的思想，就是找到一些prototype，然后每个例子离哪些prototype近，就把它归到那一类。所不同的是这是在嵌入后的空间做得，因为嵌入之前针对像素的含有太多的具体信息，不是值得泛化的信息。[8]


#### 符号表示

我们首先来规定在接下来的叙述中使用的符号表示：

* $\phi$：对于所有任务使用的初始化参数；
* $\phi^{i}$：$\phi$ 进行第 i 次更新后的值；
* $\widehat{\theta}^{n}$：模型从任务 n 中学习到的参数，这个参数由 $\phi$ 进行更新得到；
* $l^n(\widehat{\theta}^{n})$：模型参数为 $\widehat{\theta}^{n}$ 时在任务 n 的测试集上计算得到的损失；
* $L(\phi) = \sum^N\_{n=1}l^n(\widehat{\theta}^{n})$：总体的损失函数；
* $\eta$, $\varepsilon$：两个不同的学习率（值可以相同，但更多情况下不同）。

#### 算法过程

MAML 的训练过程描述如下：

1. 随机初始化 $\phi$（即得到 $\phi^0$）；
2. 从任务的概率分布中采样得到一批任务；
3. 对于这批任务中的每个任务，计算 $\nabla\_{\phi} l(\phi)$，并得到对于该任务得到的自适应参数 $\hat{\theta}=\phi-\varepsilon \nabla\_{\phi} l(\phi)$；
4. 更新 $\phi$：$\phi \leftarrow \phi-\eta \nabla\_{\phi} L(\phi)$；
5. 循环第 2～4 步，直到训练结束。

注意，我们不在意 $\phi$ 在训练任务上的直接表现，而在意用 $\phi$ 训练出来的 $\widehat{\theta}^{n}$ 在训练任务上的表现。模型预训练（Model Pre-training）看起来与 MAML 有相似之处，区别在于模型预训练试图找到在所有任务上直接表现最好的 $\phi$，但并不保证拿 $\phi$ 去训练以后会得到好的 $\widehat{\theta}^{n}$。

从第 3 步的公式 $\hat{\theta}=\phi-\varepsilon \nabla\_{\phi} l(\phi)$ 可以看到，MAML 在对于每个任务进行参数的更新时只更新一次，原因有：

* 元学习的训练的计算量很大，只更新一次参数能够提高计算速度；
* 假设 MAML 能学习出一个非常好的初始化参数，我们希望能够只进行一次参数更新就得到最好的模型参数，因此将其作为目标来看能否实现；
* 在实际测试时，如果只更新一次时效果不好，可以多更新几次；
* 小样本学习的数据很少，多次更新参数容易导致过拟合。

#### 数学推导

重复一遍 MAML 的训练方法：

$$\begin{array}{l}{\phi \leftarrow \phi-\eta \nabla\_{\phi} L(\phi)} \\\ {L(\phi)=\sum\_{n=1}^{N} l^{n}\left(\hat{\theta}^{n}\right)} \\\ {\hat{\theta}=\phi-\varepsilon \nabla\_{\phi} l(\phi)}\end{array}$$

这里，我们来推导一下梯度项 $\nabla\_{\phi} L(\phi)$ 是什么样子。将 $L(\phi)$ 替换，并将求和提取出来，则有：

$$\nabla\_{\phi} L(\phi)=\nabla\_{\phi} \sum\_{n=1}^{N} l^{n}\left(\hat{\theta}^{n}\right)=\sum\_{n=1}^{N} \nabla\_{\phi} l^{n}\left(\hat{\theta}^{n}\right)$$

梯度是一个向量，其每一个维度代表了某一个参数对损失函数的偏微分的结果，即

$$\nabla\_{\phi} l(\hat{\theta})=\left[\begin{array}{c}{\partial l(\hat{\theta}) / \partial \phi\_{1}} \\\ {\partial l(\hat{\theta}) / \partial \phi\_{2}} \\\ {\vdots} \\\ {\partial l(\hat{\theta}) / \partial \phi\_{i}}\end{array}\right]$$

其中，

$$\frac{\partial l(\hat{\theta})}{\partial \phi\_{i}}=\sum\_{j} \frac{\partial l(\hat{\theta})}{\partial \hat{\theta}\_{j}} \frac{\partial \hat{\theta}\_{j}}{\partial \phi\_{i}}$$

$\phi\_{i}$ 是学习到的初始参数，它通过影响 $\hat{\theta}\_{1}, \hat{\theta}\_{2}, \dots, \hat{\theta}\_{j}$ 来最终影响 $l(\hat{\theta})$。

$\frac{\partial l(\hat{\theta})}{\partial \hat{\theta}\_j}$ 与损失函数的形式，以及训练任务中的测试集有关，可以算出。现在来看 $\frac{\partial \hat{\theta}\_{j}}{\partial \phi\_{i}}$ 。从式子

$$\widehat{\theta}=\phi-\varepsilon \nabla\_{\phi} l(\phi)$$

中选择一个维度，则有，

$$\hat{\theta}\_{j}=\phi\_{j}-\varepsilon \frac{\partial l(\phi)}{\partial \phi\_{j}}$$

当 $i \neq j$ 时，

$$\frac{\partial \hat{\theta}\_{j}}{\partial \phi\_{i}}=-\varepsilon \frac{\partial l(\phi)}{\partial \phi\_{i} \partial \phi\_{j}}$$

而如果 $i=j$，则有

$$\frac{\partial \hat{\theta}\_{j}}{\partial \phi\_{i}}=1-\varepsilon \frac{\partial l(\phi)}{\partial \phi\_{i} \partial \phi\_{j}}$$

这样，我们就可以计算来求 $\frac{\partial l(\hat{\theta})}{\partial \phi\_{i}}$ 了。但是，在这个过程中，我们需要进行二次微分来计算 $\frac{\partial l(\phi)}{\partial \phi\_{i} \partial \phi\_{j}}$，非常花时间。因此，提出 MAML 的原论文考虑将其忽略（文中写作 using a first-order approximation），即 $i \neq j$ 时，$\frac{\partial \hat{\theta}\_{j}}{\partial \phi\_{i}} \approx 0$；$i=j$ 时，$\frac{\partial \hat{\theta}\_{j}}{\partial \phi\_{i}} \approx 1$。因此，只需要考虑 $i=j$ 的情况，即

$$\frac{\partial l(\hat{\theta})}{\partial \phi\_{i}}=\sum\_{j} \frac{\partial l(\hat{\theta})}{\partial \hat{\theta}\_{j}} \frac{\partial \hat{\theta}\_{j}}{\partial \phi\_{i}} \approx \frac{\partial l(\hat{\theta})}{\partial \hat{\theta}\_{i}}$$

因此。就变成损失函数对 $\hat{\theta}$ 做偏微分：

$$\nabla\_{\phi} l(\hat{\theta})=\left[\begin{array}{c}{\partial l(\hat{\theta}) / \partial \phi\_{1}} \\\ {\partial l(\hat{\theta}) / \partial \phi\_{2}} \\\ {\vdots} \\\ {\partial l(\hat{\theta}) / \partial \phi\_{i}}\end{array}\right]=\left[\begin{array}{c}{\partial l(\hat{\theta}) / \partial \hat{\theta}\_{1}} \\\ {\partial l(\hat{\theta}) / \partial \hat{\theta}\_{2}} \\\ {\vdots} \\\ {\partial l(\hat{\theta}) / \partial \hat{\theta}\_{i}}\end{array}\right]=\nabla\_{\hat{\theta}} l(\hat{\theta})$$

## Meta-Train

 MAML 的训练过程（一般被称为 meta-train）为：

![maml-alg](img\maml-alg.png)

可以看到对于采样出每个 task $\mathcal{T}_{i},$ 有两层循环：
- inner loop: 在从 $\operatorname{task} \mathcal{T}_{i}$ 中采样出的 support set 上计算梯度并更新参 数 (只更新一次)， 得到更新后的参数 $\theta_{\circ}^{\prime}$ 就像之前所说, 这里的 $\theta^{\prime}$ 只 是一个临时参数, 并不会作为最终的更新 (所以实际操作上是要 copy -
份当前参数去计算 $\theta^{\prime}$ )
- outer loop: 用参数 $\theta^{\prime}$ 在采样出的 query set 上计算损失, 然后对参数 $\theta$ 求梯度, 然后在 $\theta$ 上更新出最终的模型参数。

## Meta-Test[12]

在测试（mete-test）时，会把经过 meta-train 训练好的模型拿去测试集（新 task）的 support set 上 fine-tune，然后在 query set 上得到测试结果。fine-tune 的过程跟 meta-train 基本上差不多，不同点主要是：

第 1 行：meta-train 时的 \thetaθ 是随机初始化的，而 fine-tune 时直接用了经过 meta-train 后得到的 \thetaθ；

第 3 行：fine-tune 的时候就不存在 batch 了，只抽取一个 task 来学习；

第 8 行：fine-tune 的时候不存在这一步，因为这时的 query set 是用来测试模型的，不可能给你算损失然后梯度回传。所以会直接用第 6 行得到的 \theta'θ
′
  作为最终参数。
原论文表明这种优化方法使得计算速度提升了约 33%。并且通过测试发现，算法的效果没有受到明显的影响。[9]

[1]: https://github.com/ZhiqingXiao/pytorch-book/blob/master/chapter12_fewshot/omniglot.ipynb
[2]: https://zhuanlan.zhihu.com/p/55643191
[3]: https://www.tensorinfinity.com/paper_191.html
[4]: https://www.jianshu.com/p/f2af7f5688a6
[5]: https://zhuanlan.zhihu.com/p/46059552
[6]: PyTorch版：https://github.com/dragen1860/MAML-Pytorch
[7]: TensorFlow版：https://github.com/cbfinn/maml
[8]: https://zhuanlan.zhihu.com/p/94693127
[9]: https://github.com/bighuang624/Hung-yi-Lee-ML-notes/edit/master/docs/MAML.md
[10]: https://github.com/cbfinn/maml
[11]: https://arxiv.org/pdf/1703.03400.pdf
[12]: https://renovamen.ink/post/2020/08/05/meta-learning/#fomaml
