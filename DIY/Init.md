

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 20:49:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 23:50:07
 * @Description:
 * @TODO::
 * @Reference:
-->

https://github.com/znxlwm/pytorch-pix2pix/blob/master/network.py

def normal_init(m, mean, std):
    if isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Conv2d):
        m.weight.data.normal_(mean, std)
        m.bias.data.zero_()

---

https://github.com/bentrevett/pytorch-generative-models/blob/master/3%20-%20LSGAN.ipynb

def weights_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        m.weight.data.normal_(0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        m.weight.data.normal_(1.0, 0.02)
        m.bias.data.fill_(0)

---

https://github.com/NishantTharani/LearningDeepLearning/blob/master/d2l.ai/Ch7/vggnet19.ipynb

    def init_weights(self, layer):
        """ To be applied to a net """
        if type(layer) == nn.Linear or type(layer) == nn.Conv2d:
            torch.nn.init.xavier_uniform_(layer.weight)

---

https://github.com/keineahnung2345/MorvanZhou-PyTorch-Tutorial-With-Detailed-Note/blob/master/tutorial-contents-notebooks/504_batch_normalization.ipynb

    def _set_init(self, layer):
        """
        torch.nn.init.normal_
        normal_(tensor, mean=0, std=1)
        Fills the input Tensor with values drawn from the normal
        distribution :math:`\mathcal{N}(\text{mean}, \text{std})`.
        """
#         init.normal(layer.weight, mean=0., std=.1)
        init.normal_(layer.weight, mean=0., std=.1)
        """
        torch.nn.init.constant_
        constant_(tensor, val)
        Fills the input Tensor with the value :math:`\text{val}`.
        """
#         init.constant(layer.bias, B_INIT)
        init.constant_(layer.bias, B_INIT)
