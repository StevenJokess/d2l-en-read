

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 00:05:46
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 00:06:09
 * @Description:
 * @TODO::
 * @Reference:https://github.com/anilsathyan7/pytorch-image-classification/blob/master/eval.py
-->

import multiprocessing

# Configure batch size and nuber of cpu's
num_cpu = multiprocessing.cpu_count()
bs = 8

eval_loader=data.DataLoader(eval_dataset, batch_size=bs, shuffle=True,
                            num_workers=num_cpu, pin_memory=True)
