

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:41:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:41:29
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_convolutional-neural-networks/why-conv.html
 * @TODO::
 * @Reference:
-->
Continue Discussion
11 replies
14 Jul
lregistros
6.1.2 formulas make use of the u[i,j] term but there is no explanation of what is u.

2 replies
15 Jul
lregistros
Equation 6.1.1 is missing the x term that multiplies V.

1 reply
16 Jul
Steven​Jokes
6.1.6.2 When might it not make sense to allow for pigs to fly?
What does “when” mean?

16 Jul▶ lregistros
Steven​Jokes
6-1-1

No missing.
?
1 reply
16 Jul▶ lregistros
Steven​Jokes
6.1.1 formulas make use of the u[i,j] term but there is no explanation of what is u .
Wait for explanation.

17 Jul▶ lregistros
goldpiggy
6.1.2 formulas make use of the u[i,j] term but there is no explanation of what is u .

Hi @lregistros and @StevenJokes, u is the bias term here. Sorry for confusion, we will rewrite this section later.

17 Jul▶ StevenJokes
lregistros
Sorry to the confusion. It was the browser in my tablet trimming the formula.
20200717_205007
31 Jul
manuel-​arno-​korfmann
Because these networks are invariant to the order of the features, we could get similar results regardless of whether we preserve an order corresponding to the spatial structure of the pixels or if we permute the columns of our design matrix before fitting the MLP’s parameters.

https://d2l.ai/chapter_convolutional-neural-networks/index.html §1

This would require to permute the columns for all examples consistently or could we basically shuffle all examples in a different way for the same training run?

2 replies
31 Jul▶ manuel-arno-korfmann
Steven​Jokes
Couldn’t understand your meaning. Do you mean whether we keep order of examples or not?
If you ask this, the answer is not.

1 reply
27 Aug▶ StevenJokes
manuel-​arno-​korfmann
No, that wasn’t the question.

29 Aug
goldpiggy
 manuel-arno-korfmann:
Because these networks are invariant to the order of the features, we could get similar results regardless of whether we preserve an order corresponding to the spatial structure of the pixels or if we permute the columns of our design matrix before fitting the MLP’s parameters.

https://d2l.ai/chapter_convolutional-neural-networks/index.html §1

This would require to permute the columns for all examples consistently or could we basically shuffle all examples in a different way for the same training run?

Hi @manuel-arno-korfmann, great question! We need to permute the columns for all examples consistently. Since features’ sequence is important for NN, once the weights are trained. Each feature should come from specific location. Even though for the feature themselves, their order is not important.

Continue Discussion
