

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:08:40
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 17:10:32
 * @Description:
 * @TODO::
 * @Reference:
-->

# ProGAN

The key innovation of ProGAN is the progressive training – it starts by training the generator and the discriminator with a very low resolution image (e.g. 4×4) and adds a higher resolution layer every time.

ProGAN generates high-quality images but, as in most models, its ability to control specific features of the generated image is very limited. In other words, the features are entangled and therefore attempting to tweak the input, even a bit, usually affects multiple features at the same time. A good analogy for that would be genes, in which changing a single gene might affect multiple traits.



[1]: https://arxiv.org/abs/1710.10196
[2]:
