

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 18:49:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 18:52:27
 * @Description:
 * @TODO::
 * @Reference:https://www.zhihu.com/collection/533183923?page=3
-->

华为诺亚方舟实验室的论文《Co-Evolutionary Compression for Unpaired Image Translation》被ICCV 2019录用，该论文首次提出针对GAN中生成网络的剪枝算法

## 研究背景

模型往往需要较大的内存，运行这些模型需要较大的计算开销，一般只能在GPU平台上运行，不能直接将这些模型迁移到移动端上。

而现有的针对神经网络的压缩算法都是针对判别式神经网络模型设计，直接应用在生成网络上不能取得令人满意的压缩结果。


生成模型参数冗余建模

与传统剪枝方法比较：表1和表2分别列出了压缩前后，传统的剪枝方法和论文提出的剪枝方法在三个数据集上的量化结果。在cityscapes数据集采用FCN分数，horse2zebra和summer2winter数据集采用FID分数，论文提出方法结果与压缩之前的模型接近，远远好于传统的剪枝方法。


在Kirin 980芯片上，推理时间从6.8s压缩到了2.1s，线上加速三倍以上。
