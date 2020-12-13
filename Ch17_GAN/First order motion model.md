

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-10 19:43:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-10 19:44:12
 * @Description:
 * @TODO::
 * @Reference:https://aistudio.baidu.com/aistudio/projectdetail/1048840s
-->
First order motion model的任务是image animation，给定一张源图片，给定一个驱动视频，生成一段视频，其中主角是源图片，动作是驱动视频中的动作，源图像通常包含一个主体，驱动视频包含一系列动作。

以人脸表情迁移为例，给定一个源人物，给定一个驱动视频，可以生成一个视频，其中主体是源人物，视频中源人物的表情是由驱动视频中的表情所确定的。通常情况下，我们需要对源人物进行人脸关键点标注、进行表情迁移的模型训练。

但是这篇文章提出的方法只需要在同类别物体的数据集上进行训练即可，比如实现太极动作迁移就用太极视频数据集进行训练，想要达到表情迁移的效果就使用人脸视频数据集voxceleb进行训练。训练好后，我们使用对应的预训练模型就可以达到前言中实时image animation的操作。[1]
