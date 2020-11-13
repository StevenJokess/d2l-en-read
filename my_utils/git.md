

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 22:50:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 18:26:11
 * @Description:
 * @TODO::
 * @Reference:https://github.com/pytorch/pytorch#adjust-build-options-optional
 * https://github.com/liueo/TVM-deploy
-->
Get the PyTorch Source
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive

Always use git clone --recursive, if not, we can update tvm submodule git submodule update --recursive --init.

