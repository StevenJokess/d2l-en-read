

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 16:28:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 17:33:10
 * @Description:
 * @TODO::
 * @Reference:https://github.com/janvdp/code-snippets
-->

Deep Learning
# Get your CUDA Drive version

nvcc --version

## nvidia-smi和nvcc -V命令结果不一致问题[1]

cudaGetDevice() failed. Status: CUDA driver version is insufficient for CUDA runtime version

CUDA有两种API，运行时API和驱动API，即所谓的Runtime API与Driver API。nvidia-smi的结果除了有GPU驱动版本型号，还有CUDA Driver API的型号，而nvcc得结果对应CUDA Runtime API。
遇到两者不一致问题，我们可以查看 https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html 确定版本是否兼容。

[2]
        FloatTensor = torch.cuda.FloatTensor if x.is_cuda else torch.FloatTensor
        LongTensor = torch.cuda.LongTensor if x.is_cuda else torch.LongTensor

[1]: https://zhuanlan.zhihu.com/p/140080836
[2]: https://blog.csdn.net/weixin_44791964/article/details/106214657
