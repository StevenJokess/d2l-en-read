

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 21:33:09
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-10 19:59:16
 * @Description:
 * @TODO::
 * @Reference:
 * [1]: https://colab.research.google.com/github/baowenbo/DAIN/blob/master/Colab_DAIN.ipynb#scrollTo=irzjv1x4e3S4
 * [2]: https://colab.research.google.com/github/mit-han-lab/once-for-all/blob/master/tutorial/ofa.ipynb#scrollTo=u4g3bFGtjv9s
-->

# Check your current GPU[1]
# If you are lucky, you get 16GB VRAM. If you are not lucky, you get less. VRAM is important. The more VRAM, the higher the maximum resolution will go.

# 16GB: Can handle 720p. 1080p will procude an out-of-memory error.
# 8GB: Can handle 480p. 720p will produce an out-of-memory error.

!nvidia-smi --query-gpu=gpu_name,driver_version,memory.total --format=csv

---
[2]
print('Installing PyTorch...')
! pip install torch 1>/dev/null
print('Installing torchvision...')
! pip install torchvision 1>/dev/null
print('Installing numpy...')
! pip install numpy 1>/dev/null
# thop is a package for FLOPs computing.
print('Installing thop (FLOPs counter) ...')
! pip install thop 1>/dev/null
# ofa is a package containing training code, pretrained specialized models and inference code for the once-for-all networks.
print('Installing OFA...')
! pip install ofa 1>/dev/null
# tqdm is a package for displaying a progress bar.
print('Installing tqdm (progress bar) ...')
! pip install tqdm 1>/dev/null
print('Installing matplotlib...')
! pip install matplotlib 1>/dev/null
print('All required packages have been successfully installed!')

---
https://colab.research.google.com/github/fastai/fastai/blob/master/nbs/index.ipynb
#hide
#skip
! [ -e /content ] && pip install -Uqq fastai  # upgrade fastai on colab
