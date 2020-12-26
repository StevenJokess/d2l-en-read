

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-26 18:24:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 18:25:19
 * @Description:
 * @TODO::
 * @Reference:https://www.toutiao.com/a6599505914636534280/?tt_from=mobile_qq&utm_campaign=client_share&timestamp=1536578339&app=news_article&utm_source=mobile_qq&iid=43288484319&utm_medium=toutiao_android&group_id=6599505914636534280
-->

GAN Lab 的一大用途是利用其可视化来了解生成器如何增量更新，从而改进自身，生成越来越逼真的假样本。生成器通过愚弄判别器来实现这一点。在判别器将假样本分类为真实样本时，生成器的损失值下降（对判别器不利，对生成器有利）。GAN Lab 将假样本的梯度可视化（粉色线），以促成生成器的成功。


GAN Lab 使用浏览器内 GPU 加速的深度学习库 TensorFlow.js 来实现。从模型训练到可视化，所有的一切都通过 JavaScript 实现。你只需要一个网页浏览器（如 Chrome），即可运行 GAN Lab。这一实现方法极大地拓宽了人们使用深度学习交互工具的渠道。

源代码链接：https://github.com/poloclub/ganlab

论文：GAN Lab: Understanding Complex Deep Generative Models using Interactive Visual Experimentation

谷歌带来GAN入门神器：浏览器上运行的可视化工具GAN Lab
论文地址：https://arxiv.org/abs/1809.01587v1

本文提出了 GAN Lab，这是第一个为非专业人士学习、试验生成对抗网络（一种流行的复杂深度学习模型）而设计的交互式视觉工具。用户可以利用 GAN Lab 交互地训练生成模型，并可视化动态训练过程的中间结果。GAN Lab 紧密集成了总结 GAN 结构的模型概述图（model overview graph）和帮助用户解释子模型之间相互作用的分层分布视图（layered distributions view）
