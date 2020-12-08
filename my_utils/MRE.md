

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 16:27:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 16:30:31
 * @Description:
 * @TODO::
 * @Reference:https://stackoverflow.com/help/minimal-reproducible-example
 * https://stackoverflow.com/questions/5963269/how-to-make-a-great-r-reproducible-example
 * https://github.com/CCS-Lab/easyml
 *
-->

How to create a Minimal, Reproducible Example
如何创建一个最小的，可重复的例子
When asking a question, people will be better able to provide help if you provide code that they can easily understand and use to reproduce the problem. This is referred to by community members as creating a minimal, reproducible example (reprex), a minimal, complete and verifiable example (mcve), or a minimal, workable example (mwe). Regardless of how it's communicated to you, it boils down to ensuring your code that reproduces the problem follows the following guidelines:

当提出问题时，如果你提供他们能够轻松理解并用于重现问题的代码，人们将能够更好地提供帮助。社区成员称之为创建一个最小的、可重复的示例(reprex)、一个最小的、完整的和可验证的示例(mcve) ，或者一个最小的、可操作的示例(mwe)。无论如何传达给你，它归结为确保你的代码复制问题遵循以下准则:

Your code examples should be…

您的代码示例应该是..。

…Minimal – Use as little code as possible that still produces the same problem 尽可能少地使用仍然产生同样问题的代码
…Complete – Provide all parts someone else needs to reproduce your problem 提供其他人需要的所有部分来重现你的问题in the question itself 这个问题本身
…Reproducible – Test the code you're about to provide to make sure it reproduces the problem ... 可重复性——测试您将要提供的代码，以确保它能够重复出现问题
The rest of this help article provides guidance on these aspects of writing a minimal, reproducible example.

本帮助文章的其余部分提供了关于编写最小的、可重复的示例的这些方面的指导。

Minimal
最小化
The more code there is to go through, the less likely people can find your problem. Streamline your example in one of two ways:

要检查的代码越多，人们就越不可能发现你的问题。用以下两种方法之一简化你的例子:

Restart from scratch. Create a new program, adding in only what is needed to see the problem. Use simple, descriptive names for functions and variables – don’t copy the names you’re using in your existing code. 从头开始。创建一个新程序，只添加查看问题所需的内容。对函数和变量使用简单的描述性名称——不要复制现有代码中使用的名称
Divide and conquer. If you’re not sure what the source of the problem is, start removing code a bit at a time until the problem disappears – then add the last part back. 分而治之。如果您不确定问题的根源是什么，那么开始每次删除一点代码，直到问题消失——然后再添加最后一部分
Minimal and readable
简洁易读
Don't sacrifice clarity for brevity when creating a minimal example. Use consistent naming and indentation, and include code comments if needed. Use your code editor’s shortcut for formatting code. Also, use spaces instead of tabs – tabs might not get correctly formatted on Stack Overflow.

在创建最小示例时，不要为了简洁而牺牲清晰性。使用一致的命名和缩进，并在需要时包括代码注释。使用代码编辑器的快捷方式来格式化代码。另外，使用空格代替制表符在 Stack Overflow 上可能无法正确格式化。

Complete
完成
Make sure all information necessary to reproduce the problem is included in the question itself:

确保问题本身包含所有重现问题所需的信息:

If the problem requires some server-side code as well as some XML-based configuration, include code for both. If a web page problem requires HTML, some JavaScript, and a stylesheet, include code for all three. The problem might not be in the code that you think it is in.

如果问题需要一些服务器端代码以及一些基于 xml 的配置，请包含这两者的代码。如果一个网页问题需要 HTML，一些 JavaScript 和一个样式表，包括这三个代码。问题可能不在您所认为的代码中。

Use individual code blocks for each file or snippet you include. Provide a description for the purpose of each block.

对包含的每个文件或代码段使用单独的代码块。为每个代码块提供说明。

Use Stack Snippets to include runnable HTML, JavaScript, or CSS.

使用堆栈代码段包含可运行的 HTML、 JavaScript 或 CSS。

DO NOT use images of code. Copy the actual text from your code editor, paste it into the question, then format it as code. This helps others more easily read and test your code.

不要使用代码的图像。从代码编辑器中复制实际的文本，粘贴到问题中，然后将其格式化为代码。这有助于其他人更容易地阅读和测试您的代码。

Reproducible
可复制的
To help you solve your problem, others will need to verify that it exists:

为了帮助你解决问题，其他人需要验证它的存在:

Describe the problem. "It doesn't work" isn't descriptive enough to help people understand your problem. Instead, tell other readers what the expected behavior should be. Tell other readers what the exact wording of the error message is, and which line of code is producing it. Use a brief but descriptive summary of your problem as the title of your question.

描述问题。“它不起作用”并不足以帮助人们理解你的问题。相反，告诉其他读者预期的行为应该是什么。告诉其他读者错误消息的确切措辞，以及生成错误消息的代码行。用一个简短但描述性的问题总结作为问题的标题。

Eliminate any issues that aren't relevant to the problem. If your question isn’t about a compiler error, ensure that there are no compile-time errors. Use a program such as JSLint to validate interpreted languages. Validate any HTML or XML.

排除任何与问题无关的问题。如果您的问题与编译器错误无关，请确保没有编译时错误。使用诸如 JSLint 这样的程序来验证解释语言。验证任何 HTML 或 XML。

Double-check that your example reproduces the problem! If you inadvertently fixed the problem while composing the example but didn't test it again, you'd want to know that before asking someone else to help.

再次检查您的示例是否重现了问题！如果您在编写示例时无意中修复了问题，但没有再次测试它，那么您应该在请求其他人帮助之前了解这一点。

It might help to shut the system down and restart it, or transport the example to a fresh environment to confirm it really does provide an example of the problem.

它可能有助于关闭系统并重新启动它，或者将示例传输到一个新的环境以确认它确实提供了一个问题示例。

For more information on how to debug your program so that you can create a minimal example, Eric Lippert has written a fantastic blog post on the subject: How to debug small programs.

为了获得更多关于如何调试程序的信息，以便创建一个最小的示例，Eric Lippert 写了一篇关于这个主题的精彩博文: 如何调试小程序。

The use of “reprex” for Reproducible Example was inspired by Jenny Bryan’s reprex package for R.

使用“ reprex”作为可再生示例的灵感来自于 Jenny Bryan 为 r。

You may have been told to include an MCVE – Minimal, Complete, and Verifiable examples is what they were referring to. MCVE was also the former name of the page you're reading now, occasionally misspelled as MVCE, before it was renamed to Minimal, Reproducible Example (sometimes called “reprex”, “min-reprex”, “repro” or just “example”).

你可能已经被告知包括一个 MCVE-最小的，完整的，可验证的例子是他们所指的。MCVE 也是你现在正在阅读的页面的前名，偶尔拼错为 MVCE，在它被重命名为 Minimal，Reproducible Example (有时称为“ reprex” ，“ min-reprex” ，“ repro”或者只是“ Example”)之前。




