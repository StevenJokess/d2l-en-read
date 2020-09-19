

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:10:00
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:10:30
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_linear-networks/linear-regression-scratch.html
 * @TODO::
 * @Reference:
-->

Continue Discussion
36 replies
6 Jun
Angryrou
In the 3.2.7 training part, the pytorch implementation for getting w and b did a much worse job
compared to the 3.3.7, where applied built-in pytorch functions. E.g., the error for predicting b is 1.8039 in 3.2.7 but -0.0006 in 3.3.7.

I tried to dive into but failed to find the reason. Could anyone help? It is not reasonable that the error were not in the same order of magnitude.

P.S. both the mxnet implementations in 3.2.7 and 3.3.7 achieved w and b close to their real value. E.g., the error for predicting b are 0.00049448 and 0.00026846 respectively according to the notebook (also my local test with similar results)

1 reply
7 Jun▶ Angryrou
Gent​Rich
Looks like in sgd function for pytorch, it should not divide param.grad by batch_size, because in main loop, it did l.mean().backward()

1 reply
7 Jun▶ GentRich
Angryrou
Thanks for point out this! I do not think the sgd function has problem – It follows the definition. Rather I feel it would make more sense to change l.mean().backward() to l.sum().backward().

8 Jun
ouafo_​mandela
def sgd(params, lr, batch_size): #@save
for param in params:
param.data.sub_(lr*param.grad/batch_size) # this line cause the problem, we don’t divide by batch_size, if you try with param.data.sub_(lr*param.grad) you will get a right result
param.grad.data.zero_()

12 Jun
Morris​Xu-​​Driving
Just as the same as the above discussion. The “l.mean().backward()” has already calculated the mean of the 10-dimensional loss vector. Now we get back to the sgd(), the “param.data.sub_(lr * param.grad / batch_size)” is undoubtedly wrong as the update is divided by batch_size again. That is why the two different implementation has different performance. Once you correct sgd() by deleting “/batch_size”, you will get the correct answer

12 Jun
Steven​Jokes
w = torch.zeros(size=(2,1), requires_grad=True)
w
tensor([[0.],
[0.]], requires_grad=True)

lr = 0.03  # Learning rate
num_epochs = 3  # Number of iterations
net = linreg  # Our fancy linear model
loss = squared_loss  # 0.5 (y-y')^2

for epoch in range(num_epochs):
    # Assuming the number of examples can be divided by the batch size, all
    # the examples in the training data set are used once in one epoch
    # iteration. The features and tags of mini-batch examples are given by X
    # and y respectively
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # Minibatch loss in X and y
        l.mean().backward()  # Compute gradient on l with respect to [w,b]
        sgd([w, b], lr, batch_size)  # Update parameters using their gradient
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch+1}, loss {float(train_l.mean())}')
epoch 1, loss 4.442716598510742
epoch 2, loss 2.3868186473846436
epoch 3, loss 1.2835431098937988

Still works. Why? What difference with the question as follow? I think autograd would fail, but it didn’t.
datascience.stackexchange.com
Elias Strehle
Initialize perceptron weights with zero
machine-learning, neural-network, deep-learning
answered by Elias Strehle on 04:43PM - 31 Jan 18 UTC
Now, w isn’t zeros too. Really confused :cold_face:.

w
tensor([[ 1.1457],
[-2.0979]], requires_grad=True)

1 reply
12 Jun▶ StevenJokes
anirudh
@GentRich @ouafo_mandela @Angryrou Thanks for catching this bug. We’ll fix this asap.
Also @StevenJokes it still works because by diving an extra time by batch size we have just scaled down the gradients but we are still moving in the right direction towards the local minima. But technically l.sum() is correct not l.mean().

13 Jun
Steven​Jokes
Does it mean that it shouldn’t work when using the correct l.sum?
:thinking:
I think that gradient is 0 when W is ones. Why moving in the right direction?

1 reply
14 Jun▶ StevenJokes
anirudh
Hi @StevenJokes, Sorry, in my reply, I was not explaining your question about weight initialization. I probably missed that question. I was explaining the reason it works for l.mean() (Which is obviously wrong and has been fixed now.) given everything remains the same.

