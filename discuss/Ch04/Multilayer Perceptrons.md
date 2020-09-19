

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:56:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:57:17
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_multilayer-perceptrons/mlp.html
 * @TODO::
 * @Reference:
-->
Multilayer Perceptrons
Continue Discussion
13 replies
20 Jun
Andreas_​​Terzis
Nit: There is a small typo: “diagramtically” -> “diagrammatically”

1 reply
20 Jun
Andreas_​​Terzis
Should the equation (4.1.5) be H_1 = \sigma(X W_1 + b_1) to match the definition of the weight and input matrices defined in Section 3.4.1.3?

21 Jun▶ Andreas_Terzis
goldpiggy
Hi @Andreas_Terzis, sharp eyes! Fixed here https://github.com/d2l-ai/d2l-en/pull/1050/files

As for your second question, sorry for the inconsistency. They both work, but the matrixes are in “Transposed” form. To be specific:

In equation (4.1.5), we have \mathbf{W}_1, in a dimension of (q , d); and $\mathbf{X}$ in a dimension of (d, n).

On the other hand, in equation of section 3.4.1.3, we have \mathbf{W}, in a dimension of (d, q); and $\mathbf{X}$ in a dimension of (n, d).

Let me know that is clear enough.

21 Jun
Andreas_​​Terzis
Thanks for the quick reply and for clarifying the differences in matrix dimensions

You can consider whether you want to explicitly mention the dimensions of \mathbf{W}_1 and \mathbf{X} in 4.1.5 to avoid confusion with the previous definitions. Doing so would also help with readers that do go through the book sequentially.

Best

1 reply
22 Jun▶ Andreas_Terzis
goldpiggy
Hi @Andreas_Terzis, great feedback! We will consider your suggestions and fix it asap.

7 Jul
Kushagra_​​Chaturvedy
What would be the explanation for the last question? As far as I can tell, it makes little difference if we apply the activation function row-wise (which I’m guessing refers to applying the activation function to each instance of the batch one by one) or apply the function to the whole batch. Won’t both ways yield a similar result?

1 reply
7 Jul▶ Kushagra_Chaturvedy
goldpiggy
Hi @Kushagra_Chaturvedy, minibatch may not be as representative as the whole batch. As a result, parameters learned from the (small) minibatch dataset may get some weird gradients and make the model harder to converge.

1 reply
9 Jul▶ goldpiggy
Kushagra_​​Chaturvedy
Got it. But isn’t the question talking about activation functions? How will applying the activation function row-wise or batch-wise affect the learning? Also if we keep on applying the activation function row-wise for batch_size number of rows, won’t it give the same result as applying the activation function batch-wise for a single batch?

1 reply
10 Jul▶ Kushagra_Chaturvedy
goldpiggy
hey @Kushagra_Chaturvedy, from my understanding, the last question in the exercise was asking what if the minibatch size is 1?. In this case, the minibatch is too small to converge.

26 Jul
sahu.​vaibhav
How do we explain 2nd question?

1 reply
27 Jul▶ sahu.vaibhav
goldpiggy
Hi @sahu.vaibhav! Think from here~

image
30 Aug
tinkuge
In 4.1.1.3,

For a one-hidden-layer MLP whose hidden layer has h hidden units, denote by H∈Rn×h the outputs of the hidden layer, which are hidden representations

What is the sentence trying to say?

1 reply
1 Sep▶ tinkuge
goldpiggy
Hi @tinkuge, we define hidden representations or hidden layer in this sentence. (As a lot of deep learning concepts are referred to the same thing. :wink: )

Continue Discussion
