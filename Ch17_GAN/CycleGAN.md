

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 20:13:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-24 18:03:42
 * @Description:
 * @TODO::
 * @Reference:
-->

# Cycle-Consistent Adversarial Networks

Now, we introduced the basic ideas behind how GAN/DCGAN [1] work. We found that DCGAN can generate photorealistic images, like Pokemon, styleGAN[35][34].

In this section, we will demonstrate how you can use GANs to translate Unpaired image-to-image [22] which goal is to learn the mapping ( G : X → Y ) , cycle consistency loss to enforce F(G(X)) ≈ X between an input image G(X) and an output image Y using a training set of aligned image pairs. [9] We will be basing our models on the Cycle-Consistent Generative Adversarial Networks (CycleGAN website[25]) introduced in [2]. We will TODO:? , they can be leveraged to translate image-to-image. It works better if two datasets share similar visual content. For example, landscape painting<->landscape photographs, zebras<->horses[28].convert it into the style of Van Gogh or Picasso![31]
increase the quality and dimension of generated data.[33]

TODO:?  [2]
However, with large enough capacity, a network can map the same set of input images to any random permutation of images in the target domain, where any of the learned mappings can induce an output distribution that matches the target distribution. Thus, an adversarial loss alone cannot guarantee that the learned function can map an individual input  xi  to a desired output  yi .

![horse2zebra](img/horse2zebra.gif)

Qualitative results are presented on several tasks where paired training data does not exist, including collection style transfer, object transﬁguration, season transfer, photo enhancement, etc.

![mapping](img\mapping.jpg)

Left: Overall CycleGAN schema; Middle: Forward cycle-consistency loss; Right: Backward cycle-consistency loss.[22]

 (a) Our model contains two mapping functions G : X → Y and F : Y → X, and associated adversarial discriminators DY and DX. DY encourages G to translate X into outputs indistinguishable from domain Y , and vice versa for DX and F. Tofurtherregularizethemappings,weintroducetwocycleconsistencylossesthatcapturetheintuitionthatif wetranslatefromonedomaintotheotherandbackagainweshouldarriveatwherewestarted: (b)forwardcycle-consistency loss: x → G(x) → F(G(x)) ≈ x, and (c) backward cycle-consistency loss: y → F(y) → G(F(y)) ≈ y

CycleGAN tries to solve these issues with the so-called cycle consistency.
The translation will be cycle-consistent if we translate the sentence back from German into English and we arrive at the original sentence we started with.
In a mathematical context, if we have a translator, , and another translator, the two should be inverses of each other.[22]

Using CycleGAN, we only need to train one model to freely translate from image set A to image set B and vice versa.[26] We will need at least two sets of Discriminators and two Generators to achieve this.[30]

## DiscoGAN[39]

![DiscoGAN](img\DiscoGAN.jpg)[39]

On a high level, it tries to learn two generator functions in the form of neural networks $G_A$B and $G_BA$ so that an image xA, when fed through the generator $G_AB
$, produces an image xAB, that looks realistic in domain $B$. Also, when this image xAB is fed through the other generator network $G_B$A, it should produce an image $x_ABA$ which should ideally be the same as the original image $x_A$. With respect to the generator function, the following relation should hold true:

$G_{B A} G_{A B}\left(x_{A}\right)=x_{A}$

Taking all of this into consideration, we can formulate the loss the generator we would like to minimize as the reconstruction loss and the loss with respect to the discriminator identifying xAB as fake. The second loss will attempt to make the generator produce realistic images in domain B. The generator loss of mapping an image xA in domain A to an image in domain B can be expressed as follows:

$C=\left\|x_{A}-x_{A B A}\right\|_{2}^{2}=\left\|x_{A}-G_{B A} G_{A B}\left(x_{A}\right)\right\|_{2}^{2}$

The reconstruction loss under the L2 norm can be expressed as follows:

$C_{reconst(ABA)}=\left\|x_{A}-G_{BA} G_{AB}\left(x_{A}\right)\right\|_{2}^{2}$

Frobenius norm

