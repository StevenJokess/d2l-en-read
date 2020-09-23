

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 20:13:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-23 23:18:19
 * @Description:
 * @TODO::
 * @Reference:
-->

# Cycle-Consistent Adversarial Networks

Now, we introduced the basic ideas behind how GAN/DCGAN [1] work. We found that DCGAN can generate photorealistic images, like Pokemon.

In this section, we will demonstrate how you can use GANs to translate Unpaired image-to-image [22] which goal is to learn the mapping ( G : X → Y ) , cycle consistency loss to enforce F(G(X)) ≈ X between an input image G(X) and an output image Y using a training set of aligned image pairs. [9] We will be basing our models on the Cycle-Consistent Generative Adversarial Networks (CycleGAN website[25]) introduced in [2]. We will TODO:? , they can be leveraged to translate image-to-image. It works better if two datasets share similar visual content. For example, landscape painting<->landscape photographs, zebras<->horses[28].

![horse2zebra](img/horse2zebra.gif)

Qualitative results are presented on several tasks where paired training data does not exist, including collection style transfer, object transﬁguration, season transfer, photo enhancement, etc.

![mapping](img\mapping.jpg)

Left: Overall CycleGAN schema; Middle: Forward cycle-consistency loss; Right: Backward cycle-consistency loss.[22]

 (a) Our model contains two mapping functions G : X → Y and F : Y → X, and associated adversarial discriminators DY and DX. DY encourages G to translate X into outputs indistinguishable from domain Y , and vice versa for DX and F. Tofurtherregularizethemappings,weintroducetwocycleconsistencylossesthatcapturetheintuitionthatif wetranslatefromonedomaintotheotherandbackagainweshouldarriveatwherewestarted: (b)forwardcycle-consistency loss: x → G(x) → F(G(x)) ≈ x, and (c) backward cycle-consistency loss: y → F(y) → G(F(y)) ≈ y

CycleGAN tries to solve these issues with the so-called cycle consistency.
The translation will be cycle-consistent if we translate the sentence back from German into English and we arrive at the original sentence we started with.
In a mathematical context, if we have a translator, , and another translator, the two should be inverses of each other.[22]

Using CycleGAN, we only need to train one model to freely translate from image set A to image set B and vice versa.[26]



## baseline(pix2pix)

how to use pixel-wise label information to perform image-to-image translation with pix2pix and translate high-resolution images with pix2pixHD.

pix2pix [13] We also compare against pix2pix [13], which is trained on paired data, to see how close we can get to this “upper bound” without using any paired data.

Pix2pix was designed to learn of the connections between paired collections of images, for example, transforming an aerial photo taken by a satellite into a regular map, or a sketch image into a color image, and vice versa.[24]

First, open a Terminal and download the code for this section using the following command. This is also available under the pix2pix directory in this chapter's code repository:

$ git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
Then, install the prerequisites to be able to visualize the results during training:

$ pip install dominate visdom

Another code[27]


Mathematically, if we have a translator G : X → Y and another translator F : Y → X, then G and F should be inverses of each other, and both mappings should be bijections. We apply this structural assumptionbytrainingboththemapping G and F simultaneously, and adding a cycle consistency loss [12] that encourages F(G(x)) ≈ x and G(F(y)) ≈ y. Combining this loss with adversarial losses on domains X and Y yields our full objective for unpaired image-to-image translation.



## The apple2orange Dataset[4]

apple2orange: 996 apple images and 1020 orange images downloaded from ImageNet using keywords apple and navel orange.[5]

`bash ./datasets/download_cyclegan_dataset.sh dataset_name`

script.

`bash ./datasets/download_cyclegan_dataset.sh apple2orange`

MXNet code[29]


To train a model on your own datasets, you need to create a data folder with two subdirectories trainA and trainB that contain images from domain A and B. You can test your model on your training set by setting --phase train in test.py. You can also create subdirectories testA and testB if you have test data.You can also create subdirectories testA and testB if you have test data.


The dataset we will use is a collection of Pokemon sprites obtained from TODO: ?
First download, extract and load this dataset.

We resize each videos into  64×64 . The ToTensor transformation will project the pixel value into  [0,1] , while our generator will use the tanh function to obtain outputs in  [−1,1] . Therefore we normalize the data with  0.5  mean and  0.5  standard deviation to match the value range.

TODO:

Let us visualize the first 20 videos.

TODO:


## Network Architecture[14]

