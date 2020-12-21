

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-22 01:34:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 01:35:02
 * @Description:
 * @TODO::
 * @Reference:http://jiangsiyuan.com/2018/05/15/SequenceModeling/
-->
TCN 语言建模

这一部分的实现主要采用 TCN 原论文的官方实现，我们修改了一些内容以在 Notebook 上直接运行。本文主要介绍了构建 TCN 整体架构的代码和整体模型的结构，更多如评估过和训练等过程请查看 GitHub 项目。

GitHub 项目地址：https://github.com/jiqizhixin/ML-Tutorial-Experiment
原论文实现地址：https://github.com/locuslab/TCN
原论文 tcn.py 文件中实现了 TCN 的残差模块与整体网络架构，以下将依次解释该网络的各个模块。

import torch
import torch.nn as nn
from torch.nn.utils import weight_norm

#定义实现因果卷积的类（继承自类nn.Module），其中super(Chomp1d, self).__init__()表示对继承自父类的属性进行初始化。
class Chomp1d(nn.Module):
    def __init__(self, chomp_size):
        super(Chomp1d, self).__init__()
        self.chomp_size = chomp_size

    # 通过增加Padding的方式并对卷积后的张量做切片而实现因果卷积
    # tensor.contiguous()会返回有连续内存的相同张量
    def forward(self, x):
        return x[:, :, :-self.chomp_size].contiguous()
如上所示，首先类 Chomp1d 定义了通过 Padding 实现因果卷积的方法。其中 chomp_size 等于 padding=(kernel_size-1) * dilation_size，x 为一般一维空洞卷积后的结果。张量 x 的第一维是批量大小，第二维是通道数量而第三维就是序列长度。如果我们删除卷积后的倒数 padding 个激活值，就相当于将卷积输出向左移动 padding 个位置而实现因果卷积。

以下实现了 TCN 中的残差模块，它由两个空洞卷积和恒等映射（或一个逐元素的卷积）组成，并使用 torch.nn.Sequential 简单地将这些卷积层和 Dropout 等运算结合在一起。

首先 TemporalBlock 类会定义第一个空洞卷积层，dilation 控制了扩展系数，即在卷积核权重值之间需要添加多少零。卷积后的结果调用上面定义的 Chomp1d 类实现因果卷积。然后再依次添加 ReLU 非线性激活函数和训练中的 dropout 正则化方法，得出激活值后可作为输入传入相同结构的第二个卷积层。

因为残差模块可以表示为 y = H(x, W_H) + x，所以将这两个卷积结果再加上恒等映射 f(x)=x 就能完成残差模块。

# 定义残差块，即两个一维卷积与恒等映射
class TemporalBlock(nn.Module):
    def __init__(self, n_inputs, n_outputs, kernel_size, stride, dilation, padding, dropout=0.2):
        super(TemporalBlock, self).__init__()

        #定义第一个空洞卷积层
        self.conv1 = weight_norm(nn.Conv1d(n_inputs, n_outputs, kernel_size,
                                           stride=stride, padding=padding, dilation=dilation))
        # 根据第一个卷积层的输出与padding大小实现因果卷积
        self.chomp1 = Chomp1d(padding)
        #添加激活函数与dropout正则化方法完成第一个卷积
        self.relu1 = nn.ReLU()
        self.dropout1 = nn.Dropout2d(dropout)

        #堆叠同样结构的第二个卷积层
        self.conv2 = weight_norm(nn.Conv1d(n_outputs, n_outputs, kernel_size,
                                           stride=stride, padding=padding, dilation=dilation))
        self.chomp2 = Chomp1d(padding)
        self.relu2 = nn.ReLU()
        self.dropout2 = nn.Dropout2d(dropout)

        # 将卷积模块的所有组建通过Sequential方法依次堆叠在一起
        self.net = nn.Sequential(self.conv1, self.chomp1, self.relu1, self.dropout1,
                                 self.conv2, self.chomp2, self.relu2, self.dropout2)

        # padding保证了输入序列与输出序列的长度相等，但卷积前的通道数与卷积后的通道数不一定一样。
        # 如果通道数不一样，那么需要对输入x做一个逐元素的一维卷积以使得它的纬度与前面两个卷积相等。
        self.downsample = nn.Conv1d(n_inputs, n_outputs, 1) if n_inputs != n_outputs else None
        self.relu = nn.ReLU()
        self.init_weights()

    # 初始化为从均值为0，标准差为0.01的正态分布中采样的随机值
    def init_weights(self):
        self.conv1.weight.data.normal_(0, 0.01)
        self.conv2.weight.data.normal_(0, 0.01)
        if self.downsample is not None:
            self.downsample.weight.data.normal_(0, 0.01)

    # 结合卷积与输入的恒等映射（或输入的逐元素卷积），并投入ReLU 激活函数完成残差模块
    def forward(self, x):
        out = self.net(x)
        res = x if self.downsample is None else self.downsample(x)
        return self.relu(out + res)
但 TCN 的残差模块还有一个需要注意的地方，即它有可能会对 x 执行一个逐元素的卷积而不是直接添加 x。这主要是因为卷积结果的通道数与输入 x 的通道数可能不同，那么我们就需要使用 n_outputs 个卷积核将输入采样至与卷积输出相同的通道数。最后，定义前向传播以结合两部分输出而完成残差模块的构建。

