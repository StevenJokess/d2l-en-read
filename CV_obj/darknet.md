

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 22:06:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 20:53:44
 * @Description:
 * @TODO::
 * @Reference:
 * https://paddleclas.readthedocs.io/zh_CN/latest/models/Others.html
-->
DarkNet53是YOLO作者在论文设计的用于目标检测的backbone，该网络基本由1x1与3x3卷积构成，共53层，取名为DarkNet53。[1]

AlexeyAB 首字母是a，于是也被叫做 a版，darknet模型可以用 ncnn 自带的 darknet2ncnn 无痛转换，步骤比较简单[2]

[1]: https://github.com/alexeyab/darknet
[2]: 详细记录u版YOLOv5目标检测ncnn实现 - nihui的文章 - 知乎
https://zhuanlan.zhihu.com/p/275989233
