

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 21:24:05
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 21:25:07
 * @Description:
 * @TODO::
 * @Reference:https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb#scrollTo=2fLAV42oNb7M
-->
# Weights & Biases (optional)


https://wandb.ai/

In colab,
```
%pip install -q wandb
!wandb login  # use 'wandb disabled' or 'wandb enabled' to disable or enable
```

## Weights & Biases Logging 🌟 NEW

Weights & Biases (W&B) is now integrated with YOLOv5 for real-time visualization and cloud logging of training runs. This allows for better run comparison and introspection, as well improved visibility and collaboration for teams. To enable W&B pip install wandb, and then train normally (you will be guided through setup on first use).

During training you will see live updates at https://wandb.ai/home, and you can create and share detailed Reports of your results. For more information see the YOLOv5 Weights & Biases Tutorial.
