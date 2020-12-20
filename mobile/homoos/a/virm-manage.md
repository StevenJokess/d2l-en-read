

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 19:10:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 20:36:21
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/kuangyufei/article/details/108821442
-->

虚拟内存模块源码 详见:../kernel/base/vm 本篇源码超级多，很烧脑，但笔者关键处都加了注释。废话不多说，开始吧。

## 初始化整个内存

https://github.com/kuangyufei/kernel_liteos_a_note/blob/5eeb8eb6ffc8475b86e336b317dd5c39f2f3e3a1/kernel/base/include/los_vm_boot.h#L65




https://github.com/kuangyufei/kernel_liteos_a_note/blob/5eeb8eb6ffc8475b86e336b317dd5c39f2f3e3a1/kernel/base/vm/los_vm_boot.c#L74-L96

从main()跟踪可看内存部分初始化是在OsSysMemInit()中完成的。

```c
UINT32 OsSysMemInit(VOID)
{
    STATUS_T ret;

    OsKSpaceInit();//内核空间初始化

    ret = OsKHeapInit(OS_KHEAP_BLOCK_SIZE);// 内核动态内存初始化 512K
    if (ret != LOS_OK) {
        VM_ERR("OsKHeapInit fail");
        return LOS_NOK;
    }

    OsVmPageStartup();// page初始化
    OsInitMappingStartUp();// 映射初始化

    ret = ShmInit();// 共享内存初始化
    if (ret < 0) {
        VM_ERR("ShmInit fail");
        return LOS_NOK;
    }

    return LOS_OK;
}
```

https://github.com/kuangyufei/kernel_liteos_a_note/blob/9f85adba4ffa9be92543e94bd6576bf6bfd2f6d7/kernel/common/los_config.c#L275

ret = OsSysMemInit();// 完成内存的初始化操作,段页管理

鸿蒙虚拟内存整体布局图

![鸿蒙虚拟内存整体布局图](/vm_buju.png)

---

https://github.com/kuangyufei/kernel_liteos_a_note/blob/3759e9fe8bf942b2da8c2953fc6c045e830b884d/kernel/common/los_config.h#L55-L65

KERNEL_VMM_SIZE?

```c
// HarmonyOS 内核空间包含以下各段:
extern CHAR __int_stack_start;	// 运行系统函数栈的开始地址
extern CHAR __rodata_start;		// ROM开始地址 只读
extern CHAR __rodata_end;		// ROM结束地址
extern CHAR __bss_start;		// bss开始地址
extern CHAR __bss_end;			// bss结束地址
extern CHAR __text_start;		// 代码区开始地址
extern CHAR __text_end;			// 代码区结束地址
extern CHAR __ram_data_start;	// RAM开始地址 可读可写
extern CHAR __ram_data_end;		// RAM结束地址
extern UINT32 __heap_start; 	// 堆区开始地址
extern UINT32 __heap_end;		// 堆区结束地址
```

内存一开始一张白纸，这些extern就是给它画大界线的，从哪到哪是属于什么段。这些值大小取决实际项目内存条的大小，不同的内存条，地址肯定会不一样，所以必须由外部提供，鸿蒙内核采用了Linux的段管理方式。

CHAR __bss_start
.bss BSS段 （bss segment）通常是指用来存放程序中未初始化的全局变量的一块内存区域。BSS是英文Block Started by Symbol的简称。BSS段属于静态内存分配。该段用于存储未初始化的全局变量或者是默认初始化为0的全局变量，它不占用程序文件的大小，但是占用程序运行时的内存空间。

CHAR __ram_data_start
.data data段 该段用于存储初始化的全局变量，初始化为0的全局变量出于编译优化的策略还是被保存在BSS段。

CHAR __rodata_start
.rodata段,该段也叫常量区，用于存放常量数据，ro就是Read Only之意。

CHAR __text_start
.text text段 是用于存放程序代码的，编译时确定,只读。更进一步讲是存放处理器的机器指令，当各个源文件单独编译之后生成目标文件，经连接器链接各个目标文件并解决各个源文件之间函数的引用，与此同时，还得将所有目标文件中的.text段合在一起。

CHAR __int_stack_start
stack栈段，是由系统负责申请释放，用于存储参数变量及局部变量以及函数的执行。

