

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 19:19:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 18:54:59
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


