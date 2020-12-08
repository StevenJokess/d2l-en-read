# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-08 22:25:16
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-08 22:25:28
Description:
TODO::
Reference:https://blog.csdn.net/qq_41375318/article/details/106106368
'''
import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 主函数
if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    while True:
        input_content = input('输入图片路径，输入-1退出，默认值os.path.join(BASE_DIR, "data", "global-wheat-detection", "test", "51b3e36ab.jpg") ')
        if input_content.strip() == "":
            input_content = 'D:\\PycharmWorkPlaces\\DeepModel_deploy_flask\\data\\global-wheat-detection\\test\\51b3e36ab.jpg'
        if input_content.strip() == "-1":
            break
        elif not os.path.exists(input_content.strip()):
            print('输入图片路径不正确，请重新输入')
        else:
            imageFilePath = input_content.strip()
            imageFileName = os.path.split(imageFilePath)[1]
            file_dict = {
                'file':(imageFileName,
                    open(imageFilePath,'rb'),
                    'image/jpg')}
            result = requests.post(url, files=file_dict)
            predict_result = result.text
            print('图片路径:%s 预测结果为:%s\n' %(imageFilePath, predict_result))
