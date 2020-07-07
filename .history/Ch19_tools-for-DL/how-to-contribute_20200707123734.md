

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-07-07 11:34:00
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-07-07 12:37:34
 * @Description:
 * @TODO::
 * @Reference:https://zh.d2l.ai/chapter_appendix/how-to-contribute.html
 * http://preview.d2l.ai/d2l-en/PR-1111/chapter_appendix-tools-for-deep-learning/contributing.html
-->

# 如何为本书贡献

读者的贡献帮助我们改进这本书。如果你发现一个错别字，一个过时的链接，一些你认为我们错过了引用，代码看起来不优雅或解释不清楚的地方，请反馈并帮助我们帮助我们的读者。在普通的书中，印刷之间的延迟(也就是纠正错误之间的延迟)可以用几年来衡量，但在这本书中，通常需要数小时到数天来进行改进。由于版本控制和持续集成测试，这一切都是可能的。为此，您需要向GitHub存储库提交一个pull请求。当您的pull请求被作者合并到代码库中时，您将成为贡献者。

我们在“致谢”部分感谢了本书的所有贡献者，并列出他们的GitHub ID或姓名。每位贡献者也将在本书出版时获得一本贡献者专享的赠书。

## 小的文本变化

最常见的贡献是编辑一个句子或纠正打字错误。我们建议您在github repo中找到源文件并直接编辑该文件。例如，您可以通过Find file按钮(图19.6.1)搜索文件，以找到源文件，它是一个标记文件。然后单击右上角的“Edit this file”按钮，在markdown文件中进行更改。

完成之后，在页面底部的建议文件更改面板中填写更改描述，然后单击建议文件更改按钮。它会将你重定向到一个新的页面来检查你的修改(图19.6.7)。如果一切顺利，您可以通过单击“Create pull request”按钮提交pull请求。

## 提出重大改变

如果您打算更新大部分文本或代码，则需要更多地了解本书使用的格式。 源文件基于markdown格式，并通过d2lbook`包<http://book.d2l.ai/user/markdown.html>`__进行了一系列扩展，例如引用等式，图像，章节， 和引用。 您可以使用任何Markdown编辑器打开这些文件并进行更改。

如果您想更改代码，我们建议您使用Jupyter来打开19.1节中所描述的这些Markdown文件。以便您可以运行和测试您的更改。请记得在提交更改前清除所有输出，我们的CI系统将执行您更新的部分以生成输出。

有些部分可能支持多个框架实现，您可以使用d2lbook来激活一个特定的框架，这样其他框架实现就变成了Markdown代码块，并且当您在Jupyter中运行时将不会执行。换句话说，首先通过运行安装d2lbook

pip install git+https://github.com/d2l-ai/d2l-book

然后，在dl -en的根目录中，可以通过运行以下命令之一来激活一个特定的实现

d2lbook activate mxnet chapter_multilayer-perceptrons/mlp-scratch.md
d2lbook activate pytorch chapter_multilayer-perceptrons/mlp-scratch.md

如果为默认实现MXNet添加新的代码块，请使用#@tab在开始一行标记该代码块。对于exmaple， #@tab pytorch用于pytorch代码块，或者#@tab用于所有实现的共享代码块。您可以参考d2lbook获取更多信息。

在提交你的改变，请通过下列命令来清除和激活所有代码块输出

d2lbook activate all chapter_multilayer-perceptrons/mlp-scratch.md

你可以在本书的GitHub代码库查看贡献者列表 [1]。如果你希望成为本书的贡献者之一，需要安装Git并为本书的GitHub代码库提交pull request [2]。当你的pull request被本书作者合并进了代码库后，你就成为了本书的贡献者。

本附录介绍为本书贡献的基本Git操作步骤。

下列操作步骤假设贡献者的GitHub ID为“astonzhang”。

第一步，安装Git。Git的开源书里详细介绍了安装Git的方法 [3]。如果你没有GitHub账号，需要注册一个账号 [4]。

