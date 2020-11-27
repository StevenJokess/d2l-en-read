

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 19:17:50
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 19:19:44
 * @Description:
 * @TODO::
 * @Reference:https://github.com/ShusenTang/Dive-into-DL-PyTorch
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
