

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 20:49:47
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5ee64c2f06aa6_w9kwqWCY/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
-->

# Xception

## Pre

1* 1 3* 3, 5* 5

## Inception

v1-v3

## 背景

在depth convolution 改进Inception V3，构建一个Extreme的

证明卷积操作中对特征不同层的信息提取和对每一层中空间信息恶的提取是完全可分离的。

引用超2400次

## Abstract

Inception 模块可理解为介于标准卷积和深度可分离卷积的中间步骤

深度可分离卷积可理解为tower最多的Inception模块
用深度可分离卷积替换Inception模块的标准卷积，得到Xception网络
在ImageNet 和JFT数据集上，均获得了不同程度的提升。


在