第二步，登录GitHub。在浏览器输入本书的代码库地址 [2]。点击图11.20右上方红框中的“Fork”按钮获得一份本书的代码库。

这时，本书的代码库会复制到你的用户名下，例如图11.21左上方显示的“你的GitHub用户名/d2l-zh”。

图 11.21 复制代码库

第三步，点击图11.21右方的“Clone or download”绿色按钮，并点击红框中的按钮复制位于你的用户名下的代码库地址。按“获取和运行本书的代码”一节中介绍的方法进入命令行模式。假设我们希望将代码库保存在本地的~/repo路径之下。进入该路径，键入git clone并粘贴位于你的用户名下的代码库地址。执行以下命令：

# 将your_GitHub_ID替换成你的GitHub用户名
git clone https://github.com/your_GitHub_ID/d2l-zh.git
这时，本地的~/repo/d2l-zh路径下将包含本书的代码库中的所有文件。

第四步，编辑本地路径下的本书的代码库。假设我们修改了~/repo/d2l-zh/chapter_deep-learning-basics/linear-regression.md文件中的一个错别字。在命令行模式中进入路径~/repo/d2l-zh，执行命令

git status
此时Git将提示chapter_deep-learning-basics/linear-regression.md文件已被修改，如图11.22所示。

图 11.22 Git提示“chapter_deep-learning-basics/linear-regression.md”文件已被修改

确认将提交该修改的文件后，执行以下命令：

git add chapter_deep-learning-basics/linear-regression.md
git commit -m 'fix typo in linear-regression.md'
git push
其中的'fix typo in linear-regression.md'是描述提交改动的信息，也可以替换为其他有意义的描述信息。

第五步，再次在浏览器输入本书的代码库地址 [2]。点击图11.20左方红框中的“New pull request”按钮。在弹出的页面中，点击图11.23右方红框中的“compare across forks”链接，再点击下方红框中的“head fork: d2l-ai/d2l-zh”按钮。在弹出的文本框中输入你的GitHub用户名，在下拉菜单中选择“你的GitHub用户名/d2l-zh”，如图11.23所示。

第六步，如图11.24所示，在标题和正文的文本框中描述想要提交的pull request。点击红框中的“Create pull request”绿色按钮提交pull request。

提交完成后，我们会看到图11.25所示的页面中显示pull request已提交。


## pull请求

如图19.6.6所示，转到GitHub上存储库的fork，选择New pull request。这将打开一个屏幕，显示您的编辑与当前图书主存储库中的内容之间的更改。

## 提交pull请求

最后，点击按钮提交一个pull request，如图19.6.7所示。请确保描述您在pull请求中所做的更改。这将使作者更容易审查它，并与书合并。根据变更的不同，这可能会被立即接受，或者被拒绝，或者更有可能的是，您会得到一些关于变更的反馈。一旦你将它们合并，你就可以开始了。

图19.6.7创建Pull Request。您的pull请求将出现在主存储库中的请求列表中。我们将尽一切努力迅速处理它。

## 小结

* 你可以使用GitHub为这本书做贡献。
* 您可以直接在GitHub上编辑该文件以进行较小的修改。
* 对于一个重大的改变，请fork存储库，在本地编辑，只有当你准备好了才返回。
* pull请求是贡献被捆绑起来的方式（将远程尚未同步到本地的内容同步到本地）。尽量不要提交巨大的pull请求，因为这使他们很难理解和合并。最好寄几个小的。

## 练习

1. star和fork`dl-en`存储库。
1. 找到一些需要改进的代码并提交一个pull请求。
1. 找到一个我们错过的引用，并提交一个pull请求。


参考文献
[1] 本书的贡献者列表。https://github.com/d2l-ai/d2l-zh/graphs/contributors

[2] 本书的代码库地址。https://github.com/d2l-ai/d2l-zh

[3] 安装Git。https://git-scm.com/book/zh/v2

[4] GitHub网址。https://github.com/

