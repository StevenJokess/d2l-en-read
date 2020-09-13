Continue Discussion
17 replies
5 Aug
Steven​Jokes
PyTorch version: http://preview.d2l.ai/d2l-en/master/chapter_generative-adversarial-networks/dcgan.html

I noticed that c065c0e2593b8b161a2d7873e42418bf6a21106c in
image

And all DATA_HUB have such numbers.
Where did these numbers come from? @goldpiggy
How can I produce these numbers
1 reply
7 Aug
Steven​Jokes
image

Why my image is not so clear?
7 Aug
goldpiggy
 StevenJokes:
And all DATA_HUB have such numbers.
Where did these numbers come from? @goldpiggy
How can I produce these numbers

Hey @StevenJokes, great question! This is the hash code for the dataset. Please see more details here.

(BTW the pokemon dataset will be deprecated in the future because of legal constraints. :()

1 reply
8 Aug▶ goldpiggy
Steven​Jokes
hashlib.sha1() SHA1 hash. I got it .hashlib

read file:
                data = f.read(1048576) // MAX rows in EXCEL
                if not data:     // test if file is empty
                    break
1,048,576 rows—— a string (in text mode)= 2^20 rows = 2M rows
After 2007, EXCEL have 1,048,576 rows and end at XFD.
Problem: Excel CSV. file with more than 1,048,576 rows of data
How to fix it: Lazy Method for Reading Big File in Python?
Why 1,048,576 rows?:haven’t found yet.

fp.extractall(base_dir) //extract file

os.path.join(base_dir, folder) if folder else data_dir
add folder or data_dir to current path?
I noticed that BASE_DIR is used more fruently. Maybe we should change to it?
image
Privacy:

Despite being named Pokémon Database, currently we do not offer any database or API (Application Programming Interface) for use, though it may be something we offer in the future.
It should be noted here that we are unable to make a Pokémon app as Nintendo gets them taken down from all app stores.

Download:https://peltarion.com/knowledge-center/documentation/terms/dataset-licenses/pokemon-images
I noticed it is CC-BY 4.0, or was?. Where is the legal constraints?
I look all dataset legal constraints searched, and I didn’t find any information about legal constraints of dataset. :sob: How can I confirm whether a dataset can be used for public.

Awesome Public Datasets on ML

9 Aug
Steven​Jokes
conjuct:

image

separate：
image
Why didn’t the discriminator loss go up and the generator go down?
Why isn’t same as the 17.1 losses’ going together finally?

I think there is a bug:
image
After switching,
image

issue: https://github.com/d2l-ai/d2l-en/issues/1326
new PR:https://github.com/d2l-ai/d2l-en/pull/1335

1 reply
12 Aug
Steven​Jokes
But why is /2 + 0.5 , rather than other ways to normalize?
image
 GitHub

d2l-ai/d2l-en
Interactive deep learning book with code, math, and discussions. Available in multi-frameworks. - d2l-ai/d2l-en

Why we need , 1, 1

image
2 replies
12 Aug
goldpiggy
 StevenJokes:
Why we need , 1, 1

Hey @StevenJokes. In MXNet, the dimension is like (batch_size, channel, height, width).

12 Aug
goldpiggy
 StevenJokes:
But why is /2 + 0.5 , rather than other ways to normalize?

We stated that " we normalize the data with 0.5 mean and 0.5 standard deviation to match the value range" in the earlier text.

1 reply
13 Aug
Steven​Jokes
 goldpiggy:
we normalize the data with 0.5 mean and 0.5 standard deviation to match the value range

@goldpiggy
Do you mean this?

image

Got you.
16 Aug
Steven​Jokes
I’m not sure about DCGAN’s Discriminator‘s structure:
github.com/pytorch/tutorials
DCGAN's Discriminator : lack of nn.BatchNorm2d(ndf)
opened 12:34PM - 16 Aug 20 UTC
StevenJokes StevenJokes
I'm learning DCGAN by translating mxnet code to pytorch. I'm a newbie. Then in my guess, Discriminator has pretty much structures opposite to...

@goldpiggy, am I right?

21 Aug
Steven​Jokes
image

Why do we need /2?
The code I’m contrasting with is from https://aws.amazon.com/cn/blogs/china/easily-build-pytorch-generative-adversarial-networks-gan/
loss_real为真实样本的鉴别器损失(附加其计算图)，loss_fake为虚假样本的鉴别器损失(及计算图)。PyTorch能够使用+运算符将这些图形组合成一个计算图形。然后我们将反向传播和参数更新应用到组合计算图。
https://blog.csdn.net/m0_46510245/article/details/107741609

28 Aug
yoderj
I have translated this code to PyTorch, and it runs without crashing, but the network fails to train (both losses go way above 1, and the image is garbage).

Can you take a look at this file and see if there are any obvious mistakes?
github.com
yoderj/d2l-en/blob/patch-3/chapter_generative-adversarial-networks/gan.py
# Translated to torch
# https://www.d2l.ai/chapter_generative-adversarial-networks/dcgan.html#discriminator
#
# singularity shell --nv -B /data:/datatainers/pytorch.v1.05.sif
try:
    import d2l.torch as d2l
except ModuleNotFoundError:
    try:
        import d2l
    except ModuleNotFoundError:
        raise ModuleNotFoundError('Could not load d2l. Try pasting '
                                  'https://raw.githubusercontent.com/d2l-ai/d2l-en/master/d2l/torch'
                                  '.py alongside this file.')
import torchvision
import torch
from matplotlib import pyplot as plt
import torch.nn as nn
import numpy as np

#d2l.DATA_HUB['pokemon'] = (d2l.DATA_URL + 'pokemon.zip',
This file has been truncated. show original
Thank you!

1 reply
28 Aug▶ StevenJokes
yoderj
For those who were confused like me about the figure discussion, it ended up being Section 17.1 that had the legend backwards rather than Section 17.2. But both sections are now correct in the main text.

1 reply
29 Aug
Steven​Jokes
OK. I’ll learn.

 yoderj:
it ended up being 17.1 that had the legend backwards rather than 17.2

What is “it” you talked about?

Do you have ipynb file? It is easy to watch the result of every step.
I tried to translate but failed. You can take a look at this PR.
github.com/d2l-ai/d2l-en
[Completed][pytorch][no response to train, need help!] add DCGAN
d2l-ai:master ← StevenJokes:DCGAN
opened 07:25AM - 08 Aug 20 UTC
StevenJokes StevenJokes
+238 -17
1 reply
29 Aug▶ yoderj
Steven​Jokes
epoch is too small?
Why so slow?

You need to train more epochs by GPU.
It is quicker.

And thanks for your code BTW.
I think I already figure DCGAN out.
image
29 Aug▶ StevenJokes
yoderj
(Reply to this post)

Thank you! I found your ipynb notebook and converted it to a .py file. It is working great. I hope to make a cleaned up version of my file (I updated mine on the link I sent earlier to include GPU, and I think some of my arguments are named more cleanly) that still produces good results. This could be days or months before that happens, though.

What is “it” you talked about?

I’ve updated my post to include a link to the post I was following. For some reason, the software does not make it clear what you are linking to.

I don’t have Jupyter Notebook installed on my local machine – perhaps I should install that!

I’m trying to prepare for a pull request myself, and I’m running with GPU. I’ve updated the code I linked earlier (sorry, ran out of links for this post) to include GPU support. I followed d2l.ai’s chapter on GPUs in doing this.

(And now, a reply to the post right before this one):


image 585x500, 50%
Can you share the link to the code you used to create this figure? I suspect it is your code (not mine), but I’m confused as to why your code stops after a few iterations. By the way, I really like your GPU code. It is cleaner than mine. I’m going to try to make a clean version of my code that borrows heavily from yours.

1 reply
30 Aug▶ yoderj
Steven​Jokes
It was my code I forget to add image
The code didn’t not stop.
Only running. I’m so excited to tell you and thanks for your code too.
Now you can check http://preview.d2l.ai/d2l-en/PR-1309/chapter_generative-adversarial-networks/dcgan.html
It runs well.
@yoderj
If you like to research, my GAN repo which records my all code have tried:
https://github.com/StevenJokes/d2l-en-read/tree/master/chapter-generative-adversarial-networks
Free to share with you.
And I created a discussion for DCGAN pytorch.
We can talk more about the code there.
Deep Convolutional Generative Adversarial Networks

Continue Discussion
