

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-11 22:01:55
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 19:29:58
 * @Description:
 * @TODO::
 * @Reference:https://github.com/pytorch/pytorch#adjust-build-options-optional
-->

Pytorch则是从Tensor到Variable再到nn.Module，最新的Pytorch已经将Tensor和Variable合并，这分别就是从数据张量到网络的抽象层次的递进。[1]

Pytorch的torchvision模块中提供了一个dataset 包，它包含了一些基本的数据集如mnist、coco、imagenet和一个通用的数据加载器ImageFolder。


Dynamic Neural Networks: Tape-Based Autograd
PyTorch has a unique way of building neural networks: using and replaying a tape recorder.

torch.jit	a compilation stack (TorchScript) to create serializable and optimizable models from PyTorch code

torch.multiprocessing	Python multiprocessing, but with magical memory sharing of torch Tensors across processes. Useful for data loading and Hogwild training

> https://github.com/kuangliu/dgl/blob/master/gcn.py
inputs = torch.FloatTensor(data.features)
labels = torch.LongTensor(data.labels)
test_mask = torch.BoolTensor(data.train_mask)
train_mask = torch.BoolTensor(data.test_mask)



