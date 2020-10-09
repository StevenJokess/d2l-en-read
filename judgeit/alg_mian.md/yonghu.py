# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 19:44:28
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 19:45:24
Description:为了不断优化推荐效果，今日头条每天要存储和处理海量数据。假设有这样一种场景：我们对用户按照它们的注册时间先后来标号，对于一类文章，每个用户都有不同的喜好值，我们会想知道某一段时间内注册的用户（标号相连的一批用户）中，有多少用户对这类文章喜好值为k。因为一些特殊的原因，不会出现一个查询的用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。
TODO::
Reference:
'''

# 一个简单的Python实现，输入数据的时候用字典存起来，然后搜索只用去查找字典里的对应项

n = int(input())
user_list = [int(x) for x in input().split()]
q = int(input())
find = [[int(x) for x in input().split()] for _ in range(q)]

dic = {}
for i in range(n):
    try:
        dic[user_list[i]].append(i + 1)
    except:
        dic[user_list[i]] = [i + 1]
result_list = []

for i in range(q):
    l, r , k = find[i]
    if k not in dic:
        result = 0
    else:
        temp = dic[k]
        result = 0
        if temp[-1] < l or temp[0] > r:
            pass
        else:
            for i in range(len(temp)):
                if l <= temp[i] <= r:
                    result += 1
    result_list.append(result)
for r in result_list:
    print(r)
