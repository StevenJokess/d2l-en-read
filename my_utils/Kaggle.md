

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 15:00:24
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 15:00:46
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/36824585
-->
# 如何在 Kaggle Kernels 上使用 GPU

Kaggle 官网上分享了怎样能在 Kaggle Kernels 上使用 GPU，并展示了示例代码：

添加 GPU

我们首先打开 Kernel 控制界面，为当前的 Kernel 设置运行一个 GPU。


选择“Setting”选项，然后选择“Enable GPU”。接着在控制栏上检查你的 Kernel 是否连上了 GPU，连接状态应显示为“GPU ON”，如下图所示：



不少数据科学库并不能使用 GPU，因此对于一些任务来说（特别是使用 TensorFlow、Keras和 PyTorch 这些深度学习库的时候），GPU 会非常有价值。
