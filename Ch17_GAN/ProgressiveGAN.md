

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 01:48:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 21:15:18
 * @Description:
 * @TODO::
 * @Reference:
-->

allowing generation of high resolution images. To do so, the generative network is trained slice by slice. At first the model is trained to build very low resolution images, once it converges, new layers are added and the output resolution doubles. The process continues until the desired resolution is reached.




[1]: T. Karras,  T. Aila,  S. Laine,  and J. Lehtinen.   Progressive growing of GANs for improved quality, stability, and varia-tion.CoRR, abs/1710.10196, 2017. 1, 2, 7, 8, 9
[2]: https://pytorch.org/hub/facebookresearch_pytorch-gan-zoo_pgan/