

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 22:06:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 17:08:43
 * @Description:
 * @TODO::
 * @Reference:
-->

# 无监督学习（Unsupervised Learning)


http://ufldl.stanford.edu/tutorial/

Unsupervised learning is a paradigm designed to create autonomous intelligence by rewarding agents (that is, computer programs) for learning about the data they observe without a particular task in mind. In other words, the agent learns for the sake of learning.[4]

非监督学习，按照字面意思就是除了监督学习以外的学习。比如读世界名著或者欣赏音乐，多次重复的过程中并没有一个谁来告诉你，你读或者听的目的（量化意义上）是什么。你可能只是出于爱好或者无聊，选择做这件事情。但是久而久之，在重复中你会在这些书或者音乐中发现一些相似的东西，比如行为风格，思维方式，旋律和节奏，你觉得这些相似的东西非常有趣或者有价值，于是在未来你会更加容易识别或者注意到这些“有价值”的东西。这个过程，我以为就是一种非监督学习。

动机无监督学习的目标是找到在未标记数据 \{x^{(1)},...,x^{(m)}\}{x
(1)
 ,...,x
(m)
 } 中的隐含模式。

非监督学习在过程中会建立一种相对主观的价值体系，并用这种主观的价值体系来筛选和分析数据


## VS监督学习

监督学习是一种目的明确的训练方式，你知道得到的是什么；而无监督学习则是没有明确目的的训练方式，你无法提前知道结果是什么。
监督学习需要给数据打标签，成本高；而无监督学习不需要给数据打标签。
监督学习由于目标明确，所以可以衡量效果；而无监督学习几乎无法量化效果如何。

非监督学习与监督学习最大的不同就在，并且只有特征（X）而没有目标（Y）也可以叫做「标签」(label)。在整个学习过程中，没有老师的指导，没有正确答案，直接将原始信息输入到计算机中直到获得“有价值”的东西。所以，非监督学习通过建立一种相对“主观”的价值体系来筛选和分析数据。

无监督学习的目标就是通过对无标记样本的学习来发现数据内在的性质和规律，为进一步的数据分析提供基础。

全监督是所有的label都已经人工标注好；半监督是一半标注好了一半没标注就拿来一起训练；无监督则没有任何标注label,更专注聚类、降维。
## 更多无监督技术：

主成分分析（PCA）
异常检测（Anomaly detection）
自动编码（Autoencoders）
深度置信网络（Deep Belief Nets）
Hebbian Learning
生成对抗网络（GAN）
自组织映射（Self-Organizing maps）

经典的非监督学习往往有一套非常固定的数学上的价值评判标准，比如做信号处理的人会考虑minimal distortion，做统计的人会考虑maximum likelihood，做机器学习的人可能会喜欢low rank approximation等等。用这些固定的价值评判自然更有利于模型的分析和理解，因为一旦确立的范式，剩下需要做的或是实验或是理论

[2]: https://easyai.tech/ai-definition/unsupervised-learning/
[3]: https://easyai.tech/blog/unsupervised-learning-with-python/
[4]: https://deepmind.com/blog/article/unsupervised-learning
[5]: https://www.zhihu.com/question/23194489
[6]: 什么是无监督学习？ - Lanzhe Guo的回答 - 知乎 https://www.zhihu.com/question/23194489/answer/147062272
TODO:
https://stanford.edu/~shervine/l/zh/teaching/cs-229/cheatsheet-unsupervised-learning
https://reference.wolfram.com/language/tutorial/NeuralNetworksUnsupervised.html.zh?source=footer
