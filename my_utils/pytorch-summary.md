

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-21 23:25:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 18:42:19
 * @Description:
 * @TODO::
 * @Reference:[1]: https://github.com/wang-xinyu/pytorchx
-->
https://github.com/sksq96/pytorch-summary

Clone, and cd into the repo directory.[1]

git clone https://github.com/sksq96/pytorch-summary
python setup.py build
python setup.py install

```
from torchsummary import summary
summary(your_model, input_size=(channels, H, W))
```
