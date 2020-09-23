

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 20:13:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-23 22:00:05
 * @Description:
 * @TODO::
 * @Reference:
-->

# Cycle-Consistent Adversarial Networks

Now, we introduced the basic ideas behind how GAN/DCGAN [1] work. We found that DCGAN can generate photorealistic images, like Pokemon.

In this section, we will demonstrate how you can use GANs to generate image-to-image translation which goal is to learn the mapping ( G : X → Y ) , cycle consistency loss to enforce F(G(X)) ≈ X between an input image G(X) and an output image Y using a training set of aligned image pairs. [9] We will be basing our models on the Cycle-Consistent Generative Adversarial Networks (CycleGAN) introduced in [2]. We will TODO:? , they can be leveraged to translate image-to-image. It works better if two datasets share similar visual content. For example, landscape painting<->landscape photographs, zebras<->horses.

Qualitative results are presented on several tasks where paired training data does not exist, including collection style transfer, object transﬁguration, season transfer, photo enhancement, etc.

![mapping](img\mapping.jpg)
 (a) Our model contains two mapping functions G : X → Y and F : Y → X, and associated adversarial discriminators DY and DX. DY encourages G to translate X into outputs indistinguishable from domain Y , and vice versa for DX and F. Tofurtherregularizethemappings,weintroducetwocycleconsistencylossesthatcapturetheintuitionthatif wetranslatefromonedomaintotheotherandbackagainweshouldarriveatwherewestarted: (b)forwardcycle-consistency loss: x → G(x) → F(G(x)) ≈ x, and (c) backward cycle-consistency loss: y → F(y) → G(F(y)) ≈ y




## baseline

pix2pix [13] We also compare against pix2pix [13], which is trained on paired data, to see how close we can get to this “upper bound” without using any paired data.






Mathematically, if we have a translator G : X → Y and another translator F : Y → X, then G and F should be inverses of each other, and both mappings should be bijections. We apply this structural assumptionbytrainingboththemapping G and F simultaneously, and adding a cycle consistency loss [12] that encourages F(G(x)) ≈ x and G(F(y)) ≈ y. Combining this loss with adversarial losses on domains X and Y yields our full objective for unpaired image-to-image translation.



## The apple2orange Dataset[4]

apple2orange: 996 apple images and 1020 orange images downloaded from ImageNet using keywords apple and navel orange.[5]

`bash ./datasets/download_cyclegan_dataset.sh dataset_name`

script.

`bash ./datasets/download_cyclegan_dataset.sh apple2orange`


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



### Full Objective[11]

$\begin{aligned} \mathcal{L}\left(G, F, D_{X}, D_{Y}\right) &=\mathcal{L}_{\text {GAN }}\left(G, D_{Y}, X, Y\right) \\ &+\mathcal{L}_{\text {GAN }}\left(F, D_{X}, Y, X\right) \\ &+\lambda \mathcal{L}_{\text {cyc }}(G, F) \end{aligned}$

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
