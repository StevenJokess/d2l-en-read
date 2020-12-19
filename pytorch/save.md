

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 22:10:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 22:10:39
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