Network Architecture We adopt the architecture for our generative networks from Johnson et al. [15] who have shownimpressiveresultsforneuralstyletransferandsuperresolution. This network contains three convolutions, several residual blocks [17], two fractionally-strided convolutions with stride 1 2, and one convolution that maps features to RGB. We use 6 blocks for 128×128 images and 9 blocksfor 256×256 andhigher-resolutiontrainingimages. Similar to Johnson et al. [15], we use instance normalization [18]. For the discriminator networks we use 70 × 70 PatchGANs [19],[20],[21], which aim to classify whether 70×70 overlapping image patches are real or fake. Such a patch-level discriminator architecture has fewer parameters thanafull-imagediscriminatorandcanworkonarbitrarilysized images in a fully convolutional fashion [16].



### The Generator[6]

We adopt our architectures from Johnson et al. [23]. We use 6 residual blocks for 128×128 training images, and 9 residual blocks for 256× 256 or higher-resolution training images. Below, we follow the naming convention used in the Johnson et al.’s Github repository. Let c7s1-k denotea 7×7 Convolution-InstanceNormReLU layer with k ﬁlters and stride 1. dk denotes a 3×3 Convolution-InstanceNorm-ReLU layer with k ﬁlters and stride 2. Reﬂection padding was used to reduce artifacts. Rk denotes a residual block that contains two 3 × 3 convolutional layers with the same number of ﬁlters on both layer. uk denotes a 3 × 3 fractional-strided-ConvolutionInstanceNorm-ReLU layer with k ﬁlters and stride 1

The network with 6 residual blocks consists of: c7s1-64,d128,d256,R256,R256,R256, R256,R256,R256,u128,u64,c7s1-3
The network with 9 residual blocks consists of: c7s1-64,d128,d256,R256,R256,R256, R256,R256,R256,R256,R256,R256,u128 u64,c7s1-3



### The Discriminator[6]

For discriminator networks, we use 70 × 70 PatchGAN [7]. Let Ck denote a 4×4 Convolution-InstanceNorm-LeakyReLU layer with k ﬁlters and stride 2. After the last layer, we apply a convolution to produce a 1-dimensional output. We do not use InstanceNorm for the ﬁrst C64 layer. We use leaky ReLUs with a slope of 0.2. The discriminator architecture is: C64-C128-C256-C512





Image-to-image translation


The discriminator is a mirror of the generator.

## Loss Function

 For the mapping function G : X → Y and its discriminator $D_Y$ , we express the objective as:

$\begin{aligned} \mathcal{L}_{\mathrm{GAN}}\left(G, D_{Y}, X, Y\right) &=\mathbb{E}_{y \sim p_{\text {data }}(y)}\left[\log D_{Y}(y)\right] \\ &+\mathbb{E}_{x \sim p_{\text {data }}(x)}\left[\log \left(1-D_{Y}(G(x))\right],\right.\end{aligned}$

### Cycle Consistency Loss[10]

$\begin{aligned} \mathcal{L}_{\mathrm{cyc}}(G, F) &=\mathbb{E}_{x \sim p_{\text {data }}(x)}\left[\|F(G(x))-x\|_{1}\right] \\ &+\mathbb{E}_{y \sim p_{\text {data }}(y)}\left[\|G(F(y))-y\|_{1}\right] \end{aligned}$

The behavior induced by the cycle consistency loss can beobservedinFigure4: thereconstructedimages F(G(x)) end up matching closely to the input images x.

In particular, for a GAN loss $\mathcal{L}_{\mathrm{GAN}}(G, D, X, Y)$and train the $G$ to minimize $\mathbb{E}_{x \sim p_{\text {data}}(x)}\left[(D(G(x))-1)^{2}\right]$and train the $D$ to minimize $\mathbb{E}_{y \sim p_{\text {data}}(y)}\left[(D(y)-1)^{2}\right]+$ $\mathbb{E}_{x \sim p_{\text {data}}(x)}\left[D(G(x))^{2}\right]$ [14]

This measures the absolute difference between the original images, that is, x and y, and their generated counterparts, $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}} .$ Note that these paths can be viewed as jointly training two autoencoders, $F \circ G: X \rightarrow X$ and $G \circ F: Y \rightarrow Y$. Each autoencoder has a special internal structure: it maps an image to itself with the help of an intermediate representation – the translation of the image into another domain.[22]

### Full Objective[11]

