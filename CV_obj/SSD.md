

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:54:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:03:08
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/102646387
 * https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Object-Detection#single-shot-detector-ssd
-->

## SSD


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
