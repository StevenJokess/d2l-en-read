

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 20:53:50
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 20:53:52
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_deep-learning-computation/parameters.html
 * @TODO::
 * @Reference:
-->
2 replies
25 Jun
kwang
Chap 5.2.2.1
in the first and second pytorch code, for function
init_normal(m)
I guess it should be
nn.init.XXX(m.weight, *args)
since

pytorch.nn.Module.apply(fn) Applies `fn` recursively to every submodule (as returned by .children() ) as well as self.

it doesn’t make sense to repeatedly initialize net[0] and it’s aiming to initialize all parameters

1 reply
29 Jun▶ kwang
anirudh
Hi @kwang that’s a great catch. If we are to apply initialization to all the Linear layers in the network, then we should replace net[0] to m inside the init_normal function.

Ps. While I was at it, I have fixed the naming of the functions too. The second function should be named init_constant.

This is now fixed in master. You can soon see the changes in the next update to release branch.
Thanks!

Continue Discussion
