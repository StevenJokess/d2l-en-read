

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:24:01
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:24:11
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_introduction/index.html
 * @TODO::
 * @Reference:
-->
Continue Discussion
16 replies
9 Jun
manuel-​arno-​korfmann
Others (like error rate) are difficult to optimize directly, owing to non-differentiability or other complications. In these cases, it is common to optimize a surrogate objective

It’s not quite clear to me from reading what exactly is meant with “error rate”. I think it would be great if an example could be given.

1 reply
9 Jun▶ manuel-arno-korfmann
goldpiggy
Hi @manuel-arno-korfmann, “error rate” means “how much mistake the model makes”. Is that more clear?

3 replies
9 Jun▶ goldpiggy
syedmech​47
I am still unable to understand error rate.
“How much mistake to model makes” is not clear enough, did you mean how much mistake ‘the’ model makes, which is L1 distance(y-y¹).
Also can you please explain what is surrogate objective?

1 reply
9 Jun
manuel-​arno-​korfmann
I’m having a difficult time understanding

Hence, the loss 𝐿L incurred by eating the mushroom is 𝐿(𝑎=eat|𝑥)=0.2∗∞+0.8∗0=∞L(a=eat|x)=0.2∗∞+0.8∗0=∞, whereas the cost of discarding it is 𝐿(𝑎=discard|𝑥)=0.2∗0+0.8∗1=0.8L(a=discard|x)=0.2∗0+0.8∗1=0.8.

Is it possible to explain it in more depth via 1 or 2 paragraphs?

9 Jun▶ goldpiggy
manuel-​arno-​korfmann
Ok, so a person in the reading group explained that the error rate is the accumulated loss for all examples, is that correct?

1 reply
10 Jun▶ syedmech47
goldpiggy
Hey @syedmech47, Sorry for the typo here. Yes you got the idea here - the error rate is to measure the distance between y (the truth) and the $\hat{y}$ (the estimate). However the measurement metrics (which measure the error) does not limit to L1 distance, but also can accuracy, precision, recall, f1, etc.

A surrogate is a function that approximates an objective function. There are lots of measurement metrics are not differentiable (like f1 etc.), hence we need some other functions (i.e., the loss function ) to approximate the objective function.

Let me know if this is clear enough!

10 Jun▶ manuel-arno-korfmann
goldpiggy
It can be the accumulated loss, or average loss. It doesn’t make a lot difference here for optimization.

10 Jun
syedmech​47
Thanks a lot. It totally made sense.

Side Note: I just want to thank each and every person’s effort in making this wonderful resource open for all and also providing such wonderful support through discussion forums.

1 reply
10 Jun▶ syedmech47
goldpiggy
Fantastic! It’s our pleasure to enable more talents learn, apply and benefit from deep learning!

1 Aug
manuel-​arno-​korfmann
The last exercise mentions “the end-to-end learning approach”, but it is nowhere explained in the section what is “end-to-end learning”.

1 reply
3 Aug▶ manuel-arno-korfmann
goldpiggy
Great call @manuel-arno-korfmann. I suspect it refers to " Fig. 1.1.2 A typical training process".

16 Aug▶ goldpiggy
zeuslawyer
Hi @goldpiggy, i’m reading this thread and I’d like to further clarify. My understanding is:

there is a difference between error rate and cost/loss function

error rate is the number of errors in predictions for a given set of inputs X. Perhaps its the total number of errors divided by the total examples in the input data?

the loss function is a quantification of the “distance” between right and wrong predictions, which is different from the error rate which is percentage of errors as described in 2 above?

Thank you for these resources and your guidance.

2 replies
23 Aug▶ zeuslawyer
meetashok
@zeuslawyer

My understanding is as follows -

Loss function and cost functions (in this context) mean the same thing
Loss functions are a family of functions that could be relevant for a problem. For classification problems, the error rate is one such loss function. But as it isn’t differentiable. So, cross-entropy is used as a surrogate loss function
Ashok

23 Aug
meetashok
Tailors have developed a small number of parameters that describe human body shape fairly accurately for the purpose of fitting clothes. These problems are referred to as subspace estimation problems. If the dependence is linear, it is called principal component analysis.

In the above sentence, what is the word dependence referring to - dependence between what and what?

Ashok

1 reply
24 Aug
goldpiggy
 zeuslawyer:
there is a difference between error rate and cost/loss function

yes.

 zeuslawyer:
error rate is the number of errors in predictions for a given set of inputs X. Perhaps its the total number of errors divided by the total examples in the input data?

yes, we also referred it as the average error rate

 zeuslawyer:
the loss function is a quantification of the “distance” between right and wrong predictions, which is different from the error rate which is percentage of errors as described in 2 above?

Sometimes this two can be the same if error rate function is differentiable. While most of the time, it is not differentiable. For example, most of the classification error rate function is not differentiable, so we use a loss function. Check more details here.

24 Aug▶ meetashok
goldpiggy
Hi @meetashok, great question! The dependence between the principal components and the original data. So PCA transforms the data to a new coordinate system (ordering by the principal components) by orthogonal linear transformation. It tries to capture and recreate the new features from the data.

Continue Discussion