UINT32 __heap_start
heap段 它由用户申请和释放，申请时至少分配虚存，当真正存储数据时才分配相应的实存，释放时也并非立即释放实存，而是可能被重复利用。

---

## 内核空间是怎么初始化的？

https://github.com/kuangyufei/kernel_liteos_a_note/blob/62d5a09843ddec5ea0e43e72232981b655978eef/kernel/base/vm/los_vm_map.c#L195-L201

```c
//鸿蒙内核空间有两个(内核进程空间和内核动态分配空间),共用一张L1页表
VOID OsKSpaceInit(VOID)
{
    OsVmMapInit();// 初始化互斥量
    OsKernVmSpaceInit(&g_kVmSpace, OsGFirstTableGet());// 初始化内核虚拟空间，OsGFirstTableGet 为L1表基地址
    OsVMallocSpaceInit(&g_vMallocSpace, OsGFirstTableGet());// 初始化动态分配区虚拟空间，OsGFirstTableGet 为L1表基地址
}//g_kVmSpace g_vMallocSpace 共用一个L1页表
```

---

https://github.com/kuangyufei/kernel_liteos_a_note/blob/2912d9b4e69ec480fed06ee626c689ad3477868b/kernel/base/mem/bestfit/los_memory.c#L2937-L2966

```c
//初始化内核堆空间
STATUS_T OsKHeapInit(size_t size)
{
    STATUS_T ret;
    VOID *ptr = NULL;
    /*
     * roundup to MB aligned in order to set kernel attributes. kernel text/code/data attributes
     * should page mapping, remaining region should section mapping. so the boundary should be
     * MB aligned.
     */
     //向上舍入到MB对齐是为了设置内核属性。内核文本/代码/数据属性应该是页映射，其余区域应该是段映射,所以边界应该对齐。
    UINTPTR end = ROUNDUP(g_vmBootMemBase + size, MB);//用M是因为采用section mapping 鸿蒙内核源码分析(内存映射篇)有阐述
    size = end - g_vmBootMemBase;
	//ROUNDUP(0x00000200+512,1024) = 1024  ROUNDUP(0x00000201+512,1024) = 2048 此处需细品!
    ptr = OsVmBootMemAlloc(size);//因刚开机，使用引导分配器分配
    if (!ptr) {
        PRINT_ERR("vmm_kheap_init boot_alloc_mem failed! %d\n", size);
        return -1;
    }

    m_aucSysMem0 = m_aucSysMem1 = ptr;//内存池基地址，auc 是啥意思没整明白？
    ret = LOS_MemInit(m_aucSysMem0, size);//初始化内存池
    if (ret != LOS_OK) {
        PRINT_ERR("vmm_kheap_init LOS_MemInit failed!\n");
        g_vmBootMemBase -= size;//分配失败时需归还size, g_vmBootMemBase是很野蛮粗暴的
        return ret;
    }
    LOS_MemExpandEnable(OS_SYS_MEM_ADDR);//地址可扩展
    return LOS_OK;
}
```





内核空间用了三个全局变量，其中一个是互斥LosMux，IPC部分会详细讲，这里先不展开。 比较有意思的是LOS_DL_LIST_HEAD，看内核源码过程中经常会为这样的代码点头称赞，TODO:会心一笑。点赞！

https://github.com/kuangyufei/kernel_liteos_a_note/blob/5eeb8eb6ffc8475b86e336b317dd5c39f2f3e3a1/kernel/include/los_list.h#L592

```c
#define LOS_DL_LIST_HEAD(list) LOS_DL_LIST list = { &(list), &(list) }
```

---

## Page是如何初始化的？

https://github.com/kuangyufei/kernel_liteos_a_note/blob/c7eee5a9ca11f214b5601c501d9510bc8e16e802/kernel/base/vm/los_vm_page.c#L47-L55
```c
//虚拟页初始化
STATIC VOID OsVmPageInit(LosVmPage *page, paddr_t pa, UINT8 segID)
{
    LOS_ListInit(&page->node);			//页节点初始化
    page->flags = FILE_PAGE_FREE;		//映射文件初始标识
    LOS_AtomicSet(&page->refCounts, 0);	//引用次数0
    page->physAddr = pa;				//物理地址
    page->segID = segID;				//物理地址使用段管理，段ID
    page->order = VM_LIST_ORDER_MAX;	//所属伙伴算法块组
}
```


