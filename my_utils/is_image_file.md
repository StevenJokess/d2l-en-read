

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 20:25:28
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 20:25:29
 * @Description:
 * @TODO::
 * @Reference:https://github.com/0809zheng/UAN-Pytorch/blob/main/dataset.py
-->

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in [".png", ".jpg", ".jpeg"])
