

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 20:40:02
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5ee648f24314f_YkqkQu1q/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
-->

# ShuffleNet

网络是Megvii Inc. (Face++)提出。 In ARM device, ShuffleNet achieves 13× actual speedup over AlexNet while maintaining comparable accuracy.[6]

Experiments on ImageNet classification and MS COCO object detection demonstrate the superior performance of ShuffleNet over other structures, e.g. lower top-1 error (absolute 7.8%) than recent MobileNet on ImageNet classification task, under the computation budget of 40 MFLOPs.[2]


CNN
分组卷积
ResNet

分组点卷积
通道重排
shufflenet v2
pytorch复现

# 动机

数百层和数千通道，Billions of FLOPs

# 方法

属于直接训练而不是压缩

## 分组点卷积

![分组卷积](img\fenzu.jpg)

给点卷积也分组

分组点卷积某个通道的输出仅来及一部分输入通道，阻止了信息流动，特征表示。

## 通道重排(channel shuffle)

如果我们允许组卷积从不同组中获取输入数据，则输入和输出通道讲完全相关。

对于从上一个组层生成的特征图，可以先将每一个组中的通道划分为几个子组，
然后在下一层中的每个组中使用不同的子组作为输入。


ShuffleNet中的Channel Shuffle操作可以将组间的信息进行交换，并且可以实现端到端的训练。


Group convolution。其中输入特征通道被为G组(图4)，并且对于每个分组的信道独立地执行卷积，则分组卷积计算量是HWNK²M/G，为标准卷积计算量的1/G。
Channel shuffle。Grouped Convlution导致模型的信息流限制在各个group内，组与组之间没有信息交换，这会影响模型的表示能力。因此，需要引入group之间信息交换的机制，即Channel Shuffle操作。

引入的问题：[5]

channel shuffle在工程实现占用大量内存和指针跳转，这部分很耗时。
channel shuffle的规则是人工设计，分组之间信息交流存在随意性，没有理论指导。



## FLOPS

![FLOPs](img\Shuffle_Flops.jp)

```py
import torch
import torch.nn as nn
import torch.nn.functional as F


class ShuffleBlock(nn.Module):
    def __init__(self, groups):
        super(ShuffleBlock, self).__init__()
        self.groups = groups

    def forward(self, x):
        '''Channel shuffle: [N,C,H,W] -> [N,g,C/g,H,W] -> [N,C/g,g,H,w] -> [N,C,H,W]'''
        N,C,H,W = x.size()
        g = self.groups
        return x.view(N,g,C//g,H,W).permute(0,2,1,3,4).reshape(N,C,H,W)

class Bottleneck(nn.Module):
    def __init__(self, in_planes, out_planes, stride, groups):
        super(Bottleneck, self).__init__()
        self.stride = stride

        mid_planes = out_planes/4
        g = 1 if in_planes==24 else groups
        self.conv1 = nn.Conv2d(in_planes, mid_planes, kernel_size=1, groups=g, bias=False)
        self.bn1 = nn.BatchNorm2d(mid_planes)
        self.shuffle1 = ShuffleBlock(groups=g)
        self.conv2 = nn.Conv2d(mid_planes, mid_planes, kernel_size=3, stride=stride, padding=1, groups=mid_planes, bias=False)
        self.bn2 = nn.BatchNorm2d(mid_planes)
        self.conv3 = nn.Conv2d(mid_planes, out_planes, kernel_size=1, groups=groups, bias=False)
        self.bn3 = nn.BatchNorm2d(out_planes)

        self.shortcut = nn.Sequential()
        if stride == 2:
            self.shortcut = nn.Sequential(nn.AvgPool2d(3, stride=2, padding=1))

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.shuffle1(out)
        out = F.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out))
        res = self.shortcut(x)
        out = F.relu(torch.cat([out,res], 1)) if self.stride==2 else F.relu(out+res)
        return out

def ShuffleNetG2():
    cfg = {
        'out_planes': [200,400,800],
        'num_blocks': [4,8,4],
        'groups': 2
    }
    return ShuffleNet(cfg)

def ShuffleNetG3():
    cfg = {
        'out_planes': [240,480,960],
        'num_blocks': [4,8,4],
        'groups': 3
    }
    return ShuffleNet(cfg)


def test():
    net = ShuffleNetG2()
    x = torch.randn(1,3,32,32)
    y = net(x)
    print(y)
```




ShuffleNet和ResNet结构可知，ShuffleNet计算量降低主要是通过分组卷积实现。ShuffleNet虽然降低了计算量，但是引入两个新的问题：[4]

1、channel shuffle在工程实现占用大量内存和指针跳转，这部分很耗时。
2、channel shuffle的规则是人工设计，分组之间信息交流存在随意性，没有理论指导。


## Comparison with MobileNetV1

- ShuffleNet models are superior to MobileNetV1 for all the complexities.
- Though ShuffleNet network is specially designed for small models (< 150 MFLOPs), it is still better than MobileNetV1 for higher computation cost, e.g. 3.1% more accurate than MobileNetV1 at the cost of 500 MFLOPs.
- The simple architecture design also makes it easy to equip ShuffeNets with the latest advances such as Squeeze-and-Excitation (SE) blocks. (Hope I can review SENet in the future.)
- ShuffleNets with SE modules boosting the top-1 error of ShuffleNet 2× to 24.7%, but are usually 25 to 40% slower than the “raw” ShuffleNets on mobile devices, which implies that actual speedup evaluation is critical on low-cost architecture design.

[1]: https://ai.deepshare.net/detail/v_5ee645312d94a_eMNJ5Jws/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
[2]: https://arxiv.org/abs/1707.01083
[3]: https://github.com/kuangliu/pytorch-cifar/blob/master/models/shufflenet.py
[4]: https://zhuanlan.zhihu.com/p/45496826
[5]: https://cygao.xyz/2019/07/12/lightweight/
[6]: https://towardsdatascience.com/review-shufflenet-v1-light-weight-model-image-classification-5b253dfe982f