is given by $D_{B}(.),$ then the generator should make $x_{A B}$ highly probable under the
discriminator network, so that $D_{B}\left(x_{B}\right)=D_{B}\left(G_{A B}\left(x_{A}\right)\right)$ is as close to 1 as possible. In terms of
log loss, the generator should minimize the negative log of the preceding probability, which
basically gives us $C_{D(A B)}$, as shown here:
$C_{D(A B)}=-\log \left(D_{B}\left(G_{A B}\left(x_{A}\right)\right)\right)$
Combining (3) and (4), we can get the total generator cost $C_{-} G_{A B}$ of mapping an image from
domain A to domain B, as shown here:
$C_{-} G_{A B}=C_{r e c o n s t(A B A)}+C_{D(A B)}=\underset{x_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\left\|x_{A}-G_{B A} G_{A B}\left(x_{A}\right)\right\|_{2}^{2}-\log \left(D_{B}\left(G_{A B}\left(x_{A}\right)\right)\right)\right]+\underset{y_{B} \sim P\left(x_{B}\right)}{\mathbb{E}}\left[\left\|x_{B}-G_{A B} G_{B A}\left(x_{B}\right)\right\|_{2}^{2}-\log \left(D_{A}\left(G_{B A}\left(y_{B}\right)\right)\right)\right]$
Now, let's build the cost functions the discriminators would try to minimize to set up the
zero-sum min/max games. The discriminators in each domain would try to distinguish the real images from the fake images, and hence the discriminator $G_{B}$ would try to minimize the
cost $C_{-} D_{B},$ as shown here:
$C_{-} D_{B}=-\underset{x_{B} \sim P\left(x_{B}\right)}{\mathbb{E}}\left[\log \left(D_{B}\left(x_{B}\right)\right)\right]-\underset{x_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\log \left(1-G_{A B}\left(x_{A}\right)\right)\right]$
Similarly, the discriminator $D_{A}$ would try to minimize the cost $C_{-} D_{A}$ as shown here:
$C_{-} D_{A}=-\underset{x_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\log \left(D_{B}\left(x_{A}\right)\right)\right]-\underset{x_{B} \sim P\left(x_{B}\right)}{\mathbb{E}}\left[\log \left(1-G_{B A}\left(x_{B}\right)\right)\right]$
Combining ( 8 ) and ( 9 ) the overall discriminator cost is given by $C_{D}$, as follows:
$C_{D}=-\underset{y_{B} \sim P\left(y_{B}\right)}{\mathbb{E}}\left[\log \left(D_{B}\left(y_{B}\right)\right)\right]-\underset{x_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\log \left(1-G_{A B}\left(x_{A}\right)\right)\right]-\underset{x_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\log \left(D_{B}\left(x_{A}\right)\right)\right]-\underset{x_{B} \sim P\left(y_{B}\right)}{\mathbb{E}}\left[\log \left(1-G_{B A}\left(x_{B}\right)\right)\right](10)$
If we denote the parameters of the $G_{A B}, G_{B A}, D_{A},$ and $D_{B}$ as $\theta_{G A B}, \theta_{G B A}, \theta_{D A},$ and $\theta_{D B},$ then
the optimized parameters of the networks can be represented as follows:


$$\hat{\theta}_{G A B}, \hat{\theta}_{G B A}=\operatorname{argmin}_{\theta_{C A B}, \theta_{G B A}} \underset{z_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\left\|x_{A}-G_{B A} G_{A B}\left(x_{A}\right)\right\|_{2}^{2}-\log \left(D_{B}\left(G_{A B}\left(x_{A}\right)\right)\right)\right]+\underset{z_{B} \sim P\left(x_{B}\right)}{\mathbb{E}}\left[\left\|x_{B}-G_{A B} G_{B A}\left(x_{B}\right)\right\|_{2}^{2}-\log \left(D_{A}\left(G_{B A}\left(x_{B}\right)\right)\right)\right]$$
$$\hat{\theta}_{D A}, \hat{\theta}_{D B}=\operatorname{argmin}_{\theta_{D A}, \theta_{D B}}-\underset{x_{B} \sim P\left(x_{B}\right)}{\mathbb{E}}\left[\log \left(D_{B}\left(x_{B}\right)\right)\right]-\underset{x_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\log \left(1-G_{A B}\left(x_{A}\right)\right)\right]-\underset{x_{A} \sim P\left(x_{A}\right)}{\mathbb{E}}\left[\log \left(D_{B}\left(x_{A}\right)\right)\right]-\underset{x_{B} \sim P\left(x_{B}\right)}{\mathbb{E}}\left[\log \left(1-G_{B A}\left(x_{B}\right)\right)\right]$$

https://github.com/PacktPublishing/Intelligent-Projects-using-Python/tree/master/Chapter04

