

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:54:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 21:02:21
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/102646387
 * https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Object-Detection#single-shot-detector-ssd
 * http://www.tensorinfinity.com/paper_25.html
-->

## SSD

SSD对YOLO进行了改进，达到了和两阶段方法相当的精度，同时又保持了较快的运行速度。SSD也采用了网格划分的思想，和Faster RCNN不同的是它将所有的操作整合在一个卷积网络中完成。为了检测不同尺度的目标，SSD对不同卷积层的特征图像进行滑窗扫描；在前面的卷积层输出的特征图像中检测小的目标，在后面的卷积层输出的特征图像中检测大的目标。它的主要特点是：

1.基于多尺度特征图像的检测：在多个尺度的卷积特征图上进行预测，以检测不同大小的目标，一定程度上提升了小目标物体的检测精度。

2.借鉴了Faster R-CNN中的Anchor boxes思想，在不同尺度的特征图上采样候选区域，一定程度上提升了检测的召回率以及小目标的检测效果。下图是SSD的原理：



对于ssd网络我专门写了两篇blog用于描述其训练过程和预测过程，大家可以看一下SSD算法预测部分；SSD算法预测部分。
SSD其实也是一个多特征层网络，其一共具有11层，前半部分结构是VGG16。
其网络结构如下：
1、首先通过了多个3X3卷积层、5次步长为2的最大池化取出特征，形成了5个Block，其中第四个Block的shape为(?,38,38,512)，该层用于提取小目标（多次卷积后大目标的特征保存的更好，小目标特征会消失，需要在比较靠前的层提取小目标特征）。
2、进行一次卷积核膨胀dilate（关于卷积核膨胀的概念可以去网上搜索以下哈）。
3、读取第七个Block7的特征，shape为(?,19,19,1024)
4、分别利用1x1和3x3卷积提取特征，在3x3卷积的时候使用步长2，缩小特征数。获取第八个Block8的特征，shape为(?,10,10,512)
5、重复步骤4，获得9、10、11卷积层的特征，shape分别为(?,5,5,256)、(?,3,3,256)、(?,1,1,256)


SSD同样采用多特征层的思想，但是其网络结构相比于yolo3更加简单，其利用VGG16进行特征提取，同样具有比较优秀的效果。

---

Single Shot Detector (SSD)
The SSD is a purely convolutional neural network (CNN) that we can organize into three parts –

Base convolutions derived from an existing image classification architecture that will provide lower-level feature maps.

Auxiliary convolutions added on top of the base network that will provide higher-level feature maps.

Prediction convolutions that will locate and identify objects in these feature maps.

The paper demonstrates two variants of the model called the SSD300 and the SSD512. The suffixes represent the size of the input image. Although the two networks differ slightly in the way they are constructed, they are in principle the same. The SSD512 is just a larger network and results in marginally better performance.

For convenience, we will deal with the SSD300.

https://github.com/anhtuan85/Pytorch-SSD-from-scratch
