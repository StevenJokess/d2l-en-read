

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:11:43
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:11:58
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_linear-networks/softmax-regression.html
 * @TODO::
 * @Reference:
-->
Continue Discussion
43 replies
18 Jun
Steven​Jokes
Sorry, I can’t recognize the math formulas in 3.4.6. :cold_face:

1 reply
3 Jul▶ StevenJokes
Nish
The first part is the definition of the joint likelihood function:

image

How likely it is that we observe the classifications that we do, conditional on the the input data we have and the parameters we choose (the full version of this should include the parameters after x in some form I think). We’re trying to maximise this: to choose the parameters that make the combination of input data & actual labels that we observed as likely as possible.

The second part is just a mathematical manipulation of the first part:

<image of the second part that I can’t insert because I’m new :wink: )

So we can note that maximising the first is the same as minimising the second (since we took the negative of it), and therefore we can treat the second as a ‘loss function’ (thing we want to minimise).

1 reply
3 Jul▶ Nish
Steven​Jokes
Thanks. I already have known what -log does. But I still wonder the math meaning and, more importantly , realistic meaning of the definition of the joint likelihood function.

image
Why would we need to multiply all P(y|x)
image ?
Do their parameters independent surely?
image
If we multiply some numbers which stands for different meanings, the meaning of the result is hard to say.

And I think probability is often illusive if we only use pure math without any other descripition of a natural language.

1 reply
3 Jul▶ StevenJokes
goldpiggy
Hi @StevenJokes,
$P(Y | X) = P(y_1, y_2, … | x_1,x_2,…) = \prod{P(y_i | x_i)}$ since the samples are independent.

2 replies
4 Jul▶ goldpiggy
Steven​Jokes
Are we sure about the independence? How can we? Or we just naively think that all samples are independent?
I think that independence and the establish of $P(Y | X) = P(y_1, y_2, … | x_1,x_2,…) = \prod{P(y_i | x_i)}$ 's equal sign are mutual causation.In other words, just logical rename.

1 reply
4 Jul▶ goldpiggy
Steven​Jokes
Thanks. But I think I’m still confused. Are we sure about the independence? How can we? Or we just naively think that all samples are independent?
I think that independence and the establish of $P(Y | X) = P(y_1, y_2, … | x_1,x_2,…) = \prod{P(y_i | x_i)}$ 's equal sign are mutual causation. In other words, just logical rename. We should know what P*P refers in the real world. :face_with_monocle:
And I think probability just refers to how much fraction of some real whole thing, but we use it abusely to try to predict, such as whether head or tail a coin will face up nextly.
And it is understandable to use it to process natural language due to consistency required in Logic.
But we still need more information to predict a dynamic process. And we just want to be a peacemaker when we say that P = 1/2, then we will be confident to not be wrong too much.

4 Jul
Steven​Jokes
And we can’t predict any if we can’t describe what will happen and what situation we are in now.
And different ways to describe a thing usually confuses each other, then another story will happen.
The attempts to simplify our world by concluding everything maybe just deduce a contrary result that the world will be more complex due to typo, syntax error, lie, misunderstanding, distrust and so on. :cold_face:
Just my random thoughts. :ghost:

4 Jul▶ StevenJokes
Nish
I think we do assume that the samples are conditionally independent yes - after conditioning on the input data x_i, the y_i values are independent of each other. I think this comes from assuming that the Gaussian noise in the model is well-behaved (iid).

The book has more to say on this in section 4.4.1.1:

In the standard supervised learning setting, which we have addressed up until now and will stick with throughout most of this book, we assume that both the training data and the test data are drawn independently from identical distributions (commonly called the i.i.d. assumption). This means that the process that samples our data has no memory.

1 reply
5 Jul▶ Nish
Steven​Jokes
No memory is too abstract. What does it mean?
I need more examples of identical distrbutions.
What can we call that they are identical distributions?
For example, students in a class are identical distributions?
But they usually have similiar ages and live near the school.

I read an example of it:

Just like if I flip the dice and I flip it every time, that’s independent. But if I want the sum of the two flips to be greater than 8, and the rest doesn’t count, then the first flip and the second flip are not independent, because the second flip is dependent on the first flip

What I want globally will change the dependence of data itself. Am I right?
If so, I can say it is dependent or not, just by my thought.

And I think the probablity is just an ideal thought by some mathematicians who has crazy thought to predict everything just by math.

1 reply
6 Jul
goldpiggy
 StevenJokes:
