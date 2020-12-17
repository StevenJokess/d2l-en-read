

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:18:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 18:20:22
 * @Description:
 * @TODO::
 * @Reference:
-->

YOLOV4整体上的检测思路和YOLOV3相比相差并不大，都是使用三个特征层进行分类与回归预测。

YoloV4-Tiny是YoloV4的简化版，少了一些结构，但是速度大大增加了，YoloV4共有约6000万参数，YoloV4-Tiny则只有600万参数。

YoloV4-Tiny仅使用了两个特征层进行分类与回归预测。

[1]: https://blog.csdn.net/weixin_44791964/article/details/107041297
[2]: https://github.com/bubbliiiing/yolov4-tiny-pytorch
