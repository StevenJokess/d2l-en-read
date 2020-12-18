

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-28 21:15:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-18 19:21:50
 * @Description:
 * @TODO::
 * @Reference:[1]: https://github.com/PaddlePaddle/models/tree/develop/PaddleCV/gan
-->
实现StarGAN时使用了Wasserstein距离，即WGAN-GP。

StarGAN多领域属性迁移，引入辅助分类帮助单个判别器判断多个属性，可用于人脸属性转换。[1]

StarGAN中生成网络的编码部分主要由convolution-instance norm-ReLU组成，解码部分主要由transpose convolution-norm-ReLU组成，判别网络主要由convolution-leaky_ReLU组成，详细网络结构可以查看network/StarGAN_network.py文件。生成网络的损失函数是由WGAN的损失函数，重构损失和分类损失组成，判别网络的损失函数由预测损失，分类损失和梯度惩罚损失组成。

https://github.com/yunjey/stargan