page是映射的最小单位，是物理地址<--->虚拟地址映射的数据结构的基础

物理页面通常被称作Page Frames，而虚拟地址空间的页面通常被称为pages.Linux以page为单位管理内存。

https://github.com/kuangyufei/kernel_liteos_a_note/blob/c7eee5a9ca11f214b5601c501d9510bc8e16e802/kernel/base/vm/los_vm_page.c#L61-L90

```c
// page初始化
VOID OsVmPageStartup(VOID)
{
    struct VmPhysSeg *seg = NULL;
    LosVmPage *page = NULL;
    paddr_t pa;
    UINT32 nPage;
    INT32 segID;

    OsVmPhysAreaSizeAdjust(ROUNDUP((g_vmBootMemBase - KERNEL_ASPACE_BASE), PAGE_SIZE));//校正 g_physArea size

    nPage = OsVmPhysPageNumGet();//得到 g_physArea 总页数
    g_vmPageArraySize = nPage * sizeof(LosVmPage);//页表总大小
    g_vmPageArray = (LosVmPage *)OsVmBootMemAlloc(g_vmPageArraySize);//申请页表存放区域

    OsVmPhysAreaSizeAdjust(ROUNDUP(g_vmPageArraySize, PAGE_SIZE));// g_physArea 变小

    OsVmPhysSegAdd();// 段页绑定
    OsVmPhysInit();// 加入空闲链表和设置置换算法,LRU(最近最久未使用)算法

    for (segID = 0; segID < g_vmPhysSegNum; segID++) {
        seg = &g_vmPhysSeg[segID];
        nPage = seg->size >> PAGE_SHIFT;
        for (page = seg->pageBase, pa = seg->start; page <= seg->pageBase + nPage;
             page++, pa += PAGE_SIZE) {
            OsVmPageInit(page, pa, segID);//page初始化
        }
        OsVmPageOrderListInit(seg->pageBase, nPage);// 页面分配的排序
    }
}
```


## 内核空间是怎么初始化的？

https://github.com/kuangyufei/kernel_liteos_a_note/blob/169574a2a7bd690d653e5254e4335c181306c906/kernel/base/core/los_process.c#L694-764

