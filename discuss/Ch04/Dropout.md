

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:07:03
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:07:13
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_multilayer-perceptrons/dropout.html
 * @TODO::
 * @Reference:
-->
Continue Discussion
23 replies
10 Jun
Angryrou
Is there any trick when applying dropout for improving (test) accuracy? – In this example, by using the dropout approach, the test accuracy on the Fashion-MNIST dataset does not get improved compared to the MLP approach in section 4.3
Specifically, denote gap = accuracy_train (A1) - accuracy_test (A2). By using dropout, I would expect a smaller gap and a smaller A1 due to the regularization property of the dropout. Hence there should not always be guaranteed that the test accuracy A2 will increase.

1 reply
10 Jun▶ Angryrou
goldpiggy
Hey @Angryrou, yes you supposition is right! We cannot promise there is always an increase of test accuracy. However, what dropout ultimately does is to overcome “Overfitting” and stabilize the training. Once your model is overfitting (like the mlp example), dropout can help.

In practice, we usually use a dropouts of 0.2 - 0.5 ( 0.2 recommended for input layer). Too low dropout cannot have regularization effect, while a too high dropout may lead to underfitting.

1 reply
11 Jun▶ goldpiggy
Angryrou
Thanks for the reply!

Could you explain more on how the dropout stabilize the training? I do find it more stable in terms of the variance of the activations in each hidden layer (from the exercise 3), but cannot figure out the reason behind. Any intuitive explanation or references should be very helpful!

1 reply
11 Jun▶ Angryrou
goldpiggy
Hi @Angryrou, here are some intuitions. We pick random neurons to dropout at each epoch, so the layer won’t really too much on one or two specific neuron (i.e., all other neurons have a closed to zero weights)

Suppose we have 4 neurons at one layer, A, B, C, D. With some random unexpected initialization, it is possible that the weights of A & B are closed to zero. Imagine the following two situations:

If we don’t have dropout, this layer only relay on neurons C & D to transform information to the next layer. So the neurons A & B might be too “lazy” to adjust its weight since there are C & D.

If we set dropout = 0.5, then at each epoch, two neurons are dropped randomly. So it is possible that both C and D are dropped, so A & B have to transform information and adopt the gradients weights adjustment.

1 reply
11 Jun▶ goldpiggy
Angryrou
Thanks again for the reply. However, I still have some follow up issues unclear:

Without the dropout in your example, only 2 of the 4 neurons take effects mostly. In other words, the model may have less representation property (due to smaller capacity in the model) without using dropout. So my understanding from your example is: a model with more capacity should be more stable than a model with less capacity. Is my statement correct?

I do not think A & B will be too “lazy” to adjust weights. Assume the model is y = f(X) = A * x_1 + B * x_2 + C * x_3 + D * x_4, the gradient on A is dl/dy * dy/dA and the dy/dA = x_1, so the adjustment on A is mainly rely on the feature x_1 instead of the value of A.

1 reply
12 Jun▶ Angryrou
goldpiggy
Hi @Angryrou,

Without the dropout in your example, only 2 of the 4 neurons take effects mostly. In other words, the model may have less representation property (due to smaller capacity in the model) without using dropout. So my understanding from your example is: a model with more capacity should be more stable than a model with less capacity. Is my statement correct?

We don’t dropout during inference, so we still have 4 neurons to keep the original capacity.

I do not think A & B will be too “lazy” to adjust weights. Assume the model is y = f(X) = A * x_1 + B * x_2 + C * x_3 + D * x_4 , the gradient on A is dl/dy * dy/dA and the dy/dA = x_1 , so the adjustment on A is mainly rely on the feature x_1 instead of the value of A.

Your intuition is right! Theoretically it depends on the input features and the activation function. So the dropout method “force” the neurons A&B to learn if their features are not as effective as the other neurons’ features.

1 reply
12 Jun▶ goldpiggy
Angryrou
Thank you. You mentioned

what dropout ultimately does is to overcome “Overfitting” and stabilize the training.

Do you have any recommended papers or blogs that have theoretical support about how dropout can help stabilize the training (e.g., avoid gradient explode and varnish)? I find this is very interesting to explore.

Cheers

1 reply
12 Jun
goldpiggy
 sciencedirect.com

The dropout learning algorithm
Dropout is a recently introduced algorithm for training neural networks by randomly dropping units during training to prevent their co-adaptation. A m…


