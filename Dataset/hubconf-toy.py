# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-22 23:39:37
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-22 23:39:56
Description:
TODO::
Reference:https://github.com/ailzhang/torchhub_example/blob/master/hubconf.py
'''
dependencies = ['torch']
import torch
from model import Net

def mnist(pretrained=False):
    m = Net()
    if pretrained:
        m.load_state_dict(torch.hub.load_state_dict_from_url('https://github.com/ailzhang/torchhub_example/releases/download/0.1/mnist_init_ones'))
    return m

def mnist_tar(pretrained=False):
    m = Net()
    if pretrained:
        m.load_state_dict(torch.hub.load_state_dict_from_url('https://github.com/ailzhang/torchhub_example/releases/download/0.1/mnist_init_ones.tar.gz'))
    return m

def mnist_zip(pretrained=False):
    m = Net()
    if pretrained:
        m.load_state_dict(torch.hub.load_state_dict_from_url('https://github.com/ailzhang/torchhub_example/releases/download/0.1/mnist_init_ones.zip'))
    return m

def mnist_zip_1_6(pretrained=False):
    m = Net()
    if pretrained:
        m.load_state_dict(torch.hub.load_state_dict_from_url('https://github.com/ailzhang/torchhub_example/releases/download/0.1/mnist_init_ones_1_6.zip'))
    return m
