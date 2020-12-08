

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 19:48:12
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 19:48:25
 * @Description:
 * @TODO::
 * @Reference:https://github.com/t-vi/pytorch-tvmisc/blob/master/wasserstein-distance/Improved_Training_of_Wasserstein_GAN.ipynb
-->
class MyLeakyReLU(nn.Module):
    def __init__(self, negative_slope=0.01):
        super(MyLeakyReLU, self).__init__()
        self.negative_slope = negative_slope
    def forward(self, x):
        return torch.clamp(x, min=0.0)+torch.clamp(x, max=0.0)*self.negative_slope
