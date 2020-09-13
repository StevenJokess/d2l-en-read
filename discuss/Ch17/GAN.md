

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 19:51:23
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:52:05
 * @Description:
 * @TODO::
 * @Reference:
-->
Continue Discussion
10 replies
28 Jul
Donald_​​Smith
Greetings,

I really appreciated the simplicity of this GAN demonstration. Is there a way to extract the contents of net_G and compare them with A and b that were defined at the start, to show that the generator has effectively deduced the parameters used to set up the “real” data? I tried print(net_G[0]), but it just says Dense(2 -> 2, linear). How do I get it to show the actual numbers? I know that for large layers and convnets and so forth, the numbers get enormous, and not easy to simply look at and interpret, but I would think that this example would allow one to close the loop and show that the results of the training actually do match the inputs. The scatter plot shows that, graphically, but I’d love to see the numbers, too.

Thank you,

Don

28 Jul
Donald_​​Smith
Quick update. I figured out print(net_G[0].weight.data()) and print(net_G[0].bias.data()), but while the bias data looked relatively close to b, the weights looked nothing like A, so I think I am still not understanding something. Thanks for any insight you can provide.

Yours,

Don

1 reply
29 Jul▶ Donald_Smith
goldpiggy
Hi @Donald_Smith, great question! The bias are closed because the “Real” data was generated following a Normal distribution, which lead to a zero intercept at y axis.

However, as the weights of net_G apply to the noise Z (rather than like the biases of net_G apply to “1”), so we should expect net_G(Z) is close to the “data”.

Let me know if that makes sense to you!

1 reply
29 Jul▶ goldpiggy
Donald_​​Smith
Almost. I feel like I’m close, but not quite there.

As presented, I can see the graph with the blue and orange dots on them, and see intuitively that the distribution of orange dots is “like” the blue ones (and the animation wonderfully shows how it becomes “more like” with the training). I would like to take that visual intuition and be more quantitative about it. If I am reading this correctly, the blue dots are created by taking 2000 points from a normal gaussian distribution, treating them as X/Y coordinates, and then transforming them through a matrix multiplication and a vector translation to get the stretch and spread in the plot (although only 100 points of the 1000 are plotted).

The train function then generates 100 pairs of normal gaussian numbers (Z) and passes them to net_G, to make “fake_X”, which is then plotted as orange dots. If the orange dots match the blue dots, then it should be the same transformation (or at least not different).

What I would like to do, and I have very little experience with mxnet, is extract exactly what numbers net_G is using to go from Z to fake_X, so I can compare, quantitatively, those numbers with A and b that were used back to take “X” to “data” at the beginning. Clearly, net_G[0].weights.data() are not those numbers, so, how do I get those numbers?

Or am I still not understanding what it’s doing? :slight_smile: In short, I would like to know exactly what the line fake_X = net_G(Z).asnumpy() is doing.

Thanks for your help!

Don

1 reply
29 Jul▶ Donald_Smith
goldpiggy
Hi @Donald_Smith, we are not learning A but learning the data. (Maybe we should use another representation like “fake_data” rather than “fake_X”.)

As a result, you can compare the following:

image
29 Jul
Donald_​​Smith
Oh. Oh! I think I get it now. net_G is not applying the same transformation (* 2x2 matrix + 2x1 vector), it’s figuring out some kind of transformation that makes fake_X look “the most like” data. Is that right? I’ve done NN code to try to figure out linear fit parameters (total overkill, I know – it was an illustration to compare how a NN would do it compared with a least squares matrix transposition). I was interpreting this as trying to use loss minimization to drive the transformation parameters to get as close as possible to the original parameters. I got sidetracked by the fact that the first layer was a 2x2 matrix, so I thought by training the weights, it was figuring out a best match for A. But now, if I understand it better now, it’s doing a different transformation from Z to fake_X, and trying to minimize the difference between “data” and fake_X.

Thanks – I’m trying to understand what’s going on inside the “black box”. Am I closer? :slight_smile:

Yours,

Don

