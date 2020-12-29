

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 20:46:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 20:47:11
 * @Description:
 * @TODO::
 * @Reference:视频分割在移动端的算法进展综述 - SIGAI的文章 - 知乎
https://zhuanlan.zhihu.com/p/60574679
-->

## 优缺点分析

1、Siammask的多任务学习方法，同时在VOT和VOS取得精度和实时性的trade off,学术界的研究比较容易落地工业级。

2、Siammask的mask预测分支采用SharpMask语义分割模型，精度带提高，替代这部分的模型可以进一步提高mask预测精度。

3、目前tracking没有专门处理消失问题（object traker如果从当前画面离开或完全遮挡），特别的，siammask挺容易受到具有语义的distractor影响。当遮挡时，它预测的mask是两个物体的mask。VOS领域处理遮挡和消失也比较困难。
