

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:02:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:02:32
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_multilayer-perceptrons/numerical-stability-and-init.html
 * @TODO::
 * @Reference:
-->
2 replies
15 Jun
jackrcole
I’d just like to point out a small mistake in the book: In the subsection discussing Xavier Initialization, the variance of h_i is noted as E[h_i] rather than Var[h_i]. This error is also made with the variances of W_ij and x_ij. It’s just a small notational error, but one that some readers (including yours truly) may find a bit confusing.

1 reply
15 Jun▶ jackrcole
goldpiggy
Hi @jackrcole, great catch! We will fix it!

Continue Discussion
