# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-21 22:21:41
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-21 22:22:12
Description:
TODO::
Reference:https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/pix2pix/pix2pix.py
'''
import os

os.makedirs("images/%s" % opt.dataset_name, exist_ok=True)
os.makedirs("saved_models/%s" % opt.dataset_name, exist_ok=True)

