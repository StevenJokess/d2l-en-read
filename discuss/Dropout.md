

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 18:54:31
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 18:55:15
 * @Description:https://discuss.d2l.ai/t/dropout/101
 * @TODO::
 * @Reference:
-->

I noticed there isn’t test loss. Why?
I have read as following.
datascience.stackexchange.com
N.IT
What is the relationship between the accuracy and the loss in deep learning?
neural-network, deep-learning, keras, tensorflow
asked by N.IT on 09:08AM - 14 Dec 18 UTC

https://kharshit.github.io/blog/2018/12/07/loss-vs-accuracy 2

Two pics in 4.6.4.3. Training and Testing and 4.6.5. Concise Implementation are so different?

4.6.7. Exercises
I have tried to switch the dropout probabilities for layers 1 and 2 by switching dropout1 and dropout2.
Sequential(
(0): Flatten()
(1): Linear(in_features=784, out_features=256, bias=True)
(2): ReLU()
(3): Dropout(p=0.5, inplace=False)
(4): Linear(in_features=256, out_features=256, bias=True)
(5): ReLU()
(6): Dropout(p=0.2, inplace=False)
(7): Linear(in_features=256, out_features=10, bias=True)
)
trainer = torch.optim.SGD(net.parameters(), lr=lr)
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)
4-6e-1
But how can I confirm that the change’s cause is my action of switching the dropout probabilities other than random init?

num_epochs = 20
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)
4-6e-2
d2l.train_ch3? Does it train continously? I guess so.

we use .reset_parameters()?
 PyTorch Forums – 6 Jul 18

How to re-set alll parameters in a network
How to re-set the weights for the entire network, using the original pytorch weight initialization

Reading time: 1 mins 🕑Likes: 4 ❤

 PyTorch Forums – 14 Jul 18

What's the default initialization methods for layers?
So Pytorch uses He when its ReLU? Im confused what pytorch does.

And I found that searching in pytorch docs is so slow. Do you have some good advices?

How similar can we say that these pics are similar?
We can’t expect exactly the same outputs when we have the same inputs?

We use loss function just for training’s Backpropagation, and we don’t need to train anymore when we are in test. Similiarly, we just care the final scores of exam instead of the concrete answers.
Do I understand it rightly?



Dropout in the test

We don’t allow Dropout in the test.
The first answer in
How does dropout work during testing in neural network? 2 can explain well.
However, there are two main reasons you should not use dropout to test data:

Dropout makes neurons output ‘wrong’ values on purpose
Because you disable neurons randomly , your network will have different outputs every (sequences of) activation. This undermines consistency.
the weights corresponding to those zeros will still update, because the weight not only corresponds to those zeros, but also other not zeros in the same hidden layer.

After we dropouted, the corresponding hidden layers have already changed. Enable/Disable is confusing.
Test is just a process of calculating a prediction by weights after bp. We don’t need to disable Dropout!
Yes, matrix multiplication is the reason of corresponding to multiple hidden units.


