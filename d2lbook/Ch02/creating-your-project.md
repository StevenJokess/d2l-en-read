

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-27 19:04:25
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-27 19:10:46
 * @Description:
 * @TODO::
 * @Reference:https://book.d2l.ai/user/create.html
-->

# 创建您的项目

让我们从头开始一个简单的项目。





如果您再次打开index.html，您将在导航栏上看到两个链接。

让建立PDF输出，你会发现输出写在mybook.pdf(7页)。在输出日志中。

```python
!cd mybook && d2lbook build pdf
```



## 配置

您可以定制如何通过根文件夹上的`config.ini`构建和发布结果。

```ini
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

!cd mybook && rm -rf _build && d2lbook build html

配置

您可以定制如何通过根文件夹上的config.ini构建和发布结果。




在以下各节中，我们将介绍更多配置选项。 您可以检查[default_config.ini](https://github.com/d2l-ai/d2l-book/blob/master/d2lbook/config_default.ini)中的所有配置选项及其默认值。 还要检查以下示例中的`config.ini`

This website

Dive into Deep Learning

最后，让我们清除工作区。

```python
！rm -rf mybook
```
