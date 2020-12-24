

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-11 21:28:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 23:44:53
 * @Description:
 * @TODO::
 * @Reference:
-->

## 1. 什么是迁移学习

迁移学习(Transfer Learning)是一种机器学习方法，就是把为任务 A 开发的模型作为初始点，重新使用在为任务 B 开发模型的过程中。迁移学习是通过从已学习的相关任务中转移知识来改进学习的新任务，虽然大多数机器学习算法都是为了解决单个任务而设计的，但是促进迁移学习的算法的开发是机器学习社区持续关注的话题。 迁移学习对人类来说很常见，例如，我们可能会发现学习识别苹果可能有助于识别梨，或者学习弹奏电子琴可能有助于学习钢琴。

找到目标问题的相似性，迁移学习任务就是从相似性出发，将旧领域(domain)学习过的模型应用在新领域上。

## 2. 为什么需要迁移学习？

1. **大数据与少标注的矛盾**：虽然有大量的数据，但往往都是没有标注的，无法训练机器学习模型。人工进行数据标定太耗时。
2. **大数据与弱计算的矛盾**：普通人无法拥有庞大的数据量与计算资源。因此需要借助于模型的迁移。
3. **普适化模型与个性化需求的矛盾**：即使是在同一个任务上，一个模型也往往难以满足每个人的个性化需求，比如特定的隐私设置。这就需要在不同人之间做模型的适配。
4. **特定应用（如冷启动）的需求**。




consider a child who has learned to draw people as stick figures. She has discovered a representation of the human form that is both highly compact and rapidly adaptable. By augmenting each stick figure with specifics, she can create portraits of all her classmates: glasses for her best friend, her deskmate in his favorite red tee-shirt.[1]



实用的建议。在进行迁移学习时，还需要记住一些额外的事情:

来自预训练模型的约束。请注意，如果您希望使用一个预先训练过的网络，您可能会受到新数据集使用的架构的轻微限制。例如，您不能从预先训练好的网络中任意取出Conv层。但是，有些变化是直接的:由于参数共享，您可以轻松地在不同空间大小的图像上运行预训练的网络。这在Conv/Pool层中非常明显，因为它们的forward函数独立于输入卷的空间大小(只要大步“适合”)。对于FC层，这一点仍然适用，因为FC层可以转换为卷积层:例如，在AlexNet中，在第一层FC层之前的最终池卷大小为[6x6x512]。因此，查看这个容量的FC层等价于拥有一个接收域大小为6x6的卷积层，并被填充为0。

学习速率。与计算新数据集的类分数的新线性分类器(随机初始化)的权重相比，对正在进行微调的ConvNet权重使用较小的学习率是很常见的。这是因为我们期望ConvNet权重相对较好，所以我们不希望太快和太多地扭曲它们(特别是当上面的新线性分类器是通过随机初始化训练的时候)。




[1]: https://deepmind.com/blog/article/unsupervised-learning
[2]: https://cs231n.github.io/transfer-learning/
[3]: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
[4]: https://pytorch.org/tutorials/intermediate/quantized_transfer_learning_tutorial.html
[5]: https://github.com/udacity/deep-learning-v2-pytorch/blob/master/transfer-learning/Transfer_Learning_Exercise.ipynbs
[6]: https://github.com/mancinimassimiliano/DeepLearningLab/blob/master/Lab3/finetune_alexnet.ipynb
[7]: https://github.com/NLP-LOVE/ML-NLP/tree/master/Deep%20Learning/13.%20Transfer%20Learning
[8]: https://raw.githubusercontent.com/NLP-LOVE/ML-NLP/master/Deep%20Learning/13.%20Transfer%20Learning/README.md
