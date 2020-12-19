

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 01:22:43
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:23:01
 * @Description:
 * @TODO::
 * @Reference:https://github.com/anhtuan85/Generative-Adversarial-Networks-GANs-Specialization/blob/main/Course%202%20-%20Build%20Better%20Generative%20Adversarial%20Networks%20(GANs)/Week%203/BigGAN.ipynb
-->
# BigGAN-deep

Initially, the authors of the BigGAN paper didn't find much help in increasing the depth of the network. But they experimented further (research is always improving!) and added a few notes about an additional architecture, called BigGAN-deep. This modification of BigGAN is 4x deeper, sports a modified residual block architecture, and concatenates the entire $z$ vector to $c$ (as opposed to separate chunks at different resolutions).

Typically on a difficult and complex task that you're unlikely to overfit, you expect better performance when a model has more parameters, because it has more room to learn. Surprisingly, BigGAN-deep has fewer parameters than its BigGAN counterpart. Architectural optimizations such as using depthwise separable convolutions and truncating/concatenating channels in skip connections (as opposed to using pointwise convolutions) decrease parameters without trading expressivity.

For more details on the BigGAN-deep architecture, see Appendix B of the paper.

And as for the implementation of the BigGAN-deep variant, well, that's left as an exercise for the reader. You're a smart cookie, you'll figure it out! Just keep in mind that with great power comes great responsibility ;)
