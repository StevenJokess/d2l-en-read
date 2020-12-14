

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-14 21:51:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 21:51:11
 * @Description:
 * @TODO::
 * @Reference:https://github.com/lyhue1991/eat_pytorch_in_20_days/blob/master/%E4%B8%89%E3%80%81Pytorch%E7%9A%84%E5%B1%82%E6%AC%A1%E7%BB%93%E6%9E%84.md
-->
Pytorch的层次结构从低到高可以分成如下五层。

最底层为硬件层，Pytorch支持CPU、GPU加入计算资源池。

第二层为C++实现的内核。

第三层为Python实现的操作符，提供了封装C++内核的低级API指令，主要包括各种张量操作算子、自动微分、变量管理. 如torch.tensor,torch.cat,torch.autograd.grad,nn.Module. 如果把模型比作一个房子，那么第三层API就是【模型之砖】。

第四层为Python实现的模型组件，对低级API进行了函数封装，主要包括各种模型层，损失函数，优化器，数据管道等等。 如torch.nn.Linear,torch.nn.BCE,torch.optim.Adam,torch.utils.data.DataLoader. 如果把模型比作一个房子，那么第四层API就是【模型之墙】。

第五层为Python实现的模型接口。Pytorch没有官方的高阶API。为了便于训练模型，作者仿照keras中的模型接口，使用了不到300行代码，封装了Pytorch的高阶模型接口torchkeras.Model。如果把模型比作一个房子，那么第五层API就是模型本身，即【模型之屋】。
