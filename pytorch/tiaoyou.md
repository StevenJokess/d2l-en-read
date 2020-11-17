

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 20:03:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 20:03:58
 * @Description:
 * @TODO::
 * @Reference:
-->

https://0809zheng.github.io/2020/09/16/eccv-tutorial.html

use async data loading / augmentation
enable cuDNN autotuner
increase batch size
remove unnecessary computation
use DistributedDataParallel instead of DataParallel
efficiently zero-out gradients
apply PyTorch JIT to fuse pointwise operations
checkpoint to recompute intermediates