So, now, to answer your question about zero weight init, let me explain below.
Here we are using a simple squared error loss function/cost function.
When you use a convex cost function (has only one minima), you can initialize your weights to zeros and still reach the minima. The reason is that you’ll have just a single optimal point and it does not matter where you start by initializing the weights. Though, the starting point may change the epochs it takes to reach optimum you are bound to reach it. On the other hand in neural networks with the hidden layers the cost function doesnt have one single optimum and in that case to break the symmetry we don’t want to use same weights.

15 Jun
Steven​Jokes
If y = b , then gradient is 0.
I think that gradient is 0 when W is zeros. Why moving in the right direction ?
I have understand that convex cost function has only one minima .
But param.data.sub_(lr*param.grad/batch_size) will make sure that param doesn’t change, if grad == 0. :sweat_smile:
Then how to get the only minima without params changed :expressionless:?

1 reply
15 Jun
Steven​Jokes
I didn’t understand the relation between

for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # Minibatch loss in X and y
and

 with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
Why did we use features to replace x and use labels to replace y?
Can you explain The features and tags of mini-batch examples are given by X
# and y respectively in more detail?

1 reply
15 Jun▶ StevenJokes
Steven​Jokes
set y as voltage and set x as current.
No, I can’t.
image
I can’t separate variables v and T in e^(hv/KT).
y.backward(retain_graph=True)
true_w has one row and len(w) columns, but w has len(w) rows and one column.
set lr = your_num
In the last loop of for i in range(0, num_examples, batch_size): : j = torch.tensor(indices[i: num_examples)
15 Jun▶ StevenJokes
anirudh
@StevenJokes your understanding of graadients is wrong.

Let me give you a high school example.
Let’s say.
y= wx (Where x is a constant)
The dy/dw = x It doesn’t matter what the value of w is. Gradient is always x.

Get the point?
Similarly when weights are set to zero. gradient is not zero.

If you don’t believe me and you want to print out the gradient value to check:
Then do this small experiment.

X = torch.ones(10,2)
w = torch.zeros((2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
y = torch.matmul(X, w) + b
y.sum().backward()

print(w.grad)
>>>tensor([[10.],
        [10.]])

print(X.sum(dim=0))
>>>tensor([10., 10.])

1 reply
15 Jun▶ anirudh
Steven​Jokes
I just knew that gradient is dy/dw instead of dy/dx. :joy:

1 reply
15 Jun▶ StevenJokes
anirudh
We calculate the derivates with respect to weights and not the inputs.
Is this clear now?

1 reply
15 Jun▶ anirudh
Steven​Jokes
Thanks a lot. I got it why I was worry.

1 reply
15 Jun▶ StevenJokes
anirudh
Can you close the issue if your doubt is solved? @StevenJokes

1 reply
16 Jun
Steven​Jokes
You meant my github’s issue?
My issue is about " 2.5.2 does’t have PyTorch’s version."
 Auto Differentiation pytorch
Q1. Does it mean that if I ‘clone’ a tensor or a Variable that has requires_grad attribute, then I don’t need to .requires_grad() for the new one? Use detach() to remove a tensor? However, why can I still judge x.grad() == u.grad? “Remove” doesn’t mean that x will not exist? I think that x and u are just two different names for the same storage. Can my code about 2.5.2’s Variable add to 2.5.2? Q2. I have understand that d is a function of which scales a. But what difference with f(b)? …

I have heard that Variable has merge into tensor from zhihu.
Is it right?
If so, 2.5.2 doesn’t need PyTorch’s version.
1 reply
16 Jun▶ StevenJokes
anirudh
I have replied to the thread. I think that will answer your questions.
Yes, I meant closing the issue on github if your doubt is solved.

30 Jun
Kushagra_​​Chaturvedy
Could anyone explain why in the pytorch implementation we have implemented the line param.grad.data.zero_() ?

Why are we setting the gradients of the parameters to 0 after subtracting them from the parameter values? I made my model without this line and my loss kept increasing and reached inf. Also the values of my parameters w, b are large negative values.

1 reply
30 Jun▶ Kushagra_Chaturvedy
Steven​Jokes
# PyTorch accumulates the gradient in default, we need to clear the previous
# values.
x.grad.zero_()
in http://preview.d2l.ai/d2l-en/PR-1080/chapter_preliminaries/autograd.html!

You can use the searching image to find whether a function have mentioned before.

21 Jul
bobbyfyb
When I run the training code, I got the error:

‘AttributeError: ‘builtin_function_or_method’ object has no attribute ‘backward’’

with l.sum.backward()
How could a loss function we defined by ourselves be autograded ?

1 reply
21 Jul
Steven​Jokes
 bobbyfyb:
‘AttributeError: ‘builtin_function_or_method’ object has no attribute ‘backward’’

with l.sum.backward()

I can’t give your answer without the whole code you ran. Please publish your all code you ran.

1 reply
22 Jul▶ StevenJokes
bobbyfyb
Thanks for your reply. below is all my code.

%matplotlib inline
from d2l import torch as d2l
import torch
import random
def synthetic_data(w, b, num_examples):
    """ Generate y = Xw + b + noise. """
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))
​
true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)
print('features:', features[0], '\nlabel:', labels[0])
features: tensor([ 0.5924, -1.3852])
label: tensor([10.1155])
d2l.set_figsize()
# The semicolon is for displaying the plot only
d2l.plt.scatter(d2l.numpy(features[:, 1]), d2l.numpy(labels), 1)
<matplotlib.collections.PathCollection at 0x7f18c1d59750>
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    #The examples are read at random, in no particular order
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i:min(i+batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]
batch_size = 10
​
for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    break
tensor([[-0.9675,  0.7085],
        [ 0.8437, -0.6500],
        [ 0.1811,  1.1862],
        [-0.3506,  0.0772],
        [ 0.3116,  0.9374],
        [ 0.5395,  0.6735],
        [ 1.2217, -0.2031],
        [-1.3825, -1.7679],
        [ 1.2293,  0.1035],
        [ 1.2081,  0.4335]])
 tensor([[-0.1261],
        [ 8.0838],
        [ 0.5244],
        [ 3.2267],
        [ 1.6360],
        [ 2.9801],
        [ 7.3324],
        [ 7.4362],
        [ 6.3053],
        [ 5.1291]])
