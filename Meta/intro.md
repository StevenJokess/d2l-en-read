

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 21:48:04
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-14 22:43:51
 * @Description:
 * @TODO::
 * @Reference:
-->

# 什么是元学习

它将自动学习算法应用到机器学习实践用到的元数据中，它的主要目标是使用元数据来了解元学习，并且通过提高现有的学习算法的性能或者学习学习算法本身，灵活地解决学习问题。

三种方式：1）学习一个有效的距离度量标准（metric-based）；2）使用具有外部存储或者内部存储的网络（model-based）；3）明确优化模型参数以进行快速学习（optimization-based）。

元学习可以简单地定义为获取知识多样性（knowledge versatility）的能力。作为人类，我们能够以最少的信息同时快速完成多个任务，例如人类在有了世界的概念之后，看一张图片就能学会识别一种物体

对新任务的适应过程，实质上是一个最小学习单元，这个过程只需要少量的训练就可以快速完成。最终，适应后的模型可以完成新任务。这就是为什么元学习也被称为“学会学习”的原因。

元学习的目的是从已有任务中学习一种学习方法或元知识，可以加速新任务的学习．从这个角度来说，元学习十分类似于归纳迁移学习，但元学习更侧重从多种不同（甚至是不相关）的任务中归纳出一种学习方法．和元学习比较相关的另一个机器学习问题是小样本学习（Few-shot Learn-ing），即在小样本上的快速学习能力．每个类只有𝐾个标注样本，𝐾非常小．如https://nndl.github.io/
10.6元学习2020年6月14日246果𝐾 = 1，称为单样本学习（One-shot Learning）；如果𝐾 = 0，称为零样本学习（Zero-shot Learning）

## 基于优化器的元学习

目前神经网络的学习方法主要是定义一个目标损失函数ℒ(𝜃)，并通过梯度下降算法来最小化ℒ(𝜃)：


$\theta_{t+1}=\theta_{t}+g_{t}\left(\nabla \mathcal{L}\left(\theta_{t}\right) ; \phi\right)$


学习优化器𝑔𝑡(⋅)的过程可以看作一种元学习过程，其目标是找到一个适用于多个不同任务的优化器．在标准梯度下降中，每步迭代的目标是使得ℒ(𝜃)下降．而在优化器的元学习中，我们希望在每步迭代的目标是ℒ(𝜃)最小，具体的目标函数为

$\begin{aligned} \mathcal{L}(\phi) &=\mathbb{E}_{f}\left[\sum_{t=1}^{T} w_{t} \mathcal{L}\left(\theta_{t}\right)\right] \\ \theta_{t} &=\theta_{t-1}+g_{t} \\\left[g_{t} ; \boldsymbol{h}_{t}\right] &=\operatorname{LSTM}\left(\nabla \mathcal{L}\left(\theta_{t-1}\right), \boldsymbol{h}_{t-1} ; \phi\right) \end{aligned}$

其中𝑇为最大迭代次数，𝑤𝑡> 0为每一步的权重，一般可以设置𝑤𝑡= 1,∀𝑡．由于LSTM网络可以记忆梯度的历史信息，学习到的优化器可以看作一个高阶的优化方法．

在每步训练时，随机初始化模型参数，计算每一步的ℒ(𝜃𝑡)，以及元学习的损失函数ℒ(𝜙)，并使用梯度下降更新参数．由于神经网络的参数非常多，导致LSTM网络的输入和输出都是非常高维的，训练这样一个巨大的网络是不可行的．因此，一种简化的方法是为每个参数都使用一个共享的LSTM网络来进行更新，这样可以使用一个非常小的共享LSTM网络来更新参数．



## 模型无关的元学习（Model-Agnostic Meta-Learning，MAML）

模型无关的元学习（Model-Agnostic Meta-Learning，MAML）是一个简单的模型无关、任务无关的元学习算法[Finn et al.,2017]．假设所有的任务都来自于一个任务空间，其分布为𝑝(𝒯)，我们可以在这个任务空间的所有任务上学习一种通用的表示，这种表示可以经过梯度下降方法在一个特定的单任务上进行精调．假设一个模型为𝑓𝜃，如果我们让这个模型适应到一个新任务𝒯𝑚上，通过一步或多步的梯度下降更新，学习到的任务适配参数为

$\theta_{m}^{\prime}=\theta-\alpha \nabla_{\theta} \mathcal{L}_{j_{m}}\left(f_{\theta}\right)$

其中𝛼为学习率．这里𝜃′𝑚可以理解为关于𝜃的函数，而不是真正的参数更新

MAML的目标是学习一个参数𝜃使得其经过一个梯度迭代就可以在新任务上达到最好的性能，即

$\min _{\theta} \sum_{\mathcal{T}_{m} \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{J}_{m}}\left(f_{\theta_{m}^{\prime}}\right)=\min _{\theta} \sum_{\mathcal{J}_{m} \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{J}_{m}}\left(f(\underbrace{\theta-\alpha \nabla_{\theta} \mathcal{L}_{\mathcal{J}_{m}}\left(f_{\theta}\right)}_{\theta_{m}^{\prime}})\right)$

在所有任务上的元优化（Meta-Optimization）也采用梯度下降来进行优化，即

$\begin{aligned} \theta & \leftarrow \theta-\beta \nabla_{\theta} \sum_{m=1}^{M} \mathcal{L}_{\mathcal{J}_{m}}\left(f_{\theta_{m}^{\prime}}\right) \\ &=\theta-\beta \sum_{m=1}^{M} \nabla_{\theta} \mathcal{L}_{\mathcal{J}_{m}}\left(f_{\theta_{m}}\right)\left(I-\alpha \nabla_{\theta}^{2} \mathcal{L}_{\mathcal{J}_{m}}\left(f_{\theta_{m}}\right)\right) \end{aligned}$


其中𝛽为元学习率，𝐼为单位阵．这一步是一个真正的参数更新步骤．这里可以看出，当𝛼比较小时，MAML就近似为普通的多任务学习优化方法．MAML需要计算关于𝜃的二阶梯度，但用一些近似的一阶方法通常也可以达到比较好的性能．


在“元”层面运用机器学习技术[1]

这种方法指的是，在系统设计阶段，离线使用机器学习技术来发现能提高智能体在线学习效率的结构、算法和先验知识。
元学习的基本概念至少从上世纪80年代在机器学习和统计学中出现，基本思路是：在系统设计阶段，元学习过程便能访问系统在线学习时可能面临的许多潜在任务或环境的样本。
元学习器的目的不在于掌握适应单个环境的多种策略或适用于全部环境的单项策略，而是掌握一种在线学习时面临新任务或新环境时也尽可能高效学习的算法。这个目标可以通过在训练任务间引入共性，并使用这些共性形成有力的先验或归纳偏置，使在线学习的智能体只学习那些将新任务与训练任务区分开来的方面。

元学习主要关注如何在多个不同任务上学习一种可泛化的快速学习能力[4]．

[1]: https://www.leiphone.com/news/202009/VV75HfxY7dwQPurq.html
[2]: https://weread.qq.com/web/reader/62332d007190b92f62371aeka4a32da02aba4a042cf4e81
[3]: https://weread.qq.com/web/reader/62332d007190b92f62371aek1ff321e02ac1ff8a7b5d0fc
[4]: Thrun S, Pratt L, 2012. Learning to learn[M]. Springer Science & Business Media.
[5]: https://nndl.github.io/
