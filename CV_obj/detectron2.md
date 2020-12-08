

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 20:02:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 18:58:16
 * @Description:
 * @TODO::
 * @Reference:https://github.com/facebookresearch/detectron2s
 * https://www.jianshu.com/p/a88d7e25a221
-->

https://detectron2.readthedocs.io/notes/benchmarks.html

dockerhub上的几种类型：

a. base: starting from CUDA 9.0, contains the bare minimum (libcudart) to deploy a pre-built CUDA application. Use this image if you want to manually select which CUDA packages you want to install.
b. runtime: extends the base image by adding all the shared libraries from the CUDA toolkit. Use this image if you have a pre-built application using multiple CUDA libraries.
c. devel: extends the runtime image by adding the compiler toolchain, the debugging tools, the headers and the static libraries. Use this image to compile a CUDA application from sources.

通过docker镜像创建容器
创建容器需要加--shm-size=8gb，如果不加可能会出现RuntimeError: unable to write to file这样的错误
docker run --gpus all -it \
    --shm-size=8gb --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --name=detectron2 detectron2:v0
如果出现上述错误，可以在运行代码开始加入下面代码来解决

import sys
import torch
from torch.utils.data import dataloader
from torch.multiprocessing import reductions
from multiprocessing.reduction import ForkingPickler

default_collate_func = dataloader.default_collate


def default_collate_override(batch):
  dataloader._use_shared_memory = False
  return default_collate_func(batch)

setattr(dataloader, 'default_collate', default_collate_override)

for t in torch._storage_classes:
  if sys.version_info[0] == 2:
    if t in ForkingPickler.dispatch:
        del ForkingPickler.dispatch[t]
  else:
    if t in ForkingPickler._extra_reducers:
        del ForkingPickler._extra_reducers[t]
创建完容器后，进入容器运行，当下面语句出值为有效值时就可以源码安装detectron2了。这里要注意的是如果拉的镜像是runtime版的，下面语句CUDA_HOME输出为None，而且nvcc也是没有的
python -c 'import torch; from torch.utils.cpp_extension import CUDA_HOME; print(torch.cuda.is_a

git clone https://github.com/facebookresearch/detectron2.git
python -m pip install -e detectron2
