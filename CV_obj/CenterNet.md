

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 17:10:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 17:14:39
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/107748542
 *
-->
# Centernet

如今常见的目标检测算法通常使用先验框的设定，即先在图片上设定大量的先验框，网络的预测结果会对先验框进行调整获得预测框，先验框很大程度上提高了网络的检测能力，但是也会收到物体尺寸的限制。

Centernet采用不同的方法，构建模型时将目标作为一个点——即目标BBox的中心点。

Centernet的检测器采用关键点估计来找到中心点，并回归到其他目标属性。

模型是端到端可微的，更简单，更快，更精确。Centernet的模型实现了速度和精确的很好权衡。

## Loss

loss计算分为三个部分，分别是：
1、热力图的loss
2、reg中心点的loss
3、wh宽高的loss


c_loss = focal_loss(hm, batch_hms)
wh_loss = 0.1*reg_l1_loss(wh, batch_whs, batch_reg_masks)
off_loss = reg_l1_loss(offset, batch_regs, batch_reg_masks)
loss = c_loss + wh_loss + off_loss

https://www.bilibili.com/video/BV1mK411u77S?from=search&seid=10209993305168812028

https://github.com/bubbliiiing/centernet-pytorch
