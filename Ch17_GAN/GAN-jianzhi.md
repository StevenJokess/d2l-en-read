

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 18:49:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 18:50:28
 * @Description:
 * @TODO::
 * @Reference:https://www.zhihu.com/collection/533183923?page=3
-->

华为诺亚方舟实验室的论文《Co-Evolutionary Compression for Unpaired Image Translation》被ICCV 2019录用，该论文首次提出针对GAN中生成网络的剪枝算法

模型往往需要较大的内存，运行这些模型需要较大的计算开销，一般只能在GPU平台上运行，不能直接将这些模型迁移到移动端上。


生成模型参数冗余建模




在Kirin 980芯片上，推理时间从6.8s压缩到了2.1s，线上加速三倍以上。
