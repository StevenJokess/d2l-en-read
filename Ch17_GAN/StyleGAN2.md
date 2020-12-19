

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 16:36:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:34:27
 * @Description:
 * @TODO::
 * @Reference:
-->

Analyzing and Improving the Image Quality of StyleGAN

https://github.com/NVlabs/stylegan2

路径长度正规化。“感知路径长度”(或PPL，你可以在另一个可选的笔记本中探索)在StyleGAN最初的论文中被引入，作为测量中间噪声空间w的解扰度的度量。PPL测量在中间噪声向量之间插值时输出图像的变化。你会期望一个好的模型在插值过程中有一个平滑的过渡，其中相同的步长映射到结果图像中相同数量的感知变化。

使用这种直觉，您可以使空间到图像的映射更平滑，通过鼓励给定的变化来对应图像的恒定量的变化。这被称为路径长度正则化，正如你所期望的，包括在损失函数中的一个项。这种平滑性也使得生成器模型“非常容易反相”!回想一下，反转意味着从真实或虚假的图像中找到它，所以你可以通过控制轻松地调整图像的风格。

没有Progressive Growing。虽然渐进式增长看似有助于在升级到更高分辨率之前，在较低分辨率下更有效、更稳定地训练网络，但实际上还有一种更好的方法。相反,你可以把它换成1)更好的神经网络架构和跳过剩余连接(你也看到课程3模型,Pix2Pix和CycleGAN),和2)训练的决议,但逐渐发生器的注意力从低到高分辨率的维度。所以在某种程度上，仍然非常小心地处理不同的决议，使训练eaiser从低到高。[3]


[1]: Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen, and Timo Aila. Analyzing and improving the image quality of stylegan. arXiv preprint arXiv:1912.04958, 2019.
[2]: http://arxiv.org/abs/1912.04958
[3]: https://github.com/anhtuan85/Generative-Adversarial-Networks-GANs-Specialization/blob/main/Course%202%20-%20Build%20Better%20Generative%20Adversarial%20Networks%20(GANs)/Week%203/StyleGAN2.ipynb
