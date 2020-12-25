

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-26 02:38:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 02:39:13
 * @Description:
 * @TODO::
 * @Reference:https://github.com/NVIDIA/DeepLearningExamples/blob/master/PyTorch/Recommendation/DLRM/notebooks/Pytorch_DLRM_pyt_train_and_inference.ipynb
-->

DLRM是Facebook引入的一种基于深度学习的推荐方法。与其他基于深度学习的方法一样，DLRM的设计目的是利用RecSys训练数据中通常出现的分类和数字输入。通过图1可以了解DLRM的体系结构。为了处理分类数据，嵌入层将每个分类映射到一个密集表示，然后再送入密集多层感知器(MLP)。连续特征可以直接送入密集的MLP。在下一个层次上，不同特征的二阶相互作用通过所有嵌入向量对和处理过的密集特征之间的点积来显式计算。这些成对的交互被输入到一个顶级的MLP中，以计算用户和物品之间交互的可能性。

与其他基于DL的推荐方法相比，DLRM有两个不同之处。首先，DLRM明确计算特性交互，同时将交互的顺序限制为成对交互。其次，DLRM将每个嵌入的特征向量(对应于类别特征)作为一个单元，而其他方法将特征向量中的每个元素作为一个新单元，该单元应该产生不同的交叉项。这些设计选择有助于降低计算/内存成本，同时保持具有竞争力的准确性。
