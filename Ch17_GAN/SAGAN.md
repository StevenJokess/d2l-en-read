

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-26 21:41:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 21:48:29
 * @Description:
 * @TODO::
 * @Reference:
-->
Latest paper from Ian Goodfellow
Self-Attention Generative Adversarial Networks (SAGAN) (2018) [pdf] [PyTorch implementation]

https://github.com/heykeetae/Self-Attention-GAN

Both wgan-gp and wgan-hinge loss are ready, but note that wgan-gp is somehow not compatible with the spectral normalization. Remove all the spectral normalization at the model for the adoption of wgan-gp.

Self-attentions are applied to later two layers of both discriminator and generator.