one small modification. In a CycleGAN, we have the flexibility to determine how much weight to assign to the reconstruction loss with respect to the GAN loss or the loss attributed to the discriminator. This parameter helps in balancing the losses in correct proportions based on the problem at hand to help the network converge faster while training.[40]


## baseline(pix2pix)


pix2pix uses a conditional generative adversarial network (cGAN) to learn a mapping from an input image to an output image.


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

![network](CycleGAN_network.jpg)[30]

Input

Output

Goal

Generator: from A to B	We load either a real picture from A or a translation from B to A.	We translate it to domain B.	Try to create realistic-looking images in domain B.
Generator: from B to A	We load either a real picture from B or a translation from A to B.	We translate it to domain A.	Try to create realistic-looking images in domain A.
Discriminator A	We provide a picture in the A domain—either translated or real.	The probability that the picture is real.	Try to not get fooled by the Generator from B to A.
Discriminator B	We provide a picture in the B domain—either translated or real.	The probability that the picture is real.	Try to not get fooled by the Generator from A to B.


Creating the two Discriminators DA and DB and compiling them
Creating the two Generators:
Instantiating GAB and GBA
Creating placeholders for the image input for both directions
Linking them both to an image in the other domain
Creating placeholders for the reconstructed images back in the original domain
Creating the identity loss constraint for both directions
Not making the parameters of the Discriminators trainable for now
Compiling the two Generators


### Residual block[32]

![generator0](img\CycleGAN_generator.png)
create the code for the definition of the residual block, as follows:

```python
#[32]
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__()

        block = [nn.ReflectionPad2d(1),
                 nn.Conv2d(channels, channels, 3),
                 nn.InstanceNorm2d(channels),
                 nn.ReLU(inplace=True),
                 nn.ReflectionPad2d(1),
                 nn.Conv2d(channels, channels, 3),
                 nn.InstanceNorm2d(channels)]
         self.block = nn.Sequential(*block)

     def forward(self, x):
         return x + self.block(x)
```

### The Generator[6]

![generator1](img\CycleGAN_generator.jpg)


We adopt our architectures from Johnson et al. [23]. We use 6 residual blocks for 128×128 training images, and 9 residual blocks for 256× 256 or higher-resolution training images. Below, we follow the naming convention used in the Johnson et al.’s Github repository. Let c7s1-k denotea 7×7 Convolution-InstanceNormReLU layer with k ﬁlters and stride 1. dk denotes a 3×3 Convolution-InstanceNorm-ReLU layer with k ﬁlters and stride 2. Reﬂection padding was used to reduce artifacts. Rk denotes a residual block that contains two 3 × 3 convolutional layers with the same number of ﬁlters on both layer. uk denotes a 3 × 3 fractional-strided-ConvolutionInstanceNorm-ReLU layer with k ﬁlters and stride 1

The network with 6 residual blocks consists of: c7s1-64,d128,d256,R256,R256,R256, R256,R256,R256,u128,u64,c7s1-3
The network with 9 residual blocks consists of: c7s1-64,d128,d256,R256,R256,R256, R256,R256,R256,R256,R256,R256,u128 u64,c7s1-3

```python
#[32]
class Generator(nn.Module):
    def __init__(self, channels, num_blocks=9):
        super(Generator, self).__init__()
        self.channels = channels

        model = [nn.ReflectionPad2d(3)]
        model += self._create_layer(self.channels, 64, 7, stride=1, padding=0, transposed=False)
        # downsampling
        model += self._create_layer(64, 128, 3, stride=2, padding=1, transposed=False)
        model += self._create_layer(128, 256, 3, stride=2, padding=1, transposed=False)
        # residual blocks
        model += [ResidualBlock(256) for _ in range(num_blocks)]
        # upsampling
        model += self._create_layer(256, 128, 3, stride=2, padding=1, transposed=True)
        model += self._create_layer(128, 64, 3, stride=2, padding=1, transposed=True)
        # output
        model += [nn.ReflectionPad2d(3),
                  nn.Conv2d(64, self.channels, 7),
                  nn.Tanh()]

        self.model = nn.Sequential(*model)

    def _create_layer(self, size_in, size_out, kernel_size, stride=2, padding=1, transposed=False):
        layers = []
        if transposed:
            layers.append(nn.ConvTranspose2d(size_in, size_out, kernel_size, stride=stride, padding=padding, output_padding=1))
        else:
            layers.append(nn.Conv2d(size_in, size_out, kernel_size, stride=stride, padding=padding))
        layers.append(nn.InstanceNorm2d(size_out))
        layers.append(nn.ReLU(inplace=True))
        return layers

    def forward(self, x):
        return self.model(x)
```

