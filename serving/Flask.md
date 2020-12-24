

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 01:00:01
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 00:14:44
 * @Description:
 * @TODO::
 * @Reference:PyTorch深度学习模型的服务化部署 - 带萝卜的文章 - 知乎
https://zhuanlan.zhihu.com/p/111605233

-->

学习这些内容是为了方便对服务化的模型进行debug，因为web开发的同时常常表示他们很难定位到深度学习服务的bug的位置。



# 用于图片上传的服务

```py
# sim_server.py
from flask import Flask, request
from werkzeug.utils import secure_filename
import uuid
from PIL import Image
import os
import time

app = Flask(__name__)

@app.route("/run",methods = ["GET"])
def run():
    # 用于测试服务是否并行
    time.sleep(1)
    return "0"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5555,debug=True)
```



有了gunicorn和nginx就可以轻松地实现PyTorch模型的多机多卡部署了。
