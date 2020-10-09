

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-09 14:17:07
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-09 15:08:27
 * @Description:
 * @TODO::
 * @Reference:https://zhuanlan.zhihu.com/p/70124635
-->

回归常见的评价指标和局限性？？

MSE, RMSE和MAE以及R Squared，缺点下面的博文写的挺清晰的不赘述。

衡量线性回归法的指标MSE, RMSE,MAE和R Square
​
www.cnblogs.com

最初的平方差公式：

$$
\sum_{i=1}^{m}\left(y_{t e s t}^{(i)}-\hat{y}_{t e s t}^{(i)}\right)^{2}
$$

这个公式的问题在于最终的误差值和样本的数量是有关系的，样本数量m越大，则这个值越大，显然这不是我们所期望的,否则同一个问题，不同数量的情况下mse没法比较因为样本数量大往往误差的总的值越大，所以引入了MSE，均方误差：

$$
\frac{1}{m} \sum_{i=1}^{m}\left(y_{t e s t}^{(i)}-\hat{y}_{t e s t}^{(i)}\right)^{2} \quad \begin{array}{c}
\text { 均方误差 MSE } \\
\text { (Mean Squared Error) }
\end{array}
$$

但又有一个问题，之前算这个公式时为了保证其每项为正，且可导（所以没用绝对值的表示方法），我们对式子加了一个平方。但这可能会导致量纲的问题，如房子价格为万元，平方后就成了万元的平方，这样实际上反应出来的误差不是房价价格的预测误差而是房子价格平方的预测误差，这样在进行决策等方面可能会出现一些问题，另一方面，量纲的变化会引起MSE的值的变化变大，所以引入了RMSE：

$$
\sqrt{\frac{1}{m} \sum_{i=1}^{m}\left(y_{t e s t}^{(i)}-\hat{y}_{t e s t}^{(i)}\right)^{2}}=\sqrt{M S E_{t e s t}} \quad \text { . } \quad \text { (Root Mean Squared Error) }
$$

MSE与RMSE的区别仅在于对量纲是否敏感。

另外一个评价指标的思路是取绝对值：

$$
\frac{1}{m} \sum_{i=1}^{m}\left|y_{\text {test}}^{(i)}-\hat{y}_{\text {test}}^{(i)}\right| \begin{array}{c}
\text { 平均绝对误差 } \mathrm{MAE} \\
\text { (Mean Aissplats, Frror) }
\end{array}
$$


RMSE 与 MAE 的量纲相同，但求出结果后我们会发现RMSE比MAE的要大一些。这是因为RMSE是先对误差进行平方的累加后再开方，它其实是放大了较大误差之间的差距。而MAE反应的就是真实误差。因此在衡量中使RMSE的值越小其意义越大，因为它的值能反映出模型的最大误差也是比较小的（简单说就是RMSE的值一般要比MAE大，所以RMSE小了那么MAE必然小，而MAE小了，RMSE不一定小，所以直接看RMSE更好一些）。

上述指标都存在的一个问题就是，不像准确率或者auc之类的有一个明确的上下限，否则我们不能很好的判定当前的模型是否足够好。

解决方法==> 新的指标：R方

$R^{2}=1-\frac{S S_{\text {residual}}}{S S_{\text {total}}} \quad$ (Residual Sum of Squares)
$$
R^{2}=1-\frac{\sum_{i}\left(\hat{y}^{(i)}-y^{(i)}\right)^{2}}{\sum_{i}\left(\bar{y}-y^{(i)}\right)^{2}}
$$



使用baseline模型肯定会产生很多错误，我们自己的模型产生的错误会少一些。

1 - ourModelError / baselineModelError = 我们模型拟合住的部分



R方将回归结果归约到了0-1间，允许我们对不同问题的预测结果进行比对了。
$$
R^{2}=1-\frac{\sum_{i}\left(\hat{y}^{(i)}-y^{(i)}\right)^{2}}{\sum_{i}\left(\bar{y}-y^{(i)}\right)^{2}}=1-\frac{\left(\sum_{i=1}^{m}\left(\hat{y}^{(i)}-y^{(i)}\right)^{2}\right) / m}{\left(\sum_{i=1}^{m}\left(y^{(i)}-\bar{y}\right)^{2}\right) / m}
$$
我们可发现，上面其实就是MSE，下面就是方差
$$
=1-\frac{M S E(\hat{y}, y)}{\operatorname{Var}(y)}
$$


R^2最大的好处是将回归的评价归一到0-1区间，使得我们有了一个比较统一的评价标准。

另外有一点非常重要的是，也是原文中没有解释到的地方，无论是MSE、MAE、RMSE都对异常值非常敏感，而R^2因为存在归一化作用的分母使得异常值对总体值的影响大大下降了（因为如果原始的回归标签有极大极小的异常值则分母也会相应变得很大），这也是应用过程中的一个非常严重的问题，可以自己尝试一下把某个回归数据集中的小部分样本的标签值扩大10000倍然后去计算这些指标就知道影响有多严重了，所以很多时候异常值的处理是很重要的。
