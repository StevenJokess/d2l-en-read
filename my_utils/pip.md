

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 21:20:29
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-10 19:42:42
 * @Description:
 * @TODO::
 * @Reference:https://github.com/zhanghang1989/ResNeSt
 * https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html
 * https://pytorch.org/tutorials/_sources/prototype/nnapi_mobilenetv2.rst.txt
 * https://github.com/tatsath/fin-ml
 * https://github.com/HighCWu/SelfGAN/blob/master/implementations/dcgan/self_dcgan_keras_tpu.ipynb
-->

# using github url
pip install git+https://github.com/zhanghang1989/ResNeSt

# using pypi
pip install resnest --pre

pip install git+https://github.com/gautamchitnis/cocoapi.git@cocodataset-master#subdirectory=PythonAPI

pip install --upgrade --pre --find-links https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html torch==1.8.0.dev20201106+cpu torchvision==0.9.0.dev20201107+cpu


If you want to try to install a list of packages from a file. You can use the following command.

$ python3 -m pip install --upgrade -r requirements.txt


! pip install 'tensorflow>1.12,<2.0' -q
