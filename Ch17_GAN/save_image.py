# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-21 22:39:30
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-21 22:39:34
Description:
TODO::
Reference:https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/esrgan/esrgan.py
'''
        if batches_done % opt.sample_interval == 0:
            # Save image grid with upsampled inputs and ESRGAN outputs
            imgs_lr = nn.functional.interpolate(imgs_lr, scale_factor=4)
            img_grid = denormalize(torch.cat((imgs_lr, gen_hr), -1))
            save_image(img_grid, "images/training/%d.png" % batches_done, nrow=1, normalize=False)
