# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-11-10 22:35:22
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-11-10 22:35:24
Description:
TODO::
Reference:https://github.com/eriklindernoren/PyTorch-Deep-Dream/blob/master/deep_dream.py
'''
Tensor = torch.cuda.FloatTensor if torch.cuda.is_available else torch.FloatTensor
