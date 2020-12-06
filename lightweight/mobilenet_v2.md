

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:01:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 22:24:39
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/hub/pytorch_vision_mobilenet_v2/
 * https://arxiv.org/abs/1801.04381
 * https://colab.research.google.com/github/pytorch/pytorch.github.io/blob/master/assets/hub/pytorch_vision_mobilenet_v2.ipynb#scrollTo=7P8C3gMea8FU
-->

import torch
model = torch.hub.load('pytorch/vision:v0.6.0', 'mobilenet_v2', pretrained=True)
model.eval()

所有的预训练模型都期望输入图像以同样的方式归一化，即小批3通道RGB图像的形状(3 x H x W)，其中H和W预计至少为224。图像加载到范围为[0,1]，然后使用mean =[0.485, 0.456, 0.406]和std =[0.229, 0.224, 0.225]进行归一化。

模型描述

MobileNet v2架构基于一个反向残差结构，其中残差块的输入和输出是薄的瓶颈层，与传统残差模型相反，后者在输入中使用扩展表示。MobileNet v2使用轻量级深度卷积来过滤中间扩展层的特征。此外，为了保持代表性，在狭窄的层中去除了非线性。


| Model structure | Top-1 error | Top-5 error |
| --------------- | ----------- | ----------- |
|  mobilenet_v2       | 28.12       | 9.71       |
