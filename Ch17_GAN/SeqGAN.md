

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 20:16:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 22:16:15
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

## 动机

序列生成模型一般是采用和任务相关的指标来进行评价,比如BLEU、 ROUGE等而训练时是使用最大似然估计,这导致训练目标和评价方法不一致。并且这些评价指标一般都是不可微的,无法直接使用基于梯度的方法来进行优化。
BLE∪的设计思想与评判机器翻译好坏的思想是一致的:机器翻译结果越接近专业人工翻译的结果,则越好。BLEU算法实际上在做的事:判断两个句子的相似程度我想知道一个句子翻译前后的表示是否意思一致,显然没法直接比较,那我就拿这个句子的标准人工翻译与我的机器翻译的结果作比较,如果它们是很相似的,说明我的翻译很成功。因此,BLUE去做判断:一句机器翻译的话与其相对应的几个参考翻译作比较,算岀一个综合分数。这个分数越髙说明机器翻译得越好。

$P_{n}=\frac{\sum_{n-g r a m \in \hat{y}} \operatorname{count}_{c l i p}(n-\operatorname{gram})}{\sum_{n-g r a m \in \hat{y}} \operatorname{count}(n-\operatorname{gram})}$

## 能否用GAN直接优化评价目标

GAN应用于 Sequence面临着两个问题:问题1,GAN的设计初衷是用来能够生成连续的真实数据,但文本序列是非连续的。因为在GAN中, Generator是通过随机抽样作为开始,然后根据模型的参数进行确定性的转化。通过 generativemodel g的输岀, discriminative model d算得损失值,根据得到的损失梯度去指导 generative model G做轻微改变,从而使G产生更加真实的数据。如果生成的数据是非连续的序列,那么这种来自D的“ slight change”指导将变得几乎没有意义。因为在有限的 Dictionary中,这种 slight change没有相应的 token问题2,GAN只能评估出整个生成序列的 score/loss,不能够细化到去评估当前生成 token的好坏和对后面生成的影响。

## 模型

将序列产生问题看做是序列决策问题。生成器被认为是RL当中的 agent;状态是目前已经产生的 tokens,动作是下一步需要生的 token。为了给出奖励,用discriminator来评价 sequence,并且反馈评价来引导 generative model的学习为了解决当输出是离散的,梯度无法回传给generative mode的情况,将generative model看做是 stochasticparameterized policy。采用MC搜索来近似 the state- action value。直接用policy gradient来训练 policy,很自然的就避免了传统GAN中,离散数据的微分困难问题。

## 生成器



## 判别器

生成器与判别器预训练

## Highway

判别器的CNN结构采用了highway结构，从而保证深层网络结构中有足够的数据细节用于训练


而Highway Network结构的作用与残差网络相同，只是在实现上，Highway Network受LSTM的启发，增加了阀门参数，通过阀门参数来控制多少数据需要经过当前层非线性变化，以及多少数据可以进入“高速公路”直接传递给深层网络结构。


在SeqGAN训练过程中，目标LSTM是一个已经训练好的网络，不必再次训练，使用时只需要将它对应的网络参数加载回神经网络中即可，其目的是编码真实世界中的数据，交由判别器判别。

## 创新点

A将GAN应用到了文本生成中

1.蒙特卡洛采样生成 reward
2.预训练及对抗训练策略

B证明了GAN也可以应用于文本生成,并能取得比MLE更好的效果

C对后续工作有很大启发,如QA实验分析十分详尽

## 后续

RankGAN(NIPS 2017)以及MaskGAN(ICLR 2018)

The architectures used are different than those in the orignal work. Specifically, a recurrent bidirectional GRU network is used as the discriminator.[3]

对识别器的训练远远多于对生成器的训练(生成器只对一批示例进行训练，增加批的大小会损害稳定性)

Adam作为发生器，Adagrad作为鉴频器

在GAN阶段调整生成器的学习速度

在训练和测试阶段使用dropout

稳定性对几乎每个参数都非常敏感:/

GAN阶段可能并不总是导致NLL的大幅下降(有时非常小)——我怀疑这是由于所实现的政策梯度非常粗糙的本质(没有发布)。


[1]: Yu L, Zhang W, Wang J, et al., 2017. SeqGAN: Sequence generative adversarial nets with policygradient[C]//Proceedings of Thirty-First AAAI Conference on Artificial Intelligence. 2852-2858
[2]: https://ai.deepshare.net/detail/i_5d9c6af4a4044_tL23GmwT/1?fromH5=true
[3]: https://github.com/suragnair/seqGAN
