

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-30 20:36:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 20:37:36
 * @Description:
 * @TODO::
 * @Reference:https://bbs.cvmart.net/topics/1506
-->

网络剪枝
网络剪枝目的在于找出这些冗余连接并将其移除，使其不再参与网络的前向或后向运算过程中，起到减少网络计算量的作用，如下图所示。

移除的神经元及相应连接也不再存储，减少了模型的存储量。在这个过程中，一个原本稠密的神经网络由于部分连接的移除而变得稀疏。


由于全连接层冗余度远远高于卷积层，传统的网络剪枝方法多用于全连接层中。网络剪枝往往针对已经训练好的模型进行，在得到训练好的模型后，根据某种评价标准定义每条连接的重要程度。一种广泛使用的评价标准是连接权重的绝对值大小，该值越小，说明对应的神经元对网络输出结果影响越小，属于不重要的神经元，应该被移除，对应的连接也应被剪除。

虽然移除的连接不那么重要，但随着网络计算过程中的错误累积，网络性能和准确度依然会受到较大的影响，为了消除这些影响，一个很重要的步骤是对剪枝后的网络进行微调训练来恢复网络性能。整个网络剪枝和调优交替进行，直至达到模型大小与模型性能间的最佳平衡。

权重剪枝主要有两种方式：

（1）后剪枝：拿到一个模型直接对权重进行剪枝，不需要其他条件。

（2）训练时剪枝：训练迭代时边剪枝，使网络在训练过程中权重逐渐趋于0，但是由于训练时权重动态调整，使得剪枝操作对网络精度的影响可以减少，所以训练时剪枝比后剪枝更加稳定。

在剪枝结束后，权值矩阵由稠密矩阵变为稀疏矩阵。

为了减少参数的存储量，通常使用存储稀疏矩阵的压缩存储方式存储参数，代表方式为稀疏行压缩方法 (Compressed Sparse Row,CSR）和稀疏列压缩方法 (Compressed SparseColumn,CSC)。

高效网络结构
由于神经网络对于噪声不敏感，所以许多早期经典模型的参数其实是存在很大冗余度的，这样的模型很难部署在存储有限的边缘设备，嵌入式设备的高需求刺激了高效网络结构的设计。

例如 GoogleNet 使用了Inception 模块而不再是简单的堆叠网络层从而减小了计算量。ResNet 通过引入瓶颈结构取得了极好的图像识别效果。ShuffleNet 结合了群组概念和深度可分离卷积，在 ResNet 上取得了很好的加速效果。MobileNet 采用了深度可分离卷积实现了目前的最好网络压缩效果。

减小卷积核大小
使用更小的3x3卷积(加深网络来弥补感受野变小)

将大卷积核分解成一系列小的卷积核的操作组合

减少通道数
（1）1x1卷积的应用。在大卷积核前应用1X1卷积，可以灵活地缩减feature map通道数（同时1X1卷积也是一种融合通道信息的方式），最终达到减少参数量和乘法操作次数的效果。

（2）组卷积的应用。将feature map的通道进行分组，每个filter对各个分组进行操作即可，例如分成两组，每个filter的参数减少为传统方式的二分之一（乘法操作也减少）。

（3）深度可分离卷积（depthwise convolution）的应用，是组卷积的极端情况，将卷积的过程分为逐通道卷积与逐点1×1卷积两步，每一个组只有一个通道。虽然深度可分离卷积将一步卷积过程扩展为两步，但减少了冗余计算，因此总体上计算量有了大幅度降低。

如果只采用分组卷积操作，相比传统卷积方式，不同组的feature map信息无法交互，因此可以在组卷积之后在feature map间进行Shuffle Operation来加强通道间信息融合。

或者更巧妙的是像Pointwise convolution那样将原本卷积操作分解成两步，先进行 depthwise convolution，之后得到的多个通道的feature map再用一个1X1卷积进行通道信息融合，拆解成这样两步，卷积参数也减少了。

减少filter数目
直接减少的filter数目虽然可以减少参数，但是导致每层产生的feature map数目减少，网络的表达能力也会下降不少。一个方法是像DenseNet那样，一方面减少每层filter数目，同时在每层输入前充分重用之前每一层输出的feature map。

池化操作
池化操作是操作卷积神经网络的标准操作，池化层没有参数，同时又可以灵活缩减上一级的feature map大小，从而减少下一级卷积的乘法操作。

6. 卷积运算的优化
卷积转化为矩阵乘法
大部分深度学习框架会把卷积操作转化成矩阵乘法操作，这样可以利用现有成熟的矩阵乘法优化方案，比较常见的转化方式是img2col。

全连接层可以直接转化为矩阵乘法，因为全连接的操作本质上就是Y=WX的矩阵操作。从另一个角度，全连接的操作其实还可以看作 每个神经元为1x1filter，所进行的卷积操作。而对于卷积层，转化为矩阵乘法后，会引入一定冗余度。

优化矩阵乘法操作
矩阵分块可以更好地匹配各级cache的大小，这样cache局部性更好，访存时的miss率更低。除此之外，对矩阵的内存数据布局进行重排布来增加待计算数据放置的连续性，这样取数的时候cache miss率也会更低，像常见的 NCWH 和 NWHC 排布模式都是这方面考虑。

矩阵乘法的近似计算
使用其它的卷积近似替代算法，可以减少复杂度。不过有些算法有使用条件，像Winograd只是对小卷积核操作有比较大的优化效果。傅里叶变换似乎不太常用，因为要达到理论上的加速，要求卷积核要很大才可以，而实际上深度学习用的都是小卷积核。