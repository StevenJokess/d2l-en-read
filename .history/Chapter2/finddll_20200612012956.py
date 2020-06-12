#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-12 01:29:55
@LastEditors: steven
@LastEditTime: 2020-06-12 01:29:56
@Description:
'''
import psutil, os
p = psutil.Process( os.getpid() )
for dll in p.memory_maps():
  print(dll.path)
