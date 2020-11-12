

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 22:30:01
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-12 22:30:42
 * @Description:
 * @TODO::
 * @Reference:https://github.com/thu-ml/tianshou/blob/master/tianshou/data/batch.py
-->

import warnings

# Disable pickle warning related to torch, since it has been removed
# on torch master branch. See Pull Request #39003 for details:
# https://github.com/pytorch/pytorch/pull/39003

warnings.filterwarnings(
    "ignore", message="pickle support for Storage will be removed in 1.5.")
