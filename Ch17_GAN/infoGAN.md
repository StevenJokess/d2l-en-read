

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 23:10:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-14 23:16:31
 * @Description:
 * @TODO::
 * @Reference:https://www.zhihu.com/column/c_1186629504699731968
-->


解耦表示（disentangled representation）

InfoGAN，是伯克利大学和openAI联手在NIPS2016发表的论文，提出了用GAN结合互信息来学习变量的解耦表示，并在MNIST、3D人脸和椅子、CelebA、SVHN数据集上都取得了不错的实验效果。

InfoGAN的思想也很简单，GAN的原始噪声z可以看成是数据的一种latent code，但z本身是杂乱无章的，为实现解耦目的，将z按维度拆分成z和解耦表示c两个部分。其中新的z仍然是杂乱无章的，而latent code c仅仅包含原来z中若干个维度，每个维度可以是离散的也可以是连续的，用来表示数据中的解耦变化因子。比如作者在测试MNIST图像时，取z中3个维度作为c，1个离散，2个连续，最后习得的c，离散的维度表示不同数字，连续的维度分别表示了数字的旋转和粗细：



这是总的模型架构，其中值得注意的是，文章直接用判别器作为变分网络 [公式]，最后一层同时输出c的预测和真假的预测。

思考
InfoGAN的互信息项使latent code c尽可能包含更多的关于生成图像的信息，因此能够捕捉不同的变化因子，但是这无法解释c具有解耦的能力。根据近两年的一些文章，可以作出一些猜测：

1.由于c每个维度间是独立的，并且一般假设Q(c|x)维度间独立，因此这样能够促进c的不同维度间的解耦，但根据ICML2019的最佳论文可知，这样并不够。

2.我猜测，为使互信息最大，c的每个维度都应最大限度地捕捉x变化最大且独立的各个方面，而真实的变化因子一般是按照变化方差从大到小排列的，类似PCA，所以这种匹配使解耦成为了可能。
