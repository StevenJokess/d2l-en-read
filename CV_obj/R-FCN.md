

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 21:04:12
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 21:04:21
 * @Description:
 * @TODO::
 * @Reference:http://www.tensorinfinity.com/paper_25.html
-->
# R-FCN

由于现在的主流网络层数越来越多，基于Faster RCNN检测框架的方法的计算量受到了3个因素的影响：

1.基础网络的复杂度

2.候选框数量的多少

3.分类和位置回归子网络的复杂度（每个候选框的box都会独立进行前向计算）。

一般来说直接优化前两点性价比不太高。如果直接优化RoI-wise subnetwork是否可行呢,将子网络的深度尽可能减少？分类是要增加物体的平移不变性（不同的位置都是同一个物体）；目标检测时减少物体的平移变化（目标检测需要得到物体所在的位置）。通常我们所用的网络都是ImageNet的分类任务训练得到的，在目标检测的时候进行Finetune。由于得到的初始模型基于分类任务，那么会偏向于平移不变性，这和目标检测就出现了矛盾。

MSRA的Jifeng Dai等人提出了R-FCN，通过position-positive score maps（位置敏感得分图）来解决这个矛盾。位置敏感得分图通过预测RoI中不同部位的类别投票表决产生该RoI的类别预测。引用原文中的例子，“如果我们的算法要识别婴儿，那么把一个目标区域分成九宫格，其中算法认为其中五个格子中的区域分别像婴儿的头、四肢和躯干，那么根据投票机制，就认为这个目标区域里的是一个婴儿。这很符合我们人类的判断逻辑。

image.png

R-FCN沿用了 Faster RCNN 的框架结构，不同的是在Faster R-CNN的基础上通过引入位置敏感得分图，将RoI-wise subnetwork消灭了，直接在位置敏感得分图上利用ROI Pooling进行信息采样融合分类和位置信息。