No memory is too abstract. What does it mean?

“No memory” means we don’t use the result from the first trail to judge the second trail result (positive or negative). That is, the second trail outputs fresh new positive or negative result, it doesn’t depend on the first one.

1 reply
8 Jul
Steven​Jokes
 goldpiggy:
“No memory” means we don’t use the result from the first trail to judge the second trail result (positive or negative). That is, the second trail outputs fresh new positive or negative result, it doesn’t depend on the first one.

So, we only wait for the result of the second to happen?
Probability, in the begining, more depends on what we think how many categories result are.
And, because we have freedom to say, inconsistency is so common, such as famous “Bayesian method”.
Bayesian method actually looks like a good way that we try to put right after finding something wrong.
But it is hard to say that, what we tried to fix in past will be still effective in the future. :joy:
Again, my random thought!

8 Jul
Steven​Jokes
If we can fully use the past experience to guide our action in future, then how similar of past and future is the next question that we should take attention to.
In my understanding,
over-fitting problems focus more on difference of past and future, while
under-fitting on similarity.

10 Jul
sheey
In exercise 1:

Compute the second derivative of the cross-entropy loss 𝑙(𝐲,𝐲̂) for the softmax.
Is that means


?
And where can I find exercises answer?
1 reply
10 Jul▶ sheey
goldpiggy
Hi @sheey, the second derivative will be:

$\frac{\partial^2 l(\mathbf{y}, \hat{\mathbf{y}})}{{{o_j^2}}} = … = \mathrm{softmax}(\mathbf{o})_j \cdot (1- \mathrm{softmax}(\mathbf{o})_j)$

i.e.,

image
Sorry we currently don’t provide the solutions. But feel free to ask question at the discussion forum :slight_smile:

2 replies
11 Jul▶ goldpiggy
Steven​Jokes
image

j should be in the bracket?
or
When o is vector,j should be outside?
When o_j,j should be in?

image

1 reply
11 Jul▶ goldpiggy
Steven​Jokes
We only need to calculate the the derivative of softmax(o)_j （j is in or out?) to get the second derivative of the cross-entropy loss 𝑙(𝐲,𝐲̂) ?
I noticed that the second derivative of the cross-entropy loss 𝑙(𝐲,𝐲̂) is exactly the derivative of softmax(o)_j .
The derivative of y_j is 0 ? y_j is 1 or 0? j represents the label?

1 reply
12 Jul
goldpiggy
 StevenJokes:
When o is vector,j should be outside?

Hi @StevenJokes, good question! Actually, $j$ should be outside, since we first calculate softmax of the vector $o$, then take its j’s component.

1 reply
12 Jul
goldpiggy
 StevenJokes:
I noticed that the second derivative of the cross-entropy loss 𝑙(𝐲,𝐲̂) is exactly the derivative of softmax(o)_j .

Yes. I don’t fully understand your question though.

1 reply
13 Jul▶ goldpiggy
Steven​Jokes
I got it. Thanks @goldpiggy

13 Jul▶ goldpiggy
Steven​Jokes
When we calculate the derivative of $y_j$ is 0, does it mean that we think $y_j$ has no relationship about $o_j$.

1 reply
13 Jul▶ StevenJokes
goldpiggy
Hi @StevenJokes, $y_j$ is the real label while $o_j$ is the target, i.e. $y_j$ is not a function of $o_j$.

2 replies
14 Jul▶ goldpiggy
Steven​Jokes
How do we judge whether $a$ is a function of $b$ or not?
Or we just judge by that we haven’t defined it before, rather than whether $a$ has a relationship with $b$ in reality or not.

2 replies
14 Jul▶ StevenJokes
Steven​Jokes
I think it is a function in reality. But newton’s calculus can’t calculate its derivative, just because the function is discrete.

14 Jul▶ goldpiggy
Steven​Jokes
Please check https://github.com/d2l-ai/d2l-en/issues/1141 quickly, I think it maybe makes all eval wrong.

14 Jul▶ StevenJokes
goldpiggy
How do we judge whether $a$ is a function of $b$ or not?
Or we just judge by that we haven’t defined it before, rather than whether $a$ has a relationship with $b$ in reality or not.

Hi @StevenJokes, $y$ is the true label, while $\hat{y}$ is the estimated label. Hence $\hat{y}$ is a function of $o$, while $y$ is not.

