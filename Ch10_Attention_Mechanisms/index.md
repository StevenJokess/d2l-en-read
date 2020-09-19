

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-08-05 22:24:21
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-08-05 22:25:03
 * @Description:MT
 * @TODO::
 * @Reference:http://preview.d2l.ai/d2l-en/master/chapter_attention-mechanisms/index.html
-->

# 注意力机制

作为一个历史题外话，注意力研究在21认知神经科学是一个有着悠久历史的巨大领域。意识的聚焦和集中是注意的本质，它使人们能够优先处理感知，以便有效地与他人打交道。因此，我们不能处理感官输入中的所有信息。在任何时候，我们只知道环境中的一小部分信息。在认知神经科学中，有几种类型的注意，如选择性注意、隐性注意和空间注意。选择性注意的特征整合理论点燃了近年来深度学习的火花，该理论是由 Anne Treisman 和 Garry Gelade 在1980年的论文 [Treisman & Gelade, 1980]中提出的。本文认为，在感知刺激时，特征被提前、自动、并行地记录下来，而物体被单独识别，在加工的后期被识别。该理论已成为人类视觉注意最有影响的心理学模型之一。

然而，我们不会在神经科学中沉迷于过多的注意力理论，而是将注意力理念应用到深度学习中，在深度学习中，注意力可以被看作是一种广义的汇聚方法，在输入上有偏见对齐。在这一章中，我们将为你提供一些直觉，关于如何将注意力的观念转化为具体的数学模型，并使它们工作。
