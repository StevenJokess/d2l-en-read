# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-06 00:17:43
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-06 01:01:37
Description:
TODO::
Reference:https://pytorch.org/docs/stable/tensorboard.html
https://ai.deepshare.net/detail/v_5e169de5a8d9e_cXstCouX/3?from=p_5d5529ce477d5_gjTtDfAH&type=5
'''

import numpy as np
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(comment='test_tensorboard')

for x in range(100):
    writer.add_scalar('y=2x', x * 2, x)
    writer.add_scalar('y=pow(2,x)', 2**x, x)
    writer.add_scalars('data/scalar_group', {"xsinx": x * np.sin(x),
                                            "xcosx": x * np.cos(x),
                                            "arctanx": np.arctan(x)}, x)
writer.close()
