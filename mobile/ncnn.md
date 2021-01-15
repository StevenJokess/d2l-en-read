https://blog.csdn.net/qq_36810544/article/details/106911025


安装onnx简化工具
pip3 install onnx-simplifier onnxruntime
1
简化onnx模型
这一步一定要做，否则后面转onnx的时候会报错

python3 -m onnxsim model.onnx model_sim.onnx