### The Discriminator[6]

For discriminator networks, we use 70 × 70 PatchGAN [7]. Let Ck denote a 4×4 Convolution-InstanceNorm-LeakyReLU layer with k ﬁlters and stride 2. After the last layer, we apply a convolution to produce a 1-dimensional output. We do not use InstanceNorm for the ﬁrst C64 layer. We use leaky ReLUs with a slope of 0.2. The discriminator architecture is: C64-C128-C256-C512

We take the input image (128 × 128 × 3) and assign that to d1 (64 × 64 × 64).
We take d1 (64 × 64 × 64) and assign that to d2 (32 × 32 × 128).
We take d2 (32 × 32 × 128) and assign that to d3 (16 × 16 × 256).
We take d3 (16 × 16 × 256) and assign that to d4 (8 × 8 × 512).
We take d4 (8 × 8 × 512) and flatten by conv2d to 8 × 8 × 1.[30]


```python
# [30]
def build_discriminator(self):

        def d_layer(layer_input, filters, f_size=4, normalization=True):
            """Discriminator layer"""
            d = Conv2D(filters, kernel_size=f_size,
                       strides=2, padding='same')(layer_input)
            d = LeakyReLU(alpha=0.2)(d)
            if normalization:
                d = InstanceNormalization()(d)
            return d

        img = Input(shape=self.img_shape)

        d1 = d_layer(img, self.df, normalization=False)
        d2 = d_layer(d1, self.df * 2)
        d3 = d_layer(d2, self.df * 4)
        d4 = d_layer(d3, self.df * 8)

        validity = Conv2D(1, kernel_size=4, strides=1, padding='same')(d4)

        return Model(img, validity)
```

```python
#[32]
class Discriminator(nn.Module):
    def __init__(self, channels):
        super(Discriminator, self).__init__()
        self.channels = channels

        self.model = nn.Sequential(
            *self._create_layer(self.channels, 64, 2, normalize=False),
            *self._create_layer(64, 128, 2),
            *self._create_layer(128, 256, 2),
            *self._create_layer(256, 512, 1),
            nn.Conv2d(512, 1, 4, stride=1, padding=1)
        )

    def _create_layer(self, size_in, size_out, stride, normalize=True):
        layers = [nn.Conv2d(size_in, size_out, 4, stride=stride, padding=1)]
        if normalize:
            layers.append(nn.InstanceNorm2d(size_out))
        layers.append(nn.LeakyReLU(0.2, inplace=True))
        return layers

    def forward(self, x):
        return self.model(x)
```
Image-to-image translation


The discriminator is a mirror of the generator.

## Loss Function

 For the mapping function G : X → Y and its discriminator $D_Y$ , we express the objective as:

