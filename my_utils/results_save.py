# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-19 20:43:54
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-19 20:44:03
Description:
TODO::
Reference:https://github.com/znxlwm/pytorch-pix2pix/blob/master/pytorch_pix2pix.py
'''
# results save path
root = opt.dataset + '_' + opt.save_root + '/'
model = opt.dataset + '_'
if not os.path.isdir(root):
    os.mkdir(root)
if not os.path.isdir(root + 'Fixed_results'):
    os.mkdir(root + 'Fixed_results')
