# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-26 18:31:52
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-26 18:38:38
Description:
TODO::
Reference:https://weread.qq.com/web/reader/d7032cd072021a59d7038afk2a3327002582a38a4a932bf
'''
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def dataloader(dataset, input_size, batch_size, split='train'):
    transform = transform.Compose([
        transforms.Resize((input_size, input_size)),
        transforms.ToTensor(),
        ransforms.Normalize(mean=(0.5,) ,std=(0.5,))])
    if dataset == 'mnist':
        data_loader = DataLoader(datasets.MNIST('./data', train=True, download=True, transform=transform), batch_size=batch_size, shuffle=True)
    elif dataset == 'fashion-mnist':
        data_loader = DataLoader(datasets.FashionMNIST('./data', train=True, download=True), transform=transform,batch_size=batch_size, shuffle=True)
    return data_loader


