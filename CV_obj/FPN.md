

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 21:03:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 21:03:33
 * @Description:
 * @TODO::
 * @Reference:http://www.tensorinfinity.com/paper_25.html
-->

# FPN

FPN（Feature Pyramid Network）方法同时利用低层特征高分辨率和高层特征的高语义信息，通过融合这些不同层的特征达到提升预测的效果的作用。FPN中预测是在每个融合后的特征层上单独进行的，这和常规的特征融合方式有所不同。

FPN 网络结构如下图d（其中YOLO使用b结构，SSD使用c结构）所示，它的结构具有相当的灵活性，可以和各种特征提取网络结合作为检测算法的基础网络。在后文中会看到，目前大多数state-of-art的模型都采用了这种结构。其中RetinaNet在FPN的基础上使用了ResNet网络提取特征，并用Focal Loss损失改善单步目标检测算法中普遍存在的前景类和背景类损失不均衡的问题。这些基于FPN结构的检测算法能够在增加网络深度、获取更丰富语义信息的同时从浅层特征图中获取更丰富且高分辨率的图像特征，这使得这种网络结构在实际应用中表现出优异的性能。

目前主流检测框架有4种使用特征的形式：

1.图像金字塔。即将图像缩放到不同的大小，然后不同大小的图像生成对应的特征。这种方法的缺点是增加了时间成本。有些算法会在检测时采用这种图像金字塔的方案。

2.单一尺度特征层。SPPNet，Fast RCNN，Faster RCNN采用这种方式，即仅采用网络最后一层卷积层的特征。

3.SSD采用这种多尺度特征融合的方式，但是没有上采样过程，即从网络不同层抽取不同尺度的特征做预测，这种方式不会增加额外的计算量。SSD算法中没有用到足够低层的特征（在SSD中，最低层的特征是VGG网络的conv4_3），而足够低层的特征对于检测小物体是很有帮助的。

4.FPN采用bottom-up与top-down的结构，实现了低层特征和高层语义特征的融合，提高了特征映射的信息密度和分辨率，提高了小目标物体的检测效果；区别于SSD，FPN每层都是独立预测的。
