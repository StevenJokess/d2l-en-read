

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 22:59:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-14 23:00:55
 * @Description:
 * @TODO::
 * @Reference:
-->

# 自训练

自训练（Self-Training，或Self-Teaching），也叫自举法（Bootstrapping），是一种非常简单的半监督学习算法[Scudder,1965;Yarowsky,1995]

自训练是首先使用标注数据来训练一个模型，并使用这个模型来预测无标注样本的标签，把预测置信度比较高的样本及其预测的伪标签加入训练集，然后重新训练新的模型，并不断重复这个过程．算法10.2给出了自训练的训练过程



自训练和密度估计中EM算法有一定的相似之处，通过不断地迭代来提高模型能力．EM算 法 参 见第11.2.2.1节．参见习题10-3．但自训练的缺点是无法保证每次加入训练集的样本的伪标签是正确的．如果选择样本的伪标签是错误的，反而会损害模型的预测能力．因此，自训练最关键的步骤是如何设置挑选样本的标准
