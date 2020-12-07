

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 16:04:12
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 16:21:08
 * @Description:
 * @TODO::
 * @Reference:https://www.zhihu.com/people/liu-yu-fei-62
-->

刚好对 ONNX 和 PyTorch 都还算了解，不邀自来。

简单地说，技术上没有障碍，性价比很有问题。

因为 ONNX → PyTorch 几乎不能解决什么现实问题，但实现起来的工程量却一点也不小。

在 ONNX 从诞生到流行的相当长的一段时间里，ONNX 主要解决的是从五花八门的训练框架到屈指可数的部署方案之间的交流问题。虽然 ONNX 和 onnxruntime 都在探索训练的可能性，也有了实验性的提案和实现，但距离真正可用还有相当遥远的距离。

也正是因为主攻部署，无论是在自身规范的设计上，还是在各大框架导出的实现中，ONNX 只保留了推理所必须的信息，而没有保存有关训练的一切细节，也没有保存模型的层次结构，甚至连绝大多数变量名都被略去了。

话句话说，如果没有其他信息来源，那么从 .onnx 文件中只能恢复出这样的东西

class Model(nn.Module):
    def __init__(self):
        super().__init__()

---

没有训练策略和超参数、没有数据增强方法、没有层次结构，连变量名都只能是数字。显然，这种东西的使用价值是很低的：拿来训练不太现实，用于部署也远不如直接用 ONNX 来的方便。

当然了，如果题主真的需要这么个东西，那么拿这段讨论中提及的脚本改一改大概率还是能用可接受的成本解决问题的

---

https://github.com/pytorch/pytorch/issues/21683

```

import onnx
from onnx import numpy_helper
import torch
from torchvision import models

model = models.resnet18()
torch.onnx.export(model, torch.randn(1, 3, 224, 224), 'resnet18.onnx')

onnx_model = onnx.load('resnet18.onnx')

graph = onnx_model.graph
initalizers = dict()
for init in graph.initializer:
    initalizers[init.name] = numpy_helper.to_array(init)

for name, p in model.named_parameters():
    p.data = (torch.from_numpy(initalizers[name])).data

```
