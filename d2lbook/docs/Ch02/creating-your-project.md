

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-27 19:04:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-29 19:12:52
 * @Description:
 * @TODO::
 * @Reference:https://book.d2l.ai/user/create.html
 * https://github.com/d2l-ai/d2l-book/edit/master/docs/user/create.md
-->

# 创建您的项目
:label:`sec_create`

让我们从头开始一个简单的项目。

## 从头​​开始的项目

首先为我们的项目创建一个文件夹。

```{.python .input  n=1}
!mkdir -p mybook
```

然后创建两个页面。`index.md` 是包含目录(TOC)的索引页，其中包含另一个页面`get_started.md`。注意，TOC是在带有TOC标记的代码块中定义的。如果您熟悉Sphinx，您会发现它类似于Sphinx中的TOC定义。有关d2lbook添加到markdown的更多扩展，请参阅2.5节。还请注意，我们使用内置的magic `writefile`将代码块保存到[Jupyter](https://ipython.readthedocs.io/en/stable/interactive/magics.html)提供的文件中。


```{.python .input  n=2}
%%writefile mybook/index.md
# My Book

The starting page of my book with `d2lbook`.
````toc
get_started
````
```


```{.python .input  n=3}
%%writefile mybook/get_started.md
# Getting Started

Please first install my favorite package `numpy`.
```

现在，我们来构建HTML版本。

```{.python .input  n=4}
!cd mybook && d2lbook build html
```

这样，HTML索引页可在`mybook/_build/html/index.html`中获得。


## 配置

您可以定制如何通过根文件夹上的`config.ini`构建和发布结果。

```{.python .input  n=5}
%%writefile mybook/config.ini

[project]
# Specify the PDF filename to mybook.pdf
name = mybook
# Specify the authors names in PDF
author = Adam Smith, Alex Li

[html]
# Add two links on the navbar. A link consists of three
# items: name, URL, and a fontawesome icon. Items are separated by commas.
header_links = PDF, https://book.d2l.ai/d2l-book.pdf, fas fa-file-pdf,
               Github, https://github.com/d2l-ai/d2l-book, fab fa-github
```


让我们清理并重新构建。

```{.python .input}
!cd mybook && rm -rf _build && d2lbook build html
```

您可以定制如何通过根文件夹上的config.ini构建和发布结果。

如果再次打开`index.html`，您将在导航栏上看到两个链接。

让我们构建PDF输出，您会在输出日志中找到`Output written on mybook.pdf (7 pages).`上的输出。

```{.python .input}
!cd mybook && d2lbook build pdf
```

在以下各节中，我们将介绍更多配置选项。 您可以检查[default_config.ini](https://github.com/d2l-ai/d2l-book/blob/master/d2lbook/config_default.ini)中的所有配置选项及其默认值。 还要检查以下示例中的`config.ini`

- [This website](https://github.com/d2l-ai/d2l-book/blob/master/docs/config.ini)
- [Dive into Deep Learning](https://github.com/d2l-ai/d2l-en/blob/master/config.ini)

最后，让我们清除工作区。

```{.python .input}
！rm -rf mybook
```
