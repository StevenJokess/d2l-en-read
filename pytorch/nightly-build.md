

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 22:37:38
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 22:42:13
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/tutorials/intermediate/quantized_transfer_learning_tutorial.html
 * https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/quantized_transfer_learning_tutorial.ipynb#scrollTo=RNyQYNhnrW21
-->

```
pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
# For CUDA support use https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html
```

```jupyter
!yes y | pip uninstall torch torchvision
!yes y | pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html
```

Uninstalling torch-1.7.0+cu101:
  Would remove:
    /usr/local/bin/convert-caffe2-to-onnx
    /usr/local/bin/convert-onnx-to-caffe2
    /usr/local/lib/python3.6/dist-packages/caffe2/*
    /usr/local/lib/python3.6/dist-packages/torch-1.7.0+cu101.dist-info/*
    /usr/local/lib/python3.6/dist-packages/torch/*
Proceed (y/n)? y
y
y

y
y

  Successfully uninstalled torch-1.7.0+cu101
Uninstalling torchvision-0.8.1+cu101:
  Would remove:
    /usr/local/lib/python3.6/dist-packages/torchvision-0.8.1+cu101.dist-info/*
    /usr/local/lib/python3.6/dist-packages/torchvision.libs/libcudart.c740f4ef.so.10.1
    /usr/local/lib/python3.6/dist-packages/torchvision.libs/libjpeg.ceea7512.so.62
    /usr/local/lib/python3.6/dist-packages/torchvision.libs/libpng16.7f72a3c5.so.16
    /usr/local/lib/python3.6/dist-packages/torchvision.libs/libz.1328edc3.so.1
    /usr/local/lib/python3.6/dist-packages/torchvision/*
Proceed (y/n)?   Successfully uninstalled torchvision-0.8.1+cu101
Looking in links: https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html
Collecting torch
  Downloading https://download.pytorch.org/whl/nightly/cu101/torch-1.8.0.dev20201207%2Bcu101-cp36-cp36m-linux_x86_64.whl (787.8MB)
     |████████████████████████████████| 787.8MB 16kB/s
Collecting torchvision
  Downloading https://download.pytorch.org/whl/nightly/cu101/torchvision-0.9.0.dev20201207%2Bcu101-cp36-cp36m-linux_x86_64.whl (18.2MB)
     |████████████████████████████████| 18.2MB 170kB/s
Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from torch) (1.18.5)
Requirement already satisfied: typing-extensions in /usr/local/lib/python3.6/dist-packages (from torch) (3.7.4.3)
Requirement already satisfied: dataclasses; python_version < "3.7" in /usr/local/lib/python3.6/dist-packages (from torch) (0.8)
Requirement already satisfied: pillow>=4.1.1 in /usr/local/lib/python3.6/dist-packages (from torchvision) (7.0.0)
Installing collected packages: torch, torchvision
Successfully installed torch-1.8.0.dev20201207+cu101 torchvision-0.9.0.dev20201207+cu101
