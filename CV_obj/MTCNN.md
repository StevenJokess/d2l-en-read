

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-09 01:10:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-09 01:13:56
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/58825924
-->

# MTCNN -- Multi-task convolutional neural network（多任务卷积神经网络）

Positive face数据：图片左上右下坐标和label的IOU>0.65的图片
part face数据：图片左上右下坐标和label的0.65>IOU>0.4的图片
negative face 数据：图片左上右下坐标和lable的IOU<0.3的图片
landmark face数据：图片带有landmark label的图片

MTCNN的流程：图片经过Pnet，会得到feature map，通过分类、NMS筛选掉大部分假的候选；然后剩余候选去原图crop图片输入Rnet，再对Rnet的输出筛选掉False、NMS去掉众多的候选；剩余候选再去原图crop出图片再输入到Onet，这个时候就能够输出准确的bbox、landmark坐标了。
