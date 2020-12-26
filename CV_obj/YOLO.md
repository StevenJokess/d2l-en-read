

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-15 17:55:32
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 20:10:40
 * @Description:
 * @TODO::
 * @Reference:https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch08_%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/%E7%AC%AC%E5%85%AB%E7%AB%A0_%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B.md
-->
YOLO 模型最早是由 Joseph Redmon 等人在 2015 年提出的，并在随后的几篇论文中进行了修订。

YOLOv1有哪些创新点？

将整张图作为网络的输入，直接在输出层回归bounding box的位置和所属的类别
速度快，one stage detection的开山之作

https://github.com/aws-samples/aws-machine-learning-university-accelerated-cv/blob/master/notebooks/MLA-CV-Lecture3-YOLO.ipynb


每个网格有20个类条件概率，2个边界框置信度，相当于每个网格有40个得分，7x7个网格有1960个得分，每类对象有1960/20=98个得分，即98个候选框。


NMS步骤如下：
1. 设置一个Score的阈值，一个IOU的阈值；
2. 对于每类对象，遍历属于该类的所有候选框，
①过滤掉Score低于Score阈值的候选框；
②找到剩下的候选框中最大Score对应的候选框，添加到输出列表；
③进一步计算剩下的候选框与②中输出列表中每个候选框的IOU，若该IOU大于设置的IOU阈值，将该候选框过滤掉，否则加入输出列表中；
④最后输出列表中的候选框即为图片中该类对象预测的所有边界框
3. 返回步骤2继续处理下一类对象。

YOLO将识别与定位合二为一，结构简便，检测速度快，更快的Fast YOLO可以达到155FPS。相对于R-CNN系列, YOLO的整个流程中都能看到整张图像的信息，因此它在检测物体时能很好的利用上下文信息，从而不容易在背景上预测出错误的物体信息。同时YOLO可以学习到高度泛化的特征，能将一个域上学到的特征迁移到不同但相关的域上，如在自然图像上做训练的YOLO，在艺术图片上可以得到较好的测试结果。

由于YOLO网格设置比较稀疏，且每个网格只预测2个边界框，其总体预测精度不高，略低于Fast RCNN。其对小物体的检测效果较差，尤其是对密集的小物体表现比较差。
