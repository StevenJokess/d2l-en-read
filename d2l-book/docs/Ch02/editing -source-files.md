

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-29 19:13:51
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-29 19:19:15
 * @Description:
 * @TODO::
 * @Reference:https://book.d2l.ai/user/edit.html
 * https://github.com/d2l-ai/d2l-book/edit/master/docs/user/edit.md
-->

# 编辑源文件

无论是纯文本文件还是Jupyter笔记本，我们都建议您将其另存为markdown文件。 如果是笔记本，则可以在保存之前清除输出，以简化代码审查和版本控制。

您可以使用自己喜欢的降价编辑器，例如 [Typora]（https://www.typora.io/），可直接编辑markdown文件。 我们增强了markdown功能以支持其他功能，例如图像/表格标题和参考，有关更多详细信息，请参考：numref：`sec_markdown`。 对于笔记本电脑，Jupyter源代码块被放置在带有`{.python .input}`标签的markdown代码块中，例如，

````
```{.python .input}
print('this is a Jupyter code cell')
```

我们推荐的另一种方法是使用Jupyter直接编辑markdown文件，特别是当它们包含源代码块时。Jupyter的默认文件格式是`ipynb`。我们可以使用`notedown`插件让Jupyter打开并保存markdown文件。

您可以通过以下方式安装此扩展程序

```bash
pip install mu-notedown
```

（`mu-notedown`是[notedown]（https://github.com/aaren/notedown）的分支，进行了一些修改。您可能需要先卸载原始的`notedown`。）


要在运行Jupyter Notebook时默认打开' notedown '插件，请执行以下操作:首先，生成一个Jupyter笔记本配置文件(如果已经生成，则可以跳过此步骤)。

````
```bash
jupyter notebook --generate-config
```


然后，将以下行添加到Jupyter Notebook配置文件的末尾（对于Linux / macOS，通常在路径`~/.jupyter/jupyter_notebook_config.py`中）：

```bash
c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'
```


接下来，重新启动Jupyter，您现在应该可以在Jupyter中将这些降价作为笔记本打开。

![Use Jupyter to edit :numref:`sec_create`](../img/jupyter.png)
:width:`500px`
