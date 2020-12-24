

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-24 23:10:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 23:10:19
 * @Description:
 * @TODO::
 * @Reference:https://github.com/roysubhankar/gan-pytorch/blob/master/dcgan.py
-->
    # create a set of transforms for the dataset
    dset_transforms = list()
    dset_transforms.append(transforms.Resize((args.img_size, args.img_size)))
    dset_transforms.append(transforms.ToTensor())
    dset_transforms.append(transforms.Normalize(mean=[0.5, 0.5, 0.5],
                                                std=[0.5, 0.5, 0.5]))
    dset_transforms = transforms.Compose(dset_transforms)
