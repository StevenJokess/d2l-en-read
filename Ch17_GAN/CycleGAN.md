

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-23 20:13:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-23 20:32:35
 * @Description:
 * @TODO::
 * @Reference:
[1]:https://junyanz.github.io/CycleGAN/
[2]:https://arxiv.org/pdf/1703.10593.pdf
[3]:http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/dcgan.html
-->

# Cycle-Consistent Generative Adversarial Networks

Now, we introduced the basic ideas behind how GAN/DCGAN work. We found than DCGAN can generate photorealistic images, like Pokemon.

In this section, we will demonstrate how you can use GANs to generate photorealistic videos. We will be basing our models on the Cycle-Consistent Generative Adversarial Networks (CycleGAN) introduced in [1]. We will TODO:? , they can be leveraged to photorealistic videos.

## The ? Dataset

The dataset we will use is a collection of Pokemon sprites obtained from TODO: ?
First download, extract and load this dataset.

We resize each videos into  64×64 . The ToTensor transformation will project the pixel value into  [0,1] , while our generator will use the tanh function to obtain outputs in  [−1,1] . Therefore we normalize the data with  0.5  mean and  0.5  standard deviation to match the value range.

TODO:

Let us visualize the first 20 videos.

TODO:

## The Generator





Image-to-image translation




Compared to the basic GAN in Section 17.1, we use the same learning rate for both generator and discriminator since they are similar to each other. In addition, we change  β1  in Adam (Section 11.10) from  0.9  to  0.5 . It decreases the smoothness of the momentum, the exponentially weighted moving average of past gradients, to take care of the rapid changing gradients because the generator and the discriminator fight with each other. Besides, the random generated noise Z, is a 4-D tensor and we are using GPU to accelerate the computation.

We train the model with a small number of epochs just for demonstration. For better performance, the variable num_epochs can be set to a larger number.



## Summary




## Reference

[1]:https://junyanz.github.io/CycleGAN/
