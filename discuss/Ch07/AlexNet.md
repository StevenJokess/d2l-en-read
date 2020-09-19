

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:34:33
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:34:41
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_convolutional-modern/alexnet.html
 * @TODO::
 * @Reference:
-->


7 replies
12 Jun
jsouza
Hello.
what must I change in the Alexnet model for working at images with dimensions of 28x28? the kernel size?

1 reply
12 Jun▶ jsouza
goldpiggy
Hi @jsouza, LeNet (http://d2l.ai/chapter_convolutional-neural-networks/lenet.html) is designed for 28x28 size image.

12 Jun
jsouza
Thank you so much for your feedback @goldpiggy. I will verify the LeNet model.

My question is based on the experiment (private) that applied the Alexnet model without modifications at a 28x28 size image. In this experiment, the model has been closing at 10% accuracy. I have solved it by resizing the image for 224X24 size. I also have solved it by initializing the weight and bias with normal distribution, where mean = 0.0 and standard deviation equal to 0.01. What do other modifications can be done?

I’m sorry my English, I am learning.

1 reply
13 Jun▶ jsouza
goldpiggy
Hi @jsouza, great questions. There are tons of tricks/models that we talked about through the whole books. No hurries, you will learn them gradually by using more advanced architectures, more advanced optimization strategy etc.

1 reply
13 Jun
jsouza
Hello @goldpiggy, thank you again. Also, the site’s information, could you indicate me to papers that talk about the subject?

1 reply
13 Jun▶ jsouza
goldpiggy
Here are all the reference papers we used through the book. https://d2l.ai/chapter_references/zreferences.html

20 Jun▶ goldpiggy
Dummy_​​Account
Hello Ma’am, firstly, thank you so much to you and your team for such a great and insightful content on CNN. I am new to the subject and was stuck on the 2nd question given in the exercises for 7.1. That is, to design an AlexNet model that could work directly on 28*28 images. I would be really helped if you could provide any sort of help on this question, a hint maybe.
Thanks.

Continue Discussion
