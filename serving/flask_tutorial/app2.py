# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-12-25 00:58:40
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-25 00:58:51
Description:
TODO::
Reference:https://github.com/surbhardwaj/CNN-Application-SIGN-dataset-in-Pytorch-COUNT_HOW_MANY_FINGERS-/blob/master/app.py
'''
from flask import Flask, request,render_template
import os
from PIL import Image
import cv2
import numpy as np
import torch
from Image_Classifier import Image_Classifier


app = Flask(__name__)




@app.route('/')
def predict_image():
    data =request.files['imagefile']
    img = Image.open(request.files['imagefile'])
    img = np.array(img)
    img = cv2.resize(img,(64,64))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    preds = model.forward(torch.Tensor(img).unsqueeze(0).permute(0, 3, 1, 2))
    predict = np.argmax(preds.detach().numpy(), axis=1)
    result = 'The image shows a :: '+str(predict[0])


    return result






if __name__ == '__main__':

    model = Image_Classifier()
    PATH = "/home/surbhi/Desktop/Vision_Code/Classification/model.pt"
    model = torch.load(PATH)
    model.eval()
    app.run(debug=True)
