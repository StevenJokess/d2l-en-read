

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:08:59
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:09:38
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_linear-networks/linear-regression.html
 * @TODO::
 * @Reference:
-->

3 replies
23 Aug
meetashok
After training for some predetermined number of iterations (or until some other stopping criteria are met), we record the estimated model parameters, denoted 𝐰̂ ,𝑏̂ w^,b^. Note that even if our function is truly linear and noiseless, these parameters will not be the exact minimizers of the loss because, although the algorithm converges slowly towards the minimizers it cannot achieve it exactly in a finite number of steps.

I have a question about the part in bold. If we choose a large learning rate, then the algorithm can overshoot the parameter values for which loss function is minimized. So, that tells me that we should be able to find w, b that minimize the loss exactly. What could I be missing?

24 Aug
meetashok
For Q1 from the exercises, the solution for b would be the sample mean of the data. How does it relate to the normal distribution - could someone help?

Assume that we have some data 𝑥1,…,𝑥𝑛∈ℝx1,…,xn∈R. Our goal is to find a constant 𝑏b such that ∑𝑖(𝑥𝑖−𝑏)2∑i(xi−b)2 is minimized.

Find a analytic solution for the optimal value of 𝑏b.
How does this problem and its solution relate to the normal distribution?
1 reply
28 Aug▶ meetashok
osama​Gkhafagy
I believe the optimal value of b is equal to the mean of the whole dataset which represents the Mean of a normal distribution. This makes (X_i - b) is the same as the exponent of e (X_i - mu)

Continue Discussion

---

5 replies
27 Jul
manjit
i believe, for linear regression the assumption is that the residuals has to be normally distributed the noise ‘e’ y=w⊤x+b+ϵ where ϵ∼N(0,σ2) need not be

2 Aug
Angryrou
May I ask a question related to the normalization:

For categorical variable, once convert it to dummy variables (via 1-Hot encoding), is it worth to do standard normalization for it? Or what scenarios it is worth doing and what scenarios it may not?

Thanks in advance!

1 reply
3 Aug▶ Angryrou
goldpiggy
Hi @Angryrou, can you elaborate more on normalization. I imagine you mean normalizing the numerical features to a normal distribution? Or you mean Batch Normalization?

1 reply
4 Aug▶ goldpiggy
Angryrou
Sorry for the ambiguous. I mean normalizing the numerical features to a normal distribution. E.g., using sklearn.preprocessing.MinMaxScaler / StandardScaler.

Take preprocessing features like (age, major, sex, height, weights) for a students as a more concrete example. After fill null values and convert categorical variables to dummy vectors, I would like to do normalization for all the features. For the dummy vectors from categorical variables, is it worth to do standard normalization for it? Or what scenarios it is worth doing and what scenarios it may not?

1 reply
4 Aug▶ Angryrou
goldpiggy
Hey @Angryrou, you are right about normalization! And it is extremely important in deep learning world. For the numerical feature, we just apply normalization on the scalar values. While for the categorical feature, we represent its scalar value as a vector (via one-hot encoding). The feature will be look like a list of zeros and ones, and we don’t normalize further beyond that.

We combine those normalized scalar features (from numerical features) and one-hot vectors (from categorical features) together, and feed the combinations to the neural nets.

Continue Discussion
