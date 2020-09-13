

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:16:01
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:16:15
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_preliminaries/ndarray.html
 * @TODO::
 * @Reference:
-->
8 replies
9 Jun
Steven​Jokes
1.
x = torch.arange(12, dtype=torch.float32).reshape((3,4))
y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
x,y,x == y,x < y,x > y
(tensor([[ 0., 1., 2., 3.],
[ 4., 5., 6., 7.],
[ 8., 9., 10., 11.]]),
tensor([[2., 1., 4., 3.],
[1., 2., 3., 4.],
[4., 3., 2., 1.]]),
tensor([[False, True, False, True],
[False, False, False, False],
[False, False, False, False]]),
tensor([[ True, False, True, False],
[False, False, False, False],
[False, False, False, False]]),
tensor([[False, False, False, False],
[ True, True, True, True],
[ True, True, True, True]]))

2.
a = torch.arange(1, 6, dtype =torch.float32).reshape((5, 1))
b = torch.arange(1, 3).reshape((1, 2))
a, b
(tensor([[1],
[2],
[3],
[4],
[5]]),
tensor([[1, 2]]))

a + b
tensor([[2., 3.],
[3., 4.],
[4., 5.],
[5., 6.],
[6., 7.]])

a - b
tensor([[ 0., -1.],
[ 1., 0.],
[ 2., 1.],
[ 3., 2.],
[ 4., 3.]])

a * b
tensor([[1.0000, 0.5000],
[2.0000, 1.0000],
[3.0000, 1.5000],
[4.0000, 2.0000],
[5.0000, 2.5000]])

a / b
tensor([[1, 0],
[2, 1],
[3, 1],
[4, 2],
[5, 2]])

a // b
tensor([[1., 0.],
[2., 1.],
[3., 1.],
[4., 2.],
[5., 2.]])

a \ b
File “” , line 1 a \ b ^ SyntaxError : unexpected character after line continuation character

a ** b
tensor([[ 1., 1.],
[ 2., 4.],
[ 3., 9.],
[ 4., 16.],
[ 5., 25.]])

1 reply
10 Jun▶ StevenJokes
anirudh
@StevenJokes There is no \ operator in pytorch. It is actually a special chracter in python, also called the “escape” character. Hence the error.

Let me know if this is not clear.

1 reply
10 Jun▶ anirudh
Steven​Jokes
I have got it from the doc, but thanks anyway.
I’m a new bee of pytorch.

1 reply
10 Jun▶ StevenJokes
Steven​Jokes
a % b
tensor([[0., 1.],
[0., 0.],
[0., 1.],
[0., 0.],
[0., 1.]])

10 Jun
manuel-​arno-​korfmann
When having PyTorch selected:

2.1.5. Saving Memory §3:

Fortunately, performing in-place operations in MXNet is easy.

Is it intentional to discuss MXNet even though PyTorch is selected for the code examples?

1 reply
11 Jun▶ manuel-arno-korfmann
Steven​Jokes
It is understandable. :sweat_smile:
The original examples are built by MXNet. :joy:( created by mli)

19 Jun
hehao​98
Allow me to point out a small error in Section 2.1.2
“For stylistic convenience, we can write x.sum() as np.sum(x) .” should not appear in PyTorch version because it is not possible to run np.sum(x) if x is a PyTorch tensor.

x = torch.arange(12)
np.sum(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-30-1393831a87e1> in <module>
      1 x = torch.arange(12)
----> 2 np.sum(x)
1 reply
19 Jun▶ hehao98
anirudh
Thanks @hehao98 for pointng that out. We have already fixed that line in this commit and it will be updated with our next release.

Continue Discussion
