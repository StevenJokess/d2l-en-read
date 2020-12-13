

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 17:38:15
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 00:22:26
 * @Description:
 * @TODO::
 * @Reference:
-->

AttGAN利用分类损失和重构损失来保证改变特定的属性，可用于人脸特定属性转换。

AttGAN中生成网络的编码部分主要由convolution-instance norm-ReLU组成，解码部分由transpose convolution-norm-ReLU组成，判别网络主要由convolution-leaky_ReLU组成，详细网络结构可以查看network/AttGAN_network.py文件。生成网络的损失函数是由WGAN的损失函数，重构损失和分类损失组成，判别网络的损失函数由预测损失，分类损失和梯度惩罚损失组成。[2]

[1]: e,  Z.,  Zuo,  W.,  Kan,  M.,  Shan,  S.,  and  Chen,  X.  (2019).  AttGAN:Facial attribute editing by only changing what you want.IEEE Trans-actions on Image Processing, 28(11), 5464-5478.
[2]: https://github.com/PaddlePaddle/models/tree/develop/PaddleCV/gan
