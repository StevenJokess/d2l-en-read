

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 19:31:49
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 19:32:56
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_installation/index.html
 * @TODO::
 * @Reference:
-->
After run conda activate d2l

# sanity check that the path to the python
# binary matches that of the anaconda env
# after you activate it
which python
To deactivate the environment, either run conda deactivate d2l or exit the terminal. Note that every time you want to work on the assignment, you should rerun conda activate d2l . manage-environments
Reference

only cpu version:
http://preview.d2l.ai/d2l-en/PR-1304/chapter_installation/index.html in my pull

import torch
torch.__version__
torch.cuda.current_device()
torch.cuda.get_device_name(0)
Recommend my repo that records all my study process about pytorch version of d2l-en : https://github.com/StevenJokes/d2l-en-read
Recommend my post: Do these before you ask
More classes:

https://cs230.stanford.edu/blog/pytorch/;
https://cs231n.github.io/
NYU: https://atcold.github.io/pytorch-Deep-Learning/ http://t.cn/A6hkxZpv
I still suggest to use conda install to install pytorch

For Chinese users:
In CMD,
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud//pytorch/
Then look https://pytorch.org/get-started/locally/ to install.
For me,

image
For Chinese users:
It is necessary to use pypi mirror and conda mirror to get pip install and conda install quicker.
pypi mirror:https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
conda mirror:https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
For example:
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
You can add any other channels

image
unset pip mirror: pip config unset global.index-url
unset conda mirror:conda config --remove channels

Check your mirror by printing all configuration:
pip config list
conda config --show

conda config --show-sources

For more
增加清华大学镜像源：
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
删除默认镜像源：
conda config --remove channels defaults


Steven​Jokes
from d2l import torch as d2l

--------------------------------------------------------------------------- ModuleNotFoundError
Traceback (most recent call last) in
1 get_ipython ( ) . run_line_magic ( ‘matplotlib’ , ‘inline’ ) ---->
2 from d2l import torch as d2l
3 import torch
4 import random ~\anaconda3\envs\pytorch\lib\site-packages\d2l\torch.py in
17 import tarfile
18 import time
—>19 import requests
20 import zipfile
21 import hashlib
ModuleNotFoundError : No module named ‘requests’

@mli
Is there a way to install all packages advancely we need to import in torch.py or mxnet.py or tensorflow.py?

I guess the reason of No module named ‘requests’ is that mxnet has ‘requests’ defaulty while pytorch not.

d2l requirements
install_requires vs requirements files

1 reply
6 Aug
goldpiggy
 StevenJokes:
I guess the reason of No module named ‘requests’ is that mxnet has ‘requests’ defaulty while pytorch not.

hey @StevenJokes, just do a pip install requests.

1 reply
7 Aug▶ goldpiggy
Steven​Jokes
I have done this long long ago. Just curious about how to do all this type stuff advancely.

Have found the solution :conda env create -f environment.yml from handson-ml

Or can we add library “requests” to d2l package?

14 Aug
Shashwat
I have been trying to run these ipynb files of PyTorch but I am getting an error every time I try to run them.

Error is:
Unable to read notebook …ipynb notJSONERROR (notebook does not appear to be json) in Ubuntu.

Could someone help to solve me this error?

2 replies
15 Aug▶ Shashwat
goldpiggy
Hi @Shashwat, could specify the Ubuntu version you are using? Is it a local installation without GPU?

1 reply
15 Aug
Steven​Jokes
 Shashwat:
ipynb notJSONERROR

@Shashwat

My first search from google: https://github.com/jupyter/help/issues/67
It may helps you. Can you tell me where do you download there ipynb files?
And more details?

Do you install jupyter?
Maybe you don’t install jupyter book.

Read https://jupyter.org/install. And then you can find these to install jupyter notebook

conda install notebook
or

pip install notebook
Any other problem? Look Do these before you ask!. Figure it out by yourself first.

@goldpiggy
I think we don’t tell them to install jupyter at all.
new commit: https://github.com/d2l-ai/d2l-en/pull/1304/commits/198cc5ff657ae15c9c510448ffa73ac8bc19e452
Help me review!

1 reply
19 Aug▶ goldpiggy
Shashwat
I am using Ubuntu 18.04 with GTX 1050ti graphics card.
Screenshot from 2020-08-19 12-28-13
19 Aug▶ StevenJokes
Shashwat
Thanks Steven,
I already tried the approaches suggested in https://github.com/jupyter/help/issues/67. But they were of no help. I even tried renaming them with a .html extension but it didn’t help either.

I downloaded the ipynb files from https://d2l.ai/index.html from the All notebooks section.

And yeah I am using Jupyter to run these files.

Screenshot from 2020-08-19 12-49-42
1 reply
19 Aug▶ Shashwat
Steven​Jokes
I still can’t find your real problem. Have you run other .ipynb that is not in this book files before?
@Shashwat

But there is what you can try:

update your jupyter
read again: https://d2l.ai/chapter_appendix-tools-for-deep-learning/jupyter.html
image

Have you run jupyter notebook first, then read files in your browser?
install VScode to open it directly: Using Jupyter
read https://forums.fast.ai/t/unreadable-notebook-home-ubuntu-nbs-lesson1-ipynb-notjsonerror-notebook-does-not-appear-to-be-json/2966/9
I guess you choose ipynb files from local disk.
Once all packages are installed, you can open the Jupyter notebook by

jupyter notebook
At this point open http://localhost:8888 (which usually opens automatically) in the browser, then you can view and run the code in each section of the book.

from https://tvm.d2l.ai/

26 Aug
Steven​Jokes
@Shashwat
You’re trying to run the pytorch code that we don’t have now…
Please look this for more details.
 Installation tensorflow
Hello, Maybe my question seems silly. I never used MXNET before and I prefer Tensorflow, but I can’t open some implementation in Tensorflow. In the explorer, it shows .ipynb file size is 0KB and in the jupyter notebook, shows error “Unreadable Notebook: D:\Python scripts\d2l-en\tensorflow\chapter_generative-adversarial-networks\dcgan.ipynb NotJSONError(“Notebook does not appear to be JSON: ‘’…”)”. Help me. Btw, mxnet implementation works okay.
9 Sep
kuil
Hello May be it is very easy problem … I have struggled to solve it but I can’t

I installed torch & torch vision CPU only version as book guided

after installation, I activate virtual env & activate Jupyter notebook and run the code of notebook . I also install requests as your guidance

I met error message like this
OSError: [WinError 126] 지정된 모듈을 찾을 수 없습니다.
Error loading “C:~~\torch\lib\asmjit.dll” or one of its dependencies.

Plz give me a guide to fix it.

1 reply
9 Sep
Steven​Jokes
 kuil:
Error loading “C:~~\torch\lib\asmjit.dll” or one of its dependencies.

@kuil

google first… And convert your language to English next time
stackoverflow.com
