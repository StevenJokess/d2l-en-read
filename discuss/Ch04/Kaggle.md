

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:00:47
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:00:50
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_multilayer-perceptrons/kaggle-house-price.html
 * @TODO::
 * @Reference:
-->
7 replies
22 Jul
Irma_​​Ravkic
Hi, when doing standardization one would need to first calculate mean and std of the train set, and then use that mean and std to standardize the test set. Otherwise you have information leakage from training data to test data.

1 reply
6 Aug▶ Irma_Ravkic
goldpiggy
Hi @Irma_Ravkic, great catch! I agree with you about the information leak! Would you like to be a contributor?

1 reply
6 Aug
Irma_​​Ravkic
Thanks. Yes, sure, I can change that section (and if I see something else on the way).

Irma

6 Sep
gpk​2000
Is @Irma_Ravkic suggestion implemented?

6 Sep
gpk​2000
When I try to use sgd instead of Adam, I get nan as the rmse value at the end. I ran the code using the google colab link provided so there is no implementation problem from my side. Why doesn’t sgd work here?

1 reply
8 Sep▶ gpk2000
goldpiggy
Hi @gpk2000, great question. For gradients with significant variance, we may encounter issues with divergence. That is why you saw the NAN at the end. Adam and other optimization methods alleviate the problem: https://d2l.ai/chapter_optimization/adam.html.

19h▶ goldpiggy
smizerex
In both the pdf and colab version it seems that this issue was fixed and executed in the “Data Preprocessing” passage of this section, is that true?

Continue Discussion
