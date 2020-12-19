

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 01:12:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:12:36
 * @Description:
 * @TODO::
 * @Reference:https://github.com/keineahnung2345/MorvanZhou-PyTorch-Tutorial-With-Detailed-Note/blob/master/tutorial-contents-notebooks/304_save_reload.ipynb
-->
def restore_net():
    # restore entire net1 to net2
    net2 = torch.load('net.pkl')
    prediction = net2(x)

    # plot result
    plt.subplot(132)
    plt.title('Net2')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
