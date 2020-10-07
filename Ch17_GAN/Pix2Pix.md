

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 22:36:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-07 23:00:12
 * @Description:
 * @TODO::
 * @Reference:
-->

# Pix2Pix

## Abstract

CGAN在图像翻译任务(DIP)、图像合成、图像上色。表明在不手工设计损失函数的情况下，也能获得理想的结果。[6]

IQA

像素损失（MSE->PSNR）;

## 数据集

CMP Facade Database
    由捷克理工大学的机器感知中心(CMP)发布,包含606张建筑正面的校正图像,来自世界各地的不同城市,包含12类语义分割标注
    http://cmp.felk.cvut.cz/-tylecr1/facade/

Paris streetview Dataset
    由牛津大学发布,包含6412张从 Flickr上下载的包含巴黎标志性建筑的街景图像
    http://www.robots.ox.ac.uk/-vgg/data/parisbuildings/

Cityscapes Dataset
    由德国三个研究机构联合发布的城市景观数据集,拥有5000张带语义理解标注的城市街景图像
    https://www.cityscapes-dataset.com


## code

$ git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git


Then, install the prerequisites to be able to visualize the results during training:

$ pip install dominate visdom


The Image-to-Image Translation with Conditional Adversarial Networks (known as Pix2Pix, https://arxiv.org/abs/1611.07004) paper from the same team also does image-to-image translation for paired training data.

tf code:
https://github.com/affinelayer/pix2pix-tensorflow

![encode-decode](img\encode-decode.png)[4]

### The Generator

The Generator has the job of taking an input image and performing the transform we want in order to produce the target image. An example input would be a black and white image, and we want the output to be a colorized version of that image. The structure of the generator is called an "encoder-decoder" and in pix2pix the encoder-decoder looks more or less like this:


![Generator architecture](img\Pix2Pix_generator.jpg)[1]


### The Discriminator

The Discriminator has the job of taking two images, an input image and an unknown image (which will be either a target or output image from the generator), and deciding if the second image was produced by the generator or not.

![Discriminator architecture](img\Pix2Pix_discri.jpg)[1]

The discriminator network creates a 30x30 feature map to represent the loss. This kind of architecture is called PatchGAN, which means that every small image patch in the original image is mapped to a pixel in the final loss map. A big advantage of PatchGAN is that it can handle the arbitrary sizes of input images as long as the labels have been transformed so that they're the same size as the loss map. It also evaluates the quality of the input image according to the quality of the local patches, rather than their global property. Here, we will show you how the size of the image patch (that is, 70) is calculated.[1]

### Training

![train](img\Pix2Pix_train.jpg)[2]

Note that, when training pix2pix, in order to let the generated samples be as similar to the real ones as possible, an additional term is added to the loss function when training the generator network, as follows:[2]

$$V_{\text {pix} 2 \text {pix}}=\min _{G} \max _{D} V(D, G)+\lambda \mathcal{L}_{L 1}(G)$$

Here, $\mathcal{L}_{L 1}(G)$ represents the L1-loss between the generated samples and the real ones from the paired collection. The purpose of the L1-loss is to reserve the low-frequency information in the images for better image quality.[2]

MXNet code[3]

## Reference


[1]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/8d5574ec-aa41-42d3-a92d-d549488d32a9.xhtml
[2]: https://learning.oreilly.com/library/view/hands-on-generative-adversarial/9781789530513/05e25d65-5beb-412b-9b38-d99516eccbf0.xhtml
[3]: https://github.com/Ldpe2G/DeepLearningForFun/tree/master/Mxnet-Scala/Pix2Pix
[4]: https://affinelayer.com/pix2pix/
[5]: https://github.com/yenchenlin/pix2pix-tensorflow
[6]: https://ai.deepshare.net/detail/v_5f44d9dce4b0118787333e00/3?from=p_5f4c7402e4b0dd4d974c43e4&type=6
