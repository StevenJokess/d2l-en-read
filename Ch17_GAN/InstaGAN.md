

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 17:24:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 18:04:17
 * @Description:
 * @TODO::
 * @Reference:
-->

InstaGAN’s purpose is to transfigure instances of an object into another object.

The challenge is different than in CycleGAN as the objects are of different shape and size (e.g. sheep and giraffe). InstaGAN is based on CycleGAN but includes a few additional parts to support this transfiguration.





## Iterative training

Due to the fact that processing several instances simultaneously is memory inefficient, the authors suggest an iterative training. Each time a single mask is processed with the image to transfigure a single instance. The output image (and the masks summation) is then processed similarly with the next mask until all instances were transfigured. Not only that this technique more memory efficient, but it also creates data augmentation by using the intermediate images and masks.

## Context preserving loss

Finally, to incentivize the model to transfigure the instances but not the rest of the image, a new context preserving loss is added to the CycleGAN loss function. This loss punishes the model for changing background pixels, by summing the difference between the original and translated image but only in pixels that are outside of both masks (original and translated). The paper shows that the new loss preserves the background better and also improves the quality of the transfigured instance.


Though InstaGAN results are much better than CycleGAN, they are still less “recognizable” than real images of the same object.  [3]


[1]: https://arxiv.org/abs/1812.10889
[2]: https://github.com/sangwoomo/instagan/
[3]: https://www.lyrn.ai/2019/01/07/instagan-instance-aware-image-to-image-translation/
