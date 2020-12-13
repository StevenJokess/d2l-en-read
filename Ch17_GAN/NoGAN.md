

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-10 19:49:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-10 20:05:00
 * @Description:
 * @TODO::
 * @Reference:[1]: https://github.com/jantic/DeOldify#what-is-nogan
 * [2]: https://github.com/styler00dollar/Colab-DeOldify
-->
This is a new type of GAN training that I've developed to solve some key problems in the previous DeOldify model. It provides the benefits of GAN training while spending minimal time doing direct GAN training. Instead, most of the training time is spent pretraining the generator and critic separately with more straight-forward, fast and reliable conventional methods. A key insight here is that those more "conventional" methods generally get you most of the results you need, and that GANs can be used to close the gap on realism. During the very short amount of actual GAN training the generator not only gets the full realistic colorization capabilities that used to take days of progressively resized GAN training, but it also doesn't accrue nearly as much of the artifacts and other ugly baggage of GANs. In fact, you can pretty much eliminate glitches and artifacts almost entirely depending on your approach. As far as I know this is a new technique. And it's incredibly effective.[1]

[2]
