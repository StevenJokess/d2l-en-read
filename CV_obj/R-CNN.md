

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 20:08:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 20:10:43
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch09.html#idm45762347307368
-->

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