

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-15 17:55:32
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 19:55:44
 * @Description:
 * @TODO::
 * @Reference:https://github.com/scutan90/DeepLearning-500-questions/blob/master/ch08_%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/%E7%AC%AC%E5%85%AB%E7%AB%A0_%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B.md
 * [2]： https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247484909&idx=1&sn=c02ee17e5175230ed39ad63e73249f5c&chksm=fdb6987acac1116c0108ec28424baf4ea16ca11d2b13f20d4a825d7b2b82fb8765720ebd1063&scene=21#wechat_redirect
-->
# YOLO(You Only Look Once)

## 故事引入

B小朋友稍微聪明了点，会根据经验把可以区域挑选出来在进行判别，类似使用了SelectiveSearch、EdgeBoxes、Bing等proposal的方法，大大缩小了搜索的空间；

我会快速对全图进行一层层过滤，在脑海中形成一张小图总共3x3张笑脸，很容易就找到最后那张笑的最开心的脸。听过之后其它小朋友一脸疑惑……

A小朋友的套路则要高明的多，他将图片一层层在自己的脑海中进行融合缩小，最后在一张浓缩的小图上快速定位了目标，我们今天要介绍的YOLO=（You Only Look Once）和第一名A小朋友的思路有异曲同工之妙。

![](1vs2stage.jfif)

## YOLO的动机

YOLO的作者认为，之前的检测策略比较慢而且难以优化，比如R-CNN为首的候选框+预测位置、分类的这种策略。R-CNN首先产生一些潜在的region proposal，然后用分类器对每一个region进行分类并修正优化物体的边界，最后铜鼓NMS合并消除重复检测框，这个过程被业界称为two-stage。YOLO作为one-stage的鼻祖，将目标检测看作为单一的回归问题，直接由图像像素优化得到物体边界位置和分类。

YOLO作为基于深度学习的第一个one-stage的方法做快可以在TitanX GPU上做到45帧每秒的检测速度，轻量版的可以做到155帧每秒，快到没朋友有没有？相比于R-CNN精确度也有非常大的提升53.5 VS 63.4 mAP，真是做到了多快好省！[2]

YOLO 模型最早是由 Joseph Redmon 等人在 2015 年提出的，并在随后的几篇论文中进行了修订。

YOLOv1有哪些创新点？

将整张图作为网络的输入，直接在输出层回归bounding box的位置和所属的类别
速度快，one stage detection的开山之作

https://github.com/aws-samples/aws-machine-learning-university-accelerated-cv/blob/master/notebooks/MLA-CV-Lecture3-YOLO.ipynb

## 模型结构

模型灵感来自于GoogLeNet[6]，用1x1 和3x3 卷积核代替inception modules. 激活函数用的是Leaky ReLU : f(x)=max(x,0.1x)，在x小于0的时候，用了0.1x，避免使用ReLU的时候有些单元永远得不到激活（Dead ReLU Problem），在不增加计算法复杂度的前提下提升了模型的拟合能力。

YOLOv1由24 层卷积层接2层全连接组成。用ImageNet数据集做预训练(图片尺寸224×224)，做检测模型优化时对输入图片尺寸放大了两倍(图片尺寸448×448)。通过改变训练数据的饱和度，曝光度，色调，抖动进行数据增强。

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


损失函数设计

YOLOv1的损失函数设计简单粗暴对所有的项统一用sum-squared error进行优化。

