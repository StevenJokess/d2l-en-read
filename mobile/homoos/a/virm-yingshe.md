

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 21:25:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 21:29:05
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/kuangyufei/article/details/109032636
-->


# MMU的本质

虚拟地址(VA): 就是线性地址, 鸿蒙内存部分全是VA的身影, 是由编译器和链接器在定位程序时分配的，每个应用程序都使用相同的虚拟内存地址空间，而这些虚拟内存地址空间实际上分别映射到不同的实际物理内存空间上。CPU只知道虚拟地址，向虚拟地址要数据，但在其保护模式下很悲催地址信号在路上被MMU拦截了，MMU把虚拟地址换成了物理地址，从而拿到了真正的数据。

物理地址(PA)：程序的指令和常量数据，全局变量数据以及运行时动态申请内存所分配的实际物理内存存放位置。

MMU采用页表(page table)来实现虚实地址转换，页表项除了描述虚拟页到物理页直接的转换外，还提供了页的访问权限(读，写，可执行)和存储属性。 MMU的本质是拿虚拟地址的高位(20位)做文章，低12位是页内偏移地址不会变。也就是说虚拟地址和物理地址的低12位是一样的，本篇详细讲述MMU是如何变戏法的。

MMU是通过两级页表结构：L1和L2来实现映射功能的，鸿蒙内核当然也实现了这两级页表转换的实现。本篇是系列篇关于内存部分最满意的一篇，也是最不好理解的一篇, 强烈建议结合源码看, 鸿蒙内核源码注释中文版 【 Gitee仓 | CSDN仓 | Github仓 | Coding仓 】内存部分的注释已经基本完成 .


TODO:
## LOS_ArchMmuMap 生成L1，L2页表项，实现映射的过程

mmu的map 就是生成L1,L2页表项的过程，以供虚实地址的转换使用，还是直接看代码吧，代码说明一切！