```c
//初始化PCB块
STATIC UINT32 OsInitPCB(LosProcessCB *processCB, UINT32 mode, UINT16 priority, UINT16 policy, const CHAR *name)
{
    UINT32 count;
    LosVmSpace *space = NULL;
    LosVmPage *vmPage = NULL;
    status_t status;
    BOOL retVal = FALSE;

    processCB->processMode = mode;//用户态进程还是内核态进程
    processCB->processStatus = OS_PROCESS_STATUS_INIT;//进程初始状态
    processCB->parentProcessID = OS_INVALID_VALUE;//爸爸进程，外面指定
    processCB->threadGroupID = OS_INVALID_VALUE;//所属线程组
    processCB->priority = priority;//进程优先级
    processCB->policy = policy;//调度算法 LOS_SCHED_RR
    processCB->umask = OS_PROCESS_DEFAULT_UMASK;//掩码
    processCB->timerID = (timer_t)(UINTPTR)MAX_INVALID_TIMER_VID;

    LOS_ListInit(&processCB->threadSiblingList);//初始化孩子任务/线程链表，上面挂的都是由此fork的孩子线程 见于 OsTaskCBInit LOS_ListTailInsert(&(processCB->threadSiblingList), &(taskCB->threadList));
    LOS_ListInit(&processCB->childrenList);		//初始化孩子进程链表，上面挂的都是由此fork的孩子进程 见于 OsCopyParent LOS_ListTailInsert(&parentProcessCB->childrenList, &childProcessCB->siblingList);
    LOS_ListInit(&processCB->exitChildList);	//初始化记录退出孩子进程链表，上面挂的是哪些exit	见于 OsProcessNaturalExit LOS_ListTailInsert(&parentCB->exitChildList, &processCB->siblingList);
    LOS_ListInit(&(processCB->waitList));		//初始化等待任务链表 上面挂的是处于等待的 见于 OsWaitInsertWaitLIstInOrder LOS_ListHeadInsert(&processCB->waitList, &runTask->pendList);

    for (count = 0; count < OS_PRIORITY_QUEUE_NUM; ++count) { //根据 priority数 创建对应个数的队列
        LOS_ListInit(&processCB->threadPriQueueList[count]); //初始化一个个线程队列，队列中存放就绪状态的线程/task
    }//在鸿蒙内核中 task就是thread,在鸿蒙源码分析系列篇中有详细阐释 见于 https://my.oschina.net/u/3751245

    if (OsProcessIsUserMode(processCB)) {// 是否为用户模式进程
        space = LOS_MemAlloc(m_aucSysMem0, sizeof(LosVmSpace));//分配一个虚拟空间
        if (space == NULL) {
            PRINT_ERR("%s %d, alloc space failed\n", __FUNCTION__, __LINE__);
            return LOS_ENOMEM;
        }
        VADDR_T *ttb = LOS_PhysPagesAllocContiguous(1);//分配一个物理页用于存储L1页表 4G虚拟内存分成 （4096*1M）
        if (ttb == NULL) {//这里直接获取物理页ttb
            PRINT_ERR("%s %d, alloc ttb or space failed\n", __FUNCTION__, __LINE__);
            (VOID)LOS_MemFree(m_aucSysMem0, space);
            return LOS_ENOMEM;
        }
        (VOID)memset_s(ttb, PAGE_SIZE, 0, PAGE_SIZE);//内存清0
        retVal = OsUserVmSpaceInit(space, ttb);//初始化虚拟空间和本进程 mmu
        vmPage = OsVmVaddrToPage(ttb);//通过虚拟地址拿到page
        if ((retVal == FALSE) || (vmPage == NULL)) {//异常处理
            PRINT_ERR("create space failed! ret: %d, vmPage: %#x\n", retVal, vmPage);
            processCB->processStatus = OS_PROCESS_FLAG_UNUSED;//进程未使用,干净
            (VOID)LOS_MemFree(m_aucSysMem0, space);//释放虚拟空间
            LOS_PhysPagesFreeContiguous(ttb, 1);//释放物理页,4K
            return LOS_EAGAIN;
        }
        processCB->vmSpace = space;//设为进程虚拟空间
        LOS_ListAdd(&processCB->vmSpace->archMmu.ptList, &(vmPage->node));//将空间映射页表挂在 空间的mmu L1页表, L1为表头
    } else {
        processCB->vmSpace = LOS_GetKVmSpace();//内核共用一个虚拟空间,内核进程 常驻内存
    }

#ifdef LOSCFG_SECURITY_VID
    status = VidMapListInit(processCB);
    if (status != LOS_OK) {
        PRINT_ERR("VidMapListInit failed!\n");
        return LOS_ENOMEM;
    }
#endif
#ifdef LOSCFG_SECURITY_CAPABILITY
    OsInitCapability(processCB);
#endif

    if (OsSetProcessName(processCB, name) != LOS_OK) {
        return LOS_ENOMEM;
    }

    return LOS_OK;
}
```

---

https://github.com/kuangyufei/kernel_liteos_a_note/blob/62d5a09843ddec5ea0e43e72232981b655978eef/kernel/base/vm/los_vm_map.c#L56

https://github.com/kuangyufei/kernel_liteos_a_note/blob/62d5a09843ddec5ea0e43e72232981b655978eef/kernel/base/vm/los_vm_map.c#L71-L75

```c
//内核虚拟空间只有g_kVmSpace一个
LosVmSpace *LOS_GetKVmSpace(VOID)
{
    return &g_kVmSpace;
}
```
从代码可以看出，内核空间固定只有一个g_kVmSpace，而每个用户进程的虚拟内存空间都是独立的。请细品！

---

## task是如何申请内存的？

task的主体是来自进程池，task池是统一分配的，怎么创建task池的去翻系列篇里的文章。这里task只需要申请stack空间，还是直接上看源码吧，用OsUserInitProcess函数看应用程序的main() 是如何被内核创建任务和运行的。

https://github.com/kuangyufei/kernel_liteos_a_note/blob/169574a2a7bd690d653e5254e4335c181306c906/kernel/base/include/los_process_pri.h#L474

https://github.com/kuangyufei/kernel_liteos_a_note/blob/169574a2a7bd690d653e5254e4335c181306c906/kernel/base/core/los_process.c#L1605-L1645

