

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 22:02:04
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 22:09:50
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/docs/master/quantization.html
 * https://pytorch.org/blog/introduction-to-quantization-on-pytorch/
-->

# QUANTIZATION

Quantization是在beta和可能改变。

介绍了量化

量化是指以比浮点精度更低的位宽执行计算和存储张量的技术。量子化模型对具有整数而不是浮点值的张量执行部分或全部操作。这允许在许多硬件平台上使用更紧凑的模型表示和高性能向量化操作。与典型的FP32模型相比，PyTorch支持INT8量化，允许模型大小减少4倍，内存带宽需求减少4倍。INT8计算的硬件支持通常比FP32计算快2到4倍。量化主要是一种加速推理的技术，量化运算符只支持前向传递。

PyTorch支持多种量化深度学习模型的方法。在大多数情况下，模型是在FP32训练，然后模型转换到INT8。此外，PyTorch还支持量化感知训练，它使用伪量化模块对前向和后向传递中的量化错误进行建模。注意，整个计算是在浮点数中进行的。在量化感知训练的最后，PyTorch提供了转换函数，将训练好的模型转换成较低的精度。

在较低的层次上，PyTorch提供了一种表示量化张量并使用它们执行操作的方法。它们可以用来直接构建模型，以较低的精度执行全部或部分计算。提供了更高级的api，这些api包含了将FP32模型转换为更低精度的典型工作流，从而使精度损失最小化。

现在，PyTorch支持以下后台有效运行量化操作符:

支持AVX2或更高版本的x86 cpu(没有AVX2，一些操作的实现效率很低)

ARM cpu(通常用于移动/嵌入式设备)

根据PyTorch构建模式自动选择相应的实现。


