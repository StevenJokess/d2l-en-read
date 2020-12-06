

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 22:02:19
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 22:07:21
 * @Description:
 * @TODO::
 * @Reference:https://github.com/pytorch/examples/blob/master/distributed/ddp/README.md
 * https://pytorch.org/tutorials/beginner/dist_overview.html
-->

分布式数据并行(DDP)应用程序可以在多个节点上执行，每个节点可以由多个GPU设备组成。每个节点依次可以运行DDP应用程序的多个副本，每个副本在多个gpu上处理其模型。

设N为应用程序运行的节点数，G为每个节点的gpu数。同时在所有节点上运行的应用程序进程总数称为世界大小W，在每个节点上运行的进程数称为本地世界大小L。

每个应用进程被分配两个id:一个局部级别在[0,L-1]，一个全局级别在[0,W-1]。

为了说明上面定义的术语，考虑在两个节点上启动DDP应用程序的情况，每个节点都有四个gpu。然后，我们希望每个进程都跨越两个gpu。流程到节点的映射如下图所示:
