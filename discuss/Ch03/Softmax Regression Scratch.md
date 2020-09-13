

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:13:12
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:13:55
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_linear-networks/softmax-regression-scratch.html
 * @TODO::
 * @Reference:
-->
3 replies
4 Sep
gpk​2000
The cross entropy loss is given by the below formula according to this

image

But in the code below is the same thing happening?

def cross_entropy(y_hat, y):
    return - np.log(y_hat[range(len(y_hat)), y])
Am I missing something?

2 replies
4 Sep▶ gpk2000
Steven​Jokes
@gpk2000
You can test by your own next time…
Just try to input some numbers to see the outputs…

And use the search button as possible.
image
http://preview.d2l.ai/d2l-en/master/chapter_appendix-mathematics-for-deep-learning/information-theory.html?highlight=cross%20entropy%20loss
image
.mean() is for n*1 matrix?
@goldpiggy

5 Sep▶ gpk2000
osama​Gkhafagy
What this snippet of code is doing is exactly the same as the formula above. This code uses the index of the true y to fetch the predicted value y_hat and then taking the log to those predicted values for all examples in a minibatch

Continue Discussion

---

Continue Discussion
14 replies
18 Jun
Steven​Jokes
In 3.6.4, y_hat[range(len(y_hat)), y]
What did y_hat[y] mean?

print(y_hat[y])
IndexError Traceback (most recent call last)
in
----> 1 print(y_hat[y])

IndexError: index 2 is out of bounds for dimension 0 with size 2

And I found other styles:

def cross_entropy(y_hat,y):
	return -torch.log(y_hat.gather(1,y.view(-1,1)))
What differences?

18 Jun
Steven​Jokes
In class Accumulator::
self.data = [a+float(b) for a, b in zip(self.data, args)]
What is the meaning of a+float(b)?
It couldn’t be better,
if you can combine these to explain what happened behind
metric.add(float(l)*len(y), float(accuracy(y_hat, y)), len(y))
and
metric.add(l_sum, accuracy(y_hat, y), y.numpy().size)

18 Jun
Steven​Jokes
3.6.9
Nothing happened!? And, max number of 64float is 2^1024 - 2^(1023-52).
So e^1024 will overflow？
X = torch.tensor([[50., 51., 52.], [54., 55., 56.]])
X_prob = softmax(X)
X_prob
tensor([[0.0900, 0.2447, 0.6652],
[0.0900, 0.2447, 0.6652]])

log(0) will error!
Use RELU to replace softmax?
In medical diagnosis, we may more need to find all possible result to avoid condition worsening.
A large vocabulary will make every word’s probabilty near to 0.
5 Jul
Kushagra_​​Chaturvedy
In the train_epoch_ch3 function, in the line metric.add(float(l)*len(y), float(accuracy(y_hat, y)), len(y))

I don’t understand the reason why we need to multiply the loss l with the length of the label tensor. Since we are accumulating the loss wouldn’t it be fine if don’t multiply it?

1 reply
6 Jul▶ Kushagra_Chaturvedy
anirudh
Hi @Kushagra_Chaturvedy the reason for multiplying with len(y) is that when using torch’s built-in loss function i.e nn.CrossEntropyLoss, it reduces the loss to mean by default. See the default parameter value for reduction=‘mean’. We in our case want to have the sum. Hence multiplying by len(y) gives us the sum.
This is actually used in concise softmax implementation. you can check that chapter.

1 reply
7 Jul▶ anirudh
Kushagra_​​Chaturvedy
Thanks for the reply @anirudh. A couple more things, why are we accumulating the sum of the loss? Wouldn’t it make more sense to find the mean loss from the loss tensor and then accumulate that instead of accumulating the sum of the values in the loss tensor? Also, if I defined the updater as an instance of torch.optim.SGD, then pt_optimizer would return True right? And in that case how will the calculated loss ‘l’ be a scalar (since in the pt_optimizer=True condition, we calculate l.backward() instead of l.sum().backward() which would imply that l is a scalar )

