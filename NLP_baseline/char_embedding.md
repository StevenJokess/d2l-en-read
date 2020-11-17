

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 19:54:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 21:55:36
 * @Description:
 * @TODO::
 * @Reference:https://0809zheng.github.io/2020/04/29/word-embedding.html
-->


背景
在自然语言处理任务中，对于每一个单词（或字符）的表示可以使用One-hot编码，即1-of-N encoding：



这种方法每一个单词是独立的，没有考虑到单词之间的相关性。

进一步提出了word class，把语义相近的单词分为一类：
词嵌入Word Embedding的概念：



词嵌入是把单词映射到一个k维的向量空间，每一个单词用一个k维向量表示。

1. Count based

