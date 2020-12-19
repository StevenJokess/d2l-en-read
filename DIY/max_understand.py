# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-20 00:15:16
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-20 00:21:25
Description:
TODO::
Reference:https://discuss.pytorch.org/t/how-does-one-get-the-predicted-classification-label-from-a-pytorch-model/91649/3
'''
import torch

x = torch.tensor([
     [1, 2, 3],
     [4, 5, 6]
   ])

print(f'x.size() = {x.size()}')

# sum the 0th dimension (rows). So we get a bunch of colums that have the rows added together.
x0 = x.sum(0)
print(x0)

# sum the 1th dimension (columns)
x1 = x.sum(1)
print(x1)

x_1 = x.sum(-1)
print(x_1)

x0 = x.max(0)
print(x0.values)

y = torch.tensor([[
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]],

    [[13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]]])

print(y)

# into the screen [1, 13]
print(y[:,0,0])
# columns [1, 5, 9]
print(y[0,:,0])
# rows [1, 2, 3, 4]
print(y[0,0,:])

# for each remaining index, select the largest value in the "screen" dimension
y0 = y.max(0)
print(y0.values)

