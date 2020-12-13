

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 18:53:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-13 21:07:52
 * @Description:
 * @TODO::
 * @Reference:https://www.jianshu.com/p/844b4e417ad2
 * https://arxiv.org/abs/1612.08242
-->

# YOLO9000:Better, Faster, Stronger

yolov2相对于yolo来说的优势就是文章题目所说的，更好，更快，更强。下面来看看yolov2如何达到这个目的的。

一、如何更快
1. 使用BN
随着BN的提出，且在各种网络大量的引入，yolov2引入了BN（batch normalization）。文章还发现BN不仅改善了网络性能，还有一定的正则化的作用，因此文章移除了yolo中使用的dropout操作。

关于BN具体的计算，可以参考BN及其改进算法

2. 输入分辨率高
在yolov1的时候采用的是大小的图片来进行分类任务，大小的图片来进行检测任务。

文章认为直接切换为高分辨率，可能对网络性能有所伤害。yolov2在使用了大小的图片训练的分类网络中，再用大小的图片来训练10轮分类网络，之后用得到的网络来训练检测网络。

3. 引入anchor
借助fasterrcnn的思想，预测坐标的偏移量比直接预测坐标更容易学习，所以yolov2引入anchor的思想。

fasterrcn预测方式如下：


上式中，x，y是预测的框中心，、是anchor框的中心点坐标，、是anchor框的宽和高，，是网络的输出。

注意：这里与yolo9000原文不同的是，上式中是‘-’号，但是按照fasterrcnn的公式推导其实应该为‘+’，这样更好理解

fasterrcnn这种训练方式对于和没有约束，使得训练早期坐标不容易稳定。

所以yolov2的预测方式如下：





上式中，分别为预测参数，为归一化的预测框的中心坐标和长宽，是当前网格距离左上角的距离，该距离也为规划化后的距离，表示anchor的长宽，表示sigmoid函数。上述中的归一化指的是每个网格的长宽为1。这里可以看出因为加了sigmoid函数，使得预测出的始终为0-1的，就不容易造成训练早期的坐标不稳定了。

图1.png
在yolov1中，因为每个网格负责预测两个框，对于大小为大小的featuremap来说，yolov1只能预测出个预测框。但是引入anchor后，对于的featuremap来说，可以预测出个预测框（这里假定使用更大的分辨率图像作为输入，且anchor类型有9累）。所以引入anchor对于模型性能的提升，增大了优化的空间。(虽然引入anchor，使得文章的map下降了，但是召回升高了很多)

4. anchor的定义
yolov2中anchor定义不同于fasterrcnn是人工预设的比例和大小，文中通过k-means来聚类出k类anchor类，文章最终k=5。这里聚类时距离的度量值如下定义：

上式中centroid为聚类中心，box为其它待聚类的框，IOU为iou计算公式。可以看出IOU越大，两个框越近。

5. 细粒度的特征（Fine-Grained Features）
为了对小物体有更好的检测效果，文章想直接利用更为精细的特征来检测小物体，所以在进行最终的下采样之前，引入了passthrough的方法，该方法利用了下采样之前的特征是的对小物体的检测更为精确。
关于passthrough方法，网友给出的图非常详细，如下图所示：


图2.jpg
6. 多尺度训练
yolov1中对于检测任务采用的是来训练网络。yolov2为了适应多尺度的物体检测，网络的训练时采用多种图片尺寸，这些尺寸为32的倍数，有。训练过程中，每10个batches后随机选择这些尺度中的一个输入网络进行训练。

二、如何更快
文中提出了一个新的网络结构叫做Darknet-19，网络结构如下图所示。


图3.png
表中展示的是分1000类的网络结构。

对于检测任务，网络结构相对上述分类结构有所改动。

使用了三个输出通道为1024的卷积替代上表中最后的卷积操作（最后的卷积不是1000那个输出层，而是输出前那个1024层）
将最后的输出的feature接上述的passthrough结构，利用更精细的特征
对于输出，因为预测5种anchor的回归结果，且每个框分20类的概率，1类是否为正样本的概率和4个坐标回归参数共25个参数，每个anchor点需要预测125个值。
三、更强
文章的这部分主要是用来证明yolov2有较强的特征提取性能，采用了一些整理标签的方法，融合了COCO和Imagenet来做一些实验。

在Yolov2的loss计算中，每个cell有5个anchor，那么究竟该由哪个anchor来负责预测目标信息呢？答案是采用与GT(ground truth,也就是fmap尺度的box)IOU最大的anchor进行目标信息的预测。在计算时候，不考虑box的坐标位置。[4]


---

NMS[4]

第一个是“非极大值”，对于yolo来说，评估bbox是否可靠的的参数，就是它的置信度。所以这里的极大值指得是置信度。第二个关键词“抑制”，抑制是什么意思呢？表面上说，就是阻挡某个东西。

万一超过置信度阈值的框依旧很多呢？那不也是会导致满屏是框吗？？？(黑人问号表情包？？？)
那么我们还需要对这些高于置信度阈值的框做第二步操作，也就是合并操作。设置一个IOU阈值，假如两个框的交并比大于这个IOU阈值。我们就让它两合并。可以预见的是，这样合并着合并着，框就会变得很少了。

参考
https://arxiv.org/abs/1612.08242
https://zhuanlan.zhihu.com/p/47575929
https://zhuanlan.zhihu.com/p/35325884
[4]: https://blog.csdn.net/qq_36229876/article/details/105674765?utm_source=app
