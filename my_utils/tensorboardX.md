

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-11 22:03:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-11 22:11:43
 * @Description:
 * @TODO::
 * @Reference:
-->

安装方法为pip install tensorboardx，使用非常简单。[1]

第一步，引入包定义创建：

from tensorboardX import SummaryWriter
writer = SummaryWriter()

第二步，记录变量，如train阶段的 loss，writer.add_scalar('data/trainloss', epoch_loss, epoch)。

按照以上操作就完成了，完整代码可以看配套的Git 项目，我们看看训练中的记录。Loss和acc的曲线图如下：




[1]: https://mp.weixin.qq.com/s?__biz=MzA3NDIyMjM1NA==&mid=2649029881&idx=1&sn=3c869fcee3b48d3582952ab9a0683ea6&chksm=87134284b064cb924c5e7231b3f2c36ba27e3a689b067f569f2e086f62b18413bcebc5987a07&token=1879088111&lang=zh_CN#rd

TODO:
https://tensorboardx.readthedocs.io/en/latest/tutorial.html
