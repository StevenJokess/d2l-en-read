

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:20:24
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:21:20
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_preliminaries/autograd.html
 * @TODO::
 * @Reference:
-->

Continue Discussion
11 replies
2 Aug
ccpvirus
my solution to question 5

import numpy as np
from d2l import torch as d2l
x = np.linspace(- np.pi,np.pi,100)
x = torch.tensor(x, requires_grad=True)
y = torch.sin(x)
for i in range(100):
y[i].backward(retain_graph = True)

d2l.plot(x.detach(),(y.detach(),x.grad),legend = ((‘sin(x)’,“grad w.s.t x”)))
image

1 reply
17 Aug
icetea
I think it would be cool if in section 2.5.1 (and further where it occurs) there would be something like this $\frac{d}{dx}[2x^Tx]$.

10 Sep
rammy_​vadlamudi
Any take on this question :slight_smile:

Why is the second derivative much more expensive to compute than the first derivative?

I know second derivatives could be useful to give extra information on critical points found using 1st derivative, but how does 2nd derivatives are expensive ?

1 reply
10 Sep
Steven​Jokes
 rammy_vadlamudi:
I know second derivatives could be useful to give extra information on critical points found using 1st derivative, but how does 2nd derivatives are expensive ?

@rammy_vadlamudi

chain rule

11 Sep
asadalam
 ccpvirus:
d2l.plot(x.detach(),(y.detach(),x.grad),legend = ((‘sin(x)’,“grad w.s.t x”)))

My solution:

from mxnet import np, npx
npx.set_np()
from mxnet import autograd
def f(x):
      return np.sin(x)

x = np.linspace(- np.pi,np.pi,100)
x.attach_grad()
with autograd.record():
        y = f(x)

y.backward()
d2l.plot(x,(y,x.grad),legend = [('sin(x)','cos(x)')])
1 reply
11 Sep▶ asadalam
Steven​Jokes
@asadalam
You can use image or a github URLto show code…
And we should aviod import torch and mxnet at the same time…
It is confusing…

1 reply
11 Sep▶ StevenJokes
asadalam
Any specific reason not to use both torch and mxnet and how can we use the functions like attach_grad() and build a graph without using mxnet and only simple numpy ndarrays?

1 reply
11 Sep▶ asadalam
Steven​Jokes
@asadalam
For your first question, the reason is that in your code, you didn’t use anything related to pytorch.
So it is unnecessary to import torch
For your second question,
https://mxnet.apache.org/versions/1.6/api/python/docs/api/autograd/index.html#mxnet.autograd.backward
Check for source code
image

I don’t understand now…
image

What does these mean?
@szha
1 reply
11 Sep▶ StevenJokes
asadalam
Oh yes, sorry, I initially used torch to use it’s sine function but couldn’t integrate with attach_grad and building the graph. Switched to numpy function but forgot to remove import torch :slightly_smiling_face:

1 reply
11 Sep▶ asadalam
Steven​Jokes
You can try pytorch code too. It will work.

11 Sep
melis
I did a few examples and discovered a problem:

from mxnet import autograd, np, npx
import math # function exp()
npx.set_np()
x = np.arange(5)
print(x)
def f(a):
    # return 2 * a * a # works fine
    return math.exp(a) # produces error
print(f(1)) # shows 2.78181...
x.attach_grad()
print(x.grad)
with autograd.record():
    fstrich = f(x)
fstrich.backward()
print(x.grad)
works fine with the function 2xx (or other polynoms) but produces error with exp(x)
TypeError: only size-1 arrays can be converted to Python scalars

[0. 1. 2. 3. 4.]
2.718281828459045
[0. 0. 0. 0. 0.]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-78-cea180af7b0c> in <module>
     11 print(x.grad)
     12 with autograd.record():
---> 13     fstrich = f(x)
     14 fstrich.backward()
     15 print(x.grad)

<ipython-input-78-cea180af7b0c> in f(a)
      6 def f(a):
      7     # return 2 * a * a # works fine
----> 8     return math.exp(a) # produces error
      9 print(f(1)) # shows 2.78181...
     10 x.attach_grad()

c:\us....e\lib\site-packages\mxnet\numpy\multiarray.py in __float__(self)
    791         num_elements = self.size
    792         if num_elements != 1:
--> 793             raise TypeError('only size-1 arrays can be converted to Python scalars')
    794         return float(self.item())
    795

TypeError: only size-1 arrays can be converted to Python scalars
I have no idea, why exp() doesn’t work.

Continue Discussion

---

Continue Discussion
15 replies
11 Jun
Steven​Jokes
I noticed that 2.5.2 does’t have PyTorch, so I tried to convert it.

I used “.detach()” and “.clone()” to simulate “.copy()” in MXNET.

But I’m confused with differences from “.detach()” and “.clone()”.

Which one is more like to “.copy()” in MXNET?


from torch.autograd import Variable

x = torch.arange(4.0, requires_grad=True)

# make it as a Variable with a gradient taken.

x =  torch.autograd.Variable(x, requires_grad=True)

y = x * x

y.backward(torch.ones(y.size()))

