# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-11 11:34:34
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-11 11:44:22
Description:
TODO::
Reference:
'''
#coding = utf-8

import sys

if __name__ == "__main__":
    n_m = sys.stdin.readline().split()
    n = int(n_m[0])
    m = int(n_m[1])

    x_dict = {}

    for i in range(n):
        line = sys.stdin.readline().split()
        x_dict[int(line[0])] = int(line[1])

