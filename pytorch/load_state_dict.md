

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 22:00:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 22:00:10
 * @Description:
 * @TODO::
 * @Reference:https://github.com/chenyuntc/pytorch-GAN/blob/master/WGAN.ipynb
-->
t.save(netd.state_dict(),'epoch_wnetd.pth')
t.save(netg.state_dict(),'epoch_wnetg.pth')
In [8]:
netd.load_state_dict(t.load('epoch_wnetd.pth'))
netg.load_state_dict(t.load('epoch_wnetg.pth'))
