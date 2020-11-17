

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 22:15:37
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 20:24:10
 * @Description:
 * @TODO::
 * @Reference:
-->

https://zhuanlan.zhihu.com/p/87942922
什么是一字多义
以前word2vec是把lookup_table拿出来作为词向量，一个词只对应唯一一个向量，没法区分一字多义。ELMo、BERT是把字的上下文编码，取最后的h（分类层之前）作为字表示，基于分布式语义假设：

One shall know a word by the company it keeps. 我们可以通过一个词出现的语境知道这个词的意思。
所以一个字根据上下文不同会有不同的h，可以表示一字多义的情况

2. h经过分类层后越来越像自己的embedding
要知道embedding有很多个维度，不同维度包含不同的信息，刚才说词的emb对应唯一的向量（编码），可没说是对应富士苹果还是手机苹果，很可能这两种信息都包含在编码里

BERT[2]
paper：BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
arXiv：https://arxiv.org/abs/1810.04805
code：tensorflow、pytorch

Google AI 2018年提出的Bidirectional Encoder Representations from Transformers(BERT)是从大量未标注文本学习得到的语言模型。

模型在机器阅读理解顶级水平测试SQuAD1.1中表现出惊人的成绩：全部两个衡量指标上全面超越人类。在SQuAD2.0上也排名第一。并且还在其他10种不同NLP任务测试中创出最佳成绩，包括将GLUE基准推至80.4％（绝对改进7.6％），MultiNLI准确度达到86.7% （绝对改进率5.6％）等。

BERT的结构是Transformer的Encoder：




[2]: https://0809zheng.github.io/2020/04/27/elmo-bert-gpt.html
