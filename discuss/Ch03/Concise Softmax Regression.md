

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:14:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:14:50
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_linear-networks/softmax-regression-concise.html
 * @TODO::
 * @Reference:
-->

Continue Discussion
13 replies
7 Jun
S_​X
Hi @mli I get this error when I import the libraries needed for this module:

from d2l import mxnet as d2l
from mxnet import gluon, init, npx
from mxnet.gluon import nn
npx.set_np()
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-2-2bc514450bf4> in <module>
----> 1 from d2l import mxnet as d2l
      2 from mxnet import gluon, init, npx
      3 from mxnet.gluon import nn
      4 npx.set_np()

ImportError: cannot import name 'mxnet' from 'd2l' (/Users/xyz/miniconda3/envs/d2l/lib/python3.7/site-packages/d2l/__init__.py)
Is the first line for import correct? I see this error at least in all notebooks for the linear networks module
I think it should be just:
import d2l

1 reply
8 Jun▶ S_X
goldpiggy
Hi @S_X, I run the code multiple times and it goes through smoothy. Please check if you have d2l installed by running

!pip list | egrep d2l
in your jupyter notebook. It should return you the current version of d2l, such as d2l 0.13.2.

If not, please run

!pip install d2l
in your jupyter notebook.

1 reply
8 Jun▶ goldpiggy
S_​X
Hi @goldpiggy,
It worked fine for me last week. I then downloaded the latest version of d2l notebooks and this problem showed up. The issue is:

from d2l import mxnet as d2l
it should be
import d2l

In from d2l import mxnet as d2l I don’t think the intent is to import mxnet library from d2l and name it as d2l! Please correct me if I’m mistaken.

1 reply
8 Jun▶ S_X
mli
Please update to the latest version of d2l by pip install d2l==0.13.2 -f https://d2l.ai/whl.html. We updated the way to import d2l to support multiple backends. from d2l import mxnet as d2l imports the mxnet backend.

1 reply
9 Jun▶ mli
S_​X
Thanks! That helped!

9 Jun
S_​X
For the question #2 at the end:

Why might the test accuracy decrease again after a while? How could we fix this?

When I run 30 epochs, I see a small dip in test accuracy. Is this what is being referred to? I don’t see a big decrease in test accuracy.
image

9 Jun
goldpiggy
Hi @S_X, did you run the code

d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)
multiple times without reinitializing the net?

If a model is trained with too much epoch after its converge, it’s called “overfitting” (http://d2l.ai/chapter_multilayer-perceptrons/underfit-overfit.html).

1 reply
10 Jun▶ goldpiggy
S_​X
Hi @goldpiggy,
No, I ran the following:
num_epochs = 30
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)
This is the correct way, right?

1 reply
10 Jun▶ S_X
goldpiggy
Hi @S_X! Since your initial loss is quite low, it looks like you may run this cell:

num_epochs = 30
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)
multiple times with the same defined net.

If it was trained on the same net, the model will continue optimizing on the pretrained net that you ran last time. Hence even though the epoch on the plot looks like “0-30”, it is probably should be “30-60”, “60-90”, etc.

Does it make sense to you?

1 reply
11 Jun
S_​X
 goldpiggy:
multiple times with the same defined net .

Hi @goldpiggy
Yes, you are right. I ran with the same net. That explains it.
When I reinitialize the whole notebook and run larger epochs, I can see the test accuracy reduce compared to training accuracy). Thanks for your help!

Result of 30 epochs after re-initializing all the variables:
image

1 reply
11 Jun▶ S_X
goldpiggy
Great! My pleasure to help!

1 reply
19 Jun▶ goldpiggy
Rosetta
I am not able to run Huber Loss for regression

1 reply
19 Jun▶ Rosetta
goldpiggy
We will solve it! Thanks!

Continue Discussion

---

7 replies
23 Jun
Steven​Jokes
batch_size num_epochs lr
It didn’t happen in my training. Why?
3-7
I guess that the reason of “the test accuracy decrease again after a while” is that SGD updates too often.
Maybe we can try MBGD.
for more:
 cnblogs.com

深度学习——优化器算法Optimizer详解（BGD、SGD、MBGD、Momentum、NAG、Adagrad、Adadelta、RMSprop、Adam）....
在机器学习、深度学习中使用的优化算法除了常见的梯度下降，还有 Adadelta，Adagrad，RMSProp 等几种优化器，都是什么呢，又该怎么选择呢？ 在 Sebastian Ruder 的这篇论

1 reply
23 Jun▶ StevenJokes
goldpiggy
Hi @StevenJokes, we talked about the varied optimization algorithms in https://d2l.ai/chapter_optimization/index.html. Hopefully it helps!

1 reply
24 Jun▶ goldpiggy
Steven​Jokes
I will learn it next time !

15 Aug
ccpvirus
when testing the accuracy in concise Softmax regression, it seems that the max of the logits of the each example is used to determine the most probable class rather than the max of exp of logit. since that softmax is implemented in the cross entrophy loss, how did you do softmax in testing

1 reply
16 Aug▶ ccpvirus
Steven​Jokes
Testing also has cross entrophy loss to calculate. :grinning:
@ccpvirus

16 Aug
ccpvirus
where is it used? cant find it (reply should be at least 20 characters)

1 reply
19 Aug▶ ccpvirus
goldpiggy
Hi @ccpvirus, please see my reply at Implementation of Multilayer Perceptron from Scratch.

Continue Discussion
