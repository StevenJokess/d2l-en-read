

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-26 21:09:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 23:35:02
 * @Description:
 * @TODO::
 * @Reference:https://github.com/thu-ml/tianshou/commit/0c944eab68064288629188174afbdc5a9a05fece
https://github.com/ShusenTang/Dive-into-DL-PyTorch/blob/master/code/d2lzh_pytorch/__init__.py
https://github.com/thu-ml/tianshou/blob/master/tianshou/__init__.py
-->

import os
from .utils import *

name = 'tianshou'
__version__ = '0.2.0'

---

from tianshou import data, env, utils, policy, trainer, exploration


__version__ = "0.3.0"

__all__ = [
    "env",
    "data",
    "utils",
    "policy",
    "trainer",
    "exploration",
]
