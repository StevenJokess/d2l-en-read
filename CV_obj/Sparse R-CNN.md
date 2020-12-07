

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 18:34:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 18:35:24
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/310058362
-->

沿着目标检测领域中Dense和Dense-to-Sparse的框架，Sparse R-CNN建立了一种彻底的Sparse框架， 脱离anchor box，reference point，Region Proposal Network(RPN)等概念，无需Non-Maximum Suppression(NMS)后处理， 在标准的COCO benchmark上使用ResNet-50 FPN单模型在标准3x training schedule达到了44.5 AP和 22 FPS。
