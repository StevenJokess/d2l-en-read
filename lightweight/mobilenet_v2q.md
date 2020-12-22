

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-22 18:16:46
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 18:16:58
 * @Description:
 * @TODO::
 * @Reference:https://github.com/pytorch/pytorch/blob/master/android/test_app/make_assets.py
-->

mobilenet2q = torchvision.models.quantization.mobilenet_v2(pretrained=True, quantize=True)
mobilenet2q.eval()
torch.jit.trace(mobilenet2q, torch.rand(1, 3, 224, 224)).save("app/src/main/assets/mobilenet2q.pt")
