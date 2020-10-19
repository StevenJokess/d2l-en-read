

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 17:27:45
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5ee644a796c35_tAwVkVvK/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
 * https://ai.deepshare.net/detail/v_5ee644d9ed5d3_17ThW2c9/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
 * https://ai.deepshare.net/detail/v_5ee645075753a_qSt7UuAU/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
-->

## ResNet

## Activation

## 轻量化网络的客观需求

小、速度

## 本文方法

根据应用需求与资源限制（延迟，大小）
优化延迟
深度可分离卷积 设置两个超参数：balance准确率与延迟




## 结构

通过步长来降采样
(n+2p-f)/s + 1* (n+2p-f)/s + 1
尺度维度变化

## 深度可分离卷积

深度卷积负责各个通道
点卷积1*1*M，每个卷积一个像素



深度可分离卷积 分为 深度卷积和 点卷积

![普通卷积vs深度可分离卷积](img\depth_sep.jpg)

TODO:https://ai.deepshare.net/detail/v_5ee645312d94a_eMNJ5Jws/3?from=p_5ee641d2e8471_5z8XYfL6&type=6








[1]: https://arxiv.org/abs/1704.04861 MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications
[2]: https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md
