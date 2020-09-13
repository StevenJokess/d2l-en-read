

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:06:01
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:06:17
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_multilayer-perceptrons/backprop.html
 * @TODO::
 * @Reference:
-->
Continue Discussion
14 replies
25 Jun
Andreas_​​Terzis
small typo: “requried” -> “required”

Thanks again for the great resource you’ve put together!

26 Jun
Steven​Jokes
n×m
4-7-e
How to compute the memory footprint? What is in the memory?
Computational Graph of Backpropagation? Try to track all latest two times’ calculate.
Now, I can’t. How to parallelly train?
Good for updating quickly.Easy to fall into a local extremum.
22 Jul
RaphaelCS
Why does the backpropagation (I mean the way of calculating gradients) have to go in the opposite direction of forward propagation? Can’t we calculate gradients in the forward propagation, which cost less memory?

3 replies
22 Jul▶ RaphaelCS
Steven​Jokes
The purpose of backward propagation is to get near to, even same as the labels we gave.
We only calulate gradients when we know the distance of prediction and reality.
This is the backward propagation what really does.

23 Jul▶ RaphaelCS
goldpiggy
Hi @RaphaelCS, great question! Please find more details at https://mxnet.apache.org/api/architecture/note_memory to see how we manage memory efficiently.

1 reply
25 Jul▶ goldpiggy
RaphaelCS
Thanks for the reference !

2 Aug
skywalker_​H
I want to ensure some kind of achievement about back propagation which is equivalent to the normal way from my perspective. I think we could do merely the partial derivation and value calculation during the forwarding pass and multiplication during the back propagation. Is it an effective, or to say another equivalent way to achieve BP? Or they are different from some aspects?

1 reply
2 Aug▶ skywalker_H
Steven​Jokes
I think we could do merely the partial derivation and value calculation during the forwarding pass and multiplication during the back propagation.

What is different with BP?

1 reply
2 Aug▶ StevenJokes
skywalker_​H
BP do the partial derivation during back propogation step rather than the forwarding step? I just want to ensure wether these two methods have the same effect. Thanks for your reply.

1 reply
2 Aug▶ skywalker_H
Steven​Jokes
The most important thing, in my opinion, is to find out which elements we need to calculate the partial derivation. Back propogation is only the way to find it. Am I right?

1 reply
3 Aug
skywalker_​H
 StevenJokes:
my opinion, is to find out which elements we need to calculate the partial derivation. Back propogation is only the way to find it. Am I right?

I agree with you and now I think two ways mentioned above are actually the same .

8 Aug▶ RaphaelCS
Anand_​​Ram
For BP to calculate the gradients with respect to the current loss, we need to actually do the forward pass and get the loss with the current parameters, right ? How can BP be done in the forward pass if we don’t even have the loss for the current parameters.

1 reply
8 Aug▶ Anand_Ram
RaphaelCS
In my opinion, we can calculate the partial derivative of h1 w.r.t. x and the partial derivative of h2 w.r.t.h1, then we can obtain the partial derivative of h2 w.r.t. x by multiplying the previous two partial derivatives. I think these calculations can all be done in forwarding steps. (x refers to input, h1 and h2 refer to two hidden layers)
If I’m not mistaken, we can keep calculating in this manner until the loss, thus all in forward stage.

BTW, perhaps this method requires much more memory to store the intermediate partial derivatives.

1 reply
10 Aug
goldpiggy
 RaphaelCS:
BTW, perhaps this method requires much more memory to store the intermediate partial derivatives.

Great discussion @Anand_Ram and @RaphaelCS ! As you point out the memory may explode if we save all the immediate gradient. Besides, some of the saved gradients may not require for calculation. As a result, we usually do a full pass of forward propagation and then backpropagate.

Continue Discussion
