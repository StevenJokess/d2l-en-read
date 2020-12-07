

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 18:54:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 18:58:44
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
