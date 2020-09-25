

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 22:53:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-25 20:47:16
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

More recent work named pix2pixHD [32] generates Image high-resolution images from semantic label maps using the pix2pix framework. They improved the pix2pix framework by using a coarse-to-fine generator, a multiscale discriminator architecture, and a robust adversarial learning objective function. The generator G consists of two sub-networks Image, where Image generates Image images and Image generates Image images using the outputs of Image. Multiscale discriminators Image, who have an identical network structure but operate at different image scales, are used in a multitask learning setting. The objective of pix2pixHD is

$\min _{G}\left(\left(\max _{D_{1}, D_{2}, D_{3}} \sum_{k=1,2,3} \mathcal{L}_{\mathrm{cGAN}}\left(G, D_{k}\right)\right)+\lambda \sum_{k=1,2,3} \mathcal{L}_{\mathrm{FM}}\left(G, D_{k}\right)\right)$

Image(2.22)

where Image represents the newly proposed feature matching loss, which is the summation of Image distance between the discriminator's ith-layer outputs of the real and the synthesized images.[3]


## Reference

```md
[1]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/08e23744-c7b4-4e95-b7fc-c57912bc0cf1.xhtml
[2]: https://github.com/NVIDIA/pix2pixHD
[3]: https://learning.oreilly.com/library/view/multimodal-scene-understanding/9780128173596/B9780128173589000081.xhtml#st0075
[4]: T.-C. Wang, M.-Y. Liu, J.-Y. Zhu, A. Tao, J. Kautz, B. Catanzaro, High-resolution image synthesis and semantic manipulation with conditional gans, Proceedings of IEEE Conference on Computer Vision and Pattern Recognition. CVPR. 2018.

```
