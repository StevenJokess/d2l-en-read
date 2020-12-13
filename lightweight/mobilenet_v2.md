

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:01:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 00:05:00
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/hub/pytorch_vision_mobilenet_v2/
 * https://arxiv.org/abs/1801.04381
 * https://colab.research.google.com/github/pytorch/pytorch.github.io/blob/master/assets/hub/pytorch_vision_mobilenet_v2.ipynb#scrollTo=7P8C3gMea8FU
 * https://heartbeat.fritz.ai/pytorch-mobile-image-classification-on-android-5c0cfb774c5b
 * [4]: https://engineering.fb.com/2018/10/29/ml-applications/qnnpack/
 * [5]: https://paddleclas.readthedocs.io/zh_CN/latest/models/Mobile.html
-->

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

所有的预训练模型都期望输入图像以同样的方式归一化，即小批3通道RGB图像的形状(3 x H x W)，其中H和W预计至少为224。图像加载到范围为[0,1]，然后使用mean =[0.485, 0.456, 0.406]和std =[0.229, 0.224, 0.225]进行归一化。

模型描述

MobileNet v2架构基于一个反向残差结构，其中残差块的输入和输出是薄的瓶颈层，与传统残差模型相反，后者在输入中使用扩展表示。MobileNet v2使用轻量级深度卷积来过滤中间扩展层的特征。此外，为了保持代表性，在狭窄的层中去除了非线性。




Model Description
The MobileNet v2 architecture is based on an inverted residual structure where the input and output of the residual block are thin bottleneck layers opposite to traditional residual models which use expanded representations in the input. MobileNet v2 uses lightweight depthwise convolutions to filter features in the intermediate expansion layer. Additionally, non-linearities in the narrow layers were removed in order to maintain representational power.


Model structure	Top-1 error	Top-5 error
mobilenet_v2	28.12	9.71

MobileNet v2架构是基于一个倒置的残差结构，其中残差块的输入和输出是薄瓶颈层，与传统的残差模型相反，传统的残差模型在输入中使用扩展表示。MobileNet v2使用轻量级的深度卷积来过滤中间扩展层的特性。此外，为了保持代表性，在窄层中去除非线性。

相比MobileNetV1，MobileNetV2提出了Linear bottlenecks与Inverted residual block作为网络基本结构，通过大量地堆叠这些基本模块，构成了MobileNetV2的网络结构。最终，在FLOPS只有MobileNetV1的一半的情况下取得了更高的分类精度。[5]

| Model structure | Top-1 error | Top-5 error |
| --------------- | ----------- | ----------- |
|  mobilenet_v2       | 28.12       | 9.71       |


[4]: caffe2 72.14% TensorFlow Lite 70.8%
