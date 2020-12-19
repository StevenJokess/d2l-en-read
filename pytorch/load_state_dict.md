

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 22:00:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 23:39:59
 * @Description:
 * @TODO::
 * @Reference:https://github.com/chenyuntc/pytorch-GAN/blob/master/WGAN.ipynb
 * https://github.com/keineahnung2345/MorvanZhou-PyTorch-Tutorial-With-Detailed-Note/blob/master/tutorial-contents-notebooks/304_save_reload.ipynb
-->
t.save(netd.state_dict(),'epoch_wnetd.pth')
t.save(netg.state_dict(),'epoch_wnetg.pth')
In [8]:
netd.load_state_dict(t.load('epoch_wnetd.pth'))
netg.load_state_dict(t.load('epoch_wnetg.pth'))

---

def restore_params():
    # restore only the parameters in net1 to net3
    net3 = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 1)
    )

    # copy net1's parameters into net3
    net3.load_state_dict(torch.load('net_params.pkl'))
    prediction = net3(x)

    # plot result
    plt.subplot(133)
    plt.title('Net3')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
    plt.show()

---
# restore only the net parameters
restore_params()
