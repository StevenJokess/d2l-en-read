# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-09-28 17:11:32
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-28 21:17:42
Description:
TODO::
Reference:
'''
# https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/models/base_model.py
    def save_networks(self, epoch):
        """Save all the networks to the disk.
        Parameters:
            epoch (int) -- current epoch; used in the file name '%s_net_%s.pth' % (epoch, name)
        """
        for name in self.model_names:
            if isinstance(name, str):
                save_filename = '%s_net_%s.pth' % (epoch, name)
                save_path = os.path.join(self.save_dir, save_filename)
                net = getattr(self, 'net' + name)

                if len(self.gpu_ids) > 0 and torch.cuda.is_available():
                    torch.save(net.module.cpu().state_dict(), save_path)
                    net.cuda(self.gpu_ids[0])
                else:
                    torch.save(net.cpu().state_dict(), save_path)

#---------------------------------------------------------------------------------------

# https://github.com/Dipeshtamboli/GAN_for_clothes/blob/master/CycleGAN/train
    # Save models checkpoints
    torch.save(netG_A2B.state_dict(), output_folder_name+'/netG_A2B.pth')
    torch.save(netG_B2A.state_dict(), output_folder_name+'/netG_B2A.pth')
    torch.save(netD_A.state_dict(), output_folder_name+'/netD_A.pth')
    torch.save(netD_B.state_dict(), output_folder_name+'/netD_B.pth')



#----------------------
# https://github.com/WillSuen/GANs/blob/master/train_cycleGAN.py
#mxnet
        ## save model
        modG_A.save_params(os.path.join(mode_path, 'generatorA'))
        modG_B.save_params(os.path.join(mode_path, 'generatorB'))
        modD_A.save_params(os.path.join(mode_path, 'discriminatorA'))
        modD_B.save_params(os.path.join(mode_path, 'discriminatorB'))
