

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 16:28:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 16:28:56
 * @Description:
 * @TODO::
 * @Reference:
-->

## nvidia-smi和nvcc -V命令结果不一致问题[1]

cudaGetDevice() failed. Status: CUDA driver version is insufficient for CUDA runtime version

CUDA有两种API，运行时API和驱动API，即所谓的Runtime API与Driver API。nvidia-smi的结果除了有GPU驱动版本型号，还有CUDA Driver API的型号，而nvcc得结果对应CUDA Runtime API。
遇到两者不一致问题，我们可以查看 https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html 确定版本是否兼容。

[1]: https://zhuanlan.zhihu.com/p/140080836