$\begin{aligned} \mathcal{L}\left(G, F, D_{X}, D_{Y}\right) &=\mathcal{L}_{\text {GAN }}\left(G, D_{Y}, X, Y\right) \\ &+\mathcal{L}_{\text {GAN }}\left(F, D_{X}, Y, X\right) \\ &+\lambda \mathcal{L}_{\text {cyc }}(G, F) \end{aligned}$

the coefficient, λ, controls the relative importance between the two losses. CycleGAN aims to solve the following minimax objective:[22]


We aim to solve:

$G^{*}, F^{*}=\arg \min _{G, F} \max _{D_{x}, D_{Y}} \mathcal{L}\left(G, F, D_{X}, D_{Y}\right)$


## Training

Compared to the basic GAN in Section 17.1, we use the same learning rate for both generator and discriminator since they are similar to each other. In addition, we change  β1  in Adam (Section 11.10) from  0.9  to  0.5 . It decreases the smoothness of the momentum, the exponentially weighted moving average of past gradients, to take care of the rapid changing gradients because the generator and the discriminator fight with each other. Besides, the random generated noise Z, is a 4-D tensor and we are using GPU to accelerate the computation.

We train the model with a small number of epochs just for demonstration. For better performance, the variable `num_epochs` can be set to a larger number.







train.py is a general-purpose training script. It works for various models (with option --model: e.g., pix2pix, cyclegan, colorization) and different datasets (with option --dataset_mode: e.g., aligned, unaligned, single, colorization). See the main README and training/test tips for more details.[8]



## Summary



*  Finally, we demonstrate the generality of our algorithm on a wide range of applications where paired data does not exist.
*  Nonetheless, in many cases completely unpaired data is plentifully available and should be made use of. This paper pushes the boundaries of what is possible in this “unsupervised” setting.
*


## Reference


[1]: http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/dcgan.html
[2]: https://junyanz.github.io/CycleGAN/
[3]: http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/dcgan.html
[4]: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/datasets.md
[5]: J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. Imagenet: A large-scale hierarchical image database. In CVPR, 2009. 8, 13, 18
[6]: 7.2.Networkarchitectures: https://arxiv.org/pdf/1703.10593.pdf
[7]: P. Isola, J.-Y. Zhu, T. Zhou, and A. A. Efros. Imageto-image translation with conditional adversarial networks. In CVPR, 2017. 2, 3, 5, 6, 7, 8, 18
[8]: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/CycleGAN.ipynb
[9]: Abstract: https://arxiv.org/pdf/1703.10593.pdf
[10]: 3.2.CycleConsistencyLoss: https://arxiv.org/pdf/1703.10593.pdf
[11]: 3.3.FullObjective: https://arxiv.org/pdf/1703.10593.pdf
[12]: T. Zhou, P. Krahenbuhl, M. Aubry, Q. Huang, and A. A. Efros. Learning dense correspondence via 3dguided cycle consistency. In CVPR, 2016. 2, 3
[13]: L. A. Gatys, A. S. Ecker, and M. Bethge. Image style transfer using convolutional neural networks. CVPR, 2016. 3, 8, 9, 14, 15
[14]: 4.Implementation: https://arxiv.org/pdf/1703.10593.pdf
[15]: J.Johnson,A.Alahi,andL.Fei-Fei. Perceptuallosses for real-time style transfer and super-resolution. In ECCV, 2016. 2, 3, 5, 7, 18
[16]: P. Isola, J.-Y. Zhu, T. Zhou, and A. A. Efros. Imageto-image translation with conditional adversarial networks. In CVPR, 2017. 2, 3, 5, 6, 7, 8, 18
[17]: K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. In CVPR, 2016. 5
[18]: D. Ulyanov, A. Vedaldi, and V. Lempitsky. Instance normalization: Themissingingredientforfaststylization. arXiv preprint arXiv:1607.08022, 2016. 5
[19]: P. Isola, J.-Y. Zhu, T. Zhou, and A. A. Efros. Imageto-image translation with conditional adversarial networks. In CVPR, 2017. 2, 3, 5, 6, 7, 8, 18
[20]: C. Li and M. Wand. Precomputed real-time texture synthesis with markovian generative adversarial networks. ECCV, 2016. 5
[21]: C. Ledig, L. Theis, F. Husz´ar, J. Caballero, A. Cunningham, A. Acosta, A. Aitken, A. Tejani, J. Totz, Z. Wang, et al. Photo-realistic single image superresolution using a generative adversarial network. In CVPR, 2017. 5
[22]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781789956177/ba03770c-17b6-42f6-b102-8c8554e523d9.xhtml
[23]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/209b2357-05d7-48d4-9c91-e061eccf8344.xhtml
[24]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/e4242ef6-dd25-4f42-91b8-4b701fc0d503.xhtml
[25]: https://github.com/taesungp/cyclegan
[26]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/a3d5b679-d40e-43cf-a71f-0998b7c18505.xhtml
[27]: https://github.com/eriklindernoren/PyTorch-GAN/tree/master/implementations/pix2pix
[28]: https://colab.research.google.com/github/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/CycleGAN.ipynb#scrollTo=z1EySlOXwwoa
[29]: https://github.com/Ldpe2G/DeepLearningForFun/tree/master/Mxnet-Scala/CycleGAN

