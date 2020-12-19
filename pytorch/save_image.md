

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 00:41:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 00:41:37
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
