

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:31:31
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:32:11
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_recurrent-neural-networks/sequence.html
 * @TODO::
 * @Reference:
-->
3 replies
4 Aug
Shaoxuan-​​Chen
Hi Doctor Li, will there be Tensorflow code posted for Chapter 8 to 17 later? Thank you very much!

1 reply
4 Aug▶ Shaoxuan-Chen
Abhinav_​​Prakash
Yes, we’re working on it.

1 reply
6 Aug▶ Abhinav_Prakash
Shaoxuan-​​Chen
Thank you very much! Appreciate it!

Continue Discussion

---

5 replies
19 Jun
dosssman
Greetings.
Thanks for making this book available.

In the toy example 8.1.2, when creating the dataset, I was wondering if it was normal for both the train set and the test set to be the same. Namely:

train_iter = d2l.load_array((features[:n_train], labels[:n_train]),
                            batch_size, is_train=True)
test_iter = d2l.load_array((features[:n_train], labels[:n_train]),
                           batch_size, is_train=False)
For test_iter, I would have expected something like:

test_iter = d2l.load_array((features[n_train:], labels[n_train:]),
                           batch_size, is_train=False)
Thanks for your time.

1 reply
19 Jun▶ dosssman
goldpiggy
Great catch @dosssman! I believe we don’t need test_iter, as it is never used after being defined.

19 Jun
dosssman
I see. I did not get that far down yet haha.

28 Jun
Steven​Jokes
8.1.2. A Toy Example
features = d2l.zeros((T-tau, tau))
AttributeError : module ‘d2l.torch’ has no attribute ‘zeros’
Then I search http://preview.d2l.ai/d2l-en/PR-1077/search.html?q=d2l.zeros&check_keywords=yes&area=default
No source code:
http://preview.d2l.ai/d2l-en/PR-1077/chapter_appendix-tools-for-deep-learning/d2l.html?highlight=d2l%20zeros#d2l.torch.zeros
I can use ``features = d2l.torch.zeros((T-tau, tau))` to replace now, and try to code next time!
:cold_face:An hour to debug!

1 reply
6 Jul▶ StevenJokes
goldpiggy
Hi @StevenJokes, great try! Your effort will ultimately gain some tractions!

Continue Discussion
