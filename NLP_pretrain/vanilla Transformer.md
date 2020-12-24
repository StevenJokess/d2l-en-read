

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-24 21:51:43
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 21:52:06
 * @Description:
 * @TODO::
 * @Reference:
-->

为何要提这个模型？因为Transformer-XL是基于这个模型进行的改进。

Al-Rfou等人基于Transformer提出了一种训练语言模型的方法（ https://arxiv.org/abs/1808.04444 ），来根据之前的字符预测片段中的下一个字符。例如，它使用x 1 , x 2 , . . . , x n − 1 x_1, x_2, ..., x_{n-1}x
1
​
 ,x
2
​
 ,...,x
n−1
​
 预测字符x n x_nx
n
​
 ，而在x n x_nx
n
​
 之后的序列则被mask掉。论文中使用64层模型，并仅限于处理 512个字符这种相对较短的输入，因此它将输入分成段，并分别从每个段中进行学习，如下图所示。 在测试阶段如需处理较长的输入，该模型会在每一步中将输入向右移动一个字符，以此实现对单个字符的预测。

该模型在常用的数据集如enwik8和text8上的表现比RNN模型要好，但它仍有以下两个缺点：

a. 上下文长度受限：字符之间的最大依赖距离受输入长度的限制，模型看不到出现在几个句子之前的单词。
b. 上下文碎片：对于长度超过512个字符的文本，都是从头开始单独训练的。段与段之间没有上下文依赖性，会让训练效率低下，也会影响模型的性能。
c. 推理速度慢：在测试阶段，每次预测下一个单词，都需要重新构建一遍上下文，并从头开始计算，这样的计算速度非常慢。

[1]: https://blog.csdn.net/magical_bubble/article/details/89060213
