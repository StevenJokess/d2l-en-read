

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-24 22:04:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 18:51:08
 * @Description:
 * @TODO::
 * @Reference:
-->

# cGAN(conditional GAN)

conditional GAN (cGAN) proposed by Mehdi Mirza and Simon Osindero in the paper Conditional Generative Adversarial Nets (https://arxiv.org/pdf/1411.1784.pdf) uses the class label information and learns to synthesize new images conditioned on the provided label, that is, —applied to MNIST.[1]

Goal:[11]
Using labels to train both the Generator and the Discriminator
Teaching GANs to generate examples matching a specified label


 With a DCGAN, we can generate images from random vectors, but what kind of images do we achieve? Can we specify it is a woman or man face?

In this notebook, we introduce conditional GAN, which accepts label as part of the input for both generator and discriminator. With conditional GAN, you can choose which kind of data to generate with corresponding label. We'll train on MNIST dataset.[9]


标准的GAN如DCGAN等并不能控制生成的图片
的效果，条件GAN(CGAN)则使用了条件控制变
量作为输入，是几乎后续所有性能强大的GAN
的基础。

网络结构如上，其中的y就是条件变量。对于生成器 来说，输入包括z和y，两者会进行拼接后作为输 入。对于判别器来说，输入包括了x和y，两者会进 行拼接后作为输入，当然为了和z以及x进行拼接，y 需要做一些维度变换，即reshape操作。
相应的，损失函数也略有不同。
$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {崩山 }}(\boldsymbol{x})}[\log D(\boldsymbol{x} \mid \boldsymbol{y})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z} \mid \boldsymbol{y})))]
$$
可以看到其实就是加入了条件，网络结构本身和损 失函数的表达式本身没有变化。

这个变化概括来说就是将原来只接收一个输入z的生成网络，变成接收两个输入：z和y，将原来只接收一个输入x的判别网络，变成接收两个输入：x和y[10]

y就是加入的监督信息（标签类别），如MNIST数据集中的数字label信息，人脸数据中的性别、是否微笑、年龄等信息。[10]

因此，我们同样使用之前的DCGAN结构和开源项 目 $, \quad$ https://github.com/carpedm20/DCGAN-tensorflow/[2]

遇到一个更大的问题——普通的GAN无法控制生成器的输入内容。即生成器生成内容是随机的，判别器只会判断生成器生成数据的真实性，而不会判断生成器有没有生成规定的数据。[3]

传统的GAN模型对于数据的属性不加限定, 无法有效地控制生成的结果, 在生成的图像中往往会存在较多的噪点; 此外, 传统 GAN 模型一次只能学习一类数据, 对于包含多个类的数据样本集, 需逐类学习及生成相应类的样本集, 导致效率低下。[5]
Mirza等[6]提出了CGAN 模型, CGAN的结构如图1所示, 通过对生成网络G和判别网络D添加额外的信息y(如数据标签、模态数据), 可以起到连接或者区分z和x的作用, 引导学习过程, 使得网络的性能得到提升, 同时使GAN 模型具有生成多类数据的能力。


生成器要根据约束条件去生成相应的图像，所以生成器要接受约束条件，其次判别器除了判别生成器生成的图像是否真实外，还要判别生成器生成的图像与真实图像之间是否匹配，否则，就算生成了真实图像也无用

条件生成对抗网络（Conditional GAN，CGAN），简单理解就是在普通GAN的生成器与判别器上加了条件约束，如图像间风格转换。因此除给生成器喂随机生成噪声外，还需要将灰度图像也喂给生成器，要求生成器按灰度图像的分布来生成相应的图像，灰度图像对生成器而言就是一个条件约束。同样，对判别器而言，除将真实图像或生成图像传入外，还需要传入灰度图像这个条件约束，要求判别器判断生成的图像是否符合条件约束，如果生成了一张比较真实但与条件约束没有什么关系的图像，那么也判定为不合格。[4]

Defining the networks
Input of generator is the concatenation of random noise vector and digit label one hot vector. It is followed by a fully connected layer and relu activation function. Output layer is composed by another fully connected layer and sigmoid activation function.

Similar to generator, input of discriminator is the concatenation of flatten image vector and digit label. It is followed by a fully connected layer and relu activation function. Output layer is composed by another fully connected layer and sigmoid activation function. In this tutorial we don't apply sigmoid function to output to make training process more numerically stable.[9]

## Generator

1. Take label y (an integer from 0 to 9) and turn it into a dense vector of size z_dim (the length of the random noise vector) by using the Keras Embedding layer.
1. Combine the label embedding with the noise vector z into a joint representation by using the Keras Multiply layer. As its name suggests, this layer multiplies the corresponding entries of the two equal-length vectors and outputs a single vector of the resulting products.
1. Feed the resulting vector as input into the rest of the CGAN Generator network to synthesize an image.

