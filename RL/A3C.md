

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 15:28:24
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-18 19:33:33
 * @Description:
 * @TODO::
 * @Reference:
-->
A3C 算法全称为 Asynchronous Advantage Actor-Critic 算法，是 DeepMind 基于 Advantage Actor-Critic 算法提出来的异步版本 [8]，将 Actor-Critic 网络部署在多个线程中 同时进行训练，并通过全局网络来同步参数。这种异步训练的模式大大提升了训练效率， 训练速度更快，并且算法性能也更好。 如图 14.22 所示，算法会新建一个全局网络 Global Network 和 M 个 Worker 线程， Global Network 包含了 Actor 和 Critic 网络，每个线程均新建一个交互环境和 Actor 和 Critic 网络。初始化阶段 Global Network 随机初始化参数𝜃 和𝜙 ，Worker 中的 Actor-Critic 网络从 Global Network 中同步拉取参数来初始化网络。在训练时，Worker 中的 Actor-Critic 网络首先从 Global Network 拉取最新参数，然后在最新策略𝜋𝜃(𝑎𝑡|𝑠𝑡)才采样动作与私有环 境进行交互，并根据 Advantage Actor-Critic 算法方法计算参数𝜃 和𝜙的梯度信息。完成梯 度计算后，各个 Worker 将梯度信息提交到 Global Network 中，利用 Global Network 的优化 器完成 Global Network 的网络参数更新。在算法测试阶段，只使用 Global Network 与环境 交互即可。

接下来我们实现异步的 A3C 算法。和普通的 Advantage AC 算法一样，需要创建 ActorCritic 网络大类，它包含了一个 Actor 子网络和一个 Critic 子网络，有时 Actor 和 Critic 会共享前面网络数层，减少网络的参数量。平衡杆游戏比较简单，我们使用一个 2 层 全连接网络来参数化 Actor 网络，使用另一个 2 层全连接网络来参数化 Critic 网络



## 智能体

智能体负责整个 A3C 算法的训练。在智能体类初始化阶段，新建 Global Network 全局网络对象 server 和它的优化器对象 opt。代码如下：

```py
class Agent:
    # 智能体，包含了中央服务器网络 server
    def __init__(self):
        # server 优化器，client 不需要，直接从 server 拉取参数
        self.opt = optimizers.Adam(1e-3)
        # 中央模型，类似于参数服务器
        self.server = ActorCritic(4, 2) # 状态向量，动作数量
        self.server(tf.random.normal((2, 4)))
```

https://github.com/MorvanZhou/pytorch-A3C
