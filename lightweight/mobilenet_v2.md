

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:01:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-30 20:42:38
 * @Description:
 * @TODO::
 * @Reference:
-->

# MobileNet-v2

MobileNet模型是Google针对手机等嵌入式设备提出的一种轻量级的深层神经网络，其使用的核心思想便是depthwise separable convolution。

The MobilenetV2 with depthwise convolution and inverted residuals has fewer operations(faster) and less parameters(smaller) compared to other models. Additionally, it has a tunable depth-multiplier parameter(speed-accuracy) for application specific requirements.[7]


MobileNet-v2 [9] utilizes a module architecture similar to the residual unit with bottleneck architecture of ResNet; the modified version of the residual unit where conv3x3 is replaced by depthwise convolution.




As you can see from the above, contrary to the standard bottleneck architecture, the first conv1x1 increases the channel dimension, then depthwise conv is performed, and finally the last conv1x1 decreases the channel dimension.



By reordering the building blocks as above and comparing it with MobileNet-v1 (separable conv), we can see how this architecture works (this reordering does not change the overall model architecture because the MobileNet-v2 is the stack of this module).
That is to say, the above module be regarded as a modified version of separable conv where the single conv1x1 in separable conv is factorized into two conv1x1s. Letting T denote an expansion factor of channel dimension, the computational cost of two conv1x1s is 2HWN²/T while that of conv1x1 in separable conv is HWN². In [5], T = 6 is used, reducing the computational cost for conv1x1 by a factor of 3 (T/2 in general).



MobileNetV2是MobileNet的升级版，它具有两个特征点：

1、Inverted residuals，在ResNet50里我们认识到一个结构，bottleneck design结构，在3x3网络结构前利用1x1卷积降维，在3x3网络结构后，利用1x1卷积升维，相比直接使用3x3网络卷积效果更好，参数更少，先进行压缩，再进行扩张。而在MobileNetV2网络部分，其采用Inverted residuals结构，在3x3网络结构前利用1x1卷积升维，在3x3网络结构后，利用1x1卷积降维，先进行扩张，再进行压缩。

2、Linear bottlenecks，为了避免Relu对特征的破坏，在在3x3网络结构前利用1x1卷积升维，在3x3网络结构后，再利用1x1卷积降维后，不再进行Relu6层，直接进行残差网络的加法。[6]

```python
import torch
model = torch.hub.load('pytorch/vision:v0.6.0', 'mobilenet_v2', pretrained=True)
model.eval()
```

```python
import torch
from torchvision.models import mobilenet_v2

model = mobilenet_v2(pretrained=True)

model.eval()
input_tensor = torch.rand(1,3,224,224)

script_model = torch.jit.trace(model,input_tensor)
script_model.save("mobilenet-v2.pt")
```

---

```py
#[8]
import torch
import torchvision
import yaml

# Save traced TorchScript model.
traced_script_module.save("MobileNetV2.pt")

# Dump root ops used by the model (for custom build optimization).
ops = torch.jit.export_opnames(traced_script_module)

with open('MobileNetV2.yaml', 'w') as output:
    yaml.dump(ops, output)
```


所有的预训练模型都期望输入图像以同样的方式归一化，即小批3通道RGB图像的形状(3 x H x W)，其中H和W预计至少为224。图像加载到范围为[0,1]，然后使用mean =[0.485, 0.456, 0.406]和std =[0.229, 0.224, 0.225]进行归一化。

模型描述

MobileNet v2架构基于一个反向残差结构，其中残差块的输入和输出是薄的瓶颈层，与传统残差模型相反，后者在输入中使用扩展表示。MobileNet v2使用轻量级深度卷积来过滤中间扩展层的特征。此外，为了保持代表性，在狭窄的层中去除了非线性。




Model Description
The MobileNet v2 architecture is based on an inverted residual structure where the input and output of the residual block are thin bottleneck layers opposite to traditional residual models which use expanded representations in the input. MobileNet v2 uses lightweight depthwise convolutions to filter features in the intermediate expansion layer. Additionally, non-linearities in the narrow layers were removed in order to maintain representational power.


Model structure	Top-1 error	Top-5 error
mobilenet_v2	28.12	9.71

MobileNet v2架构是基于一个倒置的残差结构，其中残差块的输入和输出是薄瓶颈层，与传统的残差模型相反，传统的残差模型在输入中使用扩展表示。MobileNet v2使用轻量级的深度卷积来过滤中间扩展层的特性。此外，为了保持代表性，在窄层中去除非线性。

