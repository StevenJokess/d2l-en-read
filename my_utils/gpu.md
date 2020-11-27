

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 23:19:21
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 23:22:35
 * @Description:
 * @TODO::
 * @Reference:https://discuss.gluon.ai/t/topic/13576
-->
nvidia-smi -L

GPU 0: Tesla P100-PCIE-16GB (UUID: GPU-bdfaaf53-cf7f-4930-ccc0-8fb94dfed819)
GPU 1: Tesla P100-PCIE-12GB (UUID: GPU-fcf7844a-6bfa-f826-536c-19423c0cb5ea)
GPU 2: Tesla P100-PCIE-12GB (UUID: GPU-709abe77-f2aa-1b94-a704-34be456c2330)
GPU 3: Tesla P100-PCIE-12GB (UUID: GPU-823f8869-76f4-395c-7734-d4311c95528e)


Windows下的安装
Windows下的显卡驱动安装很简单，打开NVIDIA官网的显卡驱动下载地址 319，然后根据自己的操作系统，显卡型号，将最新的稳定版的显卡驱动下载下来双击运行，然后全部采用默认设置，按照提示便可以完成安装。这里选择的是安装最新的稳定版本的显卡驱动，因为NVIDIA官网最新稳定版的显卡驱动，肯定可以满足所有cuda版本对于显卡驱动版本的要求。

Ubuntu下的显卡驱动安装
注：这里将要说的安装方法，适用于Ubuntu 16.04和Ubuntu 18.04。其它的Ubuntu版本没测试过。
为Ubuntu安装NVIDIA驱动主要有两种方式，一种是到NVIDIA官网下载对应显卡型号的驱动的.run文件，然后按照NVIDIA官网的说明安装即可。这种安装方法失败率很高，并且安装过程十分繁琐，不推荐使用这种方式。另外一种是通过添加Ubuntu官方维护的NVIDIA显卡驱动源，然后使用apt来安装即可，推荐使用这种方法。注意，采用第二种方法时，由于Ubuntu官方维护的NVIDIA显卡驱动源在国外，因此下载速度十分缓慢，安装显卡驱动需要几个小时都有可能，而且80%的概率会因为网速问题导致显卡驱动安装失败。建议安装显卡驱动这个步骤在北京时间早上7点到9点之间进行，那个时候在国内访问该软件源的网速是最快的，几分钟就能安装好。下面是采用第二种方法来安装显卡驱动的具体的步骤。
1.执行如下命令将Ubuntu官方维护的NVIDIA显卡驱动软件源添加到系统中：

sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
2.执行如下命令，查看适合自己电脑的显卡驱动：

sudo ubuntu-drivers devices
执行上面的命令之后，会显示如下内容：

driver   : nvidia-340 - distro non-free
driver   : nvidia-driver-410 - third-party free
driver   : nvidia-driver-418 - third-party free
driver   : nvidia-driver-415 - third-party free
driver   : nvidia-driver-390 - distro non-free
driver   : nvidia-driver-430 - third-party free recommended
driver   : nvidia-driver-396 - third-party free
driver   : xserver-xorg-video-nouveau - distro free builtin
我们可以看到第六行的nvidia-driver-430的最后带有“recommended”字样，即系统推荐我们安装该版本的显卡驱动，这时候我们只需要执行如下命令来安装即可：

sudo apt install nvidia-driver-430
电脑不同推荐的版本有可能不一样，因此到时候你安装带有recommended的版本即可。安装完显卡驱动之后，重启即可。重启之后，你在Ubuntu里打开NVIDIA X Server Settings这个软件（安装显卡驱动的时候自动给装上的），便能看到你显卡驱动的详细信息了。 到此显卡驱动安装完成。

arch Linux下的显卡驱动安装
打开终端，执行如下命令便可以安装最新的长期支持版的显卡驱动：

sudo pacman  -S  nvidia-lts
