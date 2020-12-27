

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-11 21:28:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 17:42:29
 * @Description:
 * @TODO::
 * @Reference:
-->

## 1. 什么是迁移学习

类比学习（Learning by analogy）：学习者利用两个不同领域中（源域和目标域）的知识相似性，通过类比，从源域的知识推导出目标域的相应知识。类比学习相比与机械学系和示例学习，要求更多的推理。人类科学技术发展过程中，许多科学发现就是通过类比学习实现的，例如著名的卢瑟福类比就是通过将原子结构（目标域）同太阳系（源域）作类比，揭示了原子结构的奥秘。另外，机器学习中重要的迁移学习也是基于该策略[9]

迁移学习(Transfer Learning)是一种机器学习方法，就是把为任务 A 开发的模型作为初始点，重新使用在为任务 B 开发模型的过程中。迁移学习是通过从已学习的相关任务中转移知识来改进学习的新任务，虽然大多数机器学习算法都是为了解决单个任务而设计的，但是促进迁移学习的算法的开发是机器学习社区持续关注的话题。 迁移学习对人类来说很常见，例如，我们可能会发现学习识别苹果可能有助于识别梨，或者学习弹奏电子琴可能有助于学习钢琴。

找到目标问题的相似性，迁移学习任务就是从相似性出发，将旧领域(domain)学习过的模型应用在新领域上。

## 2. 为什么需要迁移学习？

1. **大数据与少标注的矛盾**：虽然有大量的数据，但往往都是没有标注的，无法训练机器学习模型。人工进行数据标定太耗时。
2. **大数据与弱计算的矛盾**：普通人无法拥有庞大的数据量与计算资源。因此需要借助于模型的迁移。
3. **普适化模型与个性化需求的矛盾**：即使是在同一个任务上，一个模型也往往难以满足每个人的个性化需求，比如特定的隐私设置。这就需要在不同人之间做模型的适配。
4. **特定应用（如冷启动）的需求**。

## 3. 迁移学习的基本问题有哪些？

基本问题主要有3个：

- **How to transfer**： 如何进行迁移学习？（设计迁移方法）
- **What to transfer**： 给定一个目标领域，如何找到相对应的源领域，然后进行迁移？（源领域选择）
- **When to transfer**： 什么时候可以进行迁移，什么时候不可以？（避免负迁移）

## 4. 迁移学习有哪些常用概念？

- 基本定义

  - 域(Domain)：数据特征和特征分布组成，是学习的主体
    - **源域 (Source domain)**：已有知识的域
    - **目标域 (Target domain)**：要进行学习的域
  - **任务 (Task)**：由目标函数和学习结果组成，是学习的结果

- 按特征空间分类

  - **同构迁移学习（Homogeneous TL）**： 源域和目标域的特征空间相同，![](https://latex.codecogs.com/gif.latex?D_s=D_t)
  - **异构迁移学习（Heterogeneous TL）**：源域和目标域的特征空间不同，![](https://latex.codecogs.com/gif.latex?D_s\ne_{}D_t)

- 按迁移情景分类

  - **归纳式迁移学习（Inductive TL）**：源域和目标域的学习任务不同
  - **直推式迁移学习（Transductive TL)**：源域和目标域不同，学习任务相同
  - **无监督迁移学习（Unsupervised TL)**：源域和目标域均没有标签

