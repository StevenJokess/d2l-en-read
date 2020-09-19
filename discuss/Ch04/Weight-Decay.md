

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:04:32
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:04:53
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_multilayer-perceptrons/weight-decay.html
 * @TODO::
 * @Reference:
-->


Continue Discussion
22 replies
24 Jun
Steven​Jokes
In 4.5.4. Concise Implementation
4-5

Typographical error！？
1 reply
24 Jun
Steven​Jokes
Animator:
http://d2l.ai/chapter_linear-networks/softmax-regression-scratch.html?highlight=d2l%20animator
http://d2l.ai/_modules/d2l/torch.html#set_axes
https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.axes.Axes.set_ylim.html

24 Jun
Steven​Jokes
4.5.1. Squared Norm Regularization
Whether we include a corresponding bias penalty b^2 can vary across implementations, and may vary across layers of a neural network. Often, we do not regularize the bias term of a network’s output layer.
Can you explain b^2 in detail?

3 replies
26 Jun▶ StevenJokes
goldpiggy
Hi @StevenJokes, thanks for the feedback, we will fix it!

26 Jun▶ StevenJokes
goldpiggy
Hi @StevenJokes

4.5.1. Squared Norm Regularization
Whether we include a corresponding bias penalty b^2 can vary across implementations, and may vary across layers of a neural network. Often, we do not regularize the bias term of a network’s output layer. Can you explain b^2 in detail?

Great question! I hardly ever see $b^2$ Generally, applying weight decay to the bias units usually makes only a small difference to the final network.

1 reply
26 Jun
Steven​Jokes
 goldpiggy:
b^2

So it just means that bias penalty is not negative?
b is not same as the b in wx+b?

18 Jul
Kushagra_​​Chaturvedy
@goldpiggy
I tried to implement the code for train_concise on my own and my loss kept increasing exponentially instead of decreasing:
image

Here is my code:

def new_train(lambd):
net=nn.Sequential(nn.Linear(num_inputs,1))
for param in net.parameters():
    param.data.normal_()
loss=nn.MSELoss()
num_epochs=100
lr=0.03
trainer=torch.optim.SGD([{"params":net[0].weight,'weight_decay':lambd},
                         {"params":net[0].bias}],lr=lr)
animator = d2l.Animator(xlabel='epochs', ylabel='loss', yscale='log',
                        xlim=[1, num_epochs], legend=['train', 'test'])
for epoch in range(num_epochs):
    for X,y in train_iter:
        with torch.enable_grad():
            trainer.zero_grad()
            l=loss(net(X),y)
        l.backward()
        trainer.step()
    if epoch%5==0:
         animator.add(epoch, (d2l.evaluate_loss(net, train_iter, loss),
                             d2l.evaluate_loss(net, test_iter, loss)))
print('L1 norm of w:', net[0].weight.norm().item())
I compared my code to the code given in the book to find where I am going wrong but I can’t figure out where I made an error and what is causing this to happen.

Intersestingly, if I increase the value of lambd to say 10, I get low generalization error but the train accuracy seems to be somewhat erratic:
image

Any ideas on this as well?

1 reply
19 Jul▶ Kushagra_Chaturvedy
goldpiggy
Hey @Kushagra_Chaturvedy, the learning rate is 0.003, while yours is different. Tuning learning rate is kind of tricky, not too small and not too high.

2 replies
19 Jul▶ goldpiggy
Kushagra_​​Chaturvedy
Ok, I didn’t know that the learning rate could cause this much disparity in results. Thanks!

19 Jul▶ goldpiggy
Steven​Jokes
Is b in b^2 same as the b in wx+b?

14 Aug▶ StevenJokes
Steven_​​Hearnt
I think the idea is that W is a really high-dimensional vector because there are so many weights. b is relatively low-dimensional, so regularizing b has a much smaller effect.

1 reply
14 Aug
Steven_​​Hearnt
Hello. I have two questions about this notebook. (1) Do I understand correctly that “weight decay” is a generic term for any regularization that involves adding some kind of norm of W (regardless of which norm) to the loss? (2) Is it not possible to add L1 regularization to the optim.SGD input? The docstring only lists L2 norm.

Thanks!

3 replies
15 Aug▶ Steven_Hearnt
goldpiggy
Great question! Weight decay ideally should be mathematically equivalent to L2 Regularization. But be carefully when you implement it in code, this article indicates that different frameworks might be slightly different.

15 Aug▶ Steven_Hearnt
Steven​Jokes
You are maybe right.
Does that mean we can use w and b as bias penalty at the same time or separately?

15 Aug
Steven​Jokes
 Steven_Hearnt:
(2) Is it not possible to add L1 regularization to the optim.SGD input? The docstring only lists L2 norm.

I think it’s possible. Can we add? @goldpiggy

1 reply
27 Aug
goldpiggy
 StevenJokes:
 Steven_Hearnt:
(2) Is it not possible to add L1 regularization to the optim.SGD input? The docstring only lists L2 norm.

I think it’s possible. Can we add?

Hi @StevenJokes and @Steven_Hearnt, great questions! L1 regularization is applicable if you specify how to handle the in-differentiable case (x=0) .

2 Sep▶ StevenJokes
kusur
Hi @StevenJokes, I might be late to the party but would like to take a stab at it from a theoretical point of view rather than practical (which has already been covered). If we regularize the bias term (b) by adding the penalty term b^2, the network would end up learning a very small value of bias term in the case where we constraint the model a lot (i.e. lambda is very big). In such a case, model would not have any average value and thus it would be predicting some value near to zero every time. So, in order to avoid such a scenario, maybe bias term isn’t regularized in the last layer.

1 reply
3 Sep
Steven​Jokes
 kusur:
If we regularize the bias term (b) by adding the penalty term b^2, the network would end up learning a very small value of bias term in the case where we constraint the model a lot (i.e. lambda is very big).

Why
“the network would end up learning a very small value of bias term”?

What does your “lambda” mean?

1 reply
3 Sep▶ StevenJokes
kusur
Lambda is the constraint imposed on the L2 norm in the loss function. It is defined in 4.5.2. If we set lambda to a very large number and include bias term in the L2 norm as well, gradient descent will set bias term to an extremely small number as well. All of this is mentioned in the section 4.5

1 reply
3 Sep▶ kusur
Steven​Jokes
image

Is it?
@kusur
1 reply
3 Sep▶ StevenJokes
kusur
Yep, If you include bias term in the l2_penalty, you set this parameter to a huge value, and train the model, you will notice that bias itself becomes very small. This removes the affine aspect of the transformation in the neural network

1 reply
3 Sep
Steven​Jokes
…still can’t understand “the affine aspect”.
Some related papers? @kusur

 kusur:
This removes the affine aspect of the transformation

Continue Discussion
