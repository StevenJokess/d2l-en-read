# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-21 22:23:26
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-21 22:25:03
Description:
TODO::
Reference:https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/pix2pix/pix2pix.py
'''
if opt.checkpoint_interval != -1 and epoch % opt.checkpoint_interval == 0:
    # Save model checkpoints
    torch.save(generator.state_dict(), "saved_models/%s/generator_%d.pth" % (opt.dataset_name, epoch))
    torch.save(discriminator.state_dict(), "saved_models/%s/discriminator_%d.pth" % (opt.dataset_name, epoch))
