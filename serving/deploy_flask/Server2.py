# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-08 22:31:30
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-08 22:35:04
Description:
TODO::
Reference:https://blog.csdn.net/qq_41375318/article/details/106106368
'''
# -*- coding: utf-8 -*-
# 导入常用的库
import time
import os
import torch
from PIL import Image
import torchvision.transforms as transforms
import json
# 导入flask库的Flask类和request对象
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # 定义字典className_list，把种类索引转换为种类名称
# className_list = ['__background__', 'wheat_head']

#------------------------------------------------------1.加载模型--------------------------------------------------------------
path_model="./saved_model/model2.pkl"
#model_loaded=torch.load(path_model,map_location='cpu') # 只有cpu加载模型
model_loaded=torch.load(path_model)
#------------------------------------------------------2.获取测试图片--------------------------------------------------------------

# img_dir=os.path.join(BASE_DIR ,"data", "global-wheat-detection","test")
# names = [name for name in list(filter(lambda x: x.endswith(".jpg"), os.listdir(img_dir)))]
#path_img = os.path.join(BASE_DIR ,"data", "global-wheat-detection","test",i)

# 根据图片文件路径获取图像数据矩阵
def get_imageNdarray(imageFilePath):
    input_image = Image.open(imageFilePath).convert("RGB")
    return input_image


#------------------------------------------------------3.定义图片预处理--------------------------------------------------------------
# 模型预测前必要的图像处理
def process_imageNdarray(input_image):
    preprocess = transforms.Compose([
        transforms.ToTensor(),
    ])
    img_chw = preprocess(input_image)
    return img_chw  # chw:channel height width

#------------------------------------------------------4.模型预测--------------------------------------------------------------
# 使用模型对指定图片文件路径完成图像分类，返回值为预测的种类名称
def predict_image(model, imageFilePath):
    model.eval()  # 参数固化
    input_image = get_imageNdarray(imageFilePath)
    img_chw = process_imageNdarray(input_image)
    if torch.cuda.is_available():
        img_chw = img_chw.to('cuda')
        model.to('cuda')
    input_list = [img_chw]
    with torch.no_grad():  # 不计算梯度
        output_list = model(input_list)
        output_dict = output_list[0]
        #print('对此图片路径 %s 的预测结果为 %s' % (output_dict))
        return output_dict

#------------------------------------------------------5.服务返回--------------------------------------------------------------


# 访问首页时的调用函数
@app.route('/')
def index_page():
    return render_template('index.html')


# 使用predict_image这个API服务时的调用函数
@app.route("/upload_image", methods=['POST'])
def anyname_you_like():
    startTime = time.time()
    received_file = request.files['input_image']
    imageFileName = received_file.filename
    if received_file:
        received_dirPath = '../resources/received_images'
        if not os.path.isdir(received_dirPath):
            os.makedirs(received_dirPath)
        imageFilePath = os.path.join(received_dirPath, imageFileName)
        received_file.save(imageFilePath)
        print('image file saved to %s' % imageFilePath)
        usedTime = time.time() - startTime
        print('接收图片并保存，总共耗时%.2f秒' % usedTime)
        startTime = time.time()
        result = predict_image(model_loaded, imageFilePath)
        result = str(result)
        usedTime = time.time() - startTime
        print('完成对接收图片的预测，总共耗时%.2f秒' % usedTime)
        # return result
        return render_template("result.html",result=result)
    else:
        return 'failed'



# 主函数
if __name__ == "__main__":
    # print('在开启服务前，先测试predict_image函数')
    # imageFilePath = 'D:\\PycharmWorkPlaces\\DeepModel_deploy_flask\\data\\global-wheat-detection\\test\\51b3e36ab.jpg'
    # result = predict_image(model_loaded, imageFilePath)
    app.run("127.0.0.1", port=5000)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
客户端：index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>测试</title>
    </head>
    <body>
        <div>
            <form method="post" action="http://localhost:5000/upload_image" enctype="multipart/form-data">
               <input type="file"  value="选择检测图片" size="22" id="select_files" name="input_image" onchange="show_selectedImage()"/>
               <br>
               <canvas id="image_canvas" height="1020" width="1020"></canvas>
               <text name="image_className" value=""/>
               <br>
               <input type="submit" class="button-new" value="提交信息" style="margin-top:15px;"/>
            </form>

            <script type="text/javascript">
                function show_selectedImage(){
                    /// get select files.
                    var selected_files = document.getElementById("select_files").files;
                    for(var file of selected_files){
                        console.log(file.webkitRelativePath);
                        /// read file content.
                        var reader = new FileReader();
                        reader.readAsDataURL(file);
                        reader.onloadend = function(){
                            /// deal data.
                            var img = new Image();
                            /// after loader, result storage the file content result.
                            img.src = this.result;
                            img.onload = function(){
                                var canvas = document.getElementById("image_canvas");
                                var cxt = canvas.getContext('2d');
                                cxt.drawImage(img, 0, 0);
                            }
                        }
                    }
                }
            </script>
        </div>
    </body>
</html>
