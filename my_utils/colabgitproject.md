

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 17:14:32
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 17:14:33
 * @Description:
 * @TODO::
 * @Reference:https://colab.research.google.com/github/tugstugi/dl-colab-notebooks/blob/master/notebooks/NVidia_Flowtron_Waveglow.ipynb#scrollTo=GHIBEHtW-eHZ
-->
import os
from os.path import exists, join, basename, splitext

git_repo_url = 'https://github.com/NVIDIA/flowtron.git'
project_name = splitext(basename(git_repo_url))[0]
if not exists(project_name):
  # clone and install
  !git clone -q --recursive {git_repo_url}
  !pip install -q librosa unidecode gdown

os.chdir(project_name)