该生成器输入两个一维向量y和noise，生成一张图片。

```py
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.label_emb = nn.Embedding(n_classes, n_classes)

        def block(in_feat, out_feat, normalize=True):
            layers = [nn.Linear(in_feat, out_feat)]
            if normalize:
                layers.append(nn.BatchNorm1d(out_feat, 0.8))
            layers.append(nn.LeakyReLU(0.2))
            return layers
        self.model = nn.Sequential(
            *block((latent_dim + n_classes), 128, normalize=False),
            *block(128, 256),
            *block(256, 512),
            *block(512, 1024),
            nn.Linear(1024, int(np.prod(img_shape))),
            nn.Tanh())

    def execute(self, noise, labels):
        gen_input = jt.contrib.concat((self.label_emb(labels), noise), dim=1)
        img = self.model(gen_input)
        img = img.view((img.shape[0], *img_shape))
        return img
```

## Discriminator

1. Take a label (an integer from 0 to 9) and—using the Keras Embedding layer—turn the label into a dense vector of size 28 × 28 × 1 = 784 (the length of a flattened image).
Reshape the label embeddings into the image dimensions (28 × 28 × 1).
1. Concatenate the reshaped label embedding onto the corresponding image, creating a joint representation with the shape (28 × 28 × 2). You can think of it as an image with its embedded label “stamped” on top of it.
1. Feed the image-label joint representation as input into the CGAN Discriminator network. Note that in order for things to work, we have to adjust the model input dimensions to (28 × 28 × 2) to reflect the new input shape.[11]

D输入一张图片和对应的y，输出是真图片的概率。

```
# [12]
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.label_embedding = nn.Embedding(n_classes, n_classes)
        self.model = nn.Sequential(
            nn.Linear((n_classes + int(np.prod(img_shape))), 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 512),
            nn.Dropout(0.4),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 512),
            nn.Dropout(0.4),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 1))

    def execute(self, img, labels):
        d_in = jt.contrib.concat((img.view((img.shape[0], (- 1))), self.label_embedding(labels)), dim=1)
        validity = self.model(d_in)
        return validity
```

Qiita的帖子[7]Qiita的帖子不一样，我们可以指定生成人物的属性，如发色、眼睛的颜色、发型，甚至是服装、装饰物，从而生成具有指定属性的图像。不一样，我们可以指定生成人物的属性，如发色、眼睛的颜色、发型，甚至是服装、装饰物，从而生成具有指定属性的图像。

We demonstrate the capability of our model to generate plausible images of birds and flowers from detailed text descriptions.[8]

## 应用

Age-cGAN（Age Conditional Generative Adversarial Networks）
面部老化有许多行业用例，包括跨年龄人脸识别，寻找失踪儿童，或者用于娱乐。Grigory Antipov，Moez Baccouche和Jean-Luc Dugelay在他们的题为“Face Aging with Conditional Generative Adversarial Networks”的论文中提出了用条件GAN进行面部老化。[13]

## Summary[11]

The additional information constrains the Generator to synthesize a certain type of output and the Discriminator to accept only real examples matching the given additional information.

[1]: https://learning.oreilly.com/library/view/python-machine-learning/9781789955750/Text/Chapter_17.xhtml#_idParaDest-342
[2]: img\CGAN_yousanai.jpeg
[3]: https://weread.qq.com/web/reader/4653238071e86dd54654969k34132fc02293416a75f431d
[4]: https://weread.qq.com/web/reader/4653238071e86dd54654969ka1d32a6022aa1d0c6e83eb4
[5]: http://www.opticsjournal.net/richHtml/gxxb/2019/39/3/0311002.html
[6]: Mirza M , Osindero S. Conditional generative adversarial nets[EB/OL]. ( 2014 -11-06)[2018-07-28]. org/abs/1411. 1784.
[7]: 通过文字描述来生成二次元妹子！聊聊conditional GAN与txt2img模型 - 何之源的文章 - 知乎
https://zhuanlan.zhihu.com/p/25542274
[8]: Generative Adversarial Text to Image Synthesis https://arxiv.org/abs/1605.05396
[9]: https://github.com/zackchase/mxnet-the-straight-dope/blob/master/chapter14_generative-adversarial-networks/conditional.ipynb
[10]: https://weread.qq.com/web/reader/d7032cd072021a59d7038af
[11]: https://livebook.manning.com/book/gans-in-action/chapter-8/1
[12]: https://github.com/Jittor/jittor/blob/master/notebook/ConditionGAN.src.md
[13]: https://www.shuzhiduo.com/A/gAJG4R6o5Z/
[14]: https://github.com/sinyeratlantis/deep_learning_gluon/blob/master/12.conv_gan.py
