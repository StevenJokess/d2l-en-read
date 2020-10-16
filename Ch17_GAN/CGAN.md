

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 22:04:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-16 20:13:27
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

遇到一个更大的问题——普通的GAN无法控制生成器的输入内容。即生成器生成内容是随机的，判别器只会判断生成器生成数据的真实性，而不会判断生成器有没有生成规定的数据。[3]



生成器要根据约束条件去生成相应的图像，所以生成器要接受约束条件，其次判别器除了判别生成器生成的图像是否真实外，还要判别生成器生成的图像与真实图像之间是否匹配，否则，就算生成了真实图像也无用

条件生成对抗网络（Conditional GAN，CGAN），简单理解就是在普通GAN的生成器与判别器上加了条件约束，如图像间风格转换。因此除给生成器喂随机生成噪声外，还需要将灰度图像也喂给生成器，要求生成器按灰度图像的分布来生成相应的图像，灰度图像对生成器而言就是一个条件约束。同样，对判别器而言，除将真实图像或生成图像传入外，还需要传入灰度图像这个条件约束，要求判别器判断生成的图像是否符合条件约束，如果生成了一张比较真实但与条件约束没有什么关系的图像，那么也判定为不合格。[4]


[1]: https://learning.oreilly.com/library/view/python-machine-learning/9781789955750/Text/Chapter_17.xhtml#_idParaDest-342
[2]: img\CGAN_yousanai.jpeg
[3]: https://weread.qq.com/web/reader/4653238071e86dd54654969k34132fc02293416a75f431d
[4]: https://weread.qq.com/web/reader/4653238071e86dd54654969ka1d32a6022aa1d0c6e83eb4