$\begin{aligned} \mathcal{L}_{\mathrm{GAN}}\left(G, D_{Y}, X, Y\right) &=\mathbb{E}_{y \sim p_{\text {data }}(y)}\left[\log D_{Y}(y)\right] \\ &+\mathbb{E}_{x \sim p_{\text {data }}(x)}\left[\log \left(1-D_{Y}(G(x))\right],\right.\end{aligned}$

1. Discriminator must approve all the original images of the corresponding categories.
1. Discriminator must reject all the images which are generated by corresponding Generators to fool them.
1. Generators must make the discriminators approve all the generated images, so as to fool them.
1. The generated image must retain the property of original image, so if we generate a fake image using a generator say  GeneratorA→B  then we must be able to get back to original image using the another generator  GeneratorB→A  - it must satisfy cyclic-consistency.

### Discriminator Loss

minimize ( Discriminator $\left._{A}(a)-1\right)^{2}$

```python
D_A_loss_1 = tf.reduce_mean(tf.squared_difference(dec_A,1))
D_B_loss_1 = tf.reduce_mean(tf.squared_difference(dec_B,1))
```


minimize(Discriminator $\left._{A}\left(\right.\right.$Generator $\left.\left._{B \rightarrow A}(b)\right)\right)^{2}$

```python
D_A_loss_2 = tf.reduce_mean(tf.square(dec_gen_A))
D_B_loss_2 = tf.reduce_mean(tf.square(dec_gen_B))

D_A_loss = (D_A_loss_1 + D_A_loss_2)/2
D_B_loss = (D_B_loss_1 + D_B_loss_2)/2
```

### Generator Loss

minimize
$\left(\text {Discriminator}_{B}\left(\text {Generator}_{A \rightarrow B}(a)\right)-1\right)^{2}$


```python
g_loss_B_1 = tf.reduce_mean(tf.squared_difference(dec_gen_A,1))
g_loss_A_1 = tf.reduce_mean(tf.squared_difference(dec_gen_A,1))
```

### Cycle Consistency Loss[10]

$\begin{aligned} \mathcal{L}_{\mathrm{cyc}}(G, F) &=\mathbb{E}_{x \sim p_{\text {data }}(x)}\left[\|F(G(x))-x\|_{1}\right] \\ &+\mathbb{E}_{y \sim p_{\text {data }}(y)}\left[\|G(F(y))-y\|_{1}\right] \end{aligned}$

The behavior induced by the cycle consistency loss can beobservedinFigure4: thereconstructedimages F(G(x)) end up matching closely to the input images x.

In particular, for a GAN loss $\mathcal{L}_{\mathrm{GAN}}(G, D, X, Y)$and train the $G$ to minimize $\mathbb{E}_{x \sim p_{\text {data}}(x)}\left[(D(G(x))-1)^{2}\right]$and train the $D$ to minimize $\mathbb{E}_{y \sim p_{\text {data}}(y)}\left[(D(y)-1)^{2}\right]+$ $\mathbb{E}_{x \sim p_{\text {data}}(x)}\left[D(G(x))^{2}\right]$ [14]

```python
cyc_loss = tf.reduce_mean(tf.abs(input_A-cyc_A)) + tf.reduce_mean(tf.abs(input_B-cyc_B))
```



This measures the absolute difference between the original images, that is, x and y, and their generated counterparts, $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}} .$ Note that these paths can be viewed as jointly training two autoencoders, $F \circ G: X \rightarrow X$ and $G \circ F: Y \rightarrow Y$. Each autoencoder has a special internal structure: it maps an image to itself with the help of an intermediate representation – the translation of the image into another domain.[22]



### Full Objective[11]

Minimize[31]
$\begin{aligned} \mathcal{L}\left(G, F, D_{X}, D_{Y}\right) &=\mathcal{L}_{\text {GAN }}\left(G, D_{Y}, X, Y\right) \\ &+\mathcal{L}_{\text {GAN }}\left(F, D_{X}, Y, X\right) \\ &+\lambda \mathcal{L}_{\text {cyc }}(G, F) \end{aligned}$

the coefficient, λ, controls the relative importance between the two losses. CycleGAN aims to solve the following minimax objective:[22]


We aim to solve:

$G^{*}, F^{*}=\arg \min _{G, F} \max _{D_{x}, D_{Y}} \mathcal{L}\left(G, F, D_{X}, D_{Y}\right)$

```python
#[31]
cyc_loss = tf.reduce_mean(tf.abs(input_A-cyc_A)) + tf.reduce_mean(tf.abs(input_B-cyc_B))
g_loss_A = g_loss_A_1 + 10*cyc_loss
g_loss_B = g_loss_B_1 + 10*cyc_loss
```

The multiplicative factor of 10 for cyc_loss assigns more importance to cyclic loss than the discrimination loss.[31]

### Putting it together[31]

With the loss function defined, all the is needed to train the model is to minimize the loss function w.r.t. model parameters.

```python
d_A_trainer = optimizer.minimize(d_loss_A, var_list=d_A_vars)
d_B_trainer = optimizer.minimize(d_loss_B, var_list=d_B_vars)
g_A_trainer = optimizer.minimize(g_loss_A, var_list=g_A_vars)
g_B_trainer = optimizer.minimize(g_loss_B, var_list=g_B_vars)
```

## Training

Compared to the basic GAN in Section 17.1, we use the same learning rate for both generator and discriminator since they are similar to each other. In addition, we change  β1  in Adam (Section 11.10) from  0.9  to  0.5 . It decreases the smoothness of the momentum, the exponentially weighted moving average of past gradients, to take care of the rapid changing gradients because the generator and the discriminator fight with each other. Besides, the random generated noise Z, is a 4-D tensor and we are using GPU to accelerate the computation.

