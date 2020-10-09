# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 18:01:53
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 18:02:03
Description:
TODO::
Reference:
'''
string = input()
for i in sorted(list(set(string))):
    item = string.count(i)
    print(i + str(item), end = '')
