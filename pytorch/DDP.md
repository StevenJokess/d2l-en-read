

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 22:02:19
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 00:18:21
 * @Description:
 * @TODO::
 * @Reference:https://github.com/pytorch/examples/blob/master/distributed/ddp/README.md
 * https://pytorch.org/tutorials/beginner/dist_overview.html
 * http://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/139986/cn_zh/1568950210259/pytorch_dist_mnist.py?spm=a2c4g.11186623.2.13.65e629cbIMeapi&file=pytorch_dist_mnist.py
-->

分布式数据并行(DDP)应用程序可以在多个节点上执行，每个节点可以由多个GPU设备组成。每个节点依次可以运行DDP应用程序的多个副本，每个副本在多个gpu上处理其模型。

设N为应用程序运行的节点数，G为每个节点的gpu数。同时在所有节点上运行的应用程序进程总数称为世界大小W，在每个节点上运行的进程数称为本地世界大小L。

每个应用进程被分配两个id:一个局部级别在[0,L-1]，一个全局级别在[0,W-1]。

为了说明上面定义的术语，考虑在两个节点上启动DDP应用程序的情况，每个节点都有四个gpu。然后，我们希望每个进程都跨越两个gpu。流程到节点的映射如下图所示:

```py
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import oss2
import re
from tqdm import tqdm

from io import BytesIO
from PIL import Image

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data.dataset import Dataset
from torchvision import datasets, transforms
from torch.nn.parallel import DistributedDataParallel as DDP

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--inputs", type=str, default='inputspath')
parser.add_argument("--checkpointDir", type=str, default='Checkpoint dir')

args = parser.parse_args()

ak = ""#ç”¨æˆ·è‡ªå·±çš„ak
akSec = ""#ç”¨æˆ·è‡ªå·±çš„secret

class OSSMnistDataset(Dataset):
  """
  Args:
    oss_prefix (string): a oss directory to mnist dataset. such as oss://bucket/mnist/
    host: oss endpoint
    ak: your oss ak
    akSec: your oss akSec
    train: wether load training data or test data
    transform: pytorch transforms for transforms and tensor conversion
  """
  training_file = 'training.pt'
  test_file = 'test.pt'

  def __init__(self, oss_path, ak, akSec, train=True, transform=None):
    self.train = train  # training set or test set
    if self.train:
      data_file = self.training_file
    else:
      data_file = self.test_file

    self.transform = transform

    o = re.search(r"oss://(.*?)\.(.*?)/(.*)", oss_path)
    bucket = o.group(1)
    host = o.group(2)
    path = o.group(3)

    auth = oss2.Auth(ak, akSec)
    bucket = oss2.Bucket(
        auth,
        host,
        bucket)
    buffer = BytesIO(bucket.get_object(os.path.join(path, data_file)).read())
    self.data, self.targets = torch.load(buffer)

  def __getitem__(self, index):
    """
        Args:
        index (int): Index
        Returns:
        tuple: (image, target) where target is index of the target class.
    """
    img, target = self.data[index], int(self.targets[index])

    # doing this so that it is consistent with all other datasets
    # to return a PIL Image
    img = Image.fromarray(img.numpy(), mode='L')

    if self.transform is not None:
      img = self.transform(img)

    return img, target

  def __len__(self):
    return len(self.data)

class Net(nn.Module):
  def __init__(self):
    super(Net, self).__init__()
    self.conv1 = nn.Conv2d(1, 20, 5, 1)
    self.conv2 = nn.Conv2d(20, 50, 5, 1)
    self.fc1 = nn.Linear(4*4*50, 500)
    self.fc2 = nn.Linear(500, 10)

  def forward(self, x):
    x = F.relu(self.conv1(x))
    x = F.max_pool2d(x, 2, 2)
    x = F.relu(self.conv2(x))
    x = F.max_pool2d(x, 2, 2)
    x = x.view(-1, 4*4*50)
    x = F.relu(self.fc1(x))
    x = self.fc2(x)
    return F.log_softmax(x, dim=1)

def train(model, device, train_loader, optimizer, epoch):
  model.train()
  for batch_idx, (data, target) in tqdm(enumerate(train_loader)):
    data, target = data.to(device), target.to(device)
    optimizer.zero_grad()
    output = model(data)
    loss = F.nll_loss(output, target)
    loss.backward()
    optimizer.step()
    if batch_idx % 10 == 0:
      print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
        epoch, batch_idx * len(data), len(train_loader.dataset),
        100. * batch_idx / len(train_loader), loss.item()))

def test(model, device, test_loader):
  model.eval()
  test_loss = 0
  correct = 0
  with torch.no_grad():
    for data, target in test_loader:
      data, target = data.to(device), target.to(device)
      output = model(data)
      test_loss += F.nll_loss(output, target, reduction='sum').item() # sum up batch loss
      pred = output.argmax(dim=1, keepdim=True) # get the index of the max log-probability
      correct += pred.eq(target.view_as(pred)).sum().item()

  test_loss /= len(test_loader.dataset)

  print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
    test_loss, correct, len(test_loader.dataset),
    100. * correct / len(test_loader.dataset)))

def main():
  device = torch.device("cuda")

  kwargs = {'num_workers': 1, 'pin_memory': True}

  train_dataset = OSSMnistDataset(
    args.inputs,
    ak,
    akSec,
    train=True,
    transform=transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ]))

  train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)

  train_loader = torch.utils.data.DataLoader(
    train_dataset, sampler=train_sampler,
    batch_size=64, **kwargs)

  test_dataset = OSSMnistDataset(
    args.inputs,
    ak,
    akSec,
    train=False,
    transform=transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ]))
  test_loader = torch.utils.data.DataLoader(
    test_dataset,
    batch_size=64, **kwargs)

  model = Net().to(device)
  model = DDP(model)
  optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)

  for epoch in range(1, 10):
    train(model, device, train_loader, optimizer, epoch)
    test(model, device, test_loader)

if __name__ == '__main__':
  torch.distributed.init_process_group("nccl")
  main()
```
