

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 23:08:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 22:11:35
 * @Description:
 * @TODO::
 * @Reference:
-->

#

[1]: https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
```py
# Handle multi-gpu if desired
if (device.type == 'cuda') and (ngpu > 1):
    netD = nn.DataParallel(netD, list(range(ngpu)))
```


[2]: https://github.com/Lyken17/Efficient-PyTorch
默认数据并行PyTorch, powerd由nn。DataParallel, in-efficienct !首先，由于Python的GIL，多线程不能充分利用所有核心torch/nn/parallel/parallel_apply.py#47。第二，DataParallel“集散”方案，将所有结果集在cuda:0上。这会导致工作负载不平衡，有时OOM尤其当你在运行细分模型时。

神经网络。DistributedDataParllel提供了一种更优雅的解决方案:它不是从不同的线程启动调用，而是从多个进程(没有GIL)开始，并为所有gpu分配一个平衡的工作负载。

(正在进行)详细的脚本和实验数据。

---

[3]: https://github.com/facebookresearch/maskrcnn-benchmark#multi-gpu-training

Multi-GPU training
We use internally torch.distributed.launch in order to launch multi-gpu training. This utility function from PyTorch spawns as many Python processes as the number of GPUs we want to use, and each Python process will only use a single GPU.

export NGPUS=8
python -m torch.distributed.launch --nproc_per_node=$NGPUS /path_to_maskrcnn_benchmark/tools/train_net.py --config-file "path/to/config/file.yaml" MODEL.RPN.FPN_POST_NMS_TOP_N_TRAIN images_per_gpu x 1000
Note we should set MODEL.RPN.FPN_POST_NMS_TOP_N_TRAIN follow the rule in Single-GPU training.

Mixed precision training
We currently use APEX to add Automatic Mixed Precision support. To enable, just do Single-GPU or Multi-GPU training and set DTYPE "float16".

export NGPUS=8
python -m torch.distributed.launch --nproc_per_node=$NGPUS /path_to_maskrcnn_benchmark/tools/train_net.py --config-file "path/to/config/file.yaml" MODEL.RPN.FPN_POST_NMS_TOP_N_TRAIN images_per_gpu x 1000 DTYPE "float16"
If you want more verbose logging, set AMP_VERBOSE True. See Mixed Precision Training guide for more details.

Evaluation
You can test your model directly on single or multiple gpus. Here is an example for Mask R-CNN R-50 FPN with the 1x schedule on 8 GPUS:

export NGPUS=8
python -m torch.distributed.launch --nproc_per_node=$NGPUS /path_to_maskrcnn_benchmark/tools/test_net.py --config-file "configs/e2e_mask_rcnn_R_50_FPN_1x.yaml" TEST.IMS_PER_BATCH 16
To calculate mAP for each class, you can simply modify a few lines in coco_eval.py. See #524 for more details.

---

PyTorch Parallel Training（单机多卡并行、混合精度、同步BN训练指南文档） - Todd的文章 - 知乎
https://zhuanlan.zhihu.com/p/145427849

---

https://github.com/ultralytics/yolov5/issues/475

---

不要用看似方便的DataParallel或DistributedDataParallel，自己调torch.distributed里面的通讯接口进行梯度通讯才是坠吼的。

---
声明模型的时候无脑加find_unused_parameters=True：

args.device = torch.device("cuda", device)
model = nn.parallel.DistributedDataParallel(model, device_ids=[args.device], output_device=args.device, find_unused_parameters=True)
