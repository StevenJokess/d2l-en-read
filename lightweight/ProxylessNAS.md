

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 14:44:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 14:48:11
 * @Description:
 * @TODO::
 * @Reference:https://github.com/MIT-HAN-LAB/ProxylessNAS
 * https://pytorch.org/hub/pytorch_vision_proxylessnas/
-->


[2]
import torch
target_platform = "proxyless_cpu"
# proxyless_gpu, proxyless_mobile, proxyless_mobile14 are also avaliable.
model = torch.hub.load('mit-han-lab/ProxylessNAS', target_platform, pretrained=True)
model.eval()

https://github.com/mit-han-lab/proxylessnas/tree/master/proxyless_nas
