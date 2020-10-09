# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 17:11:41
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 17:12:22
Description:
TODO::
Reference:有一个游戏，玩法如下：一个方块一开始放置在原点，每次投掷一个均匀的六面骰子，掷出几点，将方块往前移动几点；问：当游戏一直进行下去，方块曾经落在2019的概率为
https://www.nowcoder.com/test/question/done?tid=38378708&qid=278438#summary
'''

res = [0]*2019

res[0] = 1/6
res[1] = 1/6 + (1/6)**2
res[2] = res[1]/6 + res[0]/6 + 1/6
res[3] = res[2]/6 + res[1]/6 + res[0]/6 +1/6
res[4] = res[3]/6 + res[2]/6 + res[1]/6 + res[0]/6 +1/6
res[5] = res[4]/6 + res[3]/6 + res[2]/6 + res[1]/6 + res[0]/6 +1/6

for i in range(6,2019):
    res[i] = sum(res[i-6:i])/6

print(res[-1])