相比MobileNetV1，MobileNetV2提出了Linear bottlenecks与Inverted residual block作为网络基本结构，通过大量地堆叠这些基本模块，构成了MobileNetV2的网络结构。最终，在FLOPS只有MobileNetV1的一半的情况下取得了更高的分类精度。[5]

继续使用Mobilenet V1的深度可分离卷积降低卷积计算量。
增加skip connection，使前向传播时提供特征复用。
采用Inverted residual block结构。该结构使用Point wise convolution先对feature map进行升维，再在升维后的特征接ReLU，减少ReLU对特征的破坏。[9]

| Model structure | Top-1 error | Top-5 error |
| --------------- | ----------- | ----------- |
|  mobilenet_v2       | 28.12       | 9.71       |



```py
#[6]
class MobileNetV2(nn.Module):
    def __init__(self, n_class=1000, input_size=224, width_mult=1.):
        super(MobileNetV2, self).__init__()
        block = InvertedResidual
        input_channel = 32
        last_channel = 1280

        interverted_residual_setting = [
            # t, c, n, s
            # 473,473,3 -> 237,237,32
            # 237,237,32 -> 237,237,16
            [1, 16, 1, 1],
            # 237,237,16 -> 119,119,24
            [6, 24, 2, 2],
            # 119,119,24 -> 60,60,32
            [6, 32, 3, 2],
            # 60,60,32 -> 30,30,64
            [6, 64, 4, 2],
            # 30,30,64 -> 30,30,96
            [6, 96, 3, 1],
            # 30,30,96 -> 15,15,160
            [6, 160, 3, 2],
            # 15,15,160 -> 15,15,320
            [6, 320, 1, 1],
        ]

        assert input_size % 32 == 0
        # 建立stem层
        input_channel = int(input_channel * width_mult)
        self.last_channel = int(last_channel * width_mult) if width_mult > 1.0 else last_channel

        self.features = [conv_bn(3, input_channel, 2)]

        # 根据上述列表进行循环，构建mobilenetv2的结构
        for t, c, n, s in interverted_residual_setting:
            output_channel = int(c * width_mult)
            for i in range(n):
                if i == 0:
                    self.features.append(block(input_channel, output_channel, s, expand_ratio=t))
                else:
                    self.features.append(block(input_channel, output_channel, 1, expand_ratio=t))
                input_channel = output_channel

        # mobilenetv2结构的收尾工作
        self.features.append(conv_1x1_bn(input_channel, self.last_channel))
        self.features = nn.Sequential(*self.features)

        # 最后的分类部分
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
            elif isinstance(m, BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                n = m.weight.size(1)
                m.weight.data.normal_(0, 0.01)
                m.bias.data.zero_()

def load_url(url, model_dir='./model_data', map_location=None):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    filename = url.split('/')[-1]
    cached_file = os.path.join(model_dir, filename)
    if os.path.exists(cached_file):
        return torch.load(cached_file, map_location=map_location)
    else:
        return model_zoo.load_url(url,model_dir=model_dir)

def mobilenetv2(pretrained=False, **kwargs):
    model = MobileNetV2(n_class=1000, **kwargs)
    if pretrained:
        model.load_state_dict(load_url('http://sceneparsing.csail.mit.edu/model/pretrained_resnet/mobilenet_v2.pth.tar'), strict=False)
    return model
```



[4]: caffe2 72.14% TensorFlow Lite 70.8%

[0]: https://pytorch.org/hub/pytorch_vision_mobilenet_v2/
[1]: https://arxiv.org/abs/1801.04381
[2]: https://colab.research.google.com/github/pytorch/pytorch.github.io/blob/master/assets/hub/pytorch_vision_mobilenet_v2.ipynb#scrollTo=7P8C3gMea8FU
[3]: https://heartbeat.fritz.ai/pytorch-mobile-image-classification-on-android-5c0cfb774c5b
[4]: https://engineering.fb.com/2018/10/29/ml-applications/qnnpack/
[5]: https://paddleclas.readthedocs.io/zh_CN/latest/models/Mobile.html
[6]: https://blog.csdn.net/weixin_44791964/article/details/102851214
[7]: https://github.com/anilsathyan7/pytorch-image-classification
[8]: https://github.com/pytorch/pytorch/blob/master/android/test_app/make_assets_custom.py
[9]: https://cygao.xyz/2019/07/12/lightweight/
