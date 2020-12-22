

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-22 12:05:08
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 12:05:09
 * @Description:
 * @TODO::
 * @Reference:https://github.com/kazizzad/DCGAN-Gluon-MxNet/blob/master/MxnetDCGAN.ipynb
-->
if opt.dataset == 'cifar10':
    train_data = gluon.data.DataLoader(
        gluon.data.vision.CIFAR10(opt.dataroot, train=True, transform=transformer),
        batch_size= opt.batchSize, shuffle=True, last_batch='discard')

    test_data = gluon.data.DataLoader(
        gluon.data.vision.CIFAR10(opt.dataroot, train=False, transform=transformer),
        batch_size=opt.batchSize, shuffle=False, last_batch='discard')

if opt.dataset == 'celebA':
    opt.dataroot = '%s/celebA/Trainset' % (opt.dataroot)
    train_data = gluon.data.DataLoader(
        gluon.data.vision.ImageFolderDataset(opt.dataroot,transform=transformer),
        batch_size= opt.batchSize, shuffle=True, last_batch='discard')

    test_data = gluon.data.DataLoader(
        gluon.data.vision.ImageFolderDataset(opt.dataroot, transform=transformer),
        batch_size=opt.batchSize, shuffle=False, last_batch='discard')
