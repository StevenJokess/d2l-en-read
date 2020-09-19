

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 18:51:09
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 18:51:27
 * @Description:https://discuss.d2l.ai/t/image-classification-dataset/49
 * @TODO::
 * @Reference:
-->

batch size = 1, stochastic gradient descent (SGD)
batch size = 256, mini-batch gradient descent (MBGD)
Because using GPU to parallel read data, so MBGD is quicker.
Reducing the batch_size will make overall read performance slower.
:face_with_monocle:Does my guess right?
I’m a Windows user. Try it next time!
https://pytorch.org/docs/stable/torchvision/datasets.html
