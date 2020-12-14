

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 17:22:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 22:04:38
 * @Description:
 * @TODO::
 * @Reference:https://github.com/udacity/deep-learning-v2-pytorch/blob/master/project-tv-script-generation/helper.py
 * https://github.com/yunjey/mnist-svhn-transfer/blob/master/data_loader.py
-->

```py
import os
def load_data(path):
    """
    Load Dataset from File
    """
    input_file = os.path.join(path)
    with open(input_file, "r") as f:
        data = f.read()

    return data
```

---


def get_loader(config):
    """Builds and returns Dataloader for MNIST and SVHN dataset."""

    transform = transforms.Compose([
                    transforms.Scale(config.image_size),
                    transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    svhn = datasets.SVHN(root=config.svhn_path, download=True, transform=transform)
    mnist = datasets.MNIST(root=config.mnist_path, download=True, transform=transform)

    svhn_loader = torch.utils.data.DataLoader(dataset=svhn,
                                              batch_size=config.batch_size,
                                              shuffle=True,
                                              num_workers=config.num_workers)

    mnist_loader = torch.utils.data.DataLoader(dataset=mnist,
                                               batch_size=config.batch_size,
                                               shuffle=True,
                                               num_workers=config.num_workers)
    return svhn_loader, mnist_loader