```c
//所有的用户进程都是使用同一个用户代码段描述符和用户数据段描述符，它们是__USER_CS和__USER_DS，
//也就是每个进程处于用户态时，它们的CS寄存器和DS寄存器中的值是相同的。当任何进程或者中断异常进入内核后，
//都是使用相同的内核代码段描述符和内核数据段描述符，它们是__KERNEL_CS和__KERNEL_DS。这里要明确记得，内核数据段实际上就是内核态堆栈段。
LITE_OS_SEC_TEXT_INIT UINT32 OsUserInitProcess(VOID)
{
    INT32 ret;
    UINT32 size;
    TSK_INIT_PARAM_S param = { 0 };
    VOID *stack = NULL;
    VOID *userText = NULL;
    CHAR *userInitTextStart = (CHAR *)&__user_init_entry;//代码区开始位置 ,对应 LITE_USER_SEC_ENTRY
    CHAR *userInitBssStart = (CHAR *)&__user_init_bss;// 未初始化数据区（BSS）。在运行时改变其值 对应 LITE_USER_SEC_BSS
    CHAR *userInitEnd = (CHAR *)&__user_init_end;// 结束地址
    UINT32 initBssSize = userInitEnd - userInitBssStart;
    UINT32 initSize = userInitEnd - userInitTextStart;

    LosProcessCB *processCB = OS_PCB_FROM_PID(g_userInitProcess);//"Init进程的优先级是 28"
    ret = OsProcessCreateInit(processCB, OS_USER_MODE, "Init", OS_PROCESS_USERINIT_PRIORITY);// 初始化用户进程,它将是所有应用程序的父进程
    if (ret != LOS_OK) {
        return ret;
    }

    userText = LOS_PhysPagesAllocContiguous(initSize >> PAGE_SHIFT);// 分配连续的物理页
    if (userText == NULL) {
        ret = LOS_NOK;
        goto ERROR;
    }

    (VOID)memcpy_s(userText, initSize, (VOID *)&__user_init_load_addr, initSize);// 安全copy 经加载器load的结果 __user_init_load_addr -> userText
    ret = LOS_VaddrToPaddrMmap(processCB->vmSpace, (VADDR_T)(UINTPTR)userInitTextStart, LOS_PaddrQuery(userText),
                               initSize, VM_MAP_REGION_FLAG_PERM_READ | VM_MAP_REGION_FLAG_PERM_WRITE |
                               VM_MAP_REGION_FLAG_PERM_EXECUTE | VM_MAP_REGION_FLAG_PERM_USER);// 虚拟地址与物理地址的映射
    if (ret < 0) {
        goto ERROR;
    }
```

所有的用户进程都是通过init进程 fork来的， 可以看到创建进程的同时创建了一个task, 入口函数就是代码区的第一条指令,也就是应用程序 main函数。

这里再说下stack的大小，不同空间下的task栈空间是不一样的，鸿蒙内核中有三种栈空间size,如下

https://gitee.com/openharmony/kernel_liteos_a/blob/master/kernel/base/include/los_process_pri.h#L313-L315

https://github.com/kuangyufei/kernel_liteos_a_note/blob/master/kernel/base/include/los_process_pri.h#L313-L315

#define LOSCFG_BASE_CORE_TSK_IDLE_STACK_SIZE SIZE(0x800)//内核进程，运行在内核空间2K
#define OS_USER_TASK_SYSCALL_SATCK_SIZE 0x3000 //用户进程，通过系统调用创建的task运行在内核空间的 12K
#define OS_USER_TASK_STACK_SIZE         0x100000//用户进程运行在用户空间的1M

---


https://search.gitee.com/?skin=rec&type=code&q=OS_USER_TASK_SYSCALL_SATCK_SIZE&repo=VFZSRmVVMVVaekJPZWxwb1RucFplbHBuUFQxaE56WXpaZz09YTc2M2Y=&reponame=openharmony/kernel_liteos_a

initParam->uwStackSize = OS_USER_TASK_SYSCALL_SATCK_SIZE;

---

https://gitee.com/openharmony/kernel_liteos_a/pulls/43

https://gitee.com/openharmony/kernel_liteos_a/pulls/42
