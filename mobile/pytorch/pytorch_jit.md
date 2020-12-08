

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 20:25:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 20:30:15
 * @Description:
 * @TODO::
 * @Reference:https://lernapparat.de/pytorch-jit-android/
-->
这周，我们在慕尼黑的微软公司举行了一次PyTorch聚会。很高兴看到90多人前来参加两次会谈，并在会谈后边吃披萨边喝饮料边聊天!Piotr Bialecki在PyTorch论坛上做了一个关于语义搜索的演讲，我很荣幸地谈到了PyTorch、JIT和Android。感谢Piotr和微软!

以下是我演讲的简短概要:short synopsis

对我来说，PyTorch JIT有两个主要用途

自动优化和

导出模型到c++。

对于一个简单的损失函数——结合的交集，用于测量预测的边界盒与检测模型中的地面真相的匹配程度——我首先研究了两种“经典”优化:

从Python转移到c++只节省了10%——比观众预期的要少(我的特别调查的中值显示速度提高了2-10倍)。

编写自定义CUDA内核提供了快速的函数——但是很乏味。

好消息是，对于许多函数——即那些涉及点态计算的函数——JIT可以或多或少免费地为您提供可观的加速。

我演讲的第二部分是关于导出到c++，并让导出的模型在Android上运行。容易部署!

这里是我关于IoU优化的幻灯片和详细的笔记。如果你觉得这些有趣，我很乐意收到你的来信!

通过我的公司，MathInf，我提供PyTorch咨询和培训。




大部分时间的培训都是为客户进行的，但我目前正考虑在2月份进行一次小型的一天培训(8-10人参加)。我的训练不开始与MNIST，所以我们将有一些是初学者到中级，但没有冲淡。让我知道如果你在和什么东西你想看到覆盖!

tv@mathinf.eu

Next steps for improvement: • Mobile-adapted variant of MarkRCNN, • make some ﬁxed things constants (anchor grid) in MaskRCNN, • JIT improvements feature: pre-fuse kernels and export those into custom ops, • Quantization in PyTorch.

Android:
• C++-PyTorch feasible on Android,
• can use arbitrary JIT-exported models directly, • keeping models in PyTorch (on Python) as long as possible is good for debugging,

Open: How to get those done and also get PyTorch/Android in a good enough shape to publish.
