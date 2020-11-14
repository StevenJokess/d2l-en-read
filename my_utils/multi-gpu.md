

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 23:08:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-14 01:05:14
 * @Description:
 * @TODO::
 * @Reference:
-->

#

[1]: https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
```py
# Handle multi-gpu if desired
if (device.type == 'cuda') and (ngpu > 1):
    netD = nn.DataParallel(netD, list(range(ngpu)))
```


[2]: https://github.com/Lyken17/Efficient-PyTorch
默认数据并行PyTorch, powerd由nn。DataParallel, in-efficienct !首先，由于Python的GIL，多线程不能充分利用所有核心torch/nn/parallel/parallel_apply.py#47。第二，DataParallel“集散”方案，将所有结果集在cuda:0上。这会导致工作负载不平衡，有时OOM尤其当你在运行细分模型时。

神经网络。DistributedDataParllel提供了一种更优雅的解决方案:它不是从不同的线程启动调用，而是从多个进程(没有GIL)开始，并为所有gpu分配一个平衡的工作负载。

(正在进行)详细的脚本和实验数据。
