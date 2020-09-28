

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 22:04:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-28 19:40:02
 * @Description:
 * @TODO::
 * @Reference:
-->

conditional GAN (cGAN) proposed by Mehdi Mirza and Simon Osindero in the paper Conditional Generative Adversarial Nets (https://arxiv.org/pdf/1411.1784.pdf) uses the class label information and learns to synthesize new images conditioned on the provided label, that is, —applied to MNIST.[1]



标准的GAN如DCGAN等并不能控制生成的图片
的效果，条件GAN(CGAN)则使用了条件控制变
量作为输入，是几乎后续所有性能强大的GAN
的基础。
作者/编辑 言有三
网络结构如上，其中的y就是条件变量。对于生成器 来说，输入包括z和y，两者会进行拼接后作为输 入。对于判别器来说，输入包括了x和y，两者会进 行拼接后作为输入，当然为了和z以及x进行拼接，y 需要做一些维度变换，即reshape操作。
相应的，损失函数也略有不同。
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {崩山 }}(\boldsymbol{x})}[\log D(\boldsymbol{x} \mid \boldsymbol{y})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z} \mid \boldsymbol{y})))]
$$
可以看到其实就是加入了条件，网络结构本身和损 失函数的表达式本身没有变化。
因此，我们同样使用之前的DCGAN结构和开源项 目 $, \quad$ https://github.com/carpedm20/DCGAN-tensorflow/[2]

[1]: https://learning.oreilly.com/library/view/python-machine-learning/9781789955750/Text/Chapter_17.xhtml#_idParaDest-342
[2]: img\CGAN_yousanai.jpeg
