

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 16:46:38
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 16:47:39
 * @Description:
 * @TODO::
 * @Reference:https://arxiv.org/abs/1903.11250
-->
# Auto-Embedding Generative Adversarial Network

论文提出了一种自动嵌入的生成对抗网络（AEGAN），能够在编码全局结构特征的同时捕获细粒度的细节。论文采用了自动编码器去学习真实图像固有的high-level结构，并设计了一个去噪网络为所生成的图像提供照片般逼真的细节。在实验中，所提出的方法能够从输入的随机噪声中生成512*512分辨率的高质量图像。所生成的图像比众多数据集的baselines具有更sharp的结构和更丰富的细节。
