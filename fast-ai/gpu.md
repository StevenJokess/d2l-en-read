

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 00:05:04
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 00:07:43
 * @Description:
 * @TODO::
 * @Reference:https://docs.fast.ai/dev/gpu.html
-->


Multi-GPU



如果你没有在shell中设置环境变量，你可以在程序开始时在代码中设置这些变量，通过:import os;os.environ [' CUDA_VISIBLE_DEVICES ') = ' 2 '。

另一种不太灵活的方法是在代码中硬编码设备ID，例如将其设置为gpu1:

torch.cuda.set_device(1)