w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
def linreg(X, w, b):
    """The linear regression model."""
    return torch.matmul(X, w) + b
def  squared_loss(y_hat, y):
    """Squared loss."""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2
def sgd(params, lr, batch_size):
    """Minibatch stochastic gradient descent."""
    for param in params:
        param.data.sub_(lr*param.grad/batch_size)
        param.grad.data.zero_()
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss
​
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y) # Minibatch loss in 'X' and 'y'
        # Compute gradient on 'l' with respect to ['w', 'b']
        l.sum.backward()
        sgd([w, b], lr, batch_size) # Update parameters using their gradient
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch{epoch+1}, loss{float(train_l.mean()):f}')

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-23-fa7fa5fdb2c8> in <module>
      8         l = loss(net(X, w, b), y) # Minibatch loss in 'X' and 'y'
      9         # Compute gradient on 'l' with respect to ['w', 'b']
---> 10         l.sum.backward()
     11         sgd([w, b], lr, batch_size) # Update parameters using their gradient
     12     with torch.no_grad():

AttributeError: 'builtin_function_or_method' object has no attribute 'backward'
​

1 reply
22 Jul▶ bobbyfyb
Steven​Jokes
You should use l.sum().backward().
Try to contrast with the code given before you ask please, and it is quicker and useful usually.
image
1 reply
23 Jul▶ StevenJokes
bobbyfyb
Thinks! forgive my stupid mistake :sweat_smile: I am too careless

13 Aug
Steven_​​Hearnt
This is a minor point, and doesn’t affect the main ideas of this exercise. But I believe that the SGD result should be compared against the analytic least-squares solution, not against the true_w and true_b. The reason is that the best solution from least-squares is also unlikely to match true_* because of sampling variability in the noise. That is to say, the real best solution here is not the initial parameters; it’s the least-square solution to the observed data.

Not a big deal here, because the noise is small relative to the effect size. But I thought I would point it out anyway.

Great book so far! Thanks!

1 reply
14 Aug
Steven​Jokes
 Steven_Hearnt:
