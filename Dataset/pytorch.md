

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 20:05:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 20:43:07
 * @Description:
 * @TODO::
 * @Reference:[1]: https://autotorch.org/course/beginer_torch.html
 * [2]: https://github.com/facebookresearch/pytorch_GAN_zoo/blob/master/visualization/visualizer.py
 * [3]: https://0809zheng.github.io/2020/11/12/dataset.html
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

---

Build my Dataset in Pytorch.

在使用Pytorch进行项目时，有时候需要读入自己的数据作为训练集和测试集，并按照自己指定的方式和格式处理。

Pytorch定义了Dataset类，在实际使用中可以通过继承Dataset类来构建数据集：

from torch.utils.data import Dataset

class myData(Dataset):
    def __init__(self):
        self.all_data = []  # 用于存放所有的数据
        for i in range(N):  # 遍历所有数据
            self.all_data.append([x, y])  # 将一个样本和标签为一组存放进去

    def __getitem__(self, index):  # 返回一个样本和标签
        return self.all_data[index][0], self.all_data[index][1]

    def __len__(self):  # 返回所有样本的数目
        return len(self.all_data)
定义数据集后，通过标准类实例化可以创建并加载数据：

myDataSet = myData()  # 实例化自己构建的数据集
train_loader = Data.DataLoader(dataset=myDataSet, batch_size=BATCH_SIZE, shuffle=False)
创建数据集后，通过枚举获得数据并使用：

for iter, (data, label) in enumerate(train_loader):
    print(data.shape)
    print(label.shape)