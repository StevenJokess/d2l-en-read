

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 00:41:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 22:41:17
 * @Description:
 * @TODO::
 * @Reference:https://github.com/bentrevett/pytorch-generative-models/blob/master/RLSGAN.ipynb
-->
#display N_SHOW images
        print(f'| Epoch: {epoch:03} | D(x): {pred_real_1.mean().item():.03f} / {pred_real_2.mean().item():.03f} | D(G(z)): {pred_fake_1.mean().item():.03f} / {pred_fake_2.mean().item():.03f} | D_error: {D_error.item():.03f} | G_error: {G_error.item():.03f} |')


        torchvision.utils.save_image(generated_images,
                                     f'images/rgan/epoch{epoch:03}.png',
                                     nrow=N_SHOW,
                                     normalize=True)

        img = plt.imread(f'images/rgan/epoch{epoch:03}.png')
        plt.imshow(img)
        plt.show()

---

https://github.com/pytorch/examples/blob/master/dcgan/main.py

        if i % 100 == 0:
            vutils.save_image(real_cpu,
                    '%s/real_samples.png' % opt.outf,
                    normalize=True)
            fake = netG(fixed_noise)
            vutils.save_image(fake.detach(),
                    '%s/fake_samples_epoch_%03d.png' % (opt.outf, epoch),
                    normalize=True)
