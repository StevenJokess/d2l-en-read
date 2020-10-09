# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 17:29:30
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 17:30:20
Description:
前几个月放映的头号玩家简直火得不能再火了，作为一个探索终极AI的研究人员，月神自然去看了此神剧。
由于太过兴奋，晚上月神做了一个奇怪的梦，月神梦见自己掉入了一个被施放了魔法的深渊，月神想要爬上此深渊。

已知深渊有N层台阶构成（1 <= N <= 1000)，并且每次月神仅可往上爬2的整数次幂个台阶(1、2、4、....)，请你编程告诉月神，月神有多少种方法爬出深渊

TODO::
Reference:https://www.nowcoder.com/questionTerminal/55e34723b1d34c42af83b39de2395408
'''

#coding=utf-8
def stair(m):#动态规划
    import math #导入对数哈函数
    re=[]#实现记忆
    for n in range(m+1):#从0~m进行计算
        if n==0:#边界条件
            re.append(1)
        elif n==1:
            re.append(1)
        else:
            d,s=int(math.log(n,2)),0#找到最接近的2**i，如n=5时，d=2
            for i in range(d+1):
                s+=re[n-2**i]#re[n]=re[n-2**i]+re[n-2**(i-1)]+.....+re[n-2**0]
            re.append(s)
    return re[-1]
while 1:
    try:
        n=int(input())
        for i in range(n):
            print(stair(int(input()))%1000000003)#防止溢而取模
    except:
        break
