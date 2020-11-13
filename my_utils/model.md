

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 18:42:58
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 18:55:05
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/hub/
 * https://pytorch.org/hub/facebookresearch_pytorch-gan-zoo_dcgan/
 * https://github.com/facebookresearch/pytorch_GAN_zoo
-->
LOADING MODELS
Users can load pre-trained models using torch.hub.load() API.
Here’s an example showing how to load the resnet18 entrypoint from the pytorch/vision repo.

model = torch.hub.load('pytorch/vision', 'resnet18', pretrained=True)

---

(beta) StyleGAN
To run StyleGAN, use the model name StyleGAN when running train.py. Besides,to run StyleGAN you can use the pre-computed configurations for celeba and celebaHQ. For example:

python train.py StyleGAN -c config_celebaHQ.json --restart -n style_gan_celeba

If you want to train your own DCGAN and other GANs from scratch, have a look at [PyTorch GAN Zoo](https://github.com/facebookresearch/pytorch_GAN_zoo).

---

While image classification models have recently continued to advance, most downstream applications such as object detection and semantic segmentation still employ ResNet variants as the backbone network due to their simple and modular structure. We present a simple and modular Split-Attention block that enables attention across feature-map groups. By stacking these Split-Attention blocks ResNet-style, we obtain a new ResNet variant which we call ResNeSt. Our network preserves the overall ResNet structure to be used in downstream tasks straightforwardly without introducing additional computational costs. ResNeSt models outperform other networks with similar model complexities, and also help downstream tasks including object detection, instance segmentation and semantic segmentation.

