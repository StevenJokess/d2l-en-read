

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:01:38
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:01:50
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_multilayer-perceptrons/environment.html
 * @TODO::
 * @Reference:
-->

2 replies
6 Sep
kusur
Hi @goldpiggy, while going through section 4.9.2.1, I found that it was the mentioned that this case involved covariate shift.

As we explained to them, it would indeed be easy to distinguish between the healthy and sick cohorts with near-perfect accuracy. However, that is because the test subjects differed in age, hormone levels, physical activity, diet, alcohol consumption, and many more factors unrelated to the disease. This was unlikely to be the case with real patients. Due to their sampling procedure, we could expect to encounter extreme covariate shift.

However, as per the definition of Label Shift in 4.9.1.2., it is said that such cases are examples of Label Drift

For example, we may want to predict diagnoses given their symptoms (or other manifestations), even as the relative prevalence of diagnoses are changing over time. Label shift is the appropriate assumption here because diseases cause symptoms

Could you please let me know where am I lacking in understanding here? Thanks

1 reply
8 Sep▶ kusur
goldpiggy
Hi @kusur, great question! In the covariate shift, we focus on the distribution shift of “data” or “feature”. For example, the in age, hormone levels, physical activity, diet, alcohol consumption, and many more factors ... are all features for a sample point. While for the label shift focus on the distribution shift of the “label”, such as the disease diagnoses. Check more details in this paper: https://arxiv.org/pdf/1802.03916.pdf.

Continue Discussion
