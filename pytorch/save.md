

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 22:10:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 22:41:40
 * @Description:
 * @TODO::
 * @Reference:https://github.com/malzantot/Pytorch-conditional-GANs/blob/master/conditional_dcgan.py
-->

    parser.add_argument('--save_every', type=int, default=1,
                        help='After how many epochs to save the model.')
        if epoch_idx % args.save_every == 0:
            torch.save({'state_dict': model_d.state_dict()},
                        '{}/model_d_epoch_{}.pth'.format(
                            args.save_dir, epoch_idx))
            torch.save({'state_dict': model_g.state_dict()},
                        '{}/model_g_epoch_{}.pth'.format(
                            args.save_dir, epoch_idx))

---

https://github.com/pytorch/examples/blob/master/dcgan/main.py
    # do checkpointing
    torch.save(netG.state_dict(), '%s/netG_epoch_%d.pth' % (opt.outf, epoch))
    torch.save(netD.state_dict(), '%s/netD_epoch_%d.pth' % (opt.outf, epoch))