But I believe that the SGD result should be compared against the analytic least-squares solution, not against the true_w and true_b. The reason is that the best solution from least-squares is also unlikely to match true_* because of sampling variability in the noise. That is to say, the real best solution here is not the initial parameters; it’s the least-square solution to the observed data.

@Steven_Hearnt
Sorry, I’m an idiot. Can you explain more or give me more reference? :sweat_smile:

1 reply
14 Aug▶ StevenJokes
Steven_​​Hearnt
You’re not an idiot just because you ask a question. The real idiot wouldn’t even be on this forum :wink:

The least-squares is the best possible measure of the linear relationship because those variables. The relationship in the “real data” is not the same as the true_* parameters, because the data contain noise that was added after the true_* parameters were defined. So in the actual dataset, the least-squares solution is the best possible solution.

Here’s another example of this. If you generate normally distributed random numbers, the “true” theoretical average should be 0.00000… but the data you generate won’t have an average of 0, because of sampling variability. Maybe the average in your sample is 0.1. So the best possible estimator of the central tendency in your dataset is .1, not 0. Because the true mean of your data is .1, even though those numbers were drawn from a distribution with a theoretical mean of 0.

1 reply
14 Aug▶ Steven_Hearnt
goldpiggy
Thanks for the rigorous thought, @Steven_Hearnt. If I understand correctly, you want to point out that the mean squared error is the sum of the square of the bias, the variance and the irreducible error (or bias-variance decomposition)? I agree theoretically we should compare the sgd result with the theoretical mean (if we decompose the error to bias and variance). While if we count the irreducible error in, then that would explain our current comparison.

Let me know if you have more profound thoughts on this! :wink:

1 reply
14 Aug▶ goldpiggy
Steven_​​Hearnt
Yeah, that’s right. I guess another way to think about it is to imagine that these data are some sensor output. The sensor has a systematic error that adds .1 to all measurements. Without knowing about that systematic error, an ideal model of the data can be perfectly accurate to the sensor but can never overcome the systematic bias to be perfectly accurate to the thing the sensor is measuring.

In this notebook, we’re adding non-systematic error, but the principle is the same: The best any model can recover is the sample statistics because we don’t know the population parameters (well, we do because we defined the true_* variables, but the model doesn’t have access to that). So my thought was that the ANN should be compared to the maximum-likelihood estimator, not the true underlying parameter (which the ML estimator also wouldn’t know).

Anyway, it was just a thought; I don’t want to make a big deal of it because it’s more academic than practical :wink:

1 reply
15 Aug
Steven​Jokes
@Steven_Hearnt
I still feel confused about what you are talking.
In my understanding, linear relationship is just our idea to simplify a relationship, that maybe we get a hint from Newton “F=ma”.
And then we use words like “noise” to present what isn’t no linear.
So if you have distibution having 0.1 mean, that mean we can add this “0.1” to linear relationship. That is b.
Am I right?

1 reply
15 Aug
Steven​Jokes
 Steven_Hearnt:
So my thought was that the ANN should be compared to the maximum-likelihood estimator, not the true underlying parameter (which the ML estimator also wouldn’t know).

What do you compare with? I can’t see any relation between them.

31 Aug
oliver
I have a question about the following function, can someone please help me?

def squared_loss(y_hat, y):  #@save
    """Squared loss."""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2
Since y_hat is generated by linreg() , its shape will be batch_size * 1 , which is the same as y , then why is y.reshape(y_hat.shape) necessary? I get wrong results after deleting it.

2 replies
31 Aug▶ oliver
gpk​2000
I tested the code in MXNET colab link and removed the reshape method. It worked fine for me, you might be missing something. Also the reshape is done like a sanity check i guess, so that it won’t raise an error.

31 Aug
Steven​Jokes
show your code next time.
@oliver
 Do these before you ask! d2l-en
If you have any questions, you should do these first. 0. Read again your code and contrast with code given. Read the below discussions including all tabs “mxnet”/“pytorch”/“tensorflow” Try to Google it & Stackoverflow it. Update all your package, for example, maybe you need:), if we forget to update the version number : pip uninstall d2l pip install d2l -U -i https://pypi.python.org/simple Use the search button to find the related context. Book: [image] Discuss: [image] Old discussion:…
Continue Discussion
