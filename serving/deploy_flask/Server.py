# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-08 22:24:43
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-08 22:25:01
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
# 导入flask库的Flask类和request对象
from flask import request, Flask
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # 定义字典className_list，把种类索引转换为种类名称
# className_list = ['__background__', 'wheat_head']

#------------------------------------------------------1.加载模型--------------------------------------------------------------
path_model="./saved_model/model2.pkl"
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
# 定义回调函数，接收来自/的post请求，并返回预测结果
@app.route("/", methods=['POST'])
def return_result():
    startTime = time.time()
    received_file = request.files['file']
    imageFileName = received_file.filename
    if received_file:
        received_dirPath = './resources/received_images'
        if not os.path.isdir(received_dirPath):
            os.makedirs(received_dirPath)
        imageFilePath = os.path.join(received_dirPath, imageFileName)
        received_file.save(imageFilePath)
        print('图片文件保存到此路径：%s' % imageFilePath)
        usedTime = time.time() - startTime
        print('接收图片并保存，总共耗时%.2f秒' % usedTime)
        startTime = time.time()
        print(imageFilePath)
        result = predict_image(model_loaded, imageFilePath)
        result = str(result)
        print(result)
        usedTime = time.time() - startTime
        print('完成对接收图片的检测，总共耗时%.2f秒' % usedTime)
        print("testtest",result)
        return result
    else:
        return 'failed'


# 主函数
if __name__ == "__main__":
    #print('在开启服务前，先测试predict_image函数')
    # imageFilePath = os.path.join(BASE_DIR, "data", "global-wheat-detection", "test", "51b3e36ab.jpg")
    # result = predict_image(model_loaded, 'D:\\PycharmWorkPlaces\\DeepModel_deploy_flask\\data\\global-wheat-detection\\test\\51b3e36ab.jpg')
    # print(result)
    app.run("127.0.0.1", port=5000)
