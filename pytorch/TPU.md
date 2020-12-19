

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 14:48:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 21:01:07
 * @Description:
 * @TODO::
 * @Reference:
-->
没必要买了，Google Colab有免费的TPU，至少相当于4卡GPU的速度[1]

知道TPU有多快么？常规训练一个Resnet50只要10个小时，和8卡V100的速度相当。直接花钱用TPU也不贵，抢占式的TPUV2 8核，一个小时只要1.35美元，性价比比GPU高太多了，想跑超大规模的模型，还可以选择TPUV3，TPUV2 32核、 128核、256核。。。[2]

Installing packages for preparing the system
We are installing 2 packages for the purposes of TPU execution and f1 metric score calculation respectively You can skip this step if you already have these libraries installed in your environment[3]

```
!curl -q https://raw.githubusercontent.com/pytorch/xla/master/contrib/scripts/env-setup.py -o pytorch-xla-env-setup.py
!python pytorch-xla-env-setup.py --apt-packages libomp5 libopenblas-dev
!pip -q install seqeval
!pip install transformers
```

# Importing pytorch and the library for TPU execution

import torch
import torch_xla
import torch_xla.core.xla_model as xm
# Preparing for TPU usage
dev = xm.xla_device()


[1]: 2019 年，如何配置一台以机器学习、深度学习为用途的工作站？ - Wendell的回答 - 知乎
https://www.zhihu.com/question/310387269/answer/582991883
[2]: 计算资源有限的人如何在Deep Learning领域成长？ - Wendell的回答 - 知乎
https://www.zhihu.com/question/304263105/answer/543461352
[3]: https://colab.research.google.com/github/abhimishra91/transformers-tutorials/blob/master/transformers_ner.ipynb#scrollTo=CuxGlte69_4w
[4]: https://www.kaggle.com/eggwhites2705/transformers-ner
