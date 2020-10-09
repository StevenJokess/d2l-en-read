# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 13:47:55
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 13:48:12
Description:
TODO::
Reference:https://blog.csdn.net/sinat_30316741/article/details/80018932?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight
'''


#-*- coding:utf-8 -*-
#自己实现计算ks与调包
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
sns.set(font='SimHei')  # 解决Seaborn中文显示问题
