

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-26 21:14:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-26 21:18:14
 * @Description:
 * @TODO::
 * @Reference:https://github.com/zhangjiekui/myNotes/blob/master/d2l/0.0%20env_test.ipynb
-->

import tensorflow as tf
import mxnet as mx
from mxnet import np as mxnp
from mxnet import npx as npx
npx.set_np()
import numpy as np

from d2l import mxnet as mxd2l  # Use MXNet as the backend
from d2l import torch as tcd2l  # Use PyTorch as the backend
from d2l import tensorflow as tfd2l  # Use TensorFlow as the backend

tc.__version__,tf.__version__,mx.__version__

# !pip install --upgrade elyra && jupyter lab build
# !conda install -c conda-forge elyra && jupyter lab build

!jupyter serverextension list
!jupyter labextension list

tc.__version__,tc.cuda.current_device(),tc.cuda.get_device_name(0)
mx.__version__,mx.test_utils.list_gpus(),mx.gpu()
tf.__version__,tf.test.gpu_device_name()
tf.test.is_gpu_available(),

tf.config.list_physical_devices('GPU')

from tensorflow.python.client import device_lib
local_device_protos = device_lib.list_local_devices()
[print(x) for x in local_device_protos if x.device_type == 'GPU']
local_device_protos
!conda list
