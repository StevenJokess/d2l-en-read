

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 19:55:01
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 19:55:21
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_recommender-systems/deepfm.html
 * @TODO::
 * @Reference:
-->
3 replies
11 Aug
Steven​Jokes
image
https://discuss.d2l.ai/uploads/default/original/1X/0f0d09e9b45df2a1c6b191c903af9edb8ebe8c29.png

Why is my cpu quicker(more examples each second) than your two GPUs?
image
github.com
StevenJokes/d2l-en-read/blob/master/Ch16_Recommender_Systems/16-10.ipynb
{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python37864bitmxnetconda84e8bee5b66a4c7fa50e670e85772498",
   "display_name": "Python 3.7.8 64-bit ('mxnet': conda)"
  }
 },
This file has been truncated. show original
Sorry to miss a number…

1 reply
11 Aug
goldpiggy
 StevenJokes:
Why is my cpu quicker(more examples each second) than your two GPUs?

Hi @StevenJokes, great question! It is always to point out that CPU may outperform GPU on small networks and less dimension feature inputs.

So you may wonder how to define “a small network”? A simple example: a 100 unit MLP trained on 10 input features may count as a small network. Since there are only 100x10 = 1000 parameters that needs to trained in this network. However, if the input feature dimension increases to 1 million, then the neural net may need more compute resources provided by GPU.

1 reply
12 Aug▶ goldpiggy
Steven​Jokes
Sorry to miss a number…
GPU is quicker.

Continue Discussion
