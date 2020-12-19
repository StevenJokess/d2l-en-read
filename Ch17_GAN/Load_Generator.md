

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 22:57:40
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 22:57:41
 * @Description:
 * @TODO::
 * @Reference:https://github.com/jayleicn/animeGAN/blob/master/Visualization.ipynb
-->
Load Generator
In [2]:
model_path = 'netG.pth'
netG = models._netG_1(2, 100, 3,64, 1) # ngpu, nz, nc, ngf, n_extra_layers
netG.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage))
print(netG)
