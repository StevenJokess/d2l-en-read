

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 18:47:49
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 18:48:30
 * @Description:https://discuss.d2l.ai/t/linear-algebra/31/2
 * @TODO::
 * @Reference:
-->

pass

pass

yes,pass

first dimension:2

first dimension

not match!


A = torch.arange(20, dtype = torch.float32).reshape(5, 4)

A / A.sum(axis=1)

RuntimeError: The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 1

It will be fine.


B = torch.arange(25, dtype = torch.float32).reshape(5, 5)

B / B.sum(axis=1)

tensor([[0.0000, 0.0286, 0.0333, 0.0353, 0.0364],

    [0.5000, 0.1714, 0.1167, 0.0941, 0.0818],

    [1.0000, 0.3143, 0.2000, 0.1529, 0.1273],

    [1.5000, 0.4571, 0.2833, 0.2118, 0.1727],

    [2.0000, 0.6000, 0.3667, 0.2706, 0.2182]])
Walk:Manhattan’s distance.the â„“1 norm

# distances of avenues and streets

dist_ave = 30.0

dist_str = 40.0

dis_2pt = torch.tensor([dist_ave, dist_str])

torch.abs(dis_2pt).sum()

Can. Fly straightly and diagonally.the â„“2 norm


torch.norm(dis_2pt)

tensor(50.)

The shape is just the shape of the original tensor that deleted the axis required.
X.sum(axis = 0).size() torch.Size([3, 4])

X.sum(axis = 1).size() torch.Size([2, 4])

X.sum(axis = 2).size() torch.Size([2, 3])

$|\mathbf{x}|{2}=\sqrt{\sum{i=1}^{n} x_{i}^{2}}$

Y= torch.arange(24,dtype = torch.float32).reshape(2, 3, 4)

torch.norm(Y)

tensor(65.7571)


i = 0

for j in range(24):

    i += j**2

    j += 1

import math

print(math.sqrt(i))

65.75712889109438

The numbers are same.

For more:

https://pytorch.org/docs/master/generated/torch.norm.html 1

https://www.cnblogs.com/wanghui-garcia/p/11266298.html
