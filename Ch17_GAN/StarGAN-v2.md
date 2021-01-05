

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-14 22:00:30
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-18 19:21:58
 * @Description:
 * @TODO::
 * @Reference:https://github.com/clovaai/stargan-v2
-->
Diverse Image Synthesis for Multiple Domains

 A good image-to-image translation model should learn a mapping between different visual domains while satisfying the following properties: 1) diversity of generated images and 2) scalability over multiple domains. Existing methods address either of the issues, having limited diversity or multiple models for all domains. We propose StarGAN v2, a single framework that tackles both and shows significantly improved results over the baselines. Experiments on CelebA-HQ and a new animal faces dataset (AFHQ) validate our superiority in terms of visual quality, diversity, and scalability. To better assess image-to-image translation models, we release AFHQ, high-quality animal faces with large inter- and intra-domain variations. The code, pre-trained models, and dataset are available at clovaai/stargan-v2.


一个理想的图像到图像的翻译方法应该能够综合考虑各个领域的不同风格的图像。也就是说一个好的gan就要能将我们输入的图片按照domain和style生成新的图片.StarGAN仍然会为每个domain学习一个确定性映射，它不能捕获数据分布的多模态特性。这个限制来自于这样一个事实，即每个domain都由一个预定的label表示。注意，Generator接收一个固定的label（例如一个热向量）作为输入，因此它不可避免地在给定源图像的每个domain中生成相同的输出。

解决风格多样性问题，通常是将标准高斯分布随机抽样出来的低维latent code(隐编码)送人生成器得到的.在生成图片时把通过latent code方式得到的Style加入到图片生成器中，来得到相应的图片。这样的方法就只考虑两个domain之间映射，不能扩展到不断增加的域数量。如果有K个domain我们就需要训练K（K-1）个生成器去处理每个域之间的转换，这样就限制了他们的应用.

为了解决可伸缩性的问题，早版本的StarGAN是通过使用一个生成器来映射所有的Domain（stargan的名字就是因为这样模型结构而得名的）.Generator将domain label作为附加输入，并学习将image转换为相应的Domain。

想要两全其美，就有了现在的Starganv2，他是一种可伸缩的方法，可以在多个Domain中生成不同的图像。特别是，他从StarGAN开始，提出的领域特定样式代码替换其domain label，该代码可以表示特定Domain的不同样式。为此，先介绍了两个模块，一个Mapping Network（映射网络）和一个Style Encoder（风格编码器）。mapping network学习将随机高斯噪声转换为Style code，而style encoder从给定的参考图像中提取style code。考虑多重因素Domain，两个模块都有多个输出分支，每个分支都提供特定Domain的style code。最后，利用这些样式代码，Starganv2的Generator学会了成功地在多个Domain上合成不同的图像.



Starganv2论文还开源了一个新的动物脸数据集（AFHQ），Animal Faces-HQ.



StarGAN v2：

1. 采用Style Encoder,Mapping Network来得到图片的style code。其中Style Encoder来获取参考图片的style code,用来生成我们想要的图片;Mapping Network来随机生成style code，保证style分布多样性。
1. 多domain输出，除了Generator网络，其他三个网络都是多domain输出，让一个模型就可以学得多个domain的信息。
1. 自适应实例归一化（AdaIN）层，AdaIN层与BN、IN类似，都是在网络内部改变feature map的分布，实现风格迁移。
1. 借鉴CycleGAN了思想，使生成图片与原图片相近。
1. 增加了style diversity loss与 R1 正则，保证训练的收敛。
1. 利用EMA，能使得模型更加的鲁棒。
1. 一个预训练好的人脸关键点模型FAN，产生关键部位的mask，使得原图像mask区域在转换后仍能得以保留。

https://github.com/clovaai/stargan-v2
https://aistudio.baidu.com/aistudio/projectdetail/638962?channelType=0&channel=-1
