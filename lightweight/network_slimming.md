

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 23:06:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-06 00:01:36
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5f40e7bce4b0dd4d974a9620/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
-->

一种channel-level的裁剪方案，可以通过稀疏化尺度因子（BN层的scaling factor）来裁掉“不重要”的channel。
  文中的方案为：

在训练时，对BN层的scaling factor施加L 1 L_1L
1
​
 正则化，在训练网络的同时得到稀疏化的尺度因子；
裁掉低于指定阈值的channel；【（1）设定裁剪的百分比；（2）依据百分比找到所有尺度因子对应的值作为阈值；（3）逐层进行裁剪】
对得到的模型进行fine-tune以恢复因裁剪损失的精度。

几种不同细粒度的裁剪方法的对比：

weight-level的稀疏化裁剪，可以有较大的灵活性、压缩率，但需要特定的硬件和库才能实现性能的提升（加速）； ?非结构的
layer-level的稀疏化裁剪，需要对完整的Layer进行裁剪，其灵活性较差。而且事实上，当网络足够深的时候（大于50层），移除layer才会带来收益；
channel-level的稀疏化裁剪，是一个折中方案，其具有灵活性，可以适用于任何CNN中。

BN 用在卷积层后，激活层前，使模型训练更稳定，避免梯度爆炸或者小时，并起到正则化作用，几乎代替了Dropout。
1. 缓解 Internal Coveriate Shift(ICS)，学习慢。
2. 缓解梯度消失，归一化散两边的回到中间。
3. 缓解模型过拟合，降低非线性变换。

![img](img\BN_intro.jpg)

重要性通道剪枝
![img](img\BN_judge.jpg)

TODO:https://ai.deepshare.net/detail/v_5f40e84ee4b011878732abb6/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
3：00

[1]: Learning Efficient Convolutional Networks through Network Slimming https://arxiv.org/abs/1708.06519
[2]: https://blog.csdn.net/qq_19784349/article/details/107214544
