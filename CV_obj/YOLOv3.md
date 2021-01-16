

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 19:19:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 19:38:25
 * @Description:
 * @TODO::
 * @Reference:https://pjreddie.com/darknet/yolo/
 * https://www.jianshu.com/p/d5b65e89d4c8
 * https://arxiv.org/abs/1804.02767
-->

YOLO: Real-Time Object Detection
You only look once (YOLO) is a state-of-the-art, real-time object detection system. On a Pascal Titan X it processes images at 30 FPS and has a mAP of 57.9% on COCO test-dev.


Comparison to Other Detectors
YOLOv3 is extremely fast and accurate. In mAP measured at .5 IOU YOLOv3 is on par with Focal Loss but about 4x faster. Moreover, you can easily tradeoff between speed and accuracy simply by changing the size of the model, no retraining required!

## 相较于前两版的改进点：[6]

1、提出了darknet53，由于加深了网络，应用resnet的思想，添加了residual block，降低了梯度消失的风险。不再使用pooling层，而是用步长为2的卷积层代替，避免了信息丢失，想进一步了解的同学可以拜读一下这篇文章Springenberg J T, Dosovitskiy A, Brox T, et al. Striving for simplicity: The all convolutional net[J]. arXiv preprint arXiv:1412.6806, 2014.。



2、在检测部分，作者参考了FPN（feature pyramid networks）的思想。用非线性插值方法上采样了两次，获得了3个不同大小的feature maps。和v2相似，作者依然对ground truth 框的大小进行了聚类，不同的是，v3获得的9个尺度的anchor boxes。每个feature map分配3个尺度的anchor boxes。由于深层、语义特征丰富的负责预测大物体（分配大anchor）；浅层、几何特征丰富的负责预测小物体（分配小anchor）。这次不仅框多了，而且更细致了，对检测小物体放了大招，所以就目前来说这种策略对检测小物体已经做到头了，想要再改进，可能要换思路了，如果一味地增大输入尺寸显然是不合理的。



3、用Sigmoid代替Softmax，这个改进主要是用于多标签分类。Softmax输出的结果有互斥性，只能预测一类，而如果一个物体有多个标签（如：人和女人），那么Softmax是做不到的。但是在真实的检测场景中存在这样的情况，所以作者使用了Sigmoid函数替代。

# YOLOv3: An Incremental
按照原文的说法，它其实是一篇技术试验的报告。本文通过一些试验来改进yolo方法。

## 检测框的预测
这部分的预测和yolov2是一样的，详情可以参考yolov2算法详解。

## 类别预测
文章采用的是多标签的分类方法，文章认为softmax对于好的预测结果的获取不一定是有帮助的。训练的时候类别的loss采用的是binary cross-entropy loss。

## 多尺度框的预测
对于多尺度框的预测类似于有FPN结构的fastrcnn，不同的feature大小负责不同大小的框的检测。为了更好的解释，先看看yolov3的网络结构


1
上面为yolov3新提出的网络用于分类任务，网络中采用了resnet提出的残差结构，并且使用了53层卷积，所以网络称为Darknet-53。不同于分类任务，检测任务需要多尺度的特征来检测不同尺度的物体，所以需要采用FPN的结构，具体网络结构图如下，下图中图片输入大小为416，通道顺序为(N,C,H,W)，每个方块中的括号里的维度代表该方块的输出feature维度，标红的框为最终的输出


yolov3.jpg
可以看到类似FPN结构有三层的输出，这里每一层有3类的anchor，三层总共为9类，而这9类anchor的设定是使用yolov2提出的kmeans聚类选出来的，不同数据集不一样，对于COCO数据集来说为这9类尺度。

需要说明的是，上图中输出的通道是255，这个数字是针对COCO数据集有80类来举例的，具体的就是[3 * (4 + 1 + 80)] = 255，3表示3类anchor，4表示预测的框，1表示框的置信度，80表示类别置信度

## 未奏效的尝试
采用frcnn的方式预测x,y的偏移量，发现效果不好
采用线性激活而不是代替logistic激活，效果不好
采用focal loss，效果不好，至于为什么作者猜测可能yolo将类别和框置信度分开对focal loss需要解决的问题已经有一定的鲁棒性了，具体原因作者也不是很确定
尝试采用frcnn来定义正负样本，即anchor iou与标定框小于0.3的为负样本，大于0.7的为正样本，在[0.3, 0.7]范围的忽略，效果不太好
上述1,2点可以参考yolov2算法详解, 第3点参考Focal Loss for Dense Object Detection论文详解，第4点参考Faster R-CNN文章详细解读

YOLO 目标检测算法。图源：https://arxiv.org/pdf/1506.02640.pdf。

Faster R-CNN 及在其基础上改进的 Mask R-CNN 在实例分割、目标检测、人体关键点检测等任务上都取得了很好的效果，但通常较慢。而 YOLO 的创新之处在于，它提出了 one-stage，即目标定位和目标识别在一个步骤中完成，是名副其实的「You Only Look Once」。

由于 YOLO 只使用单个网络，因此可以直接在检测性能上进行端到端优化，使得基础 YOLO 模型能以每秒 45 帧的速度实时处理图像。YOLO 的一个小规模版本——Fast YOLO 可以达到每秒 155 帧的处理速度。

YOLO 有着让人惊艳的速度，同时也有让人止步的缺陷：不擅长小目标检测。为了弥补这一缺陷，2018 年，Redmon 等人发布了 YOLO v3。这一新版本保持了 YOLO 的速度优势，提升了模型精度，尤其加强了小目标、重叠遮挡目标的识别，补齐了 YOLO 的短板，是目前速度和精度均衡的目标检测网络。


随着yolo123版本的更新，预测效果越来越好，但是预测速度也不断在下降，yolo3的速度还是比较快的，官网在推出yolo3后直接下了yolo2和yolo1，可以看出来很自信……其优秀的检测结果主要的得益于残差网络、反卷积和多特征层的思想，这些特点使其可以很好的提取特征，同时训练效果好，且对大目标和小目标都有很好的检测效果。[4]

[1]: https://github.com/YunYang1994/tensorflow-yolov3
[2]: https://github.com/HaloTrouvaille/YOLO-Multi-Backbones-Attention
[3]: https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650781020&idx=1&sn=0cb4ae88c603ec778ef5acc1228fb3c1
[4]: https://blog.csdn.net/weixin_44791964/article/details/102646387
[5]: https://github.com/sthanhng/yoloface
[6]: https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247484909&idx=1&sn=c02ee17e5175230ed39ad63e73249f5c&chksm=fdb6987acac1116c0108ec28424baf4ea16ca11d2b13f20d4a825d7b2b82fb8765720ebd1063&scene=21#wechat_redirect
https://github.com/ayooshkathuria/pytorch-yolo-v3
https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/
https://github.com/minar09/yolov3-pytorch
https://github.com/pjreddie/darknet
300 行代码基于 Pytorch 精确复现 YOLOv3 - Devymex Wang的文章 - 知乎
https://zhuanlan.zhihu.com/p/343039250
