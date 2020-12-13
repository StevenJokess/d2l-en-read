

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 22:27:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 00:07:12
 * @Description:
 * @TODO::
 * @Reference:[2]: https://paddleclas.readthedocs.io/zh_CN/latest/models/Mobile.html
-->

https://github.com/d-li14/mobilenetv3.pytorch

MobileNetV3是Google于2019年提出的一种基于NAS的新的轻量级网络，为了进一步提升效果，将relu和sigmoid激活函数分别替换为hard_swish与hard_sigmoid激活函数，同时引入了一些专门减小网络计算量的改进策略。

MobileNetV3代表了目前主流的轻量级神经网络结构。在MobileNetV3中，作者为了获得更高的精度，在global-avg-pooling后使用了1x1的卷积。该操作大幅提升了参数量但对计算量影响不大，所以如果从存储角度评价模型的优异程度，MobileNetV3优势不是很大，但由于其更小的计算量，使得其有更快的推理速度。


此外，我们模型库中的ssld蒸馏模型表现优异，从各个考量角度下，都刷新了当前轻量级模型的精度。由于MobileNetV3模型结构复杂，分支较多，对GPU并不友好，GPU预测速度不如MobileNetV1[2]
