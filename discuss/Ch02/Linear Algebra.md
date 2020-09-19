

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:18:47
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:18:49
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_preliminaries/linear-algebra.html
 * @TODO::
 * @Reference:
-->

2 replies
23 Aug
gpk​2000
We can access the scalar element aijaij of a matrix AA in :eqref: eq_matrix_def by specifying the indices for the row (ii) and column (jj), such as [A]ij[A]ij. When the scalar elements of a matrix AA, such as in :eqref: eq_matrix_def

what is :eqref: eq_matrix_def here?

1 reply
24 Aug▶ gpk2000
goldpiggy
Hey @gpk2000, thanks for pointing out the typo. The equation doesn’t render properly, it should mean to be equation 2.3.2.

Continue Discussion

7 replies
10 Jun
Steven​Jokes
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

https://pytorch.org/docs/master/generated/torch.norm.html

https://www.cnblogs.com/wanghui-garcia/p/11266298.html

10 Jun
Steven​Jokes
github.com
StevenJokes/D2L_enread/blob/master/Chapter2/2-3.md
<!--
 * @version:
 * @Author: steven
 * @Date: 2020-06-10 23:28:38
 * @LastEditors: steven
 * @LastEditTime: 2020-06-11 00:35:44
 * @Description:
-->

1. pass
2. pass
3. yes,pass
4. first dimension:2
5. first dimension
6. not match!
```python
A = torch.arange(20, dtype = torch.float32).reshape(5, 4)
A / A.sum(axis=1)
```
RuntimeError: The size of tensor a (4) must match the size of tensor b (5) at non-singleton dimension 1
This file has been truncated. show original
11 Jun
manuel-​arno-​korfmann
http://d2l.ai/chapter_preliminaries/linear-algebra.html#equation-chapter-preliminaries-linear-algebra-0

The matrix should be indexed via nm instead of mn, since the original matrix is mn and this is the transposed version.

1 reply
11 Jun▶ manuel-arno-korfmann
goldpiggy
Hi @manuel-arno-korfmann, could you specify which is “the matrix” you were referred to ?

1 reply
11 Jun▶ goldpiggy
manuel-​arno-​korfmann
Hey @goldpiggy, the link given includes a # query parameter which directly links to “the matrix”. Does that work for you?

2 replies
12 Jun▶ manuel-arno-korfmann
goldpiggy
Hi @manuel-arno-korfmann, you mean the matirx index like $a_12$ and $a_21$? The indexes’ location is flipped, while they have to keep the original values. Ultimately, $a_mn$ and $a_nm$ have different values at the original matrix

1 reply
13 Jun
Steven​Jokes
 manuel-arno-korfmann:
the matrix

@manuel-arno-korfmann
I think @goldpiggy is right.
A_mn:
A_mn
AT_nm:
AT_nm
Continue Discussion
