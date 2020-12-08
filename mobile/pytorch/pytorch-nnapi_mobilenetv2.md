

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 21:45:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 21:48:46
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/tutorials/prototype/nnapi_mobilenetv2.html
 * [mobile_perf](https://pytorch.org/tutorials/recipes/mobile_perf.html)
-->

PYTORCH移动性能配方

介绍

性能(即延迟)对移动设备上的ML模型推断的大多数应用程序和用例至关重要。

现在，PyTorch在CPU后端执行模型，等待其他硬件后端(如GPU、DSP和NPU)的可用性。

在这个食谱中，你会学到:

如何优化您的模型，以帮助减少移动设备上的执行时间(更高的性能，更低的延迟)。

如何进行基准测试(检查优化是否对用例有帮助)。

基准测试

进行基准测试(检查优化是否帮助了您的用例)的最佳方法是度量您想要优化的特定用例，因为在不同的环境中性能行为可能不同。

PyTorch分发提供了一种对向前运行模型的裸二进制进行基准测试的方法，这种方法可以提供更稳定的度量，而不是在应用程序内部进行测试。
