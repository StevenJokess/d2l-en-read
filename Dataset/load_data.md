

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 17:22:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 17:22:42
 * @Description:
 * @TODO::
 * @Reference:https://github.com/udacity/deep-learning-v2-pytorch/blob/master/project-tv-script-generation/helper.py
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
