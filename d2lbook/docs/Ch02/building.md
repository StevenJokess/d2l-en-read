

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-29 19:20:36
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-29 19:36:51
 * @Description:
 * @TODO::
 * @Reference:https://book.d2l.ai/user/build.html
 * https://github.com/d2l-ai/d2l-book/edit/master/docs/user/build.md
-->

＃ 构建

本节我们将解释构建项目的各种选项。此选项可以分为四类：

1. 健全性检查
    -`d2lbook build linkcheck`将检查是否可以访问所有内部和外部链接。
    -`d2lbook build outputcheck`将检查是否没有笔记本包含代码输出
1. 构建结果
    -`d2lbook build html`：将HTML版本构建到`_build / html`中
    -`d2lbook build pdf`：将PDF版本构建到`_build / pdf`中
    -`d2lbook build pkg`：构建一个包含所有`.ipynb`笔记本的zip文件
1. 附加特征
    - `d2lbook build colab`：将可以在Google Colab上运行的所有笔记本转换为`_build / colab`。 在numref：`sec_colab中查看更多
    - `d2lbook build lib`：构建一个Python包，以便我们可以在其他笔记本中重用代码。 在XXX中查看更多内容。
1.  内部阶段，通常是自动触发的。
    - `d2lbook build eval`:计算所有笔记本并保存为'。ipynb将笔记本转换为_build/eval
    - `d2lbook build rst`:将所有笔记本转换为' rst '文件，并在' _build/rst '中创建一个Sphinx项目

## 构建缓存

我们建议您评估笔记本以获得代码单元结果，而不是将这些结果保留在源文件中，原因有两个：
1.这些结果使代码检查变得困难，特别是当它们由于数值精度或随机数生成器而具有随机性时。
1.一段时间未评估的笔记本可能会由于软件包升级而损坏。

但是评估会在构建过程中增加额外的开销。 我们建议在几分钟之内限制每个笔记本的运行时间。 d2lbook将重用以前构建的笔记本，并且仅评估修改后的笔记本。

例如，由于训练神经网络，在[Deep into Deep Learning]（https://d2l.ai）中，笔记本电脑（部分）的平均运行时间在GPU机器上约为2分钟。 它包含100多个笔记本，因此总运行时间为2-3小时。 实际上，每次代码更改只会修改几个笔记本，因此[构建时间]（http://ci.d2l.ai/blue/organizations/jenkins/d21-en/activity）通常少于10分钟。

让我们看看它是如何工作的。 首先像在`sec_create`中创建一个项目一样。

```{.python .input}
!mkdir -p cache
```

```{.python .input}
%%writefile cache/index.md
# My Book

The starting page of my book with `d2lbook`.

````toc
get_started
````
```

```{.python .input}
%%writefile cache/get_started.md
# Getting Started

Please first install my favorite package `numpy`.
```

```{.python .input}
!cd cache; d2lbook build html
```

您可以看到`index.md`已评估。 （尽管它不包含代码，但可以将其评估为Jupyter笔记本。）

如果再次构建，我们将不会评估任何笔记本。

```{.python .input}
!cd cache; d2lbook build html
```

现在让我们修改`get_started.md`，您将看到它会被重新评估，但不会被`index.md`评估。

```{.python .input}
%%writefile cache/get_started.md
# Getting Started

Please first install my favorite package `numpy>=1.18`.
```

触发整个构建的一种方法是删除`_build/eval`中保存的笔记本，或简单地删除`_build`。 另一种方法是指定一些依赖项。 例如，在下面的单元格中，我们将`config.ini`添加到依赖项中。 每次修改`config.ini`时，它将使所有笔记本的缓存无效，并从头开始构建。

```{.python .input}
%%writefile cache/config.ini

[build]
dependencies = config.ini
```

```{.python .input}
!cd cache; d2lbook build html
```

最后，让我们清理一下我们的工作空间。

```{.python .input}
!rm -rf cache
```
