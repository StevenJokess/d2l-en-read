

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 00:49:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 14:21:01
 * @Description:
 * @TODO::
 * @Reference:
-->

而判别器D的出现改变了这一点，判别器D的目标是尽可能准确地辨别生成样本和真实样本，而这时生成器G的训练目标就由最小化“生成-真实样本差异”变为了尽量弱化判别器D的辨别能力（这时候训练的目标函数中包含了判别器D的输出）。

后大家注意一点，这里生成样本的loss衡量方法是JS散度。

解决这个问题可以采用Inverse Reinforcement Learning （IRL)。也就是给Critic不仅有Actor的输出，还有Human Expert的决策过程，然后反向推断可能的Q函数，从而让Critic有了某种参考的标准。这个不仅对RL有帮助作用，对于生成离散输出的GAN（比如SeqGAN，用于文本训练的GAN）也有很大帮助。前段时间
@纳米酱
 写过一篇文章，https://zhuanlan.zhihu.com/p/25862041。指出了这一思路的实现过程。行文略有春秋笔法，微言大义，很受启发。（感谢知友评论，已经找到重新补上链接）[2]

[1]:  https://zhuanlan.zhihu.com/p/29168803
[2]: 为什么知乎上感觉讨论Deep reinforcement learning比讨论GAN少很多？ - Yulong的回答 - 知乎
https://www.zhihu.com/question/60167306/answer/173152304
