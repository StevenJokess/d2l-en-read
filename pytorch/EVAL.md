

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 23:54:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 23:54:12
 * @Description:
 * @TODO::
 * @Reference:https://github.com/anilsathyan7/pytorch-image-classification/blob/master/eval.py
-->
# Paths for image directory and model
EVAL_DIR=sys.argv[1])
EVAL_MODEL='models/mobilenetv2.pth'

# Load the model for evaluation
model = torch.load(EVAL_MODEL)
model.eval()