$\lambda_{\text {noobj}} \sum_{i=0}^{l . h * l . w} \sum_{j=0}^{l, n} 1_{i j}^{\text {noobj}}\left(C_{i}-\hat{C}_{i}\right)^{2}$ //不含物体的 BB 的 confidence 预测
$+\lambda_{o b j} \sum_{i=0}^{l . h * l . w} \sum_{j=0}^{l . n} 1_{i j}^{o b j}\left(C_{i}-\hat{C}_{i}\right)^{2} \quad$ //含有物体的 $\mathrm{BB}$ 的 confidence 预测
$+\lambda_{\text {class}} \sum_{i=0}^{l_{i=0} * l . w} 1_{i}^{o b j} \sum_{c \in \text {classes}}\left(p_{i}(c)-\hat{p}_{i}(c)\right)^{2} / /$ 类别预测
$+\lambda_{\text {coord}} \sum_{i=0}^{l . w * l . w} \sum_{j=0}^{l, n} 1_{i j}^{o b j}\left[\left(x_{i}-\hat{x}_{i}\right)^{2}+\left(y_{i}-\hat{y}_{i}\right)^{2}\right] / /$ 坐标 $\mathrm{x}, \mathrm{y}$ 预测
$$
+\lambda_{\text {coord}} \sum_{i=0}^{l . h * l . w} \sum_{j=0}^{l, n} 1_{i j}^{o b j}\left[\left(\sqrt{w_{i}}-\sqrt{\hat{w}}_{i}\right)^{2}+\left(\sqrt{h_{i}}-\sqrt{\hat{h}}_{i}\right)^{2}\right] / / \mathrm{w}, \mathrm{h} \text { 预测 }
$$

## 损失函数分析：

1. 图片:判断第i个cell里的第j个BBox是否负责预测这个物体：与GT的IOU最大的BBox负责预测
2. 图片:判断是否有物体落在第i个cell中：如果cell中包含有物体的中心，就负责预测该类。
3. 图片:之所以图片取0.5是因为背景框的数量要远大于前景框，不加以限制，confidence的值将趋近于零；为什么图片取5，作者说得很模糊，意思是如果坐标框的系数和类别一样的话显然是不合理的，所以加大了对框的惩罚，但YOLOv2和YOLOv3改用全卷积网络后这个参数s就改为1了。
4. 图片:作者对宽高都进行开根是为了使用大小差别比较大的边界框差别减小。例如，一个同样将一个100x100的目标与一个10x10的目标都预测大了10个像素，预测框为 $110 \times 110$
与20 $\times$ 20。显然第一种情况我们还可以接受，但第二种情况相当于把边界框预测大了1倍, 但如
果不使用根号函数，那么损失相同, 但把宽高都增加根号时：
$$
\begin{array}{l}
(\sqrt{20}-\sqrt{10})^{2}=3.43 \\
(\sqrt{110}-\sqrt{100})^{2}=0.48
\end{array}
$$

显然，对小框预测偏差10个像素带来了更高的损失。通过增加根号，使得预测相同偏差与更小的框产生更大的损失。但根据YOLOv2的实验证明，还有更好的方法解决这个问题。



## YOLOv1的优点

1、YOLO v1检测物体非常快。 因为没有复杂的检测流程，YOLO将目标检测重建为一个单一的回归问题，从图像像素直接到边界框坐标和分类概率，而且只预测98个框，YOLO可以非常快的完成物体检测任务。YOLO在Titan X 的 GPU 上能达到45 FPS。Fast YOLO检测速度可以达到155 FPS。
2、YOLO可以很好的避免背景错误，其它物体检测算法使用了滑窗或region proposal，分类器只能得到图像的局部信息。YOLO在训练和测试时，由于最后进行回归之前接了4096全连接，所以每一个Grid cell对应的预测结果都相当于使用了全图的上下文信息，从而不容易在背景上预测出错误的物体信息。和Fast-R-CNN相比，YOLO的背景错误不到Fast-R-CNN的一半。
3、YOLO可以学到更泛化的特征。 当YOLO在自然图像上做训练，在艺术作品上做测试时，YOLO表现的性能比DPM、R-CNN等之前的物体检测系统要好很多。因为YOLO可以学习到高度泛化的特征，从而迁移到其他领域。

## YOLO v1的缺点

1、对邻近物体检测效果差，由于每个grid cell仅预测两个框和一个分类，对于  多物体的中心位置落入同一cell，YOLOv1力所不及。
2、用全连接的问题在于，虽然获取了全局信息，但是比起1×1卷积来说也丢失了局部细节信息；全连接带来了参数量的巨增。
3、对不常见的长宽比物体泛化能力偏弱，这个问题主要是YOLO没有Anchor的不同s尺度框的设计，只能通过数据去驱动。
4、损失函数的设计问题，对坐标的回归和分类的问题同时用MSE损失明显不合理。
5、由于YOLOv1是直接预测的BBox位置，相较于预测物体的偏移量，模型会不太好稳定收敛。
