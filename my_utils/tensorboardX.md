

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-11 22:03:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-28 20:38:35
 * @Description:
 * @TODO::
 * @Reference:
-->

You can optionally install crc32c to speed up.

pip install crc32c

Starting from tensorboardX 2.1, You need to install soundfile for the add_audio() function (200x speedup).

pip install soundfile

安装方法为pip install tensorboardx，使用非常简单。[1]

第一步，引入包定义创建：

from tensorboardX import SummaryWriter
writer = SummaryWriter()

第二步，记录变量，如train阶段的 loss，writer.add_scalar('data/trainloss', epoch_loss, epoch)。

按照以上操作就完成了，完整代码可以看配套的Git 项目，我们看看训练中的记录。Loss和acc的曲线图如下：

#[4]
    # Summary writer
    writer = SummaryWriter("runs/cnn_attention_{:%Y-%m-%d_%H-%M-%S}".format(datetime.now()))

pytorch 1.1以后的版本内置了SummaryWriter 函数,所以不需要再安装tensorboardx了
from torch.utils.tensorboard import SummaryWriter
安装完成后与 visdom一样执行独立的命令 tensorboard --logdir logs 即可启动，默认的端口是 6006,在浏览器中打开 http://localhost:6006/ 即可看到web页面。
对于Pytorch的1.3版本来说，实测 SummaryWriter在处理结构图的时候是有问题的（或者是需要加什么参数，目前我还没找到），所以建议大家继续使用tensorboardx。[2]


[1]: https://mp.weixin.qq.com/s?__biz=MzA3NDIyMjM1NA==&mid=2649029881&idx=1&sn=3c869fcee3b48d3582952ab9a0683ea6&chksm=87134284b064cb924c5e7231b3f2c36ba27e3a689b067f569f2e086f62b18413bcebc5987a07&token=1879088111&lang=zh_CN#rd
[2]: https://github.com/zergtant/pytorch-handbook/blob/master/chapter4/4.2.2-tensorboardx.ipynb
[3]: https://github.com/lanpa/tensorboardX
[4]: https://github.com/0aqz0/pytorch-attention-mechanism/blob/master/cnn-with-attention.py
TODO:
https://tensorboardx.readthedocs.io/en/latest/tutorial.html
