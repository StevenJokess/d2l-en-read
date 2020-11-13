

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 21:33:09
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 21:33:10
 * @Description:
 * @TODO::
 * @Reference:https://colab.research.google.com/github/mit-han-lab/once-for-all/blob/master/tutorial/ofa.ipynb#scrollTo=u4g3bFGtjv9s
-->
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
