

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 20:08:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 20:10:43
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch09.html#idm45762347307368
 * https://www.hhyz.me/2018/04/11/RCNN/
-->

# R-CNN

4 个应用于不同任务的已有的算法很好的结合了起来，最终在目标检测任务中取得了不错的效果

当然在后续的 Fast-RCNN 与 Faster-RCNN 中模型逐步完善并整合成为一个模型，但是在 R-CNN 中是没有的。

R-CNN 由 4 个部分构成:

区域建议算法（ss）
特征提取算法（AlexNet）
线性分类器（线性 SVM）
边界框修正回归模型（Bounding box）

简单来说，RCNN 使用以下四步实现目标检测：

在图像中确定约 1000-2000 个候选框
对于每个候选框内图像块，使用深度网络提取特征
对候选框中提取出的特征，使用分类器判别是否属于一个特定类
对于属于某一特征的候选框，用回归器进一步调整其位置

Bounding box也是个古老的话题了，计算机视觉常见任务中，在分类与检测之间还有一个定位任务，在一副图像中只有一个目标，然后把这个目标框出来，用到的就是Bounding box回归模型。在R-CNN中，Bounding box的作用是修正ss推荐的区域的边界，输入的特征是AlexNet的第五层特征，与SVM分类器一样，它也是每一个类别都有一个模型，一共20个。

## R-CNN 的训练

R-CNN训练了CNN，SVM与Bounding box三个模型，因为ss不用训练。ss在生成了1000-2000个推荐区域之后，就和训练任务没关系了，训练样本是由ss区域生成出来的子图构建起来的。 而且三个部分的训练时独立的，并没有整合在一起。

1. 训练CNN
CNN是在ImageNet上pre-train的AlexNet模型，在R-CNN中进行fine-tune，fine-tune的过程是将AlexNet的Softmax改为任务需要的类别数，然后还是当做一个分类模型来训练，训练样本的构建使用ss生成的子图，当这些图与实际样本的框（Ground-truth）的IoU大于等于0.5时，认为是某一个类的正样本，这样的类一共有20个；IoU小于0.5时，认为是负样本。然后就可以AlexNet做pre-train了，pre-train之后AlexNet的Softmax层就被扔掉了，只剩下训练后的参数，这套参数就用来做特征提取。

2. 训练SVM
之前提到了，SVM的输入特征是AlexNet fc7的输出，然后SVM做二分类，一个有20个SVM模型。那么对于其中某一个分类器来说，它的正样本是所有Ground-truth区域经过AlexNet后输出的特征，负样本是与Ground-truth区域重合IoU小于0.3的区域经过AlexNet后输出的特征，特征和标签确定了，就可以训练SVM了。




Faster R-CNN and Mask R-CNN
Facebook Research has produced the maskrcnn-benchmark library, which contains reference implementations of both object detection and segmentation algorithms. We’re going to install the library and add code to generate predictions. At the time of this writing, the easiest way to build the models is by using Docker (this may change when PyTorch 1.2 is released). Clone the repository from https://github.com/facebookresearch/maskrcnn-benchmark and add this script, predict.py, into the demo directory to set up a prediction pipeline using a ResNet-101 backbone:

import matplotlib.pyplot as plt

from PIL import Image
import numpy as np
import sys
from maskrcnn_benchmark.config import cfg
from predictor import COCODemo

config_file = "../configs/caffe2/e2e_faster_rcnn_R_101_FPN_1x_caffe2.yaml"

cfg.merge_from_file(config_file)
cfg.merge_from_list(["MODEL.DEVICE", "cpu"])

coco_demo = COCODemo(
    cfg,
    min_image_size=500,
    confidence_threshold=0.7,
)


pil_image = Image.open(sys.argv[1])
image = np.array(pil_image)[:, :, [2, 1, 0]]
predictions = coco_demo.run_on_opencv_image(image)
predictions = predictions[:,:,::-1]

plt.imsave(sys.argv[2], predictions)
In this short script, we’re first setting up the COCODemo predictor, making sure that we pass in the configuration that sets up Faster R-CNN instead of Mask R-CNN (which will produce segmented output). We then open an image file set on the command line, but we have to turn it into BGR format instead of RGB format as the predictor is trained on OpenCV images rather than the PIL images we’ve been using so far. Finally, we use imsave to write the predictions array (the original image plus bounding boxes) to a new file, also specified on the command line. Copy in a test image file into this demo directory and we can then build the Docker image:

docker build docker/
We run the script from inside the Docker container and produce output that looks like Figure 9-7 (I actually used the library to generate that image). Try experimenting with different confidence_threshold values and different pictures. You can also switch to the e2e_mask_rcnn_R_101_FPN_1x_caffe2.yaml configuration to try out Mask R-CNN and generate segmentation masks as well.

To train your own data on the models, you’ll need to supply your own dataset that provides bounding box labels for each image. The library provides a helper function called BoxList. Here’s a skeleton implementation of a dataset that you could use as a starting point:

from maskrcnn_benchmark.structures.bounding_box import BoxList

class MyDataset(object):
    def __init__(self, path, transforms=None):
        self.images = # set up image list
        self.boxes = # read in boxes
        self.labels = # read in labels

    def __getitem__(self, idx):
        image = # Get PIL image from self.images
        boxes = # Create a list of arrays, one per box in x1, y1, x2, y2 format
        labels = # labels that correspond to the boxes

        boxlist = BoxList(boxes, image.size, mode="xyxy")
        boxlist.add_field("labels", labels)

        if self.transforms:
            image, boxlist = self.transforms(image, boxlist)

        return image, boxlist, idx

    def get_img_info(self, idx):
        return {"height": img_height, "width": img_width
You’ll then need to add your newly created dataset to maskrcnn_benchmark/data/datasets/init.py and maskrcnn_benchmark/config/paths_catalog.py. Training can then be carried out using the supplied train_net.py script in the repo. Be aware that you may have to decrease the batch size to train any of these networks on a single GPU.

That wraps it up for object detection and segmentation, though see “Further Reading” for more ideas, including the wonderfully entitled You Only Look Once (YOLO) architecture. In the meantime, we look at how to maliciously break a model.
