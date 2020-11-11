

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 01:05:44
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-12 01:08:26
 * @Description:
 * @TODO::
 * @Reference:TorchScript使用的注意事项和常见错误 - 带萝卜的文章 - 知乎
https://zhuanlan.zhihu.com/p/96397421
-->

## 注意事项

1. 如果代码中有`if`条件控制，尽量避免使用`torch.jit.trace`来转换代码，因为它不能处理变化条件，如果非要用`trace`的话，可以把`if`条件控制改成别的形式，比如：

def f(x):
  if x > 0:
    return False
  else:
    return True
可以改成:

def f(x):
  return x <= 0
2. jit不能转换第三方Python库中的函数，尽量所有代码都使用pytorch实现，如果速度不理想的话，可以参考PyTorch官网的用C++自定义TorchScript算子的教程，用C++实现需要的功能，然后注册成jit操作，最后转成torchscript；

3. 如果要转Mobilenet，最好使用pytorch1.3以上，否则识别不出来其中的depth wise conv，转换出来的torchscript模型会比原模型大很多；

4. 模型的forward函数中尽量不要包含中文注释；

5. 函数的默认参数如果不是tensor的话，需要指定类型；

6. list中元素默认为tensor，如果不是，也要指定类型；

7. tensor.bool()操作不支持，可以直接用tensor>0来替代；

8. 不支持with语句；

9. 不支持花式赋值，比如下面这种：

[[pt1[0]], [pt1[1]]] = t
10. 如果在model的forward函数中调用了另一个model0，需要先在model的构造函数中将model0设为model的子模型；

11. 在TorchScript中，有一种Optional类型，举例：在一个函数中，如果可以通过if控制来返回None或者tensor，那么这个返回值会被认定为Optional[Tensor]，这会导致无法对该返回值使用tensor的内置方法或属性，比如tensor.shape,tensor.size()等；

12. TorchScript中对tensor类型的要求严格得多，比如torch.tensor(1.0)这个变量会被默认为doubletensor，可能会在计算中出现错误；

13. TorchScript中带有梯度的零维张量无法当做标量进行计算，这个问题可能会在使用C++自定义TorchScript算子时遇到。

## 常见错误

ValueError: substring not found
forward函数中不允许出现中文注释

Module is not iterable(大概是这样的错误)
不支持模型遍历及对模型取下标的操作

torch.jit.frontend.UnsupportedNodeError: Dict aren’t supported
forward 函数里初始化字典，由 a={} 改成 a=dict()，不过dict类型尽量不要在forward中使用，容易出错

    torch.jit.frontend.UnsupportedNodeError: continue statements aren’t supported

不支持continue

```
torch.jit.frontend.UnsupportedNodeError: try blocks aren’t supported
```

不支持try-except

```
Unknown builtin op: aten::Tensor
```

不能使用torch.Tensor()，如果是把python中的int，float等类型转成tensor可以使用torch.tensor()
