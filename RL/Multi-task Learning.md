

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-24 23:35:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 23:35:38
 * @Description:
 * @TODO::
 * @Reference:https://github.com/NLP-LOVE/ML-NLP/tree/master/Deep%20Learning/14.%20Reinforcement%20Learning
-->

什么是多任务学习
在机器学习中，我们通常关心优化某一特定指标，不管这个指标是一个标准值，还是企业KPI。为了达到这个目标，我们训练单一模型或多个模型集合来完成指定得任务。然后，我们通过精细调参，来改进模型直至性能不再提升。尽管这样做可以针对一个任务得到一个可接受得性能，但是我们可能忽略了一些信息，这些信息有助于在我们关心的指标上做得更好。具体来说，这些信息就是相关任务的监督数据。通过在相关任务间共享表示信息，我们的模型在原始任务上泛化性能更好。这种方法称为多任务学习（Multi-Task Learning）

在不同的任务中都会有一些共性，而这些共性就构成了多任务学习的一个连接点，也就是任务都需要通过这个共性能得出结果来的。比如电商场景中的点击率和转化率，都要依赖于同一份数据的输入和神经网络层次。多语种语音识别等。