下面定义了 TCN 的整体架构，简单而言即根据层级数将残差模块叠加起来。其中 num_channels 储存了所有层级（残差模块）的通道数，它的长度即表示一共有多少个残差模块。这里每一个空洞卷积层的扩张系数随着层级数成指数增加，这确保了卷积核在有效历史信息中覆盖了所有的输入，同样也确保了使用深度网络能产生极其长的有效历史信息。

在从 num_channels 列表中抽取当前残差模块的输入与输出通道数后，就能定义这一层的残差模块。将不同层级的残差模块使用 Sequential 堆叠起来就能构建整个网络架构。

# 定义时间卷积网络的架构
class TemporalConvNet(nn.Module):
    def __init__(self, num_inputs, num_channels, kernel_size=2, dropout=0.2):
        super(TemporalConvNet, self).__init__()
        layers = []

        # num_channels为各层卷积运算的输出通道数或卷积核数量，它的长度即需要执行的卷积层数量
        num_levels = len(num_channels)
        # 空洞卷积的扩张系数若随着网络层级的增加而成指数级增加，则可以增大感受野并不丢弃任何输入序列的元素
        # dilation_size根据层级数成指数增加，并从num_channels中抽取每一个残差模块的输入通道数与输出通道数
        for i in range(num_levels):
            dilation_size = 2 ** i
            in_channels = num_inputs if i == 0 else num_channels[i-1]
            out_channels = num_channels[i]
            layers += [TemporalBlock(in_channels, out_channels, kernel_size, stride=1, dilation=dilation_size,
                                     padding=(kernel_size-1) * dilation_size, dropout=dropout)]
        # 将所有残差模块堆叠起来组成一个深度卷积网络
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)
以上的三个类都在定义在 tcn.py 文件中，它适用于所有的测试任务。在语言建模中，还有另一部分定义模型过程的类比较重要，它会将输入序列馈送到网络以完成整个推断过程。

class TCN(nn.Module):

    def __init__(self, input_size, output_size, num_channels,
                 kernel_size=2, dropout=0.3, emb_dropout=0.1, tied_weights=False):
        super(TCN, self).__init__()

        # 将一个批量的输入数据（one-hot encoding）送入编码器中成为一个批量的词嵌入向量
        # 其中output_size为词汇量，input_size为一个词向量的长度
        self.encoder = nn.Embedding(output_size, input_size)

        # 构建网络
        self.tcn = TemporalConvNet(input_size, num_channels, kernel_size, dropout=dropout)

        # 定义最后线性变换的纬度，即最后一个卷积层的通道数（类似2D卷积中的特征图数）到所有词汇的映射
        self.decoder = nn.Linear(num_channels[-1], output_size)

        # 是否共享编码器与解码器的权重，默认是共享。共享的话需要保持隐藏单元数等于词嵌入长度，这样预测的向量才可以视为词嵌入向量
        if tied_weights:
            if num_channels[-1] != input_size:
                raise ValueError('When using the tied flag, nhid must be equal to emsize')
            self.decoder.weight = self.encoder.weight
            print("Weight tied")

        # 对输入词嵌入执行Dropout 表示随机从句子中舍弃词，迫使模型不依赖于单个词完成任务
        self.drop = nn.Dropout(emb_dropout)
        self.emb_dropout = emb_dropout
        self.init_weights()

    def init_weights(self):
        self.encoder.weight.data.normal_(0, 0.01)
        self.decoder.bias.data.fill_(0)
        self.decoder.weight.data.normal_(0, 0.01)

    #先编码，训练中再随机丢弃词，输入到网络实现推断，最后将推断结果解码为词
    def forward(self, input):
        """Input ought to have dimension (N, C_in, L_in), where L_in is the seq_len; here the input is (N, L, C)"""
        emb = self.drop(self.encoder(input))
        y = self.tcn(emb.transpose(1, 2)).transpose(1, 2)
        y = self.decoder(y)
        return y.contiguous()
如上所示，模型的主要过程即先将输入的向量编码为词嵌入向量，再作为输入投入到时间卷积网络中。该网络的输出为 y，它的第一个纬度表示批量大小，第二个纬度是通道数量，而第三个纬度代表序列长度。全卷积主要体现在解码的过程，我们不需要再向量化卷积结果而进行仿射变换，而是直接将不同的序列通道映射到全部的词汇中以确定预测的词。

如果读者安装了 PyTorch，那么 TCN 的测试就可以使用 Git 复制原论文官方实践，然后转到 word_cnn 目录下就能直接在 PyCharm 等 IDE 中运行 word_cnn_test.py 文件，当然我们也可以使用命令行运行。此外，为了让更多的入门读者可以运行该模型，我们会修正这个实现语言建模的 TCN，并放到谷歌 Colaboratory 中，这样读者就能使用免费的 GPU 资源进行训练。这一部分还在修正中，稍后我们会上传至机器之心 GitHub 项目。

最后，Shaojie Bai 等研究者还在很多序列建模任务上测试了 TCN 与传统循环网络的性能：


上表展示了 TCN 和循环架构在合成压力测试、复调音乐建模、字符级语言建模和单词级语言建模任务上的评估结果。一般 TCN 架构在全部任务和数据集上都比经典循环网络性能优秀，上标 h 代表数值越高越好，l 代表数值越低越好。

从经典的隐马尔科夫模型到现在基于循环神经网络与卷积神经网络的深度方法，序列建模已经走过了很长一段旅程，它对于自然语言处理与语音识别等都非常重要。本文只是简单的介绍了基础的序列建模深度方法，它还有很多地方需要探索与讨论，那么让我们真真切切地去了解它吧。
