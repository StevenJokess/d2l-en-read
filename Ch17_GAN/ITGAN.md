

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 19:15:43
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 19:58:08
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5f44cfeae4b0118787333996/3?from=p_5f4c7402e4b0dd4d974c43e4&type=6
 * https://ai.deepshare.net/detail/v_5f44d0c6e4b0dd4d974b2498/3?from=p_5f4c7402e4b0dd4d974c43e4&type=6
 * https://ai.deepshare.net/detail/v_5f44d57fe4b0dd4d974b2699/3?from=p_5f4c7402e4b0dd4d974c43e4&type=6
-->

# ITGAN

## GAN的训练改进

### 收敛性的问题

* GAN网络的目的是在高维非凸的参数空间中，找到一个价值函数的纳什均衡点
* 使用梯度下降来优化GAN网络，只能得到较低的损失，不能找到真正的纳什均衡
* 例如，一个网络修改x来最小化xy，另一个网 络修改y来最小化-xy，使用梯度下降进行优化，结果进入一个稳定的轨道中，并不会收敛(0,0)点
* 作者引入了一些方法，希望提高网络的收敛性

## 特征匹配 feature matching

* 判别器的隐层中，经过训练逐渐得到了可用于区分真假样本的特征
* 生成器生成样本的过程中，如果也生成近似这些特征的样本，就可以 更好的近似真实样本
* 尽管不能保证到达均衡点，不过收敛的稳定性应该是有所提高
* 用f(x)表示判别器隐层中的特征，生成器新的目标函数可以被定义为：$\left\|E_{x \sim p_{\text {data }}} f(x)-E_{z \sim p_{z}(z)} f(G(z))\right\|_{2}^{2}$

## 小批量判别 Minibatch discrimination

* 没有一个机制保证生成器需要生成不一样的数据
* 当模式崩溃即将发生时，判别器中许多相似点的 梯度会指向一个相近的方向
* 计算判别器中某一层特征中，同一个batch各样 本特征间的差异，来作为下一层的额外输入
* 这种方法使我们能够非常快速地生成视觉上吸引 人的样本，并且它的效果优于特征匹配
* 如果使用第5节中描述的半监督学习方法获得强 分类器，则特征匹配比本方法效果更好

## 虚拟批归一化(VBN)

* Batch normalization在DCGAN中被应用，能大大减少GAN优化的难度
* 但BN层有个缺点，它会使生成的同一个batch中，每张图片之间存在关联（如一个batch中的图片都有比较多的绿色）
* 为了解决这个问题，训练开始前先选择一个固定的reference batch， 每次算出这个特定batch的均值和方差，再用它们对训练中的batch进行normalization
* 这种方法的缺点是需要进行两次前向传播，增加了计算成本，所以只 在生成器上进行应用

## 历史平均 Historical average

• 在生成网络和判别网络的损失函数中添加一个历史参数的平 均项，这个项在网络训练过程中也会更新
• θ[i]是过去第i时刻，模型的所有参数值 • 加入历史平均项后，梯度就不容易进入稳定的轨道，能够继 续朝着均衡点前进$\left\|\theta-\frac{1}{t} \sum_{i=1}^{t} \theta[i]\right\|^{2}$


## 单向的标签平滑 Label smoothing

• 判别器的目标函数中正负样本的目标输出α和β不再是1和0，而 是接近它们的数字，比如0.9和0.1，则优化目标变为D(X)
• 最近的研究显示，这项技术可以增强分类网络对于对抗样本的 鲁棒性
• 在pdata接近0，而pmodel很大时，D(X)的梯度也接近0，无法优化 • 只将正样本的标签做平滑，负样本的标签仍然设为0
$D(x)=\frac{\alpha p_{\text {data }}(x)+\beta p_{\text {model }}(x)}{p_{\text {data }}(x)+p_{\text {model }}(x)}$


## Assessment of image quality

### 人工评价 Human

* 使用Amazon Mechanical Turk，即亚马逊众包平台进行人工标注
* 将真实图片和生成图像掺杂在一起，标注者需要逐个指出给定图像是真实的还是生
成的
* 当给标注者提供标注反馈时，结果会发生 巨大变化；通过学习这些反馈，标注者能
够更好地指出生成图像中的缺陷，从而更
倾向于把图像标记为生成的

### Inception score

* 提出了一种自动评估样本的方法，这个方法评估的结果与人类的评估高度相关
* 使用Inception模型，以生成图片x为输入，以x的推断类标签概率p(y|x)为输 出
* 单个样本的输出分布应该为低熵，即高预测置信度，好样本应该包含明确有意义 的目标物体
* 所有样本的输出整体分布应该为高熵，也就是说，所有的x应该尽量分属于不同 的类别，而不是属于同一类别
* 因此，Inception score定义为
$\exp \left(E_{x} K L(p(y \mid x) \| p(y))\right)$
$\exp \left(\frac{1}{N} \sum_{i=1}^{N} D_{K L}\left(p\left(y \mid \mathbf{x}^{(i)}\right) \| \hat{p}(y)\right)\right)$

## 半监督学习

流形假设(Manifold Assumption)：将高维数据嵌
入到低维流形中，当两个样例位于低维流形中的一
个小局部邻域内时，它们具有相似的类标签

![unlabelled](img\unlabelled.jpg)

主动学习小于半监督学习。（问老师、查攻略）

$\left.L_{D}=L_{\text {label }}+\left(\frac{w}{2}\right) (L_{\text {unlabel }}+L_{\text {fake }}\right)$
$L_{G}=-L_{\text {fake }}$



* 除了在半监督学习中实现最先进的结果之外，经过主观评测发现，使用半监督学习训练出的生成 器，其生成的图像相比于原始生成器也得到了让人意外的提升
* 这说明我们的视觉系统，对图像类别的理解和对图像质量的理解存在显著相关性，这也佐证了使 用Inception score 来评价生成图像质量的合理性
* 这个关联性可以用来理解迁移学习的作用，并且存在广泛的应用前

* 在DCGAN的基础上，通过多种正则化手段提升可收敛性
* 综合质量和多样性，给出了一条评价GAN生成效果的新路径
* 展示了把GAN生成图像，作为其他图像任务训练集的可行性

 提出的评价指标 Inception score 可以用来比较模型的生成效果
• 将这些技术应用于半监督学习中，在多个数据集上取得了state-of-the-art



[1]: Improved Techniques for Training GANs https://arxiv.org/abs/1606.03498
[2]: videos : https://www.youtube.com/watch?v=bThj0t703v4