We train the model with a small number of epochs just for demonstration. For better performance, the variable `num_epochs` can be set to a larger number.



For each training iteration do[30]

1. Train the Discriminator:
    Take a mini-batch of random images from each domain (imgsA and imgsB).
    Use the Generator GAB to translate imgsA to domain B and vice versa with GBA.
    Compute DA(imgsA, 1) and DA(GBA(imgsB), 0) to get the losses for real images in A and translated images from B, respectively. Then add these two losses together. The 1 and 0 in DA serve as labels.
    Compute DB(imgsB, 1) and DB(GAB(imgsA), 0) to get the losses for real images in B and translated images from A, respectively. Then add these two losses together. The 1 and 0 in DB serve as labels.
2. Add the losses from steps c and d together to get a total Discriminator loss. Train the Generator:
    We use the combined model to
    Input the images from domain A (imgsA) and B (imgsB)
        The outputs are
        Validity of A: DA(GBA(imgsB))
        Validity of B: DB(GAB(imgsA))
        Reconstructed A: GBA(GAB(imgsA))
        Reconstructed B: GAB(GBA(imgsB))
        Identity mapping of A: GBA(imgsA))
        Identity mapping of B: GAB(imgsB))
    We then update the parameters of both Generators inline with the cycle-consistency loss, identity loss, and adversarial loss with
        Mean squared error (MSE) for the scalars (discriminator probabilities)
        Mean absolute error (MAE) for images (either reconstructed or identity-mapped)

[30]
1 Adversarial loss ground truths
2 Now we begin to train the Discriminators. These lines translate images to the opposite domain.
3 Trains the Discriminators (original images = real / translated = Fake)
4 Total Discriminator loss
5 Trains the Generators
6 If at save interval => save generated image samples
7 This function is similar to what you have encountered and is made explicit in the GitHub repository.



train.py is a general-purpose training script. It works for various models (with option --model: e.g., pix2pix, cyclegan, colorization) and different datasets (with option --dataset_mode: e.g., aligned, unaligned, single, colorization). See the main README and training/test tips for more details.[8]

```python
#[31]
def image_pool(self, num_gen, gen_img, gen_pool):
    if(num_gen < pool_size):
        gen_img_pool[num_gen] = gen_img
        return gen_img
    else :
        p = random.random()
        if p > 0.5:
            # Randomly selecting an id to return for calculating the discriminator loss
            random_id = random.randint(0,pool_size-1)
            temp = gen_img_pool[random_id]
            gen_pool[random_id] = gen_img
            return temp
        else :
            return gen_img
```

```python
#[31]
gen_image_pool_A = tf.placeholder(tf.float32, [batch_size, img_width, img_height, img_layer], name="gen_img_pool_A")
gen_image_pool_B = tf.placeholder(tf.float32, [batch_size, img_width, img_height, img_layer], name="gen_img_pool_B")

gen_pool_rec_A = build_gen_discriminator(gen_image_pool_A, "d_A")
gen_pool_rec_B = build_gen_discriminator(gen_image_pool_B, "d_B")

# Also the discriminator loss will change as follow

D_A_loss_2 = tf.reduce_mean(tf.square(gen_pool_rec_A))
D_A_loss_2 = tf.reduce_mean(tf.square(gen_pool_rec_A))
```

## Model[43]

```python
model = torch.hub.load('facebookresearch/pytorch_GAN_zoo:hub', 'PGAN',
                       model_name='celebAHQ-512',
                       pretrained=True,
                       useGPU=use_gpu)
```

## Summary

* Finally, we demonstrate the generality of our algorithm on a wide range of applications where paired data does not exist.
* Nonetheless, in many cases completely unpaired data is plentifully available and should be made use of. This paper pushes the boundaries of what is possible in this “unsupervised” setting.

## Summary[30]

* Image-to-image translation frameworks are frequently difficult to train because of the need for perfect pairs; the CycleGAN solves this by making this an unpaired domain translation.
* The CycleGAN has three losses:
* Cycle-consistent, which measures the difference between the original image and an image translated into a different domain and back again
* Adversarial, which ensures realistic images
* Identity, which preserves the color space of the image
* The two Generators use the U-Net architecture, and the two Discriminators use the PatchGAN-based architecture.
* We implemented an object-oriented design of the CycleGAN and used it to convert apples to oranges.
* Practical applications of the CycleGAN include self-driving car training and extensions that allow us to create different styles of images during the translation process.