https://papers.nips.cc/paper/4882-dropout-training-as-adaptive-regularization.pdf 1 reply
12 Jun▶ goldpiggy
Angryrou
Thank you :slight_smile:

24 Jun
Steven​Jokes
I noticed there isn’t test loss. Why?
I have read as following.
datascience.stackexchange.com
N.IT
What is the relationship between the accuracy and the loss in deep learning?
neural-network, deep-learning, keras, tensorflow
asked by N.IT on 09:08AM - 14 Dec 18 UTC

https://kharshit.github.io/blog/2018/12/07/loss-vs-accuracy 1 reply
25 Jun
Steven​Jokes
I noticed that nn.Flatten() haven’t mentioned.
https://pytorch.org/docs/master/generated/torch.nn.Flatten.html
Why do we need to nn.Flatten() first?

25 Jun
Steven​Jokes
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

1 reply
26 Jun▶ StevenJokes
anirudh
You need to reset params before you start training again.
Otherwise you are just updating already trained params.

Also nn.Flatten() is needed to flatten the image into a single vector (28*28=784) for the input of the linear layer.

Cam you check again 4.6.5 and 4.6.4.3 look similar here.

1 reply
26 Jun
Steven​Jokes
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

26 Jun▶ StevenJokes
goldpiggy
Hi @StevenJokes, for your question:

I noticed there isn’t test loss. Why?

For any ML problem, we ultimately care about the model performance through evaluation metrics (such as accuracy). However, lots of metrics are not differentiable, hence we use the loss functions to approximate them.

1 reply
26 Jun▶ goldpiggy
Steven​Jokes
We use loss function just for training’s Backpropagation, and we don’t need to train anymore when we are in test. Similiarly, we just care the final scores of exam instead of the concrete answers.
Do I understand it rightly?

6 Jul
S_​X
@goldpiggy In this discussion thread, you refer to “model capacity”. What exactly does it mean?

6 Jul
Nish
I tried swapping the dropout probabilities for Layers 1 and 2, and did not notice much of a change:

image
Is there an error in my implementation? Or is this because of the simple nature of the dataset (eg I note that dropout doesn’t help too much over the standard implementation in the first place) and would I normally notice some difference? Thanks!

1 reply
6 Jul▶ Nish
goldpiggy
Hi @Nish, great question! It may be hard to observe a huge loss/acc difference if the network is shallow and can converge quickly. As you can find in the original dropout paper (http://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf) as well, the improvement with dropout on MNIST is less than 1%.

21 Jul
RaphaelCS
Hi, I’ve noticed that we enable Dropout while training, and we may disable it while doing inference. But whether we enable or disable Dropout while testing? If I am not mistaken, in our implementation, we have allowed Dropout in the test. Is that right?

Also, I have another question. We implement Dropout just by zeroing some elements in the forward stage, but whether the weights corresponding to those zeros update in the backward stage?

1 reply
21 Jul
Steven​Jokes
 RaphaelCS:
Dropout in the test

We don’t allow Dropout in the test.
The first answer in
How does dropout work during testing in neural network? can explain well.
However, there are two main reasons you should not use dropout to test data:

Dropout makes neurons output ‘wrong’ values on purpose
Because you disable neurons randomly , your network will have different outputs every (sequences of) activation. This undermines consistency.
the weights corresponding to those zeros will still update, because the weight not only corresponds to those zeros, but also other not zeros in the same hidden layer.
1 reply
22 Jul▶ StevenJokes
RaphaelCS
Thanks for your answer. But I’m still wondering for something:

How we disable Dropout in testing in the implementation of this book, either from scratch or using high-level API? I’ve found in the implementation from scratch that during training and testing we use the same net, whose attibute is_training is to True. Also, in the implementation using high-level API, I didn’t find the difference of Dropout layer while training and testing.
So could you please tell me where in the code did we disable Dropout while testing?

because the weight not only corresponds to those zeros, but also other not zeros in the same hidden layer.

Is this means each weight corresponds to multiple hidden units? I’m not sure about this, but I think each weight corresponds to a unique input (hidden units) and a unique output in MLP.

1 reply
22 Jul▶ RaphaelCS
Steven​Jokes
After we dropouted, the corresponding hidden layers have already changed. Enable/Disable is confusing.
Test is just a process of calculating a prediction by weights after bp. We don’t need to disable Dropout!
Yes, matrix multiplication is the reason of corresponding to multiple hidden units.
Continue Discussion
