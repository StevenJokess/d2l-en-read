

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 19:17:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 19:17:30
 * @Description:
 * @TODO::
 * @Reference:facebookresearch_pytorch
-->
# let's plot these images using torchvision and matplotlib
import matplotlib.pyplot as plt
import torchvision
plt.imshow(torchvision.utils.make_grid(generated_images).permute(1, 2, 0).cpu().numpy())
# plt.show()
