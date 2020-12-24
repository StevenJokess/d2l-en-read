

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 19:54:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 22:55:28
 * @Description:
 * @TODO::
 * @Reference:https://0809zheng.github.io/2020/04/27/elmo-bert-gpt.html[1]
-->

 ELMO
paper：Deep contextualized word representations
arXiv：https://arxiv.org/abs/1802.05365
Embeddings from Language Model(ELMO)是一个基于RNN的语言模型，从大量句子训练得到。

传统的词嵌入把每一个character或word转化成一个词向量，相同type的词向量在不同的句子中位于不同的token，可能具有不同的含义，如：

It is safest to deposit your money in the bank.
The victim was found lying dead on the river bank.
Contextualized Word Embedding的方法是指对每一个token进行词嵌入，当文本不同时，同一个type也具有不同的词嵌入向量。

用一个双向的、深层的RNN训练语言模型，每个方向、每一层的隐状态看作对输入的词嵌入编码：



对每一层的隐状态向量加权求和，作为最终的词嵌入向量：


ELMo具有如下的优良特性：[2]

上下文相关：每个单词的表示取决于使用它的整个上下文。
深度：单词表示组合了深度预训练神经网络的所有层。
基于字符：ELMo表示纯粹基于字符，然后经过CharCNN之后再作为词的表示，解决了OOV问题，而且输入的词表也很小。
资源丰富：有完整的源码、预训练模型、参数以及详尽的调用方式和例子，又是一个造福伸手党的好项目！而且：还有人专门实现了多语的，好像是哈工大搞的，戳这里看项目。

[2]: https://blog.csdn.net/Magical_Bubble/article/details/89160032
