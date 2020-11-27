

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 19:17:50
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 21:20:14
 * @Description:
 * @TODO::
 * @Reference:https://github.com/ShusenTang/Dive-into-DL-PyTorch
 * https://github.com/jantic/DeOldify
-->

使用如下命令创建一个名称为「d2dl」的docker镜像：

docker build -t d2dl .
镜像创建好后，运行如下命令创建一个新的容器：

docker run -dp 3000:3000 d2dl
最后在浏览器中打开这个地址http://localhost:3000/#/，就能愉快地访问文档了。

---
Dockerfile

FROM node:alpine
RUN npm i docsify-cli -g
COPY . /data
WORKDIR /data
CMD [ "docsify", "serve", "docs" ]

---

Docker
Docker for Jupyter
You can build and run the docker using the following process:

Cloning

git clone https://github.com/jantic/DeOldify.git DeOldify
Building Docker

cd DeOldify && docker build -t deoldify_jupyter -f Dockerfile .
Running Docker

echo "http://$(curl ifconfig.io):8888" && nvidia-docker run --ipc=host --env NOTEBOOK_PASSWORD="pass123" -p 8888:8888 -it deoldify_jupyter
Docker for API
You can build and run the docker using the following process:

Cloning

git clone https://github.com/jantic/DeOldify.git DeOldify
Building Docker

cd DeOldify && docker build -t deoldify_api -f Dockerfile-api .
Note: The above command produces a docker image configured for image processing. To build a docker image for video processing, edit the Dockerfile-api file, replacing CMD ["app.py"] with CMD ["app-video.py"]

Running Docker

echo "http://$(curl ifconfig.io):5000" && nvidia-docker run --ipc=host -p 5000:5000 -d deoldify_api
Calling the API for image processing

curl -X POST "http://MY_SUPER_API_IP:5000/process" -H "accept: image/png" -H "Content-Type: application/json" -d "{\"source_url\":\"http://www.afrikanheritage.com/wp-content/uploads/2015/08/slave-family-P.jpeg\", \"render_factor\":35}" --output colorized_image.png
Calling the API for video processing

curl -X POST "http://MY_SUPER_API_IP:5000/process" -H "accept: application/octet-stream" -H "Content-Type: application/json" -d "{\"source_url\":\"https://v.redd.it/d1ku57kvuf421/HLSPlaylist.m3u8\", \"render_factor\":35}" --output colorized_video.mp4
Note: If you don't have Nvidia Docker, here is the installation guide.
