#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-12 01:29:55
@LastEditors: steven
@LastEditTime: 2020-06-12 01:29:56
@Description:https://discuss.pytorch.org/t/pytorch-compiled-from-source-for-windows-is-failing-when-importing-torch/75567/28
'''
import psutil, os
p = psutil.Process( os.getpid() )
for dll in p.memory_maps():
  print(dll.path)