## Explore[36]

it will be time to explore other networks such as the Least Squares GAN (LSGAN) and Wasserstein GAN (WGAN). Then, there is this large playing field of conditional GANs such as the Conditional GAN (cGan), InfoGAN, Auxiliary Classifier GAN (AC-GAN), and Semi-Supervised GAN (SGAN). Once you've done this, you'll have set the stage for advanced topics such as CycleGAN, BigGAN, and StyleGAN.

## Exercises[37]

What are the main tasks that autoencoders are used for?

Suppose you want to train a classifier, and you have plenty of unlabeled training data but only a few thousand labeled instances. How can autoencoders help? How would you proceed?

If an autoencoder perfectly reconstructs the inputs, is it necessarily a good autoencoder? How can you evaluate the performance of an autoencoder?

What are undercomplete and overcomplete autoencoders? What is the main risk of an excessively undercomplete autoencoder? What about the main risk of an overcomplete autoencoder?

How do you tie weights in a stacked autoencoder? What is the point of doing so?

What is a generative model? Can you name a type of generative autoencoder?

What is a GAN? Can you name a few tasks where GANs can shine?

What are the main difficulties when training GANs?

Try using a denoising autoencoder to pretrain an image classifier. You can use MNIST (the simplest option), or a more complex image dataset such as CIFAR10 if you want a bigger challenge. Regardless of the dataset you’re using, follow these steps:

Split the dataset into a training set and a test set. Train a deep denoising autoencoder on the full training set.

Check that the images are fairly well reconstructed. Visualize the images that most activate each neuron in the coding layer.

Build a classification DNN, reusing the lower layers of the autoencoder. Train it using only 500 images from the training set. Does it perform better with or without pretraining?

Train a variational autoencoder on the image dataset of your choice, and use it to generate images. Alternatively, you can try to find an unlabeled dataset that you are interested in and see if you can generate new samples.

Train a DCGAN to tackle the image dataset of your choice, and use it to generate images. Add experience replay and see if this helps. Turn it into a conditional GAN where you can control the generated class.

## Answers[38]

Here are some of the main tasks that autoencoders are used for:

Feature extraction

Unsupervised pretraining

Dimensionality reduction

Generative models

Anomaly detection (an autoencoder is generally bad at reconstructing outliers)

If you want to train a classifier and you have plenty of unlabeled training data but only a few thousand labeled instances, then you could first train a deep autoencoder on the full dataset (labeled + unlabeled), then reuse its lower half for the classifier (i.e., reuse the layers up to the codings layer, included) and train the classifier using the labeled data. If you have little labeled data, you probably want to freeze the reused layers when training the classifier.

The fact that an autoencoder perfectly reconstructs its inputs does not necessarily mean that it is a good autoencoder; perhaps it is simply an overcomplete autoencoder that learned to copy its inputs to the codings layer and then to the outputs. In fact, even if the codings layer contained a single neuron, it would be possible for a very deep autoencoder to learn to map each training instance to a different coding (e.g., the first instance could be mapped to 0.001, the second to 0.002, the third to 0.003, and so on), and it could learn “by heart” to reconstruct the right training instance for each coding. It would perfectly reconstruct its inputs without really learning any useful pattern in the data. In practice such a mapping is unlikely to happen, but it illustrates the fact that perfect reconstructions are not a guarantee that the autoencoder learned anything useful. However, if it produces very bad reconstructions, then it is almost guaranteed to be a bad autoencoder. To evaluate the performance of an autoencoder, one option is to measure the reconstruction loss (e.g., compute the MSE, or the mean square of the outputs minus the inputs). Again, a high reconstruction loss is a good sign that the autoencoder is bad, but a low reconstruction loss is not a guarantee that it is good. You should also evaluate the autoencoder according to what it will be used for. For example, if you are using it for unsupervised pretraining of a classifier, then you should also evaluate the classifier’s performance.

An undercomplete autoencoder is one whose codings layer is smaller than the input and output layers. If it is larger, then it is an overcomplete autoencoder. The main risk of an excessively undercomplete autoencoder is that it may fail to reconstruct the inputs. The main risk of an overcomplete autoencoder is that it may just copy the inputs to the outputs, without learning any useful features.

To tie the weights of an encoder layer and its corresponding decoder layer, you simply make the decoder weights equal to the transpose of the encoder weights. This reduces the number of parameters in the model by half, often making training converge faster with less training data and reducing the risk of overfitting the training set.

