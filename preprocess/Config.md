

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 22:00:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 22:00:43
 * @Description:
 * @TODO::
 * @Reference:https://github.com/chenyuntc/pytorch-GAN/blob/master/WGAN.ipynb
-->
class Config:
    lr = 0.00005
    nz = 100 # noise dimension
    image_size = 64
    image_size2 = 64
    nc = 3 # chanel of img
    ngf = 64 # generate channel
    ndf = 64 # discriminative channel
    beta1 = 0.5
    batch_size = 32
    max_epoch = 50 # =1 when debug
    workers = 2
    gpu = True # use gpu or not
    clamp_num=0.01# WGAN clip gradient

opt=Config()
