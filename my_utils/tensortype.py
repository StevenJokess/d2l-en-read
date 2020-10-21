# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-21 22:24:51
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-21 22:24:56
Description:
TODO::
Reference:https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/pix2pix/pix2pix.py
'''
# Tensor type
Tensor = torch.cuda.FloatTensor if cuda else torch.FloatTensor
