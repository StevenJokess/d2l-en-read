

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 22:12:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 22:12:36
 * @Description:
 * @TODO::
 * @Reference:https://github.com/ypwhs/deeplearning-models/blob/master/pytorch_ipynb/gan/dc-wgan-1.ipynb
-->
from torchsummary import summary
model = model.to('cuda:0')
summary(model.generator, input_size=(100,))
summary(model.discriminator, input_size=(1, 28, 28))
