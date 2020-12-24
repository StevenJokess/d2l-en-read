

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-24 23:17:53
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 23:18:02
 * @Description:
 * @TODO::
 * @Reference:https://github.com/roysubhankar/visual-domain-adaptation/blob/master/dann/train.py
-->
    # create the dataloaders
    dataloader = {}
    if args.source == 'svhn':
        dataloader['source_train'] = DataLoader(SVHN(os.path.join(args.data_root, args.source), split='train',
                                                transform=dset_transforms, domain_label=0, download=True),
                                                batch_size=args.batch_size, shuffle=True, drop_last=True)
    elif args.source == 'mnist':
        dataloader['source_train'] = DataLoader(MNIST(os.path.join(args.data_root, args.source), train=True,
                                                transform=gray_transforms, domain_label=0, download=True),
                                                batch_size=args.batch_size, shuffle=True, drop_last=True)
    elif args.source == 'mnistm':
        dataloader['source_train'] = DataLoader(MNISTM(os.path.join(args.data_root, args.source), train=True,
                                                      transform=mnistm_transforms, domain_label=0, download=True),
                                                batch_size=args.batch_size, shuffle=True, drop_last=True)
    else:
        raise NotImplementedError

    if args.target == 'svhn':
        dataloader['target_train'] = DataLoader(SVHN(os.path.join(args.data_root, args.target), split='train',
                                                transform=dset_transforms, domain_label=1, download=True),
                                                batch_size=args.batch_size, shuffle=True, drop_last=True)
        dataloader['target_test'] = DataLoader(SVHN(os.path.join(args.data_root, args.target), split='test',
                                               transform=dset_transforms, domain_label=1, download=True),
                                               batch_size=args.batch_size, shuffle=False, drop_last=False)
    elif args.target == 'mnist':
        dataloader['target_train'] = DataLoader(MNIST(os.path.join(args.data_root, args.target), train=True,
                                                transform=gray_transforms, domain_label=1, download=True),
                                                batch_size=args.batch_size, shuffle=True, drop_last=True)
        dataloader['target_test'] = DataLoader(MNIST(os.path.join(args.data_root, args.target), train=False,
                                                transform=gray_transforms, domain_label=1, download=True),
                                                batch_size=args.batch_size, shuffle=False, drop_last=False)
    elif args.target == 'mnistm':
        dataloader['target_train'] = DataLoader(MNISTM(os.path.join(args.data_root, args.target), train=True,
                                                      transform=mnistm_transforms, domain_label=1, download=True),
                                                batch_size=args.batch_size, shuffle=True, drop_last=True)
        dataloader['target_test'] = DataLoader(MNISTM(os.path.join(args.data_root, args.target), train=False,
                                                     transform=mnistm_transforms, domain_label=1, download=True),
                                               batch_size=args.batch_size, shuffle=False, drop_last=False)
    else:
        raise NotImplementedError
