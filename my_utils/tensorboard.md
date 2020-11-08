

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-06 00:16:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 16:33:46
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

[1]: https://ai.deepshare.net/detail/v_5e169de5a8d9e_cXstCouX/3?from=p_5d5529ce477d5_gjTtDfAH&type=5
[2]: https://www.tensorflow.org/tutorials/generative/pix2pix
TODO: https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html
