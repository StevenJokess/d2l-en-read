

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 20:16:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-16 20:58:14
 * @Description:
 * @TODO::
 * @Reference:https://nndl.github.io
-->

GAN无法直接生成文本数据，因为文本数据是离散的，我们介绍了多种方法，而SeqGAN就是利用GAN+RL的方法来实现序列数据的生成。



具体的计算方式就是Policy Gradient。至此生成器对抗训练的逻辑就完成了。


![SeqGAN](img\SeqGAN.jpg)

Yu L, Zhang W, Wang J, et al., 2017. SeqGAN: Sequence generative adversarial nets with policygradient[C]//Proceedings of Thirty-First AAAI Conference on Artificial Intelligence. 2852-2858