1 reply
30 Jul
goldpiggy
 Donald_Smith:
But now, if I understand it better now, it’s doing a different transformation from Z to fake_X, and trying to minimize the difference between “data” and fake_X.

That’s correct! It’s always fascinating to go through this thought process, while it is hard to unravel the blackbox if you have a model with billions parameters :wink:

12 Aug
Steven​Jokes
PyTorch version: http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/gan.html
Exercises
An equilibrium exists when the generator catch up with all real data.

12 Aug
Steven​Jokes
Does time.stop() mean that only first epoch time?
github.com/d2l-ai/d2l-en
add how many seconds cost for all training
opened 05:15PM - 11 Aug 20 UTC
StevenJokes StevenJokes
1 reply
12 Aug
goldpiggy
 StevenJokes:
Does time.stop() mean that only first epoch time?

Yes, it times for one epoch.

Continue Discussion

---

https://discuss.d2l.ai/t/generative-adversarial-networks/776

D2L Discussion
Sign Up
Log In
Generative Adversarial Networks
d2l-en
pytorch

StevenJokes
20d
http://d2l.ai/chapter_generative-adversarial-networks/gan.html 4




created
20d
last reply
4d
3
replies
61
views
2
users
1
link
3
11 DAYS LATER

StevenJokes
1
9d
http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/gan.html

The loss of discriminator is better to be bigger.
The loss of generator is better to be smaller.

I can’t figure out a question: https://stackoverflow.com/questions/63763835/why-is-my-loss-of-generator-0-why-is-loss-of-discriminator-bigger-than-generato
Anyone helps me?




goldpiggy
5d
Hi @StevenJokes, we want to minimize both loss. Can you specify where do you see the following augment? Thanks

The loss of discriminator is better to be bigger.
The loss of generator is better to be smaller.




StevenJokes
4
4d
GAN:
image
image
1009×422 28.7 KB

DCGAN:
image
image
891×429 30.5 KB

I forgot the book name… Too many books I have read…
I found 《深入浅出PyTorch：从模型到源码》writen by 张校捷
 GitHub

zxjzxj9/PyTorchIntroduction
《深入浅出 PyTorch——从模型到源码》源代码和勘误（见Issues）. Contribute to zxjzxj9/PyTorchIntroduction development by creating an account on GitHub.


GAN: https://github.com/zxjzxj9/PyTorchIntroduction/blob/master/Chapter4/gan.py
4.7 生成模型：VAE和GAN
可以看到，生成器的损失函数的目的是让生成器的输出在判别器上输出的概率尽可能大，判别器的损失函数目的是让真实数据在判别器上输出的概率尽可能大（见式（4.11）第一项），而让生成器生成的输出在判别器上的概率尽可能小（见式（4.11）第二项）

LossD = -(logD(x) +log(1-D(G(z))) (4.11)

Do you understand Chinese? Just keep same to the passage.
I have tried google translation to English, which is understandable for me.
BTW, recommend a chrome extension https://chrome.google.com/webstore/detail/沙拉查词-聚合词典划词翻译/cdonnmffkdaoajfknoeeecmchibpmkmg/reviews?hl=en
It is convient to translate Chinese to Engish and English to Chinese.
image
image
1594×395 106 KB
Will your team give me an AI job now?
I really need to learn AI from working with you…
Would you like to train me…



Hello! Looks like you’re enjoying the discussion, but you haven’t signed up for an account yet.

When you create an account, we remember exactly what you’ve read, so you always come right back where you left off. You also get notifications, here and via email, whenever someone replies to you. And you can like posts to share the love. heartpulse

Sign Up Remind me tomorrowno thanks
Suggested Topics
Topic	Replies	Activity
Installation
pytorch
13	4d
Attention Mechanisms
pytorch
2	9h
Data Preprocessing
pytorch
9	6d
Softmax Regression from Scratch
pytorch
14	19d
Concise Linear Regression
pytorch
20	11h
Want to read more? Browse other topics in
pytorch
 or view latest topics.