---
https://learning.oreilly.com/library/view/advanced-deep-learning/9781789956177/262cfe39-8f03-49b7-ba8b-f8db88ff65d6.xhtml

Building the generator and discriminator
First, we'll implement the build_generator function. The GAN models we've looked at so far started with some sort of latent vector. But here, the generator input is an image from one of the domains and the output is an image from the opposite domain. Following the paper's guidelines, the generator is a U-Net style network. It has a downsampling encoder, an upsampling decoder, and shortcut connections between the corresponding encoder/decoder blocks. We'll start with the build_generator definition:

def build_generator(img: Input) -> Model:
The U-Net downsampling encoder consists of a number of convolutional layers with LeakyReLU activations, followed by InstanceNormalization. The difference between batch and instance normalization is that batch normalization computes its parameters across the whole mini-batch, while instance normalization computes them separately for each image of the mini-batch. For clarity, we'll implement a separate subroutine called downsampling2d, which defines one such layer. We'll use this function to build the necessary number of layers when we build the network encoder (please note the indentation here; downsampling2d is a subroutine defined within build_generator):

    def downsampling2d(layer_input, filters: int):
        """Layers used in the encoder"""
        d = Conv2D(filters=filters,
                   kernel_size=4,
                   strides=2,
                   padding='same')(layer_input)
        d = LeakyReLU(alpha=0.2)(d)
        d = InstanceNormalization()(d)
        return d
Next, let's focus on the decoder, which isn't implemented with transpose convolutions. Instead, the input data is upsampled with the UpSampling2D operation, which simply duplicates each input pixel as a 2×2 patch. This is followed by a regular convolution to smooth out the patches. This smoothed output is concatenated with the shortcut (or skip_input) connection from the corresponding encoder block. The decoder consists of a number of such upsampling blocks. For clarity, we'll implement a separate subroutine called upsampling2d, which defines one such block. We'll use it to build the necessary number of blocks for the network decoder (please note the indentation here; upsampling2d is a subroutine defined within build_generator):

    def upsampling2d(layer_input, skip_input, filters: int):
        """
        Layers used in the decoder
        :param layer_input: input layer
        :param skip_input: another input from the corresponding encoder block
        :param filters: number of filters
        """
        u = UpSampling2D(size=2)(layer_input)
        u = Conv2D(filters=filters,
                   kernel_size=4,
                   strides=1,
                   padding='same',
                   activation='relu')(u)
        u = InstanceNormalization()(u)
        u = Concatenate()([u, skip_input])
        return u
Next, we'll implement the full definition of the U-Net using the subroutines we just defined (please note the indentation here; the code is part of build_generator):

    # Encoder
    gf = 32
    d1 = downsampling2d(img, gf)
    d2 = downsampling2d(d1, gf * 2)
    d3 = downsampling2d(d2, gf * 4)
    d4 = downsampling2d(d3, gf * 8)

    # Decoder
    # Note that we concatenate each upsampling2d block with
    # its corresponding downsampling2d block, as per U-Net
    u1 = upsampling2d(d4, d3, gf * 4)
    u2 = upsampling2d(u1, d2, gf * 2)
    u3 = upsampling2d(u2, d1, gf)

    u4 = UpSampling2D(size=2)(u3)
    output_img = Conv2D(3, kernel_size=4, strides=1, padding='same',
    activation='tanh')(u4)

    model = Model(img, output_img)

    model.summary()

    return model
Then, we should implement the build_discriminator function. We'll omit the implementation here because it is a fairly straightforward CNN, similar to those shown in the previous examples (you can find this in the book's GitHub repository). The only difference is that, instead of using batch normalization, it uses instance normalization.
