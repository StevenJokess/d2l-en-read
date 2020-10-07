

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-25 18:38:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-07 19:03:18
 * @Description:
 * @TODO::
 * @Reference:
-->

# StyleGAN

StyleGAN is a type of generative adversarial network. It uses an alternative generator architecture for generative adversarial networks, borrowing from style transfer literature; in particular, the use of adaptive instance normalization. Otherwise it follows Progressive GAN in using a progressively growing training regime. Other quirks include the fact it generates from a fixed value tensor not stochastically generated latent variables as in regular GANs. The stochastically generated latent variables are used as style vectors in the adaptive instance normalization at each resolution after being transformed by an 8-layer feedforward network. Lastly, it employs a form of regularization called mixing regularization, which mixes two style latent variables during training.[8]

The new architecture leads to an automatically learned, unsupervised separation of high-level attributes (e.g., pose and identity when trained on human faces) and stochastic variation in the generated images (e.g., freckles, hair), and it enables intuitive, scale-specific control of the synthesis. The new generator improves the state-of-the-art in terms of traditional distribution quality metrics, leads to demonstrably better interpolation properties, and also better disentangles the latent factors of variation.[4]

##






2018/12
![（a）无条件GAN和（b）有条件GAN的流程图。](img\StyleGAN.md)[7]

[1]: https://www.bilibili.com/video/BV1ot4y197MG
[2]: https://medium.com/swlh/hairstyle-transfer-semantic-editing-gan-latent-code-b3a6ccf91e82
[3]: https://github.com/Azmarie/Hairstyle-Transfer
[4]: https://arxiv.org/abs/1812.04948
[5]: https://twitter.com/dl_from_scratch/status/1308266572503367680
[6]: https://paperswithcode.com/paper/analyzing-and-improving-the-image-quality-of
[7]: https://syncedreview.com/2019/08/29/ai-creates-fashion-models-with-custom-outfits-and-poses/
[8]: https://paperswithcode.com/method/stylegan
[9]:
