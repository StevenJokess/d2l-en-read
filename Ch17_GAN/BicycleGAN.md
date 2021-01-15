# BicycleGAN

Pix2pix最大的缺点就是需要输入一张ground truth与input image的图像对，G才能从input image中还原出ground truth. 此外，生成的结果也十分单一，为了增加多样性，人们又提出BicycleGAN. 这个GAN主要是结合了cVAE-GAN和cLR-GAN两个变种，同时训练这两个网络，如下图：

[1]: 生成对抗网络系列(3)——cGAN及图像条件 - cuicuicui的文章 - 知乎 https://zhuanlan.zhihu.com/p/35983991
