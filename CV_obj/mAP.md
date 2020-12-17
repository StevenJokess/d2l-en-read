

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:51:30
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 18:52:23
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/102414522
-->

## 什么是mAP


说到mAP，也要说到，AP是什么。

说到AP，就要联系到上一部分所说的Precision和Recall。

对于目标检测而言任务，每一个类都可以计算出其Precision和Recall，通过合理的计算，每个类都可以得到一条P-R曲线，
**曲线下的面积就是AP的值**。

假设存在M张图片，对于其中一张图片而言，其具有N个检测目标，其具有K个检测类，使用检测器得到了S个Bounding Box(BB)，每个BB里包含BB所在的位置以及对于K个类的得分C。
利用BB所在的位置可以得到与其对应的GroundTruth的IOU值。

1、步骤1：
对于每一个类I而言，我们执行以下步骤：

对所有的BB，计算BB所在的位置与其最对应的GroundTruth的IOU值，，记为MaxIOU，此时再设置一个门限threshold，一般设置为0.5。
当MaxIOU<threshold，认为该预测框无真实框与其对应，
此时可以记录其属于False Positive，使其FPi = 1，并记录其属于类I的分数C。

当MaxIOU>threshold，认为该预测框与该真实框最对应；
此时再分两类：
当该框的类别属于类型I时，此时可以记录其属于True Positive，使其TPi = 1，并记录其属于类I的分数C。
当该框的类别不属于类型I时，此时可以记录其属于False Positive，使其FPi = 1，并记录其属于类I的分数C。

2、步骤2：
由步骤1我们可以得到K * S个分数C 和 TP 和 FP的元祖，在python中，我们可以将其构成形如(C,TP, FP)的元组，对这K * S个元祖按照得分C进行排序。

3、步骤3
将得分从大到小排序后进行截取，截取得分最大的S个，通过该步骤可以获得每个框是否成功对应了自己所属的类，计算每次截取所获得的recall和precision。

（此处Recall所用的TP+FN = N（一张图片所具有的N的目标，所有确实是正类的数量））
这样得到S个recall和precision点，便画出PR曲线了。

通过PR曲线便可以得到AP值。

**而mAP就是对所有的AP值进行求平均即可。**
