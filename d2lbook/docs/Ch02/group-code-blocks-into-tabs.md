

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-29 21:00:17
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-29 21:07:49
 * @Description:
 * @TODO::
 * @Reference:https://book.d2l.ai/user/code_tabs.html
 *
-->

# 将代码块分选项卡

下面是一个将代码块分组为三个选项卡的示例。

## 例子

让我们实现$a + b$。 我们首先显示说明，然后演示代码。

:begin_tab:`python`
您需要安装python

:end_tab:

:begin_tab:`numpy`
您需要安装numpy，用
```bash
pip install numpy
```
:end_tab:


```{.python .input}
a = [1,1,1]
b = [2,2,2]
[ia+ib for ia, ib in zip(a,b)]
```

```{.python .input}
#@tab numpy
import numpy as np
a = np.ones(3)
b = np.ones(3)*2
a + b
```

```{.python .input}
#@tab cpython
# Just a place holder
print(1+2)
```


接下来让我们实现$a - b$

```{.python .input}
a = [1,1,1]
b = [2,2,2]
[ia-ib for ia, ib in zip(a,b)]
```

```{.python .input}
#@tab numpy
a = np.ones(3)
b = np.ones(3)*2
a - b
```

## 用法

要启用多选项卡，首先在`config.ini`文件中配置选项卡条目。例如，这里我们使用`tabs = python, numpy, cpython`。`python`是默认选项卡。要指定不属于默认选项卡的代码块，请在代码块的第一行添加`#@tab`，后跟选项卡名称(大小写不敏感)。

有时这些代码块会相互冲突。我们可以一次激活一个选项卡，所以只有属于这个选项卡的代码块可以在Jupyter中评估。例如

```bash
d2lbook activate default user/code_tabs.md  # activate the default tab
d2lbook activate numpy user/code_tabs.md    # activate the numpy tab
d2lbook activate all user/code_tabs.md      # activate all tabs
```


