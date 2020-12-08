

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-06 00:16:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 01:20:22
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

[1]: https://ai.deepshare.net/detail/v_5e169de5a8d9e_cXstCouX/3?from=p_5d5529ce477d5_gjTtDfAH&type=5
[2]: https://www.tensorflow.org/tutorials/generative/pix2pix
[3]: https://docs.fast.ai/callback.tensorboard.html#TensorBoardCallback
TODO: https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html
