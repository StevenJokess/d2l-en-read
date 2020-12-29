

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 21:28:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 21:30:41
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/234506503
-->

Yolo-Fastest，顾名思义，应该是现在已知开源最快的最轻量的改进版yolo通用目标检测算法（貌似也是现在通用目标检测算法中最快最轻量的），其实初衷就是打破算力的瓶颈，能在更多的低成本的边缘端设备实时运行目标检测算法

更慢啊xl就不多讲了，肯定树莓派3b没法实时，嘻嘻，但是这边有个基于麒麟990的NCNN的速度基准

其实旷视的thundernet才是大佬，250mbflops的计算量，VOC能达到70%，可惜没开源，但是是个二阶检测算法，估计没yolo好部署。不过话说，如果我用object365把模型在训练一遍迁移到voc是不是又得暴涨几个点
