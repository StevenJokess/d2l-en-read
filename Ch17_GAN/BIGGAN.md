

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:22:07
 * @Description:
 * @TODO::
 * @Reference:
-->

在 SAGAN 的基础上，BigGAN [2]尝试将 GAN 的训练扩展到大规模上去，利用正交 正则化等技巧保证训练过程的稳定性。BigGAN 的意义在于启发人们，GAN 网络的训练同 样可以从大数据、大算力等方面受益。BigGAN 图片生成效果达到了前所未有的高度： Inception score 记录提升到 166.5(提高了 52.52)；Frechet Inception Distance 下降到 7.4，降 低了 18.65，如图 13.13 所示，图片的分辨率可达512 × 512，图片细节极其逼真。

网络已经学会了如何表示其训练的图片的许多关键特征，如动物身体的结构、草的纹理以及光影的细节效果（即使是通过肥皂泡折射的）。但仔细观察下面这些图，就不免能发现些许小异常，如白狗明显多了条腿，喷泉其中一个喷嘴的水流呈奇怪的直角状。虽然生成式模型的开发者在努力避免这种不完美，但这些可见的不完美也突显了重建熟悉的数据（如图像）的一个好处，即研究人员可以通过检查样本，推断出模型学到了什么以及没有学到什么。[1]



[1]: https://www.leiphone.com/news/201904/LhyoY2oy3cC5MzII.html
[2]: https://github.com/huggingface/pytorch-pretrained-BigGAN
[3]: https://github.com/anhtuan85/Generative-Adversarial-Networks-GANs-Specialization/blob/main/Course%202%20-%20Build%20Better%20Generative%20Adversarial%20Networks%20(GANs)/Week%203/BigGAN.ipynb

