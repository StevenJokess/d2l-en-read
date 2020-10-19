

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 18:44:46
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5ee648f24314f_YkqkQu1q/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
-->

Experiments on ImageNet classification and MS COCO object detection demonstrate the superior performance of ShuffleNet over other structures, e.g. lower top-1 error (absolute 7.8%) than recent MobileNet on ImageNet classification task, under the computation budget of 40 MFLOPs.[2]


CNN
分组卷积
ResNet

分组点卷积
通道重排
shufflenet v2
pytorch复现

# 动机

数百层和数千通道，Billions of FLOPs

# 方法

属于直接训练而不是压缩

## 分组点卷积

![分组卷积](img\fenzu.jpg)

给点卷积也分组

分组点卷积某个通道的输出仅来及一部分输入通道，阻止了信息流动，特征表示。

## 通道重排(channel shuffle)

如果我们允许组卷积从不同组中获取输入数据，则输入和输出通道讲完全相关。

对于从上一个组层生成的特征图，可以先将每一个组中的通道划分为几个子组，
然后在下一层中的每个组中使用不同的子组作为输入。


## FLOPS

![FLOPs](img\Shuffle_Flops.jp)

[1]: https://ai.deepshare.net/detail/v_5ee645312d94a_eMNJ5Jws/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
[2]: https://arxiv.org/abs/1707.01083
