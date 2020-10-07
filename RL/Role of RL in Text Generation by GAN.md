

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 00:49:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-08 00:55:18
 * @Description:
 * @TODO::
 * @Reference:
-->

而判别器D的出现改变了这一点，判别器D的目标是尽可能准确地辨别生成样本和真实样本，而这时生成器G的训练目标就由最小化“生成-真实样本差异”变为了尽量弱化判别器D的辨别能力（这时候训练的目标函数中包含了判别器D的输出）。

后大家注意一点，这里生成样本的loss衡量方法是JS散度。


[1]:  https://zhuanlan.zhihu.com/p/29168803
