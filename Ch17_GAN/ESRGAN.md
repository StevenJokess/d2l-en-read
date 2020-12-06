

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 20:15:19
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 20:18:19
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch09.html#idm45762347307368s
-->
ESRGAN
The Enhanced Super-Resolution Generative Adversarial Network (ESRGAN) is a network developed in 2018 that produces impressive super-resolution results. The generator is a series of convolutional network blocks with a combination of residual and dense layer connections (so a mixture of both ResNet and DenseNet), with BatchNorm layers removed as they appear to create artifacts in upsampled images. For the discriminator, instead of simply producing a result that says this is real or this is fake, it predicts a probability that a real image is relatively more realistic than a fake one, and this helps to make the model produce more natural results.

RUNNING ESRGAN
To show off ESRGAN, we’re going to download the code from the GitHub repository. Clone that using git:

git clone https://github.com/xinntao/ESRGAN
We then need to download the weights so we can use the model without training. Using the Google Drive link in the README, download the RRDB_ESRGAN_x4.pth file and place it in ./models. We’re going to upsample a scaled-down version of Helvetica in her box, but feel free to place any image into the ./LR directory. Run the supplied test.py script and you’ll see upsampled images being generated and saved into the results directory.

That wraps it up for super-resolution, but we haven’t quite finished with images yet.
