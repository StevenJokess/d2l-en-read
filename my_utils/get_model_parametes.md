

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 22:31:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 22:32:02
 * @Description:
 * @TODO::
 * @Reference:https://github.com/leaderj1001/MobileNetV3-Pytorch
-->
def get_model_parameters(model):
    total_parameters = 0
    for layer in list(model.parameters()):
        layer_parameter = 1
        for l in list(layer.size()):
            layer_parameter *= l
        total_parameters += layer_parameter
    return total_parameters

print("Number of model parameters: ", get_model_parameters(model))

