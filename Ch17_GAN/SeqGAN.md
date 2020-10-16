

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 20:16:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-16 21:16:15
 * @Description:
 * @TODO::
 * @Reference:https://nndl.github.io
 * https://weread.qq.com/web/reader/4653238071e86dd54654969kd2d32c50249d2ddea18fb39
-->

GAN无法直接生成文本数据，因为文本数据是离散的，我们介绍了多种方法，而SeqGAN就是利用GAN+RL的方法来实现序列数据的生成。



具体的计算方式就是Policy Gradient。至此生成器对抗训练的逻辑就完成了。


![SeqGAN](img\SeqGAN.jpg)

当我们训练判别器时，会使用真实世界中获得的真实序列数据以及生成器生成的序列数据，此时判别器会分辨获得的序列数据是来自真实世界的数据还是生成器生成的数据。对于生成器而言，生成器会尝试生成离散的序列数据，以文本数据为例，在每一次训练时，生成器都会尝试生成一个词对应的概率分布向量，这个词的概率分布向量会与前面已经生成的词的概率分布向量连接成一个句子。


SeqGAN中采用蒙特卡罗搜索的方式来，从已有的状态（State）推导采样出未来的状态，从而让生成器可以向判别器输出一个完整的句子序列，这种采样策略被称为rolloutpolicy。而判别器获得一个完整的序列数据后，会计算出奖励（Reward），因为生成器生成的是离散类型的数据，所以SeqGAN利用Policy Gradient算法将判别器的奖励传递给生成器，实现对生成器的指导。至此SeqGAN实现了对判别器D与生成器G的对抗训练，在训练生成器G时利用了RL中的PolicyGradient算法。

Policy Gradient算法

生成器与

判别器预训练

## Highway

判别器的CNN结构采用了highway结构，从而保证深层网络结构中有足够的数据细节用于训练


而Highway Network结构的作用与残差网络相同，只是在实现上，Highway Network受LSTM的启发，增加了阀门参数，通过阀门参数来控制多少数据需要经过当前层非线性变化，以及多少数据可以进入“高速公路”直接传递给深层网络结构。


在SeqGAN训练过程中，目标LSTM是一个已经训练好的网络，不必再次训练，使用时只需要将它对应的网络参数加载回神经网络中即可，其目的是编码真实世界中的数据，交由判别器判别。





Yu L, Zhang W, Wang J, et al., 2017. SeqGAN: Sequence generative adversarial nets with policygradient[C]//Proceedings of Thirty-First AAAI Conference on Artificial Intelligence. 2852-2858
