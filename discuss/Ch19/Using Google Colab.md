

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 18:58:37
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 18:59:00
 * @Description:https://discuss.d2l.ai/t/using-google-colab/424
 * @TODO::
 * @Reference:
-->



StevenJokes
5
Aug 13
[colab]read img: No such file: solved
git clone whole repo(include /img):
Go to https://colab.research.google.com/

Create a new notebook

image
image
1004×680 37.5 KB
image

Mount it to your google Drive
image

image
image
850×202 13.6 KB
Create a new folder:
image

name it d2l-en:

image

git clone : reference

%cd drive/My Drive/d2l-en

!git clone https://github.com/d2l-ai/d2l-en-colab.git

!git clone https://github.com/d2l-ai/d2l-pytorch-colab.git

!git clone https://github.com/d2l-ai/d2l-tensorflow-colab.git

The result is

image
image
1165×882 76.1 KB
mxnet repo: https://github.com/d2l-ai/d2l-en-colab

pytorch repo:https://github.com/d2l-ai/d2l-pytorch-colab

tensorflow repo:https://github.com/d2l-ai/d2l-tensorflow-colab

Delete a folder:


import shutil

shutil.rmtree('/content/drive/My Drive/d2l-en', ignore_errors=True)

More Tutorial 1

An issue I have: Still can’t open .ipynb file in my drive

https://drive.google.com/drive/folders/1V84YTT-yhRPAZIF7tRoQN9a6pYm8Ju24?usp=sharing 1

read img
mount
https://colab.research.google.com/github/d2l-ai/d2l-en-colab/blob/master/chapter_computer-vision/fcn.ipynb?hl=en 1
image

run:

from google.colab import drive
drive.mount('/content/drive')
image
image
2044×267 56.9 KB

image
cd drive/My Drive/d2l-en/d2l-en-colab
!ls

!pwd

%cd drive/My Drive/d2l-en

%cd d2l-en-colab
image
image
1944×855 77.1 KB
imread
..img instead of .img
image
image
1569×296 49.6 KB
My code: colab or github
It applies to any imread or ·file control· if you have the matching repo to framework.

@mli, @astonzhang, @goldpiggy
Maybe you can get some help for all colab code to aviod this issue from 1:19:
CS231n Google Colab Assignment Workflow Tutorial
CS231n Google Colab Assignment Workflow Tutorial



StevenJokes
2
29d
PyTorch is already installed. Both the CPU and GPU should work: pytorch-latest-cpu

pytorch-latest-gpu

image
image

For more details on using PyTorch on Google Cloud, see:
https://cloud.google.com/deep-learning-vm/docs/images 1

from https://github.com/rmunro/pytorch_active_learning

!pip show d2l
image
