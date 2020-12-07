

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-14 22:24:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 20:53:19
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html
 * [2]: https://github.com/t-vi/AICamera/blob/pytorch_master/Exporting%20Squeezenet%20to%20mobile.ipynb
-->
For this tutorial, you will need to install ONNX and ONNX Runtime. You can get binary builds of ONNX and ONNX Runtime with

pip install onnx onnxruntime

. Note that ONNX Runtime is compatible with Python versions 3.5 to 3.7.

# Export the model[2]
torch_out = torch.onnx._export(torch_model,             # model being run
                               x,                       # model input (or a tuple for multiple inputs)
                               "squeezenet.onnx",       # where to save the model (can be a file or file-like object)
                               export_params=True)      # store the trained parameter weights inside the model file
