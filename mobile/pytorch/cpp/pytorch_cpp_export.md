

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 20:33:04
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 20:43:14
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/tutorials/advanced/cpp_export.html
-->

在c++中加载TORCHSCRIPT模型

顾名思义，PyTorch的主要接口是Python编程语言。虽然对于许多需要动态化和易于迭代的场景，Python是一种合适的首选语言，但也有同样多的情况恰恰是Python的这些属性不适合的。后者经常应用于生产环境——这是低延迟和严格部署需求的领域。对于生产场景，c++通常是首选语言，即使只是为了将其绑定到另一种语言，如Java、Rust或Go。下面的段落将概述PyTorch提供的从现有Python模型到序列化表示的路径，这种序列化表示可以完全从c++加载和执行，而不依赖于Python。

步骤1:将你的PyTorch模型转换为Torch脚本

一个PyTorch模型从Python到c++的过程是通过Torch脚本实现的，它是一个PyTorch模型的表示，可以被Torch脚本编译器理解、编译和序列化。如果您从一个用普通的“eager”API编写的现有PyTorch模型开始，您必须首先将您的模型转换为Torch脚本。在下面的讨论中，在最常见的情况下，这只需要很少的努力。如果您已经有了Torch脚本模块，您可以跳到本教程的下一节。

有两种方法可以将PyTorch模型转换为Torch脚本。第一种称为跟踪，在这种机制中，通过使用示例输入对模型进行一次评估，并记录这些输入在模型中的流，从而捕获模型的结构。这适用于控制流使用有限的模型。第二种方法是向您的模型添加显式的注释，通知Torch脚本编译器它可以直接解析和编译您的模型代码，这取决于Torch脚本语言所施加的约束。

提示

您可以在官方Torch脚本参考中找到这两种方法的完整文档，以及关于使用哪种方法的进一步指导。

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)



---

