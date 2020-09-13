

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:19:44
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:19:59
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_preliminaries/calculus.html
 * @TODO::
 * @Reference:
-->
7 replies
25 Aug
gpk​2000
I think it would be better to make a quote that you need to install these packages before running this code such as in the code-block below. Anaconda comes with these pre-installed but Miniconda doesn’t. I am saying this cause the book suggested to download Miniconda.

1 reply
25 Aug▶ gpk2000
gpk​2000
Also in that example this didn’t work

from d2l import mxnet as d2l

this works

import mxnet as d2l

1 reply
3 Sep
goldpiggy
Hey @gpk2000, thanks for the suggestion of Anaconda. We recommend installing miniconda as it has most of the necessary libraries but not as heavy-lifting as anaconda.

 gpk2000:
Also in that example this didn’t work

from d2l import mxnet as d2l

this works

import mxnet as d2l

As for your question, please make sure you have the latest version of D2L and MXNet installed. :wink:

7 Sep
smizerex
Is exercise 4 in section 2.4 possible?
How would we do it?

1 reply
8 Sep▶ smizerex
goldpiggy
Hey @smizerex, yes chain rule can be applied here. Feel free to share your idea and discuss here.

11 Sep
asadalam
Does the first part of answer for Q.4 in 2.4 is: du/da = (du/dx)(dx/da) + (du/dy)(dy/da) + (du/dz)*(dz/da)

1 reply
11 Sep▶ asadalam
goldpiggy
Hi @asadalam, I believe you are right!

Continue Discussion
