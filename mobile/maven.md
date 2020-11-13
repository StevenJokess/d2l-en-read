

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 17:25:03
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 17:26:20
 * @Description:
 * @TODO::
 * @Reference:
-->
https://maven.apache.org/guides/introduction/introduction-to-the-pom.html

## Project Object Model or POM

项目对象模型或POM是Maven中的基本工作单元。 这是一个XML文件，其中包含有关项目的信息以及Maven用于构建项目的配置详细信息。 它包含大多数项目的默认值。 例子是构建目录，它是目标。 源目录是src / main / java； 测试源目录为src / test / java； 等等。 当执行任务或目标时，Maven在当前目录中查找POM。 它读取POM，获取所需的配置信息，然后执行目标。

可以在POM中指定的一些配置是项目依赖项，可以执行的插件或目标，构建配置文件等等。 也可以指定其他信息，例如项目版本，描述，开发人员，邮件列表等。
