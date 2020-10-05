# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-05 21:24:15
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-05 21:26:05
Description:
TODO::
Reference:https://github.com/enhuiz/transformer-pytorch/blob/master/scripts/train.py
'''
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=str)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    # opts = parse_config(args.config)
    # print(opts)