23 Jul
lokeshkvn
Hi everyone,

I want to know why we have not used with torch.no_grad(): while calculating the loss in cross_entropy() function or while evaluating the model. As in the linear regression from scratch we have used it. Why we are not using it in this chapter?

I think we should use

train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
with torch.no_grad():
   test_acc = evaluate_accuracy(net, test_iter)
   animator.add(epoch + 1, train_metrics + (test_acc,))
in train_ch3() function.

Please let me know.
Thank you.

1 reply
24 Jul
goldpiggy
 lokeshkvn:
torch.no_grad():

Hi @lokeshkvn, great question. We use net.eval() in evaluate_accuracy() function, which will be set to evaluation mode. https://discuss.pytorch.org/t/model-eval-vs-with-torch-no-grad/19615

def evaluate_accuracy(net, data_iter):  #@save
    """Compute the accuracy for a model on a dataset."""
    if isinstance(net, torch.nn.Module):
        net.eval()  # Set the model to evaluation mode
    metric = Accumulator(2)  # No. of correct predictions, no. of predictions
    for _, (X, y) in enumerate(data_iter):
        metric.add(accuracy(net(X), y), d2l.size(y))
    return metric[0] / metric[1]
1 reply
25 Jul
Steven​Jokes
 goldpiggy:
# No. of correct predictions, no. of predictions

What does " No. of correct predictions, no. of predictions" mean?

1 reply
27 Jul▶ StevenJokes
goldpiggy
Number of correct predictions, number of total predictions.

25 Aug
Gavin
Hi all, is there anyone encounter the issue – “The kernel appears to have died. It will restart automatically.” when running train_ch3? I checked it is the code below in the train_ch3 causes the issue:

animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                        legend=['train loss', 'train acc', 'test acc'])
Does any one know the reason for this issue? Any help would be appreciated.

1 reply
25 Aug
Steven​Jokes
 Do these before you ask! d2l-en
If you have any questions, you should do these first. 0. Read again your code and contrast with code given. Read the below discussions including all tabs “mxnet”/“pytorch”/“tensorflow” Try to Google it & Stackoverflow it. Update all your package, for example, maybe you need:), if we forget to update the version number : pip uninstall d2l pip install d2l -U -i https://pypi.python.org/simple Use the search button to find the related context. Book: [image] Discuss: [image] Old discussion:…

@Gavin
Have you googled it?
You can try pip uninstall numpy, then pip install -U numpy from https://www.youtube.com/watch?reload=9&v=RhpkTBvb-WU
If you have any other questions, try to solve it by googling it.
If you still have problem, then publish all your code or give me a github URL, and more informations of your environment.
1 reply
25 Aug▶ StevenJokes
Gavin
@StevenJokes Thanks a lot. It solved my issue. It turns out my numpy version was 1.18.1, after I updated it to 1.19.1, the codes work perfectly.

Btw, I did google it before I asked, but couldn’t find the right answer. :rofl:

1 reply
25 Aug▶ Gavin
Steven​Jokes
Give the helpful reply a love. It will make forum more active. :blush:

Continue Discussion

---

4 replies
18 Aug
6cyu
I have a question related to coding with tensorflow…
in the function train_epoch_ch3, the object updater has method “apply_gradients”
however, i found that this method is not defined in the Updater class…how can it be?
thank you…

1 reply
19 Aug▶ 6cyu
nmnduy
I think that’s only the case when the updater is tf.keras.optimizers.Optimizer . In this chapter, we use a custom updater.

27 Aug
tinkuge
In train_epoch_ch3, what is net.trainable_variables referring to? The net function defined earlier in 3.6.3 does not have a trainable_variables field in it.

1 reply
28 Aug▶ tinkuge
Morteza
net.trainable_variables is for the case you use Keras network and would be used in section 3.7 . I agree that it is a bit confusing to write train_epoch_ch3 in a way to work with both sections 3.6 and 3.7

Continue Discussion
