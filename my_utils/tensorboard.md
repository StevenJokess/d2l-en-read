

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-06 00:16:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-14 21:48:24
 * @Description:
 * @TODO::
 * @Reference:
-->

```bash
pip install -q -U tensorboard
```

To launch the viewer paste the following into a code-cell:[2]

%load_ext tensorboard
%tensorboard --logdir {log_dir}

```bash
tensorboard --logdir=./runs
```

Validate results in tensorboard[3]
Run the following command in the command line to check if the projector embeddings have been correctly wirtten:

tensorboard --logdir=~/tmp/runs
Open http://localhost:6006 in browser (TensorBoard Projector doesn't work correctly in Safari!)

## Writing to TensorBoard
Now let’s write an image to our TensorBoard - specifically, a grid - using make_grid.

# get some random training images
dataiter = iter(trainloader)
images, labels = dataiter.next()

# create grid of images
img_grid = torchvision.utils.make_grid(images)

# show images
matplotlib_imshow(img_grid, one_channel=True)

# write to tensorboard
writer.add_image('four_fashion_mnist_images', img_grid)
Now running

tensorboard --logdir=runs
```

---


[4]
# Look at training curves in tensorboard:
%load_ext tensorboard
%tensorboard --logdir output

---

[5]

# 仅查看一张图片
writer = SummaryWriter('./data/tensorboard')
writer.add_image('images[0]', images[0])
writer.close()

# 将多张图片拼接成一张图片，中间用黑色网格分割
writer = SummaryWriter('./data/tensorboard')
# create grid of images
img_grid = torchvision.utils.make_grid(images)
writer.add_image('image_grid', img_grid)
writer.close()

# 将多张图片直接写入
writer = SummaryWriter('./data/tensorboard')
writer.add_images("images",images,global_step = 0)
writer.close()



[1]: https://ai.deepshare.net/detail/v_5e169de5a8d9e_cXstCouX/3?from=p_5d5529ce477d5_gjTtDfAH&type=5
[2]: https://www.tensorflow.org/tutorials/generative/pix2pix
[3]: https://docs.fast.ai/callback.tensorboard.html#TensorBoardCallback
[4]: https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5#scrollTo=hBXeH8UXFcqU
[5]: https://github.com/lyhue1991/eat_pytorch_in_20_days/blob/master/5-4%2CTensorBoard%E5%8F%AF%E8%A7%86%E5%8C%96.md

TODO: https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html
