

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 20:13:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-23 21:13:20
 * @Description:
 * @TODO::
 * @Reference:
-->

# Cycle-Consistent Adversarial Networks

Now, we introduced the basic ideas behind how GAN/DCGAN [1] work. We found that DCGAN can generate photorealistic images, like Pokemon.

In this section, we will demonstrate how you can use GANs to generate image-to-image translation which goal is to learn the mapping ( G : X → Y ) , cycle consistency loss to enforce F(G(X)) ≈ X between an input image G(X) and an output image Y using a training set of aligned image pairs. [9] We will be basing our models on the Cycle-Consistent Generative Adversarial Networks (CycleGAN) introduced in [2]. We will TODO:? , they can be leveraged to translate image-to-image. It works better if two datasets share similar visual content. For example, landscape painting<->landscape photographs, zebras<->horses.

Qualitative results are presented on several tasks where paired training data does not exist, including collection style transfer, object transﬁguration, season transfer, photo enhancement, etc.

##
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



## The Generator[6]

The network with 6 residual blocks consists of: c7s1-64,d128,d256,R256,R256,R256, R256,R256,R256,u128,u64,c7s1-3
The network with 9 residual blocks consists of: c7s1-64,d128,d256,R256,R256,R256, R256,R256,R256,R256,R256,R256,u128 u64,c7s1-3



## The Discriminator[6]

For discriminator networks, we use 70 × 70 PatchGAN [7]. Let Ck denote a 4×4 Convolution-InstanceNorm-LeakyReLU layer with k ﬁlters and stride 2. After the last layer, we apply a convolution to produce a 1-dimensional output. We do not use InstanceNorm for the ﬁrst C64 layer. We use leaky ReLUs with a slope of 0.2. The discriminator architecture is: C64-C128-C256-C512





Image-to-image translation



The discriminator is a mirror of the generator.



## Training

Compared to the basic GAN in Section 17.1, we use the same learning rate for both generator and discriminator since they are similar to each other. In addition, we change  β1  in Adam (Section 11.10) from  0.9  to  0.5 . It decreases the smoothness of the momentum, the exponentially weighted moving average of past gradients, to take care of the rapid changing gradients because the generator and the discriminator fight with each other. Besides, the random generated noise Z, is a 4-D tensor and we are using GPU to accelerate the computation.

We train the model with a small number of epochs just for demonstration. For better performance, the variable `num_epochs` can be set to a larger number.



## Cycle Consistency Loss

$\begin{aligned} \mathcal{L}_{\mathrm{cyc}}(G, F) &=\mathbb{E}_{x \sim p_{\text {data }}(x)}\left[\|F(G(x))-x\|_{1}\right] \\ &+\mathbb{E}_{y \sim p_{\text {data }}(y)}\left[\|G(F(y))-y\|_{1}\right] \end{aligned}$


## Full Objective

$\begin{aligned} \mathcal{L}\left(G, F, D_{X}, D_{Y}\right) &=\mathcal{L}_{\text {GAN }}\left(G, D_{Y}, X, Y\right) \\ &+\mathcal{L}_{\text {GAN }}\left(F, D_{X}, Y, X\right) \\ &+\lambda \mathcal{L}_{\text {cyc }}(G, F) \end{aligned}$




train.py is a general-purpose training script. It works for various models (with option --model: e.g., pix2pix, cyclegan, colorization) and different datasets (with option --dataset_mode: e.g., aligned, unaligned, single, colorization). See the main README and training/test tips for more details.[8]


## Summary




## Reference


[1]:http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/dcgan.html
[2]:https://junyanz.github.io/CycleGAN/
[3]:http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/dcgan.html
[4]:https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/datasets.md
[5]:J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. Imagenet: A large-scale hierarchical image database. In CVPR, 2009. 8, 13, 18
[6]:7.2.Networkarchitectures: https://arxiv.org/pdf/1703.10593.pdf
[7]:P. Isola, J.-Y. Zhu, T. Zhou, and A. A. Efros. Imageto-image translation with conditional adversarial networks. In CVPR, 2017. 2, 3, 5, 6, 7, 8, 18
[8]:https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/CycleGAN.ipynb
[9]:Abstract: https://arxiv.org/pdf/1703.10593.pdf
