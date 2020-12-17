

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 17:29:38
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 17:36:11
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/106214657
 * https://github.com/bubbliiiing/yolov4-pytorch
-->
# YOLOV4

YOLOV4是YOLOV3的改进版，在YOLOV3的基础上结合了非常多的小Tricks。
尽管没有目标检测上革命性的改变，但是YOLOV4依然很好的结合了速度与精度。
根据上图也可以看出来，YOLOV4在YOLOV3的基础上，在FPS不下降的情况下，mAP达到了44，提高非常明显。

YOLOV4改进的部分（不完全）
1、主干特征提取网络：DarkNet53 => CSPDarkNet53

2、特征金字塔：SPP，PAN

3、分类回归层：YOLOv3（未改变）

4、训练用到的小技巧：Mosaic数据增强、Label Smoothing平滑、CIOU、学习率余弦退火衰减

5、激活函数：使用Mish激活函数

以上并非全部的改进部分，还存在一些其它的改进，由于YOLOV4使用的改进实在太多了，很难完全实现与列出来，这里只列出来了一些我比较感兴趣，而且非常有效的改进。

还有一个重要的事情：
论文中提到的SAM，作者自己的源码也没有使用。

还有其它很多的tricks，不是所有的tricks都有提升，我也没法实现全部的tricks。
