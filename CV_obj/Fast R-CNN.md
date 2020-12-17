

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 18:52:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 18:17:09
 * @Description:
 * @TODO::
 * @Reference:
-->

## FasterRCNN

Faster-RCNN可以采用多种的主干特征提取网络，常用的有VGG，Resnet，Xception等等，本文以Resnet网络为例子来给大家演示一下。

Faster-Rcnn对输入进来的图片尺寸没有固定，但是一般会把输入进来的图片短边固定成600，如输入一张1200x1800的图片，会把图片不失真的resize到600x900上。

ResNet50有两个基本的块，分别名为Conv Block和Identity Block，其中Conv Block输入和输出的维度是不一样的，所以不能连续串联，它的作用是改变网络的维度；Identity Block输入维度和输出维度相同，可以串联，用于加深网络的。

文章《Fast R-CNN》，是在SPP-net的基础上对R-CNN的再次改造。 关于R-CNN的细节请查看R-CNN文章详细解读，关于SPP-net的细节请查看SPP-net文章详细解读[1]

FasterRCNN是Two-Stage目标检测算法的杰出代表，其蕴含的思想在如今许多网络中都得以体现。
与SSD、YOLOV3这些One-Stage目标检测算法相比，它有一点复杂，但是检测效果很好。[2]





[1]: https://www.zhuanzhi.ai/document/980e4f5b28e5284e8d30ea888f75a3ea
[2]: https://www.bilibili.com/video/BV1BK41157Vs
[3]: https://github.com/bubbliiiing/faster-rcnn-pytorch
