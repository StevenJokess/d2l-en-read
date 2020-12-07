

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 14:44:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 16:28:16
 * @Description:
 * @TODO::
 * @Reference:https://github.com/MIT-HAN-LAB/ProxylessNAS
 * https://pytorch.org/hub/pytorch_vision_proxylessnas/
-->

---

News
Next generation of ProxylessNAS: Once-for-All (First place in the 3rd and 4th Low-Power Computer Vision Challenge).
First place in the Visual Wake Words Challenge, TF-lite track, @CVPR 2019
Third place in the Low Power Image Recognition Challenge (LPIRC), classification track, @CVPR 2019

---

专业化

人们习惯于将一个模型部署到所有平台上，但这并不好。为了充分利用效率，我们应该为每个平台专门化架构。

我们提供了搜索过程的可视化。更多结果请参考我们的论文。



[2]
import torch
target_platform = "proxyless_cpu"
# proxyless_gpu, proxyless_mobile, proxyless_mobile14 are also avaliable.
model = torch.hub.load('mit-han-lab/ProxylessNAS', target_platform, pretrained=True)
model.eval()



https://github.com/mit-han-lab/proxylessnas/tree/master/proxyless_nas
