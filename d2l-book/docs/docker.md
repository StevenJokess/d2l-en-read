

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-28 02:51:46
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-28 02:56:18
 * @Description:
 * @TODO::
 * @Reference:https://github.com/louielong/d2l-zh/commit/d58a4ae0a07decbe9613bb80b78b3321efbb7257
 * https://hub.docker.com/search?q=d2l&type=image&sort=updated_at&order=desc
-->
## Docker 镜像

快速上手

```shell
docker run -itd --name d2l -p 8888:8888 d2l-zh:latest
```

- 8888为jupyter notebook的web端口

指定工作目录映射

特别的，需要映射工作目录操作如下

```shell
docker run -itd --name d2l -v workplace:/root/d2l-zh/workplace -p 8888:8888 d2l-zh:latest
```

容器通过`docker hub`构建，若需要在国内本地构建，可以开启163和清华源进行加速，加快构建

```shell
sed -i "s/archive\.ubuntu\.com/mirrors\.163\.com/g" /etc/apt/sources.list
sed -i "s/security\.ubuntu\.com/mirrors\.163\.com/g" /etc/apt/sources.list
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



##激活gluon环境**

登录容器后，按照提示使用`source activate gluon`激活`gluon`环境，通过`jupyter notebook list`命令查看`token`

```shell
root@ubuntu:/# source activate gluon
(gluon) root@ubuntu:/# jupyter notebook list
Currently running servers:
http://0.0.0.0:8888/?token=e46448ca9158f6ba8c0b0c0108ffb85c90a1b4dcca5ac30a :: /root/d2l-zh
```

## [使用GPU版的MXNET](https://zh.d2l.ai/chapter_prerequisite/install.html)

安装的MXNet只支持CPU计算，如果你的计算机上有NVIDIA显卡并安装了CUDA，建议使用GPU版的MXNet。

第一步是卸载CPU版本MXNet。如果没有安装虚拟环境，可以跳过此步。如果已安装虚拟环境，需要先激活该环境，再卸载CPU版本的MXNet。

```shell
pip uninstall mxnet
```

然后退出虚拟环境。

第二步是更新依赖为GPU版本的MXNet。使用文本编辑器`vim`打开`/root/d2l-zh/environment.yml`，将里面的字符串“mxnet”替换成对应的GPU版本。例如，如果计算机上装的是8.0版本的CUDA，将该文件中的字符串“mxnet”改为“mxnet-cu80”。如果计算机上安装了其他版本的CUDA（如7.5、9.0、9.2等），对该文件中的字符串“mxnet”做类似修改（如改为“mxnet-cu75”“mxnet-cu90”“mxnet-cu92”等）。保存文件后退出。

第三步是更新虚拟环境，执行命令

```
conda env update -f environment.yml
```

之后，我们只需要再激活安装环境就可以使用GPU版的MXNet运行本书中的代码了。需要提醒的是，如果之后下载了新代码，那么还需要重复这3步操作以使用GPU版的MXNet。
