

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-07-07 13:10:33
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-07-07 13:13:07
 * @Description:
 * @TODO::
 * @Reference:http://preview.d2l.ai/d2l-en/PR-1111/chapter_appendix-tools-for-deep-learning/colab.html
-->

# 使用Google Colab

我们在第19.2节和第19.3节中介绍了如何在AWS上运行本书。这本书的另一种选择是在Google Colab上运行这本书，如果您拥有Google帐户，它将提供免费的GPU。

要在Colab上运行一个部分，只需单击该部分标题右侧的Colab按钮，如图19.4.1所示。

../_images/colab.png图19.4.1在Colab上打开一个区域

第一次执行代码单元时，您将收到一条警告消息，如图19.4.2所示。您可以单击“仍然运行”将其忽略。

../_images/colab-2.png图19.4.2在Colab上运行部分的警告消息

接下来，Colab将您连接到实例以运行此笔记本。具体来说，如果需要GPU，例如在调用d2l.try_gpu（）函数时，我们将请求Colab自动连接到GPU实例。

## 小结

* 您可以使用Google Colab使用GPU运行本书的每个部分。

## 练习

1. 尝试使用Google Colab编辑和运行本书中的代码。
