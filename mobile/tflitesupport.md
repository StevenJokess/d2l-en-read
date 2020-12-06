

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 19:38:16
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 19:39:54
 * @Description:
 * @TODO::
 * @Reference:https://github.com/tensorflow/tflite-support
-->

TensorFlow Lite的支持

TFLite支持是一个工具包，帮助用户开发ML并将TFLite模型部署到移动设备上。它可以跨平台工作，支持Java、c++ (WIP)和Swift (WIP)。TFLite支持项目由以下主要组成部分组成:

TFLite支持库:一个跨平台库，帮助将TFLite模型部署到移动设备上。

TFLite模型元数据:(元数据填充器和元数据提取器库):包括关于模型做什么以及如何使用模型的人类可读信息和机器可读信息。

TFLite支持Codegen工具:基于支持库和元数据自动生成模型包装器的可执行文件。

TFLite支持任务库:一个灵活的、随时可用的库，用于常见的机器学习模型类型，如分类和检测，客户端也可以在任务库infra上构建自己的native/Android/iOS推理API。

TFLite支持库提供不同层次的部署需求，从简单的加载到完全可定制。TFLite支持的目标主要有三个用例:

为用户提供随时可用的api来与模型交互。

这是通过TFLite支持Codegen工具实现的，在这个工具中，用户可以通过简单地将模型传递给Codegen工具来获得模型接口(包含随时可用的api)。设计了基于TFLite元数据的自动码元策略。

为流行的ML任务提供优化的模型界面。

与codegen版本相比，TFLite支持任务库提供的模型接口在可用性和性能方面都进行了特别优化。用户还可以用每个任务中的默认模型交换他们自己的自定义模型。

提供定制模型接口和构建推理管道的灵活性。

TFLite支持Util库包含各种Util方法和数据结构，以执行前/后处理和数据转换。它还被设计为匹配TensorFlow模块的行为，比如TF。形象和TF。文本，确保从训练到推理的一致性。

请参阅tensorflow.org上的文档以获得更多指令和示例。

构建指令

我们使用Bazel来建造这个项目。当你构建Java (Android) Utils时，你需要正确设置以下env变量:

ANDROID_NDK_HOME

ANDROID_SDK_HOME

ANDROID_NDK_API_LEVEL

ANDROID_SDK_API_LEVEL

ANDROID_BUILD_TOOLS_VERSION

联系我们

通过创建一个新的Github问题，让我们知道您对TFLite支持的看法，或者发送电子邮件到TFLite - Support -team@google.com。