- 按迁移方法分类

  - **基于样本的迁移 (Instance based TL)**：通过权重重用源域和目标域的样例进行迁移

    基于样本的迁移学习方法 (Instance based Transfer Learning) 根据一定的权重生成规则，对数据样本进行重用，来进行迁移学习。下图形象地表示了基于样本迁移方法的思想源域中存在不同种类的动物，如狗、鸟、猫等，目标域只有狗这一种类别。在迁移时，为了最大限度地和目标域相似，我们可以人为地提高源域中属于狗这个类别的样本权重。

    ![](https://gitee.com/kkweishe/images/raw/master/ML/2019-8-17_22-16-3.jpg)

  - **基于特征的迁移 (Feature based TL)**：将源域和目标域的特征变换到相同空间

    基于特征的迁移方法 (Feature based Transfer Learning) 是指将通过特征变换的方式互相迁移,来减少源域和目标域之间的差距；或者将源域和目标域的数据特征变换到统一特征空间中,然后利用传统的机器学习方法进行分类识别。根据特征的同构和异构性,又可以分为同构和异构迁移学习。下图很形象地表示了两种基于特 征的迁移学习方法。

    ![](https://gitee.com/kkweishe/images/raw/master/ML/2019-8-17_22-21-18.jpg)

  - **基于模型的迁移 (Parameter based TL)**：利用源域和目标域的参数共享模型

    基于模型的迁移方法 (Parameter/Model based Transfer Learning) 是指从源域和目标域中找到他们之间共享的参数信息,以实现迁移的方法。这种迁移方式要求的假设条件是： 源域中的数据与目标域中的数据可以共享一些模型的参数。下图形象地表示了基于模型的迁移学习方法的基本思想。

    ![](https://gitee.com/kkweishe/images/raw/master/ML/2019-8-17_22-27-58.jpg)

  - **基于关系的迁移 (Relation based TL)**：利用源域中的逻辑网络关系进行迁移

    基于关系的迁移学习方法 (Relation Based Transfer Learning) 与上述三种方法具有截然不同的思路。这种方法比较关注源域和目标域的样本之间的关系。下图形象地表示了不 同领域之间相似的关系。

    ![](https://gitee.com/kkweishe/images/raw/master/ML/2019-8-17_22-30-12.jpg)

![](https://gitee.com/kkweishe/images/raw/master/ML/2019-8-17_21-51-51.png)

## 5. 迁移学习与传统机器学习有什么区别？

|          | 迁移学习                   | 传统机器学习         |
| -------- | -------------------------- | -------------------- |
| 数据分布 | 训练和测试数据不需要同分布 | 训练和测试数据同分布 |
| 数据标签 | 不需要足够的数据标注       | 足够的数据标注       |
| 建模     | 可以重用之前的模型         | 每个任务分别建模     |

consider a child who has learned to draw people as stick figures. She has discovered a representation of the human form that is both highly compact and rapidly adaptable. By augmenting each stick figure with specifics, she can create portraits of all her classmates: glasses for her best friend, her deskmate in his favorite red tee-shirt.[1]



实用的建议。在进行迁移学习时，还需要记住一些额外的事情:

来自预训练模型的约束。请注意，如果您希望使用一个预先训练过的网络，您可能会受到新数据集使用的架构的轻微限制。例如，您不能从预先训练好的网络中任意取出Conv层。但是，有些变化是直接的:由于参数共享，您可以轻松地在不同空间大小的图像上运行预训练的网络。这在Conv/Pool层中非常明显，因为它们的forward函数独立于输入卷的空间大小(只要大步“适合”)。对于FC层，这一点仍然适用，因为FC层可以转换为卷积层:例如，在AlexNet中，在第一层FC层之前的最终池卷大小为[6x6x512]。因此，查看这个容量的FC层等价于拥有一个接收域大小为6x6的卷积层，并被填充为0。

学习速率。与计算新数据集的类分数的新线性分类器(随机初始化)的权重相比，对正在进行微调的ConvNet权重使用较小的学习率是很常见的。这是因为我们期望ConvNet权重相对较好，所以我们不希望太快和太多地扭曲它们(特别是当上面的新线性分类器是通过随机初始化训练的时候)。

## 7. 迁移学习与其他概念的区别？

1. 迁移学习与多任务学习关系：
   - **多任务学习**：多个相关任务一起协同学习；
   - **迁移学习**：强调信息复用，从一个领域(domain)迁移到另一个领域。
2. 迁移学习与领域自适应：**领域自适应**：使两个特征分布不一致的domain一致。
3. 迁移学习与协方差漂移：**协方差漂移**：数据的条件概率分布发生变化。

## 8. 什么情况下可以使用迁移学习？

迁移学习**最有用的场合**是，如果你尝试优化任务B的性能，通常这个任务数据相对较少。 例如，在放射科中你知道很难收集很多射线扫描图来搭建一个性能良好的放射科诊断系统，所以在这种情况下，你可能会找一个相关但不同的任务，如图像识别，其中你可能用 1 百万张图片训练过了，并从中学到很多低层次特征，所以那也许能帮助网络在任务在放射科任务上做得更好，尽管任务没有这么多数据。

假如两个领域之间的区别特别的大，**不可以直接采用迁移学习**，因为在这种情况下效果不是很好。在这种情况下，推荐以上的方法，在两个相似度很低的domain之间一步步迁移过去（踩着石头过河）。

## 9. 什么是finetune？

度网络的finetune也许是最简单的深度网络迁移方法。**Finetune**,也叫微调、fine-tuning, 是深度学习中的一个重要概念。简而言之，finetune就是利用别人己经训练好的网络，针对自己的任务再进行调整。从这个意思上看，我们不难理解finetune是迁移学习的一部分。

**为什么需要已经训练好的网络？**

在实际的应用中,我们通常不会针对一个新任务,就去从头开始训练一个神经网络。这样的操作显然是非常耗时的。尤其是，我们的训练数据不可能像ImageNet那么大，可以训练出泛化能力足够强的深度神经网络。即使有如此之多的训练数据,我们从头开始训练,其代价也是不可承受的。

**为什么需要 finetune？**

因为别人训练好的模型,可能并不是完全适用于我们自己的任务。可能别人的训练数据和我们的数据之间不服从同一个分布；可能别人的网络能做比我们的任务更多的事情；可能别人的网络比较复杂,我们的任务比较简单。

## 10. 什么是深度网络自适应？

深度网络的 finetune 可以帮助我们节省训练时间，提高学习精度。但是 finetune 有它的先天不足:它无法处理训练数据和测试数据分布不同的情况。而这一现象在实际应用中比比皆是。因为 finetune 的基本假设也是训练数据和测试数据服从相同的数据分布。这在迁移学习中也是不成立的。因此，我们需要更进一步，针对深度网络开发出更好的方法使之更好地完成迁移学习任务。

以我们之前介绍过的数据分布自适应方法为参考，许多深度学习方法都开发出了自适应层(AdaptationLayer)来完成源域和目标域数据的自适应。自适应能够使得源域和目标域的数据分布更加接近，从而使得网络的效果更好。




[1]: https://deepmind.com/blog/article/unsupervised-learning
[2]: https://cs231n.github.io/transfer-learning/
[3]: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
[4]: https://pytorch.org/tutorials/intermediate/quantized_transfer_learning_tutorial.html
[5]: https://github.com/udacity/deep-learning-v2-pytorch/blob/master/transfer-learning/Transfer_Learning_Exercise.ipynbs
[6]: https://github.com/mancinimassimiliano/DeepLearningLab/blob/master/Lab3/finetune_alexnet.ipynb
[7]: https://github.com/NLP-LOVE/ML-NLP/tree/master/Deep%20Learning/13.%20Transfer%20Learning
[8]: https://raw.githubusercontent.com/NLP-LOVE/ML-NLP/master/Deep%20Learning/13.%20Transfer%20Learning/README.md
[9]: https://kangcai.github.io/2018/10/24/ml-overall-1/