AttributeError: ‘Tensor’ object has no attribute ‘copy’


# detach

u = x.detach()

# replace :u = torch.autograd.Variable(u, requires_grad=True)

# make tensor autograd works

u.requires_grad()

v = u * u

v.backward(torch.ones(v.size()))

x.grad == u.grad

tensor([True, True, True, True])


# clone

u = x.clone()

u.requires_grad()

v = u * u

v.backward(torch.ones(v.size()))

x.grad == u.grad

tensor([True, True, True, True])

For more:

Links that I have searched:
github.com
StevenJokes/D2L_enread/blob/master/Chapter2/2-5-2.md


<!--
 * @version:
 * @Author: steven
 * @Date: 2020-06-11 19:06:46
 * @LastEditors: steven
 * @LastEditTime: 2020-06-11 19:23:57
 * @Description:
-->
I noticed that 2.5.2 does't have PyTorch, so I tried to convert it.

I used ".detach()" and ".clone()" to simulate  ".copy()" in MXNET.

But I'm confused with differences from ".detach()" and ".clone()".

Which one is more like to ".copy()" in MXNET?

```python
from torch.autograd import Variable
This file has been truncated. show original
11 Jun
Steven​Jokes
2.5.4.
“Consequently d / a allows us to verify that the gradient is correct.”
I didn’t understand the meaning of d / a.
So I code as follow. But now, I’m more confused.

b = torch.randn(size=(1,), requires_grad=True)
b = b + 1000
# record the calculation
d = f(b)
d.backward()
b.grad == (d / b)
False

d tensor([1999.6416], grad_fn=)
b tensor([999.8208], grad_fn=)

t = b.grad
t
no return?

2.5.5.
The MXnet code of prediction mode haven’t mentioned.
I was wondering about the PyTorch’s code.

11 Jun
Steven​Jokes
I’m not very clear. Maybe second derivative is more easy to overflow the scope of storages.


y.backward()

RuntimeError: Trying to backward through the graph a second time, but the buffers have already been freed. Specify retain_graph=True when calling backward the first time.


y = 2 * torch.dot(x, x)

y

y.backward(retain_graph=True)

y.backward(retain_graph=True)

no Error!

Error happened!

# matrix

a = torch.randn(20, requires_grad=True).reshape(5, 4)

d = f(a)

d.backward()

RuntimeError: grad can be implicitly created only for scalar outputs

analyze:

source code:~.conda\envs\pytorch\lib\site-packages\torch\autograd_init_.py in _make_grads(outputs, grads)

rows:from 32 to 35 :


        elif grad is None: # why grad is None? Does f(a) not support matrix?

            if out.requires_grad:

                if out.numel() != 1:

                    raise RuntimeError("grad can be implicitly created only for scalar outputs")

TODO:

I’m trying to import plot in 2.4, so I convert the “2-4.ipynb” to “two-four.py”.

But when I import it, it just happens as follow.
How to fix it?


from ..d2l import torch as d2l

from IPython import display

import numpy as np

from .two_four import plot

ImportError Traceback (most recent call last)

in

----> 1 from …d2l import torch as d2l

  2 from IPython import display

  3 import numpy as np

  4 from .two_four import plot
ImportError: attempted relative import with no known parent package

TODO:

1 reply
11 Jun▶ StevenJokes
anirudh
Can you explain what exactly is the doubt here?
To import -> from d2l import torch as d2l you first need to install the d2l package in your environment.

12 Jun
Steven​Jokes
The first reply is my 2.5.2’s pytorch code. I use “detach” and “clone” to simulate what “copy” do in MXNET. But which one is best, “detach” or “clone”?

The second reply is about "the meaning of d / a " in 2.5.4. I tried another “b”.The return of “b.grad == (d / b)” is false rather than true. why?

The third reply is my answer to 2.5.7. I’m still working on how to import plot in 2.4.

1 reply
12 Jun
Steven​Jokes
After running pip install -U d2l -f https://d2l.ai/whl.html,
I can directly run from d2l import torch as d2l :relaxed:

Thanks :shushing_face:
But I’m confused about the bug when I directly run the imtorch.py(rename from d2l/torch.py）

$ /usr/bin/env python "d:\onedrive\文档\read\d2l\d2l\imtorch.py"
Traceback (most recent call last):
  File "d:\onedrive\文档\read\d2l\d2l\imtorch.py", line 22, in <module>
    import torch
  File "C:\ProgramData\Anaconda3\lib\site-packages\torch\__init__.py", line 81, in <module>
    ctypes.CDLL(dll)
  File "C:\ProgramData\Anaconda3\lib\ctypes\__init__.py", line 364, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: [WinError 126] The specified module could not be found
12 Jun▶ StevenJokes
anirudh
Answer to first question.
tensor.detach() creates a tensor that shares the same storage with tensor that does not require grad.
But tensor.clone() will also give you original tensor’s requires_grad attributes. It is basically an exact copy including the computation graph.

Use detach() to remove a tensor from computation graph and use clone to copy the tensor while still keeping the copy as a part of the computation graph it came from.

The second answer about "the meaning of d / a " in 2.5.4.
“a.grad == (d / a)” is true because if you see how d is calculate using f(a). It is basically scaling a by some constant factor k. And if you were to do differentiate such a function say function d=k*a with respect to a then you would get that k. Hence these are true and obviously it won’t hold for b because d is a function of which scales a and not b.

Answer to third question.
As i suggested earlier and you probably did it, you can simply pip install d2l to import torch from d2l.
If you want to import the specific rename imtorch.py just add this to the start of your code before making the import. ->

import sys
sys.path.insert(0, "../")
Let me know if these answers solve your issue. :slight_smile:

1 reply
13 Jun▶ anirudh
Steven​Jokes
Q1.
Does it mean that if I ‘clone’ a tensor or a Variable that has requires_grad attribute, then I don’t need to .requires_grad() for the new one?

Use detach() to remove a tensor? However, why can I still judge x.grad() == u.grad? “Remove” doesn’t mean that x will not exist? I think that x and u are just two different names for the same storage.

Can my code about 2.5.2’s Variable add to 2.5.2?

Q2.
I have understand that d is a function of which scales a. But what difference with f(b)?
Because, I think that f(b) = 2 * b.

First, b(formal parameter) =2 * a (argument b).
Then, not enter the loop. (b > 1000)
Then, True for if, return b(formal parameter) which is 2 * b(argument)
Q3.
Thanks. I will try it next time. I have did pip install d2l
The specified module could not be found
Did the problem happen because the module doesn’t exist in my sys.path?

1 reply
16 Jun▶ StevenJokes
anirudh
Ans1.
Yes we don’t use Variable in PyTorch now. We can use Tensor to do everything a variable did earlier with the latest version.

Ans2.
Yes, f(b) will be 2*b and if you change it to the following you will get True.

b = torch.randn(size=(1,), requires_grad=True)
d=f(b)
d.backward()

b.grad == d/b
>>>True
Ans3. Just uninstall the pip version and run python setup.py develop in your root d2l-en directory for installing the library.

2 replies
17 Jun▶ anirudh
anirudh
Ans3.
Just run this python setup.py develop in your repository.

18 Jun▶ anirudh
Steven​Jokes
Q2.

b = b + 1000
Why does it make False?
I found that print(b.grad) is None?
Why did it happen?

2 Aug
ccpvirus
my solution to question 5

import numpy as np
from d2l import torch as d2l
x = np.linspace(- np.pi,np.pi,100)
x = torch.tensor(x, requires_grad=True)
y = torch.sin(x)
for i in range(100):
y[i].backward(retain_graph = True)

d2l.plot(x.detach(),(y.detach(),x.grad),legend = ((‘sin(x)’,“grad w.s.t x”)))
image
looks dummy since I compute the grad 100 times, is there any better way?

27 Aug
SONG_​PAN
I don’t quite understand 2.5.2.

My understanding is that by default the framework will convert the actual output matrix into a vector based on a “gradient vector” that we passed in. The description of this “gradient vector” is

which specifies the gradient of the differentiated function w.r.t self.

What does it mean? Does “gradient of differentiated function” mean “second order gradient”?

1 reply
27 Aug
SONG_​PAN
My answers to the questions: please point out if I am misunderstood anything

Why is the second derivative much more expensive to compute than the first derivative?
Because instead of following the original computation graph, we need to construct a new one that corresponds to the calculation of first-order gradient?

After running the function for backpropagation, immediately run it again and see what happens.
RuntimeError: Trying to backward through the graph a second time, but the saved intermediate results have already been freed. Specify retain_graph=True when calling backward the first time.

In the control flow example where we calculate the derivative of d with respect to a , what would happen if we changed the variable a to a random vector or matrix. At this point, the result of the calculation f(a) is no longer a scalar. What happens to the result? How do we analyze this?
Directly changing would give the “blah blah … only scalar output” which is what 2.5.2 is talking about. I changed the code to

a = torch.randn(size=(3,), requires_grad=True)
d = f(a)
d.sum().backward()
and a.grad == d / a still gives true. This is because in the function, there is no cross-element operation. So each element of the vector is independent and doesn’t affect other element’s differentiation.

Redesign an example of finding the gradient of the control flow. Run and analyze the result.
SKIP

Let $f(x) = \sin(x)$. Plot $f(x)$ and $\frac{df(x)}{dx}$, where the latter is computed without exploiting that $f’(x) = \cos(x)$.
import numpy as np
from d2l import torch as d2l
x = np.linspace(- np.pi,np.pi,100)
x = torch.tensor(x, requires_grad=True)
y = torch.sin(x)
y.sum().backward()

d2l.plot(x.detach(),(y.detach(),x.grad),legend = (('sin(x)',"grad w.s.t x")))
29 Aug
goldpiggy
 SONG_PAN:
which specifies the gradient of the differentiated function w.r.t self .

What does it mean? Does “gradient of differentiated function” mean “second order gradient”?

Hi @SONG_PAN, this is a first order gradient. The gradient is only available after we differentiate the function. :wink:

Continue Discussion

---
