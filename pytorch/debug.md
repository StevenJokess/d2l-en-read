

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 18:54:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 22:33:25
 * @Description:
 * @TODO::
 * @Reference:https://oldpan.me/archives/how-to-debug-pytorch-deeper
-->

对Pytorch的debug一般都是在python端进行，这对于一般搭建模型的任务来说足够了。但如果我们需要对Pytorch进行一些修改或者研究一下机器或深度学习系统是如何搭建的，想要深入探索就必须涉及到C++的源码层面。

既然要对Pytorch的源码进行debug，首先我们需要对Pytorch的源码进行编译。编译时需要修改DEBUG环境变量，编译Debug版的pytorch，命令为DEBUG=1 python setup.py install，更多详细的编译步骤看下面这篇文章，这里不赘述了：

https://oldpan.me/archives/pytorch-build-simple-instruction

如何卸载
如果是源码安装的Pytorch，卸载需要执行：

pip uninstall torch
python setup.py clean

---

PyTorch到底好用在哪里? - 郑华滨的回答 - 知乎
https://www.zhihu.com/question/65578911/answer/249906275

PyTorch这种动态图框架在debug的时候超级超级超级方便！

因为基本上计算图运行出错的地方，就在图定义的那行代码上。

tensor shape和网络层的input shape不匹配？该用Long类型但是却用了Float类型？

Don't panic！直接在报错的那行代码前面熟练地插入一句：

import ipdb; ipdb.set_trace()
然后就愉快地断点调试吧。


