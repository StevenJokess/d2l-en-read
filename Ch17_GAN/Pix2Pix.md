

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 22:36:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-23 22:52:22
 * @Description:
 * @TODO::
 * @Reference:
-->


$ git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
Then, install the prerequisites to be able to visualize the results during training:

$ pip install dominate visdom


The Image-to-Image Translation with Conditional Adversarial Networks (known as Pix2Pix, https://arxiv.org/abs/1611.07004) paper from the same team also does image-to-image translation for paired training data.

### The Generator

![Generator architecture](img\Pix2Pix_generator.jpg)[1]


### The Discriminator

![Discriminator architecture](img\Pix2Pix_discri.jpg)[1]

The discriminator network creates a 30x30 feature map to represent the loss. This kind of architecture is called PatchGAN, which means that every small image patch in the original image is mapped to a pixel in the final loss map. A big advantage of PatchGAN is that it can handle the arbitrary sizes of input images as long as the labels have been transformed so that they're the same size as the loss map. It also evaluates the quality of the input image according to the quality of the local patches, rather than their global property. Here, we will show you how the size of the image patch (that is, 70) is calculated.[1]

### Training

![train](img\Pix2Pix_train.jpg)[2]

Note that, when training pix2pix, in order to let the generated samples be as similar to the real ones as possible, an additional term is added to the loss function when training the generator network, as follows:[2]

$$V_{\text {pix} 2 \text {pix}}=\min _{G} \max _{D} V(D, G)+\lambda \mathcal{L}_{L 1}(G)$$

Here, $\mathcal{L}_{L 1}(G)$ represents the L1-loss between the generated samples and the real ones from the paired collection. The purpose of the L1-loss is to reserve the low-frequency information in the images for better image quality.[2]


[1]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/8d5574ec-aa41-42d3-a92d-d549488d32a9.xhtml
[2]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/05e25d65-5beb-412b-9b38-d99516eccbf0.xhtml
