

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 21:47:35
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5ee644a796c35_tAwVkVvK/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
 * https://ai.deepshare.net/detail/v_5ee644d9ed5d3_17ThW2c9/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
 * https://ai.deepshare.net/detail/v_5ee645075753a_qSt7UuAU/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
-->

## ResNet

## Activation

## 轻量化网络的客观需求

小、速度

## 本文方法

根据应用需求与资源限制（延迟，大小）
优化延迟
深度可分离卷积 设置两个超参数：balance准确率与延迟




## 结构

通过步长来降采样
(n+2p-f)/s + 1* (n+2p-f)/s + 1
尺度维度变化

## 深度可分离卷积

深度卷积负责各个通道
点卷积1*1*M，每个卷积一个像素



深度可分离卷积 分为 深度卷积和 点卷积

![普通卷积vs深度可分离卷积](img\depth_sep.jpg)

TODO:https://ai.deepshare.net/detail/v_5ee645312d94a_eMNJ5Jws/3?from=p_5ee641d2e8471_5z8XYfL6&type=6

```py
import torch.nn as nn
import math


def conv_bn(inp, oup, stride):
    return nn.Sequential(
        nn.Conv2d(inp, oup, 3, stride, 1, bias=False),
        nn.BatchNorm2d(oup),
        nn.ReLU(inplace=True)
    )


def conv_dw(inp, oup, stride):
    return nn.Sequential(
        nn.Conv2d(inp, inp, 3, stride, 1, groups=inp, bias=False),
        nn.BatchNorm2d(inp),
        nn.ReLU(inplace=True),

        nn.Conv2d(inp, oup, 1, 1, 0, bias=False),
        nn.BatchNorm2d(oup),
        nn.ReLU(inplace=True),
    )


class MobileNet(nn.Module):
    def __init__(self, n_class,  profile='normal'):
        super(MobileNet, self).__init__()

        # original
        if profile == 'normal':
            in_planes = 32
            cfg = [64, (128, 2), 128, (256, 2), 256, (512, 2), 512, 512, 512, 512, 512, (1024, 2), 1024]
        # 0.5 AMC
        elif profile == '0.5flops':
            in_planes = 24
            cfg = [48, (96, 2), 80, (192, 2), 200, (328, 2), 352, 368, 360, 328, 400, (736, 2), 752]
        else:
            raise NotImplementedError

        self.conv1 = conv_bn(3, in_planes, stride=2)

        self.features = self._make_layers(in_planes, cfg, conv_dw)

        self.classifier = nn.Sequential(
            nn.Linear(cfg[-1], n_class),
        )

        self._initialize_weights()

    def forward(self, x):
        x = self.conv1(x)
        x = self.features(x)
        x = x.mean(3).mean(2)  # global average pooling

        x = self.classifier(x)
        return x

    def _make_layers(self, in_planes, cfg, layer):
        layers = []
        for x in cfg:
            out_planes = x if isinstance(x, int) else x[0]
            stride = 1 if isinstance(x, int) else x[1]
            layers.append(layer(in_planes, out_planes, stride))
            in_planes = out_planes
        return nn.Sequential(*layers)

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                n = m.weight.size(1)
                m.weight.data.normal_(0, 0.01)
                m.bias.data.zero_()
```





[1]: https://arxiv.org/abs/1704.04861 MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications
[2]: https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md
[3]: https://github.com/mit-han-lab/amc/blob/master/models/mobilenet.py
