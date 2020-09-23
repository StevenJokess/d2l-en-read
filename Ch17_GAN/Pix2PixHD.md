

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 22:53:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-23 23:05:53
 * @Description:
 * @TODO::
 * @Reference:
-->

The training of pix2pixHD is both time- and memory-consuming. It requires about 24 GB GPU memory to train 2,048x1,024 images. Therefore, we will only train on a 1,024x512 resolution in order to fit this on a single graphic card.


Use Automatic Mixed Precision (AMP) to reduce the GPU memory consumption (or even the training time) during training by replacing the standard floating-point values with lower bit floats.


NVIDIA has already open-sourced the full source code of pix2pixHD for PyTorch. All we need to do is download the source code and dataset to produce our own high resolution synthesized images. Let's do this now:


$ git clone https://github.com/NVIDIA/pix2pixHD

$V_{\text {pix} 2 \text {pixHD}}=\min _{G} \max _{D_{1}, D_{2}} \sum_{k=1,2} V\left(D_{k}, G\right)+\lambda \mathcal{L}_{F M}\left(D_{k}, G\right)$

## Generator

![Generator](img\Pix2PixHD.jpg)
Here, $\lambda \mathcal{L}_{F M}\left(D_{k}, G\right)$ measures the L1-loss between the feature maps of the generated and real images at multiple layers in the discriminator networks. It forces the generator to approximate the real data at different scales, thereby generating more realistic images.

## Reference


1. https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/08e23744-c7b4-4e95-b7fc-c57912bc0cf1.xhtml
2. https://github.com/NVIDIA/pix2pixHD

