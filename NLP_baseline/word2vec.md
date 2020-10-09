

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-08 21:12:15
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-08 22:04:08
 * @Description:
 * @TODO::
 * @Reference:[1]:
 * [2]: https://ai.deepshare.net/detail/v_5eb61989a4ee9_VbsAKp5S/3?from=p_5ee62f90022ee_zFpnlHXA&type=6
 * [3]: https://ai.deepshare.net/detail/v_5eb6199549958_3vI2Ua62/3?from=p_5ee62f90022ee_zFpnlHXA&type=6
-->

# 语言模型

通过概率计算，概率相乘

问题：
有词没出现过
短语太长

以前没出现，不代表它不可能存在。
平滑：给没出现的也给一个小概率
Laplace Smoothing:
都默认出现1次

## 马尔科夫假设

最后词和第一词关系不大

### 困惑度

P开n次

### SVD

矩阵太大，分解效率低，可解释性差。

### word2vec评价

#### 内部

差+

#### 外部

命名实体识别、文本分类


