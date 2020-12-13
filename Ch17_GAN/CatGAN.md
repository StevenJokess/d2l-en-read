

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-12 18:59:03
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-12 19:00:14
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/u014625530/article/details/82393414?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.control
-->

现在将推导出用于无监督和半监督学习的分类生成对抗网络（CatGAN）的目标函数。作者首先将自己局限于无监督设置，这可以通过将GAN框架推广到多个类来获得，并在3.3章中介绍了半监督学习。应该注意的是，从正则化信息最大化（RIM）的角度出发，可以等效地推导出CatGAN模型，如附录中所述（注：附录未翻译），且具有相同的结果。

简而言之：CatGAN模型性能与现有最佳算法相当，在MNIST上实现了237 ± 6 237\pm6237±6的对数似然，相比下，Goodfellow等2014年的结果是225 ± 2 225\pm2225±2。然而这并不一定意味着CatGAN模型是优越的，因为比较生成模型通过Parzen窗口估计测量的对数似然可能会产生误导（Theis等2015的深入讨论）。

CatGAN与更先进的生成对抗网络架构的组合会是很有趣的未来工作。
