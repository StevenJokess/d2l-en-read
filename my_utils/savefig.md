

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 19:43:51
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 21:04:56
 * @Description:
 * @TODO::
 * @Reference:
-->

⑧保存为pdf格式：

fig.savefig("XXX.pdf", format='pdf', transparent=True, dpi=300, pad_inches=0)
https://0809zheng.github.io/2020/09/25/curve.html

fig.savefig("gan_mnist/%d.png" % epoch)

https://blog.csdn.net/nyz5211314/article/details/106260225


---

plt.imsave(f"outputs/output_{filename}", dreamed_image)
https://github.com/eriklindernoren/PyTorch-Deep-Dream/blob/master/deep_dream.py
