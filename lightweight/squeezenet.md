

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 20:38:25
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5ee64a7d02a5f_iff07RH8/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
-->

# SqueezeNet

## 动机

给定一个参数，少参数的CNN：

1. **越小的模型，训练越快。**更高效的分布式训练：分布式训练的数据并行方法在每个服务器上保留整个模型的副本，处理训练数据集的不同子集。因此，通信开销与模型中的参数数成正比，越小的模型，训练越快。
2. **越小的模型，通信少，频繁更新** Over-the-air update(OTA)，
3. **更容易在嵌入式设备上嵌入**

## Background

![AlexNet](img\AlexNet.jpg)

4.8MB->0.47MB
AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size
2300+引用
不同SR 和 不同3*3卷积核数量下




[1]: https://arxiv.org/abs/1602.07360
[2]: https://ai.deepshare.net/detail/v_5ee64a7d02a5f_iff07RH8/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
