

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 19:10:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 19:10:08
 * @Description:
 * @TODO::
 * @Reference:https://oldpan.me/archives/pytorch-build-simple-instruction
-->
pytorch
检查Pytorch安装是否成功：

>>> import torch

>>> print(torch.cuda.is_available())
>>> print(torch.backends.cudnn.is_acceptable(torch.cuda.FloatTensor(1)))
... print(torch.backends.cudnn.version())```
True  # 出现Turn说明cuda正常
Ture  # 出现Ture说明cudnn正常
7401  # 这是我的版本号
