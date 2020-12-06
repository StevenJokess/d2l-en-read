

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 18:18:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 18:23:48
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/practical-java-programming/9781119560012/b01.xhtmls
-->


JAR教程

Java Archive (JAR)格式允许您将多个文件压缩并捆绑到一个JAR文件中。JAR是一种独立于平台的文件格式，基于流行的ZIP算法。它模仿Unix TAR(磁带存档)文件格式。jar和tar工具具有相同的命令行选项。Java运行时(JRE)可以直接从JAR文件运行Java程序，而不需要解压缩文件。JAR文件也可以通过WinZIP或WinRAR程序直接打开。

在项目中使用JAR文件有几个好处。

压缩:通过压缩文件，您将实现一个较小的项目大小。

易于部署:单个JAR文件更容易部署和分发。

身份验证:通过对JAR文件进行数字签名，您可以通过数字签名和数字证书为用户提供身份验证。

您可以使用jar工具从多个Java文件或多个目录创建jar文件。例如，下面的命令从两个Java类HelloWorld.class和HelloWorld2.class创建一个名为hello.jar文件:

jar cvf hello.jar HelloWorld.class HelloWorld2.class

选项如下(注意JAR文档中显示的破折号前缀是可选的):

创建一个新的存档

v指示系统在标准输出上生成详细输出

-f指定存档文件名，在本例中为hello.jar

要了解关于JAR选项的更多信息，只需在命令行中单独键入JAR。

jar

下面的命令从所有的Java类(*.class)中创建一个名为hello.jar的文件:

jar cvf hello.jar *.class

下面的命令从所有的Java类(*.class)和子目录图像中创建一个名为hello.jar文件:

jar cvf hello.jar *.class images

下面的命令从ProjectA子目录中的所有Java类(*.class)中创建一个名为hello.jar的文件:

jar cvf hello.jar ProjectA/*.class

下面的命令从三个子目录DIR1、DIR2和DIR3中创建一个名为hello.jar文件。与前面只添加类文件的示例不同，这个示例将所有文件添加到JAR文件中:

jar cvf hello.jar DIR1 DIR2 DIR3

JAR工具最重要的用途之一是创建可执行的JAR文件。这样，只需双击可执行JAR文件，就可以运行Java程序。

要创建可执行JAR文件，首先需要创建一个清单文件，该文件指定要运行的主Java类。例如，下面的清单文件指定主Java类为HelloWorld.class，类路径为hello.jar:

Main-Class: HelloWorld
Class-Path: hello.jar

将此内容保存到一个名为hello.mf的文本文件中。下面的命令将manifest文件和所有的Java (*.class)文件组合在一起，创建一个名为hello.jar的可执行JAR文件:

jar cmf hello.mf hello.jar *.class

其中-m选项指示JAR包含来自指定清单文件的清单信息。

要运行这个JAR文件，只需在文件资源管理器中双击它，或者在Windows终端中键入以下命令:

java jar hello.jar

---

Useful Java Resources
The following is a list of useful resources for Java, including documentation and download web sites, as well as sites recommending online Java books:

The Java official web site:
https://www.java.com/

https://www.oracle.com/java/

The Java SE JDK download web site:
https://www.oracle.com/technetwork/java/javase/downloads/index.html

The Java SE Documentation web site:
https://www.oracle.com/technetwork/java/javase/documentation/api-jsp-136079.html

The Java JDK version 10 API web site:
https://docs.oracle.com/javase/10/docs/api/overview-summary.html

The Javadoc web site:
https://www.oracle.com/technetwork/java/javase/tech/index-137868.html

https://www.tutorialspoint.com/java/java_documentation.htm

The command-line jar tool: jar.exe:
http://docs.oracle.com/javase/7/docs/technotes/tools/windows/jar.html

Java books:
https://whatpixel.com/best-java-books/

https://dzone.com/articles/10-all-time-great-books-for-java-programrs-best

https://www.journaldev.com/6162/5-best-core-java-books-for-beginners

https://www.javacodegeeks.com/2011/10/top-10-java-books-you-dont-want-to-miss.html
