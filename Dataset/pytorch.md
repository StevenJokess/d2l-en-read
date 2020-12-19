

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 20:05:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 20:38:45
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

---

[4]: https://github.com/wnma3mz/pytorch_init/blob/master/pipline.py

```py

from torchvision.datasets import CIFAR100, CIFAR10

def get_dataset(batch_size, dataset_dir='./'):
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2023, 0.1994, 0.2010)),
    ])

    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2023, 0.1994, 0.2010)),
    ])

    trainset = CIFAR100(root=dataset_dir,
                        train=True,
                        download=False,
                        transform=transform_train)

    testset = CIFAR100(root=dataset_dir,
                       train=False,
                       download=False,
                       transform=transform_test)

    trainloader = DataLoader(trainset,
                             batch_size=batch_size,
                             shuffle=True,
                             num_workers=0)

    testloader = DataLoader(testset,
                            batch_size=batch_size,
                            shuffle=False,
                            num_workers=0)

    return trainloader, testloader
```

---
from torchvision import datasets

    svhn = datasets.SVHN(root=config.svhn_path, download=True, transform=transform)
    mnist = datasets.MNIST(root=config.mnist_path, download=True, transform=transform)

---
[6]: https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb#scrollTo=V0AJnSeCIHyJ
# Download COCO test-dev2017
torch.hub.download_url_to_file('https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip', 'tmp.zip')
!unzip -q tmp.zip -d ../ && rm tmp.zip  # unzip labels
!f="test2017.zip" && curl http://images.cocodataset.org/zips/$f -o $f && unzip -q $f && rm $f  # 7GB,  41k images
%mv ./test2017 ./coco/images && mv ./coco ../  # move images to /coco and move /coco next to /yolov5

---
[7]: https://github.com/omerbsezer/Fast-Pytorch

torchvision.datasets.MNIST(root='data/mnist', train=True, transform=transform, target_transform=None, download=True) # with example
torchvision.datasets.FashionMNIST(root='data/fashion-mnist', train=True, transform=transform, target_transform=None, download=True) # with example
torchvision.datasets.KMNIST(root, train=True, transform=None, target_transform=None, download=False)
torchvision.datasets.EMNIST(root, split, **kwargs)
torchvision.datasets.FakeData(size=1000, image_size=(3, 224, 224), num_classes=10, transform=None, target_transform=None, random_offset=0)
torchvision.datasets.CocoCaptions(root, annFile, transform=None, target_transform=None)
torchvision.datasets.CocoDetection(root, annFile, transform=None, target_transform=None)
torchvision.datasets.LSUN(root, classes='train', transform=None, target_transform=None)
torchvision.datasets.CIFAR10(root, train=True, transform=None, target_transform=None, download=False)
torchvision.datasets.STL10(root, split='train', transform=None, target_transform=None, download=False)
torchvision.datasets.SVHN(root, split='train', transform=None, target_transform=None, download=False)
torchvision.datasets.PhotoTour(root, name, train=True, transform=None, download=False)
torchvision.datasets.SBU(root, transform=None, target_transform=None, download=True)
torchvision.datasets.Flickr8k(root, ann_file, transform=None, target_transform=None)
torchvision.datasets.VOCSegmentation(root, year='2012', image_set='train', download=False, transform=None, target_transform=None)
torchvision.datasets.Cityscapes(root, split='train', mode='fine', target_type='instance', transform=None, target_transform=None)
