

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 20:05:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 20:11:54
 * @Description:
 * @TODO::
 * @Reference:[1]: https://autotorch.org/course/beginer_torch.html
 * [2]: https://github.com/facebookresearch/pytorch_GAN_zoo/blob/master/visualization/visualizer.py
-->
[1]:
# get the datasets

trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

## dataloaders

trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True, num_workers=2)
testloader = torch.utils.data.DataLoader(testset, batch_size=128, shuffle=False, num_workers=2)

---
[2]:

    out_data_size = (data.size()[0], data.size()[
                     1], out_size_image[0], out_size_image[1])

    outdata = torch.empty(out_data_size)
    data = torch.clamp(data, min=-1, max=1)
