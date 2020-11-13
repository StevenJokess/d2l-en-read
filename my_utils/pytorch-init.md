

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 14:50:19
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 19:38:39
 * @Description:
 * @TODO::
 * @Reference: https://github.com/ZhiqingXiao/pytorch-book/blob/master/chapter10_GAN/cifar_gan.ipynb
 * https://github.com/kuangliu/pytorch-groupnorm/blob/master/groupnorm.py
-->
import torch.nn.init as init

def weights_init(m): # 用于初始化权重值的函数
    if type(m) in [nn.ConvTranspose2d, nn.Conv2d]:
        init.xavier_normal_(m.weight)
    elif type(m) == nn.BatchNorm2d:
        init.normal_(m.weight, 1.0, 0.02)
        init.constant_(m.bias, 0)

gnet.apply(weights_init)
dnet.apply(weights_init)

---

        self.weight = nn.Parameter(torch.ones(1,num_features,1,1))
        self.bias = nn.Parameter(torch.zeros(1,num_features,1,1))
