

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-27 18:32:44
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-27 18:37:56
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/94206978
-->



在渐进式训练的PGAN中，作者认为他们的问题不再是internal covariate shift,而采用了一种没有参数的归一化方式Pixelwise Normalization；另外还提到了一种叫Equalized Learning Rate 的参数约束方法，这样可以更好地稳定训练过程，具体可以参考原论文。
