

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-22 23:58:21
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 23:58:32
 * @Description:
 * @TODO::
 * @Reference:https://github.com/ultralytics/yolov5/issues/22
-->
from models.yolo import Model
yaml_path='models/yolov5m.yaml'
new_weights='weights/yolov5m_resave.pt'
model = Model(yaml_path).to(device)
model.load_state_dict(torch.load(new_weights))
