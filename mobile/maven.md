

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 17:25:03
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 18:13:17
 * @Description:
 * @TODO::
 * @Reference:
-->
https://maven.apache.org/guides/introduction/introduction-to-the-pom.html

## Project Object Model or POM

项目对象模型或POM是Maven中的基本工作单元。 这是一个XML文件，其中包含有关项目的信息以及Maven用于构建项目的配置详细信息。 它包含大多数项目的默认值。 例子是构建目录，它是目标。 源目录是src / main / java； 测试源目录为src / test / java； 等等。 当执行任务或目标时，Maven在当前目录中查找POM。 它读取POM，获取所需的配置信息，然后执行目标。

可以在POM中指定的一些配置是项目依赖项，可以执行的插件或目标，构建配置文件等等。 也可以指定其他信息，例如项目版本，描述，开发人员，邮件列表等。

---
https://learning.oreilly.com/library/view/practical-java-programming/9781119560012/b02.xhtml

Apache Maven教程

在开发Java软件项目时，需要处理许多任务:下载依赖项、将JAR文件放在类路径中、将源代码编译成二进制字节码、运行测试、将字节码打包到可部署的JAR文件中、将JAR文件部署到远程存储库服务器，等等。Apache Maven是一种基于项目对象模型(POM)概念的软件项目管理和理解工具，它可以自动化所有这些任务。Maven主要用作管理基于java的项目的工具，但它也可以用于使用其他编程语言(如c#和Ruby)的项目。作为Maven的替代品，Ant和Gradle也是流行的软件项目管理工具。


有关Ant的更多信息，请参见http://ant.apache.org/。

有关Gradle的更多信息，请参见https://gradle.org/guides/#getting-started。

有关Ant、Maven和Gradle之间的比较，请参见https://www.baeldung.com/antmaven-gradle。


---

xml文件，如下所示，是Maven项目的核心，它描述项目细节，管理依赖关系，并配置用于构建软件的插件。请确保插入了如清单所示的<Properties>部分。

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
 <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>my-app</name>
  <url>http://maven.apache.org</url>
  <properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>

---


Downloading Maven
You can download Apache Maven as a zipped file, apache-maven-3.6.0-bin.zip, from the following address:

https://maven.apache.org/download.cgi

After downloading it, just unzip the file to a directory, for example, c:\apache-maven-3.6.0\. Once it is unzipped, you will find the Maven program, mvn.jar, in the bin subdirectory. To test your Maven, just run the following command:

mvn --version
But you need to add c:\apache-maven-3.6.0\bin\ to your system PATH first, or simply run the Maven program with its full path. Either way, the result should show the version of Maven, the version of Java, and the information about your operating system, as shown in Figure B.1.

---

图B.4:编译和构建Maven项目的命令(顶部)和显示项目已经成功构建的消息(底部)

运行Maven项目

输入以下命令来运行项目，它将显示“Hello world!”如图B.5所示。

java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App

有关Maven的更多信息，请参阅以下参考资料:

https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

https://www.javatpoint.com/maven-tutorial

http://tutorials.jenkov.com/maven/maven-tutorial.html

https://www.guru99.com/maven-tutorial.html

https://examples.javacodegeeks.com/enterprise-java/maven/create-java-project-with-maven-example/



