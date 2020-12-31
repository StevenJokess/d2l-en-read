

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:56:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-31 01:38:56
 * @Description:
 * @TODO::
 * @Reference:https://ai.deepshare.net/detail/v_5ee644a796c35_tAwVkVvK/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
 * https://ai.deepshare.net/detail/v_5ee644d9ed5d3_17ThW2c9/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
 * https://ai.deepshare.net/detail/v_5ee645075753a_qSt7UuAU/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
 * [5]: https://paddleclas.readthedocs.io/zh_CN/latest/models/Mobile.html
 * [6]: https://github.com/shicai/MobileNet-Caffe
 * [7]: https://www.zhihu.com/question/58941804
-->

该网络将传统的卷积操作替换深度可分离卷积，即Depthwise卷积和Pointwise卷积的组合，相比传统的卷积操作，该组合可以大大节省参数量和计算量。与此同时，MobileNetV1也可以用于目标检测、图像分割等其他视觉任务中。[5]

%%writefile ../d2cl/chapter_lightweight/index.md

# Introduction
:label:`chap_lightweight`

```toc
:maxdepth: 2

mobilenet
```

```py
pip install --upgrade --pre --find-links https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html torch==1.8.0.dev20201106+cpu torchvision==0.9.0.dev20201107+cpu
```

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
# [3]
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

```py
[4]
import torch.nn as nn
import math


def conv_bn(inp, oup, stride):
    return nn.Sequential(
        nn.Conv2d(inp, oup, 3, stride, 1, bias=False),
        nn.BatchNorm2d(oup),
        nn.ReLU6(inplace=True)
    )


def conv_1x1_bn(inp, oup):
    return nn.Sequential(
        nn.Conv2d(inp, oup, 1, 1, 0, bias=False),
        nn.BatchNorm2d(oup),
        nn.ReLU6(inplace=True)
    )


class InvertedResidual(nn.Module):
    def __init__(self, inp, oup, stride, expand_ratio):
        super(InvertedResidual, self).__init__()
        self.stride = stride
        assert stride in [1, 2]

        hidden_dim = round(inp * expand_ratio)
        self.use_res_connect = self.stride == 1 and inp == oup

        if expand_ratio == 1:
            self.conv = nn.Sequential(
                # dw
                nn.Conv2d(hidden_dim, hidden_dim, 3, stride, 1, groups=hidden_dim, bias=False),
                nn.BatchNorm2d(hidden_dim),
                nn.ReLU6(inplace=True),
                # pw-linear
                nn.Conv2d(hidden_dim, oup, 1, 1, 0, bias=False),
                nn.BatchNorm2d(oup),
            )
        else:
            self.conv = nn.Sequential(
                # pw
                nn.Conv2d(inp, hidden_dim, 1, 1, 0, bias=False),
                nn.BatchNorm2d(hidden_dim),
                nn.ReLU6(inplace=True),
                # dw
                nn.Conv2d(hidden_dim, hidden_dim, 3, stride, 1, groups=hidden_dim, bias=False),
                nn.BatchNorm2d(hidden_dim),
                nn.ReLU6(inplace=True),
                # pw-linear
                nn.Conv2d(hidden_dim, oup, 1, 1, 0, bias=False),
                nn.BatchNorm2d(oup),
            )

    def forward(self, x):
        if self.use_res_connect:
            return x + self.conv(x)
        else:
            return self.conv(x)


class MobileNetV2(nn.Module):
    def __init__(self, n_class=1000, input_size=224, width_mult=1.):
        super(MobileNetV2, self).__init__()
        block = InvertedResidual
        input_channel = 32
        last_channel = 1280
        interverted_residual_setting = [
            # t, c, n, s
            [1, 16, 1, 1],
            [6, 24, 2, 2],
            [6, 32, 3, 2],
            [6, 64, 4, 2],
            [6, 96, 3, 1],
            [6, 160, 3, 2],
            [6, 320, 1, 1],
        ]

        # building first layer
        assert input_size % 32 == 0
        input_channel = int(input_channel * width_mult)
        self.last_channel = int(last_channel * width_mult) if width_mult > 1.0 else last_channel
        self.features = [conv_bn(3, input_channel, 2)]
        # building inverted residual blocks
        for t, c, n, s in interverted_residual_setting:
            output_channel = int(c * width_mult)
            for i in range(n):
                if i == 0:
                    self.features.append(block(input_channel, output_channel, s, expand_ratio=t))
                else:
                    self.features.append(block(input_channel, output_channel, 1, expand_ratio=t))
                input_channel = output_channel
        # building last several layers
        self.features.append(conv_1x1_bn(input_channel, self.last_channel))
        # make it nn.Sequential
        self.features = nn.Sequential(*self.features)

        # building classifier
        self.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(self.last_channel, n_class),
        )

        self._initialize_weights()

    def forward(self, x):
        x = self.features(x)
        x = x.mean(3).mean(2)
        x = self.classifier(x)
        return x

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


```
#[5]
import torch
model = torch.hub.load('pytorch/vision:v0.6.0', 'mobilenet_v2', pretrained=True)
model.eval()
```

TODO:
(PROTOTYPE) CONVERT MOBILENETV2 TO NNAPI
https://pytorch.org/tutorials/prototype/nnapi_mobilenetv2.html



```py
pip install --upgrade --pre --find-links https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html torch==1.8.0.dev20201106+cpu torchvision==0.9.0.dev20201107+cpu
```


這邊把各個Block多用一層Sequential包起來是因為Network Pruning的時候抓Layer比較方便。

import torchvision.models.quantization.mobilenet


MobileNetV1[6]
The first version of the MobileNet architecture pioneered the use of depthwise convolutions to make a model more suitable for mobile devices. MobileNetV1 consists almost entirely of 1×1 convolutions and depthwise 3×3 convolutions. We converted the quantized MobileNetV1 model from TensorFlow Lite and benchmarked it on 32-bit ARM builds of TensorFlow Lite and QNNPACK. With both runtimes using 4 threads, we observed 1.8x geomean speedup of QNNPACK over the TensorFlow Lite runtime.

深度可分离卷积（Depthwise separable convolution）代替标准的卷积，并使用宽度因子(width multiply)减少参数量。深度可分离卷积把标准的卷积因式分解成一个深度卷积(depthwise convolution)和一个逐点卷积(pointwise convolution)。[7]


[1]: https://arxiv.org/abs/1704.04861 MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications
[2]: https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md
[3]: https://github.com/mit-han-lab/amc/blob/master/models/mobilenet.py
[4]: https://github.com/mit-han-lab/amc/blob/master/models/mobilenet_v2.py
[5]: https://pytorch.org/hub/pytorch_vision_mobilenet_v2/s
[6]: https://engineering.fb.com/2018/10/29/ml-applications/qnnpack/
[7]: https://cygao.xyz/2019/07/12/lightweight/

https://github.com/0809zheng/Hung-yi-Lee-ML2020-homework/blob/master/hw7_Network_Compression/hw7_Architecture_Design.ipynb
