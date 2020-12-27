

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 01:48:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 18:37:14
 * @Description:
 * @TODO::
 * @Reference:
-->

allowing generation of high resolution images. To do so, the generative network is trained slice by slice. At first the model is trained to build very low resolution images, once it converges, new layers are added and the output resolution doubles. The process continues until the desired resolution is reached.

2018年，Progressive GAN（PGAN）的出现，生成令人震撼地1024X1024人脸图像。事实上，到现在很多论文也是在128X128和256X256的图像大小上进行搞事情，因为再大，就南了，或者就崩了。[4]


we describe several implementation details that are important for discouraging unhealthy competition between the generator and discriminator.

[1]: T. Karras,  T. Aila,  S. Laine,  and J. Lehtinen.   Progressive growing of GANs for improved quality, stability, and varia-tion.CoRR, abs/1710.10196, 2017. 1, 2, 7, 8, 9
[2]: https://pytorch.org/hub/facebookresearch_pytorch-gan-zoo_pgan/
[3]: https://github.com/tkarras/progressive_growing_of_gans
[4]: https://zhuanlan.zhihu.com/p/94206978