A generative model is a model capable of randomly generating outputs that resemble the training instances. For example, once trained successfully on the MNIST dataset, a generative model can be used to randomly generate realistic images of digits. The output distribution is typically similar to the training data. For example, since MNIST contains many images of each digit, the generative model would output roughly the same number of images of each digit. Some generative models can be parametrized—for example, to generate only some kinds of outputs. An example of a generative autoencoder is the variational autoencoder.

A generative adversarial network is a neural network architecture composed of two parts, the generator and the discriminator, which have opposing objectives. The generator’s goal is to generate instances similar to those in the training set, to fool the discriminator. The discriminator must distinguish the real instances from the generated ones. At each training iteration, the discriminator is trained like a normal binary classifier, then the generator is trained to maximize the discriminator’s error. GANs are used for advanced image processing tasks such as super resolution, colorization, image editing (replacing objects with realistic background), turning a simple sketch into a photorealistic image, or predicting the next frames in a video. They are also used to augment a dataset (to train other models), to generate other types of data (such as text, audio, and time series), and to identify the weaknesses in other models and strengthen them.

Training GANs is notoriously difficult, because of the complex dynamics between the generator and the discriminator. The biggest difficulty is mode collapse, where the generator produces outputs with very little diversity. Moreover, training can be terribly unstable: it may start out fine and then suddenly start oscillating or diverging, without any apparent reason. GANs are also very sensitive to the choice of hyperparameters.

For the solutions to exercises 9, 10, and 11, please see the Jupyter notebooks available at https://github.com/ageron/handson-ml2.

## Mobile[42]

The runPix2PixBlurryModel method is similar to the code in the previous chapters where we used an image input to feed into our models.

## Reference

```md
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
[21]: C. Ledg, L. Theis, F. Husz´ar, J. Caballero, A. Cunningham, A. Acosta, A. Aitken, A. Tejani, J. Totz, Z. Wang, et al. Photo-realistic single image superresolution using a generative adversarial network. In CVPR, 2017. 5
[22]: https://learning.oreilly.com/library/view/advanced-deep-learning/9781789956177/ba03770c-17b6-42f6-b102-8c8554e523d9.xhtml
[23]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/209b2357-05d7-48d4-9c91-e061eccf8344.xhtml
[24]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/e4242ef6-dd25-4f42-91b8-4b701fc0d503.xhtml
[25]: https://github.com/taesungp/cyclegan
[26]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/a3d5b679-d40e-43cf-a71f-0998b7c18505.xhtml
[27]: https://github.com/eriklindernoren/PyTorch-GAN/tree/master/implementations/pix2pix
[28]: https://colab.research.google.com/github/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/CycleGAN.ipynb#scrollTo=z1EySlOXwwoa
[29]: https://github.com/Ldpe2G/DeepLearningForFun/tree/master/Mxnet-Scala/CycleGAN
[30]: https://learning.oreilly.com/library/view/gans-in-action/9781617295560/OEBPS/Text/kindle_split_019_split_000.html
[31]: https://hardikbansal.github.io/CycleGANBlog/
[32]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/e32d5a1f-ed74-4535-8b83-d06560ce17a9.xhtml
[33]: https://learning.oreilly.com/library/view/pytorch-computer-vision/9781838644833/8be6fe30-e2d7-4901-ba08-a02c10606a0a.xhtml
[34]: https://thispersondoesnotexist.com/
[35]: https://arxiv.org/abs/1912.04958
[36]: https://learning.oreilly.com/library/view/the-deep-learning/9781839219856/B15385_07_Final_VK_ePub.xhtml#_idParaDest-232
[37]: https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ch17.html#idm46182870531912
[38]: https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/app01.html#solutions_appendix
[39]: https://learning.oreilly.com/library/view/intelligent-projects-using/9781788996921/f3bb58fe-be48-477a-bfbe-46732978d741.xhtml
[40]: https://learning.oreilly.com/library/view/intelligent-projects-using/9781788996921/89968ae6-5da7-4f1b-ae5f-74a6a6b5c63c.xhtml
[41]: https://affinelayer.com/pix2pix/
[42]: https://learning.oreilly.com/library/view/intelligent-mobile-projects/9781788834544/0992a92e-6f99-4057-8783-f165265b06a4.xhtml
[43]: https://pytorch.org/docs/stable/hub.html

```

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
