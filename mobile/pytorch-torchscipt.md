

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 23:17:27
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 23:31:59
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/docs/master/jit.html
-->

TorchScript是一种从PyTorch代码创建可序列化和可优化模型的方法。任何TorchScript程序都可以从Python进程中保存并加载到不依赖Python的进程中。

我们提供了一些工具，可以将模型从纯Python程序递增地转换为可以独立于Python运行的TorchScript程序，例如在独立的c++程序中。这使得我们可以使用Python中熟悉的工具在PyTorch中训练模型，然后通过TorchScript将模型导出到生产环境中，在这种环境中，Python程序可能会因为性能和多线程的原因而不利。

要了解TorchScript的介绍，请参阅TorchScript介绍教程。
https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html

关于将PyTorch模型转换为TorchScript并在c++中运行它的端到端示例，请参阅c++教程加载PyTorch模型。


---
https://pytorch.org/docs/master/jit_unsupported.html

下面的函数需要dtype, layout, device作为TorchScript中的参数，但是这些参数在Python中是可选的

torch.randint()

torch.sparse_coo_tensor()

to()


PyTorch不支持的模块和类

TorchScript目前无法编译许多其他常用的PyTorch构造。下面列出了TorchScript不支持的模块，以及不支持的PyTorch类的不完整列表。对于不支持的模块，我们建议使用torch.jit.trace()。


