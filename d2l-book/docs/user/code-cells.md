

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-29 20:51:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-29 20:59:38
 * @Description:
 * @TODO::
 * @Reference:https://book.d2l.ai/user/code.html
 * https://github.com/d2l-ai/d2l-book/edit/master/docs/user/code.md
-->

# 代码块
:label:`sec_code`

## 最大线长

我们建议您将最大行长设置为78，以避免在PDF中自动换行。 您可以在[nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)中启用标尺扩展，以在编写代码时在Jupyter中添加可视垂直线。

```{.python .input}
'-' * 78
```

## 隐藏源和输出

我们可以通过在单元格中添加注释行`# hide code`来隐藏代码单元格的源代码。我们还可以使用`# hide outputs`隐藏代码单元格输出

例如，这里是正常的代码单元:

```{.python .input}
# Hide code
1+2+3
```

也尝试下隐藏输出

```{.python .input}
# Hide outputs
1+2+3
```

## 绘图

我们建议您使用svg格式绘制图形。 例如，以下代码配置`matplotlib`。

```{.python .input  n=3}
%matplotlib inline
from IPython import display
from matplotlib import pyplot as plt
import numpy as np

display.set_matplotlib_formats('svg')

x = np.arange(0, 10, 0.1)
plt.plot(x, np.sin(x));
```
