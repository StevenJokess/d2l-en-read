

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-26 21:09:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 20:18:13
 * @Description:
 * @TODO::
 * @Reference:
-->
ULMFiT
In contrast to the behemoths of BERT and GPT-2, ULMFiT is based on a good old RNN. No Transformer in sight, just the AWD-LSTM, an architecture originally created by Stephen Merity. Trained on the WikiText-103 dataset, it has proven to be amendable to transfer learning, and despite the old type of architecture, has proven to be competitive with BERT and GPT-2 in the classification realm.

While ULMFiT is, at heart, just another model that can be loaded and used in PyTorch like any other, its natural home is within the fast.ai library, which sits on top of PyTorch and provides many useful abstractions for getting to grips with and being productive with deep learning quickly. To that end, we’ll look at how to use ULMFiT with the fast.ai library on the Twitter dataset we used in Chapter 5.

We first use fast.ai’s Data Block API to prepare our data for fine-tuning the LSTM:

data_lm = (TextList
           .from_csv("./twitter-data/",
           'train-processed.csv', cols=5,
           vocab=data_lm.vocab)
           .split_by_rand_pct()
           .label_from_df(cols=0)
           .databunch())
This is fairly similar to the torchtext helpers from Chapter 5 and just produces what fast.ai calls a databunch, from which its models and training routines can easily grab data. Next, we create the model, but in fast.ai, this happens a little differently. We create a learner that we interact with to train the model instead of the model itself, though we pass that in as a parameter. We also supply a dropout value (we’re using the one suggested in the fast.ai training materials):

learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.3)
Once we have our learner object, we can find the optimal learning rate. This is just like what we implemented in Chapter 4, except that it’s built into the library and uses an exponentially moving average to smooth out the graph, which in our implementation is pretty spiky:

learn.lr_find()
learn.recorder.plot()
From the plot in Figure 9-12, it looks like 1e-2 is where we’re starting to hit a steep decline, so we’ll pick that as our learning rate. Fast.ai uses a method called fit_one_cycle, which uses a 1cycle learning scheduler (see “Further Reading” for more details on 1cycle) and very high learning rates to train a model in an order of magnitude fewer epochs.

ULMFiT learning rate plot
Figure 9-12. ULMFiT learning rate plot
Here, we’re training for just one cycle and saving the fine-tuned head of the network (the encoder):

learn.fit_one_cycle(1, 1e-2)
learn.save_encoder('twitter_encoder')
With the fine-tuning of the language model completed (you may want to experiment with more cycles in training), we build a new databunch for the actual classification problem:

twitter_classifier_bunch = TextList
           .from_csv("./twitter-data/",
           'train-processed.csv', cols=5,
           vocab=data_lm.vocab)
           .split_by_rand_pct()
           .label_from_df(cols=0)
           .databunch())
The only real difference here is that we supply the actual labels by using label_from_df and we pass in a vocab object from the language model training that we performed earlier to make sure they’re using the same mapping of words to numbers, and then we’re ready to create a new text_classifier_learner, where the library does all the model creation for you behind the scenes. We load the fine-tuned encoder onto this new model and begin the process of training again:

learn = text_classifier_learner(data_clas, drop_mult=0.5)
learn.load_encoder('fine_tuned_enc')

learn.lr_find()
learn.recorder.plot()

learn.fit_one_cycle(1, 2e-2, moms=(0.8,0.7))
And with a tiny amount of code, we have a classifier that reports an accuracy of 76%. We could easily improve that by training the language model for more cycles, adding differential learning rates and freezing parts of the model while training, all of which fast.ai supports with methods defined on the learner.

What to Use?
Given that little whirlwind tour of the current cutting edge of text models in deep learning, there’s probably one question on your mind: “That’s all great, but which one should I actually use?” In general, if you’re working on a classification problem, I suggest you start with ULMFiT. BERT is impressive, but ULMFiT is competitive with BERT in terms of accuracy, and it has the additional benefit that you don’t need to buy a huge number of TPU credits to get the best out of it. A single GPU fine-tuning ULMFiT is likely to be enough for most people.