1 reply
14 Jul▶ goldpiggy
Steven​Jokes
I already have understand $y_j$ is the true label, such as one-hot. But the diverce of our thinking is that I think the true label has a certain relationship with $o_j$, so I think $y_j$ is also $o_j$'s function. When we get same $o_j$, we get only one and $y_j$. Doesn’t it conform the defination of function.
But the function is discrete.

20 Jul
Steven​Jokes
As we saw in “Freshness and Distribution Shift”, if production data is different from the data a model was trained on, a model may struggle to perform. To help with this, you should check the inputs to your pipeline.

In https://learning.oreilly.com/library/view/building-machine-learning/9781492045106/ch10.html#model_engineering

29 Jul
Harvinder_​singh
Although softmax is a nonlinear function, the outputs of softmax regression are still determined by an affine transformation of input features; thus, softmax regression is a linear model.

Can anyone explain this why is it so? because when we say that a model is linear model , then it means model is linear in the parameter but in softmax regression , we are applying softmax function which is non linear so our model parameter will become non linear.

1 reply
29 Jul
Steven​Jokes
Predicting House Prices on Kaggle
Hey @pr2tik1, it won’t be linear regression if we add non-linearity, but statistically we called “logistic regression” a “generalized linear model” since its outputs depend on a linear combinations of model parameters (beta’s), rather than products of quotients.

Just a statistical speaking!

11 Aug
ccpvirus
exercise 1.1

image
apparrently i copied the answer above, 1.2 the variance is a vector and the j-th element is exactly the form of above which is softmax(0)_j(1-softmax(0)_j)
exercise 3.3 use the squeeze theorem and it’s easy to prove
3.4 softmin could be softmin(-x)? i dont know
3.5 pass (too hard to type on the computer)
21 Aug
Gavin
In formula 3.4.7,

Screen Shot 2020-08-21 at 16.11.48

I couldn’t understand why the later 2 equations are equal, could someone explain a bit more to me? Thanks.
2 replies
21 Aug▶ Gavin
Steven​Jokes
@goldpiggy,
I can’t understand too. :sweat_smile:

21 Aug
goldpiggy
 Gavin:
I couldn’t understand why the later 2 equations are equal, could someone explain a bit more to me? Thanks.

Hi @Gavin, great question. A simple answer is:
image
For more details, please check https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/maximum-likelihood.html

2 replies
22 Aug▶ goldpiggy
Steven​Jokes
@goldpiggy
The simple answer seems to be Tautology.

I have read URL you give.
But I think it didn’t solve this question.
I can’t find anything in it.

22 Aug▶ goldpiggy
Gavin
@goldpiggy Many thanks! Finally understood it!

1 reply
23 Aug▶ Gavin
Steven​Jokes
Really? @Gavin
image
What is it related to image ?
Could you explain it?

1 reply
24 Aug▶ StevenJokes
goldpiggy
It’s explained in 3.4.8 :wink: @StevenJokes

1 reply
24 Aug▶ goldpiggy
Steven​Jokes
@goldpiggy.
ok…
just log image to

image
27 Aug
Abinash_​​Sahu
Hello. I am still not able to understand clearly how these 2 equations are related. Can you please explain, how for a particular observation i, the probability y given x is related to the entropy definition overall classes?

image
1 reply
28 Aug▶ Abinash_Sahu
Steven​Jokes
image

The green thing is same.
28 Aug
Abinash_​​Sahu
Thank you for your response. My question was more specifically why
image is same as
l(y,y_hat)

Is this because y when 1-hot encoded has only single position with 1 and hence when we sum up the y * log(y_hat) over the entire class, we are left with the probability y_hat corresponding to true y. Please advise.

1 reply
28 Aug
Steven​Jokes
 Abinash_Sahu:
Is this because y when 1-hot encoded has only single position with 1 and hence when we sum up the y * log(y_hat) over the entire class, we are left with the probability y_hat corresponding to true y. Please advise.

@Abinash_Sahu
l (y，y _ hat)

Cross entropy loss
Only one type of these losses we often use.
https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html

image
32m
J​MianT
Q1.2. Compute the variance of the distribution given by softmax(𝐨)softmax(o) and show that it matches the second derivative computed above.

Can someone point me in the right direction? I tried to use Var[𝑋]=𝐸[(𝑋−𝐸[𝑋])^2]=𝐸[𝑋^2]−𝐸[𝑋]^2 to find the variance but I ended up having the term 1/q^2… it doesn’t look like the second derivative from Q1.1.

Thanks!

Continue Discussion
