

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 17:48:47
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 17:48:58
 * @Description:
 * @TODO::
 * @Reference:https://kangcai.github.io/2018/10/30/ml-overall-2/
-->

在图1中，按时间轴顺序事件详情如下:

1943年【NN基础理论】，McCulloch和Pitts提出了神经网络层次结构模型，确立了神经网络的计算模型理论，从而为机器学习的发展奠定了基础

1950年【重要事件】，Turing提出了著名的“图灵测试”，使人工智能成为了科学领域的一个重要研究课题

1957年【NN第一次崛起】，Rosenblatt提出了Perceptron（感知器）概念，用Rosenblatt算法对Perceptron进行训练。并且首次用算法精确定义了自组织自学习的神经网络数学模型，设计出了第一个计算机神经网络（NN算法），开启了NN研究活动的第一次兴起

1958年【正式LR】，Cox给Logistic Regression方法正式命名，用于解决美国人口普查任务

1959年【重要事件】，Samuel设计了一个具有学习能力的跳棋程序，曾经战胜了美国保持8年不败的冠军。这个程序向人们初步展示了机器学习的能力，Samuel将机器学习定义为无需明确编程即可为计算机提供能力的研究领域

1960年【NN发展】，Widrow用delta学习法则来对Perceptron进行训练，可以比Rosenblatt算法更有效地训练出良好的线性分类器（最小二乘法问题）

1962年【雏形CNN】，Hubel和Wiesel发现了猫脑皮层中独特的神经网络结构可以有效降低学习的复杂性，从而提出著名的Hubel-Wiese生物视觉模型，该模型卷积神经网络（CNN）的雏形，这之后提出的神经网络模型也均受此启迪

1963年【雏形SVM】，Vapnik和Chervonenkis发明原始支持向量方法，即起决定性作用的样本为支持向量（SVM算法）

1969年【NN第一次停滞】，Minsky和Papert出版了对机器学习研究有深远影响的著作《Perceptron》，其中对于机器学习基本思想的论断：解决问题的算法能力和计算复杂性，影响深远且延续至今。文章中提出了著名的线性感知机无法解决异或问题，打击了NN社区，从那以后NN研究活动直到1980s都萎靡。

1971年【重要事件】，Vapnik和Chervonenkis提出VC维概念，描述了假设空间和模型复杂度，衡量了经验误差和泛化误差的逼近程度，它给诸多机器学习方法的可学习性提供了坚实的理论基础

1980年【重要事件】，在美国卡内基梅隆大学举行了第一届机器学习国际研讨会，标志着机器学习研究在世界范围内兴起，该研讨会也是著名会议ICML的前身

1981年【NN第二次崛起】，Werbos提出多层感知机，解决了线性模型无法解决的异或问题，第二次兴起了NN研究

1984年【重要事件】，Leslie Valiant提出概率近似正确学习（Probably approximately correct learning，PAC learning），是机器学习的数学分析的框架，它将计算复杂度理论引入机器学习，描述了机器学习的有限假设空间的可学习性，无限空间的VC维相关的可学习性等问题。

1984年【决策树】，Breiman发表分类回归树（CART算法，一种决策树）

1986年【决策树】，Quinlan提出ID3算法（一种决策树）

1986年【NN的BP算法】，Rumelhart，Hinton和Williams联合在《Nature》杂志发表了著名的反向传播算法（BP算法）

1989年【正式CNN】，Yann和LeCun提出了目前最为流行的卷积神经网络（CNN）计算模型，推导出基于BP算法的高效训练方法，并成功地应用于英文手写体识别

1995年【正式SVM】，Vapnik和Cortes发表软间隔支持向量机（SVM算法），开启了随后的机器学习领域NN和SVM两大社区的竞争

1995年【NN第二次停滞】，自1995年到随后的10年，NN研究发展缓慢，SVM在大多数任务的表现上一直压制着NN，并且Hochreiter的工作证明了NN的一个严重缺陷-梯度爆炸和梯度消失问题

1997年【Adaboost】，Freund和Schapire提出了另一种可靠的机器学习方法-Adaboost，

2001年【随机森林】，Breiman发表随机森林方法（Random forest），Adaboost在对过拟合问题和奇异数据容忍上存在缺陷，而随机森林在这两个问题上更加鲁棒。

2005年【NN第三次崛起】，经过多年的发展，NN众多研究发现被现代NN大牛Hinton, LeCun, Bengio, Andrew Ng和其它老一辈研究者整合，NN随后开始被称为深度学习（Deep Learning），迎来了第三次崛起。
