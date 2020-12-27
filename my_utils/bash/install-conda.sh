

###
 # @version:
 # @Author:  StevenJokess https://github.com/StevenJokess
 # @Date: 2020-12-27 23:44:33
 # @LastEditors:  StevenJokess https://github.com/StevenJokess
 # @LastEditTime: 2020-12-28 00:14:09
 # @Description:
 # @TODO::
 # @Reference:https://gist.github.com/arose13/fcc1d2d5ad67503ba9842ea64f6bac35

###
# Setup Ubuntu
sudo apt update --yes
sudo apt upgrade --yes

# Get Miniconda and make it the main Python interpreter
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/miniconda
export PATH=~/miniconda/bin:$PATH
rm ~/miniconda.sh


jupyter notebook --port 9999 --allow-root
jupyter notebook --generate-config

