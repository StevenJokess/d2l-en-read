

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 18:13:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 22:45:53
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/weixin_44791964/article/details/105739918
 * https://github.com/ultralytics/yolov5/issues/36
-->
import torch.utils.model_zoo as model_zoo

model_urls = {
'resnet18': 'https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth',
'resnet34': 'https://s3.amazonaws.com/pytorch/models/resnet34-333f7ec4.pth',
'resnet50': 'https://s3.amazonaws.com/pytorch/models/resnet50-19c8e357.pth',
'resnet101': 'https://s3.amazonaws.com/pytorch/models/resnet101-5d3b4d8f.pth',
'resnet152': 'https://s3.amazonaws.com/pytorch/models/resnet152-b121ed2d.pth',
}

def resnet50():
    model = ResNet(Bottleneck, [3, 4, 6, 3])
    # 获取特征提取部分
    features = list([model.conv1, model.bn1, model.relu, model.maxpool, model.layer1, model.layer2, model.layer3])
    # 获取分类部分
    classifier = list([model.layer4, model.avgpool])
    features = nn.Sequential(*features)
    classifier = nn.Sequential(*classifier)
    return features,classifier
---


model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='yolov5s_voc_best.pt')
model = model.autoshape()  # for PIL/cv2/np inputs and NMS

---

https://pytorch.org/docs/stable/hub.html

state_dict = torch.hub.load_state_dict_from_url('https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth')
