

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-11 21:28:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 17:17:10
 * @Description:
 * @TODO::
 * @Reference:
-->

consider a child who has learned to draw people as stick figures. She has discovered a representation of the human form that is both highly compact and rapidly adaptable. By augmenting each stick figure with specifics, she can create portraits of all her classmates: glasses for her best friend, her deskmate in his favorite red tee-shirt.[1]



实用的建议。在进行迁移学习时，还需要记住一些额外的事情:

来自预训练模型的约束。请注意，如果您希望使用一个预先训练过的网络，您可能会受到新数据集使用的架构的轻微限制。例如，您不能从预先训练好的网络中任意取出Conv层。但是，有些变化是直接的:由于参数共享，您可以轻松地在不同空间大小的图像上运行预训练的网络。这在Conv/Pool层中非常明显，因为它们的forward函数独立于输入卷的空间大小(只要大步“适合”)。对于FC层，这一点仍然适用，因为FC层可以转换为卷积层:例如，在AlexNet中，在第一层FC层之前的最终池卷大小为[6x6x512]。因此，查看这个容量的FC层等价于拥有一个接收域大小为6x6的卷积层，并被填充为0。

学习速率。与计算新数据集的类分数的新线性分类器(随机初始化)的权重相比，对正在进行微调的ConvNet权重使用较小的学习率是很常见的。这是因为我们期望ConvNet权重相对较好，所以我们不希望太快和太多地扭曲它们(特别是当上面的新线性分类器是通过随机初始化训练的时候)。



[1]: https://deepmind.com/blog/article/unsupervised-learning
[2]: https://cs231n.github.io/transfer-learning/
[3]: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
[4]: https://pytorch.org/tutorials/intermediate/quantized_transfer_learning_tutorial.html
[5]: https://github.com/udacity/deep-learning-v2-pytorch/blob/master/transfer-learning/Transfer_Learning_Exercise.ipynbs
