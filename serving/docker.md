

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 21:11:37
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 21:47:43
 * @Description:
 * @TODO::
 * @Reference:https://github.com/ultralytics/yolov5/wiki/Docker-Quickstart
 * GPU开发环境 - xyoungli的文章 - 知乎
https://zhuanlan.zhihu.com/p/85789000
-->

1. Install Docker and Nvidia-Docker
Docker images come with all dependencies preinstalled, however Docker itself requires installation, and relies of nvidia driver installations in order to interact properly with local GPU resources. The requirements are:

Nvidia Driver >= 455.23 https://www.nvidia.com/Download/index.aspx
Nvidia-Docker https://github.com/NVIDIA/nvidia-docker
Docker Engine - CE >= 19.03 https://docs.docker.com/install/
2. Pull Image
3. Run Container
Run an interactive instance of this image (called a "container") using -it:

sudo docker run --ipc=host -it ultralytics/yolov5:latest
Run a container with local file access (like COCO training data in /coco) using -v:

sudo docker run --ipc=host -it -v "$(pwd)"/coco:/usr/src/coco ultralytics/yolov5:latest
Run a container with GPU access using --gpus all:

sudo docker run --ipc=host --gpus all -it ultralytics/yolov5:latest
