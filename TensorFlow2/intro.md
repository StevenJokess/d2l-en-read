

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 15:10:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 22:38:55
 * @Description:
 * @TODO::
 * @Reference:
-->
```python
import tensorflow as tf
# 此处代码需要使用 tf 2 版本运行 # 1.创建输入张量，并赋初始值 a = tf.constant(2.) b = tf.constant(4.)
# 2.直接计算，并打印结果
print('a+b=',a+b)
```

这种运算时同时创建计算图𝑐 = 𝑎 + 𝑏和数值结果6.0 = 2.0 + 4.0的方式叫做命令式编 程，也称为动态图模式。TensorFlow 2 和 PyTorch 都是采用动态图(优先)模式开发，调试方 便，所见即所得。一般来说，动态图模式开发效率高，但是运行效率可能不如静态图模 式。TensorFlow 2 也支持通过 tf.function 将动态图优先模式的代码转化为静态图模式，实现 开发和运行效率的双赢

```python
# 创建在 CPU 环境上运算的 2 个矩阵
with tf.device('/cpu:0'):
    cpu_a = tf.random.normal([1, n])
    cpu_b = tf.random.normal([n, 1])
    print(cpu_a.device, cpu_b.device)
# 创建使用 GPU 环境运算的 2 个矩阵
with tf.device('/gpu:0'):
    gpu_a = tf.random.normal([1, n])
    gpu_b = tf.random.normal([n, 1])
    print(gpu_a.device, gpu_b.device)
```

TensorFlow 在运行时，默认会占用所有 GPU 显存资源，这是非常不友好的行为，尤其 是当计算机同时有多个用户或者程序在使用 GPU 资源时，占用所有 GPU 显存资源会使得 其他程序无法运行。因此，一般推荐设置 TensorFlow 的显存占用方式为增长式占用模式， 即根据实际模型大小申请显存资源，代码实现如下：

```python
# 设置 GPU 显存使用方式
# 获取 GPU 设备列表
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
    # 设置 GPU 为增长式占用
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)    except RuntimeError as e:
    # 打印异常
    print(e)
```


```python
with tf.GradientTape() as tape: # 构建梯度记录环境
    # 打平操作，[b, 28, 28] => [b, 784]
    x = tf.reshape(x, (-1, 28*28))
    # Step1. 得到模型输出
    output [b, 784] => [b, 10]
    out = model(x)
    # [b] => [b, 10]
    y_onehot = tf.one_hot(y, depth=10)
    # 计算差的平方和，[b, 10]
    loss = tf.square(out-y_onehot)
    # 计算每个样本的平均误差，[b]
    loss = tf.reduce_sum(loss) / x.shape[0]
再利用 TensorFlow 提供的自动求导函数 tape.gradient(loss, model.trainable_variables)求出模 型中所有参数的梯度信息𝜕ℒ 𝜕𝜃 ,𝜃 ∈ {𝑾1,𝒃1,𝑾2,𝒃2,𝑾3,𝒃3}。
    # Step3. 计算参数的梯度 w1, w2, w3, b1, b2, b3
    grads = tape.gradient(loss, model.trainable_variables)
```

计算获得的梯度结果使用 grads 列表变量保存。再使用 optimizers 对象自动按照梯度更新法 则去更新模型的参数𝜃。
𝜃′ = 𝜃 −𝜂 ∙𝜕ℒ /𝜕𝜃

实现如下。

```py
# 自动计算梯度
grads = tape.gradient(loss, model.trainable_variables)
# w' = w - lr * grad，更新网络参数
optimizer.apply_gradients(zip(grads, model.trainable_variables))
```

[1]: https://github.com/dragen1860/Deep-Learning-with-TensorFlow-book/blob/master/%E3%80%90%E3%80%8ATensorFlow%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E3%80%8B%E3%80%91.pdf
[2]: https://medium.com/coinmonks/8-things-to-do-differently-in-tensorflows-eager-execution-mode-47cf429aa3ad
