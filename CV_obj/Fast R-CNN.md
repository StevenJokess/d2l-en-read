

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 18:52:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 20:26:41
 * @Description:
 * @TODO::
 * @Reference:
-->

## FasterRCNN

## 简介

​ Fast R-CNN是基于R-CNN和SPPnets进行的改进。SPPnets，其创新点在于计算整幅图像的the shared feature map，然后根据object proposal在shared feature map上映射到对应的feature vector（就是不用重复计算feature map了）。当然，SPPnets也有缺点：和R-CNN一样，训练是多阶段（multiple-stage pipeline）的，速度还是不够"快"，特征还要保存到本地磁盘中。

将候选区域直接应用于特征图，并使用RoI池化将其转化为固定大小的特征图块。以下是Fast R-CNN的流程图

## 创新点

1. 只对整幅图像进行一次特征提取，避免R-CNN中的冗余特征提取
1. 用RoI pooling层替换最后一层的max pooling层，同时引入建议框数据，提取相应建议框特征
1. Fast R-CNN网络末尾采用并行的不同的全连接层，可同时输出分类结果和窗口回归结果，实现了end-to-end的多任务训练【建议框提取除外】，也不需要额外的特征存储空间【R-CNN中的特征需要保持到本地，来供SVM和Bounding-box regression进行训练】
1. 采用SVD对Fast R-CNN网络末尾并行的全连接层进行分解，减少计算复杂度，加快检测速度。



Faster-RCNN可以采用多种的主干特征提取网络，常用的有VGG，Resnet，Xception等等，本文以Resnet网络为例子来给大家演示一下。

Faster-Rcnn对输入进来的图片尺寸没有固定，但是一般会把输入进来的图片短边固定成600，如输入一张1200x1800的图片，会把图片不失真的resize到600x900上。

ResNet50有两个基本的块，分别名为Conv Block和Identity Block，其中Conv Block输入和输出的维度是不一样的，所以不能连续串联，它的作用是改变网络的维度；Identity Block输入维度和输出维度相同，可以串联，用于加深网络的。

文章《Fast R-CNN》，是在SPP-net的基础上对R-CNN的再次改造。 关于R-CNN的细节请查看R-CNN文章详细解读，关于SPP-net的细节请查看SPP-net文章详细解读[1]

FasterRCNN是Two-Stage目标检测算法的杰出代表，其蕴含的思想在如今许多网络中都得以体现。
与SSD、YOLOV3这些One-Stage目标检测算法相比，它有一点复杂，但是检测效果很好。[2]





[1]: https://www.zhuanzhi.ai/document/980e4f5b28e5284e8d30ea888f75a3ea
[2]: https://www.bilibili.com/video/BV1BK41157Vs
[3]: https://github.com/bubbliiiing/faster-rcnn-pytorch
[4]: https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch08_%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/%E7%AC%AC%E5%85%AB%E7%AB%A0_%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B.md
