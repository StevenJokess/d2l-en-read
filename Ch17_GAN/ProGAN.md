

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:08:40
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 18:33:06
 * @Description:
 * @TODO::
 * @Reference:
-->

# ProGAN

The key innovation of ProGAN is the progressive training – it starts by training the generator and the discriminator with a very low resolution image (e.g. 4×4) and adds a higher resolution layer every time.

ProGAN generates high-quality images but, as in most models, its ability to control specific features of the generated image is very limited. In other words, the features are entangled and therefore attempting to tweak the input, even a bit, usually affects multiple features at the same time. A good analogy for that would be genes, in which changing a single gene might affect multiple traits.


However, DCGAN used transpose convolutions to change the representation size. In constrast, ProGAN uses nearest neighbors for upscaling and average pooling for downscaling. These are simple operations with no learned parameters. They are then followed by two convolutional layers.[2]

## Generator




## Discriminator






A detailed view of the discriminator architecture, when it has “grown” to resolution k. Here, x is the input image (either generated or from the training set), α is the extent to which the last generator layer is “faded in”, and D(x) is the probability the generator has assigned to x being from the training set. The representation size is halved at each set of layers by an average pooling operation.

## Loss Function




[1]: https://arxiv.org/abs/1710.10196 Progressive Growing of GANs For Improved Quality, Stability, and and Variation.
[2]: https://towardsdatascience.com/progan-how-nvidia-generated-images-of-unprecedented-quality-51c98ec2cbd2
