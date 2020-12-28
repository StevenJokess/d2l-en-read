

###
 # @version:
 # @Author:  StevenJokess https://github.com/StevenJokess
 # @Date: 2020-12-28 20:22:15
 # @LastEditors:  StevenJokess https://github.com/StevenJokess
 # @LastEditTime: 2020-12-28 20:22:35
 # @Description:
 # @TODO::
 # @Reference:玩转 GPU 实例之终结篇 – 深度学习的工具与框架 - AWS云计算的文章 - 知乎
https://zhuanlan.zhihu.com/p/258432964
###
#!/bin/bash
set -e

#check dir
if [ ! -d "$HOME/Projects" ]; then
  mkdir -p $HOME/Projects
fi
cd $HOME/Projects

# check git
if ! [ -x "$(command -v git)" ]; then
  echo 'Error: git is not installed.' >&2
  sudo apt -y install git
fi

if [ -d $HOME/.venvs/pytorch_env ];then
  source $HOME/.venvs/pytorch_env/bin/activate
else
  echo "Please setup your pytorch env."
  exit 1
fi

sudo apt install -y libomp-dev libmpfr-dev libgmp-dev libfftw3-dev
pip3 install ninja setuptools wheel numpy pytest -U -q
pip3 install mypy mypy-extensions -U -q

if [ -d pytorch ]; then
  cd pytorch
  git clean -f
else
  # git pull repo
  git clone --recursive https://github.com/pytorch/pytorch
  cd pytorch
fi

# if you are updating an existing checkout
git checkout master
git pull
git submodule sync
git submodule update --init --recursive
pip3 install -r requirements.txt -q

if [ -f  build_pytorch.sh ]; then
  /bin/rm build_pytorch.sh
Fi

cat <<EOT >> build_pytorch.sh
#!/bin/bash

/bin/rm -rf build/*
/bin/rm -rf dist/*

prefix=i\$(python3 -c "import sys;print(sys.prefix)")
if [[ \$prefix == *"pytorch"* ]];then
        echo "You are the venv of pytorch..."
else
        source \$HOME/.venvs/pytorch_env/bin/activate
fi

python3 setup.py clean
USE_CUDA=1 \\
USE_CUDNN=1 \\
CUDNN_LIB_DIR=/usr/lib/x86_64-linux-gnu \\
CUDNN_INCLUDE_DIR=/usr/include \\
BUILD_TEST=0 \\
USE_MKLDNN=1 \\
USE_NNPACK=1 \\
USE_DISTRIBUTED=1 \\
USE_SYSTEM_NCCL=1 \\
USE_NCCL=1 \\
USE_OPENCV=1 \\
NCCL_ROOT=/usr \\
NCCL_INCLUDE_DIR=/usr/include \\
NCCL_LIB_DIR=/usr/lib/x86_64-linux-gnu \\
USE_TENSORRT=0 \\
BUILD_BINARY=1 \\
BUILD_TORCH=ON \\
python3 setup.py bdist_wheel

#install torch
if [ -f dist/*.whl ]; then
  pip3 install -U dist/*.whl -q
  cp dist/*.whl ~/Downloads
fi
EOT

chmod +x build_pytorch.sh
deactivate
echo "Done."
