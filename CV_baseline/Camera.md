

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:22:04
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 18:23:47
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/104839376
-->

## 实现思路

利用opencv调用摄像头，读取每一帧传入目标检测网络检测，将检测结果呈现。
由于本文所用的检测格式为RGB格式，CV2读取的时候会使用BGR格式，因此在检测的时候要利用cv2.cvtColor进行转换。

## 使用到的库
opencv-python==4.1.2.30
Pillow==6.2.1
numpy==1.17.4

```py
from keras.layers import Input
from retinanet import Retinanet
from PIL import Image
import numpy as np
import cv2

retinanet = Retinanet()

# 调用摄像头
capture=cv2.VideoCapture(0)
while(True):
    # 读取某一帧
    ref,frame=capture.read()
    # 格式转变，BGRtoRGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))

    # 进行检测
    frame = np.array(retinanet.detect_image(frame))
    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    cv2.imshow("video",frame)
    c= cv2.waitKey(30) & 0xff
    if c==27:
        capture.release()
        break

retinanet.close_session()
```

---

## FPS记录的原理

FPS简单来理解就是图像的刷新频率，也就是每秒多少帧。
假设目标检测网络处理1帧要0.02s。

```py
#-------------------------------------#
#       调用摄像头检测
#-------------------------------------#
from ssd import SSD
from PIL import Image
import numpy as np
import cv2
import time
ssd = SSD()
# 调用摄像头
capture=cv2.VideoCapture(0) # capture=cv2.VideoCapture("1.mp4")
fps = 0.0
while(True):
    t1 = time.time()
    # 读取某一帧
    ref,frame=capture.read()
    # 格式转变，BGRtoRGB
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))

    # 进行检测
    frame = np.array(ssd.detect_image(frame))

    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

    fps  = ( fps + (1./(time.time()-t1)) ) / 2
    print("fps= %.2f"%(fps))
    frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("video",frame)
    c= cv2.waitKey(30) & 0xff
    if c==27:
        capture.release()
        break
```
