

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:21:43
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:22:10
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_preliminaries/probability.html
 * @TODO::
 * @Reference:
-->
Continue Discussion
15 replies
1 Jul
zplovekq
I have the question on Exercises 4:Why not just run the first test a second time?
I think it just like roll a die twice. The two result is independent. So by the same formula, i have the result P(H = 1 | D1 = 1, D2 = 1)=0.0015/0.00159985=93%. This is better.
Looking forward for discuss!

1 reply
1 Jul▶ zplovekq
goldpiggy
Hi @zplovekq, $P(H = 1, D1 = 1, D2 = 1)$ is not equal to 0.0015, since in the second test some true positive cases are tested as negative.

2 Jul
zplovekq
Thanks for your reply!~
I compute P(H = 1, D1 = 1, D2 = 1) by this:
P(D1 = 1, D2 = 1 | H = 1)=P(D1 = 1 | H = 1)P(D2 = 1 | H = 1)=11=1 (Because it just like roll a die twice, i think the two diagnosis is independent).
Then P(D1 = 1, D2 = 1)=P(D1 = 1, D2 = 1 | H = 0)P(H = 0) + P(D1 = 1, D2 = 1 | H = 1)P(H = 1)
=0.010.01*(1-0.0015)+1*0.0015=0.00159985
So if the two diagnosis are all 1, then:
P(H = 1 | D1 = 1, D2 = 1)= $P(D1 = 1, D2 = 1 | H = 1)P(H = 1) / P(D1 = 1, D2 = 1)$
= 1 * 0.0015/0.00159985=93%
Thus i think use the first test twice will have more accurate.
Is there any thing wrong?
Thanks!

3 replies
3 Jul
goldpiggy
 zplovekq:
P(D2 = 1 | H = 1)

This is not equal to 1. It is 0.98, as the table says.

3 replies
6 Jul▶ goldpiggy
zplovekq
emm…Thanks for reply!
I mean use the first test twice…So i think P（D2 = 1 | H = 1）= P（D1 = 1 | H = 1）=1…

1 reply
6 Jul▶ zplovekq
goldpiggy
Hi @zplovekq, no problem at all!

7 Aug▶ zplovekq
Hyu​Pete
I have the same thought as you. Still don’t know the answer to this question :thinking:

7 Aug▶ goldpiggy
Hyu​Pete
The question suggests that D2 is the same as D1. So I think P(D2 = 1 | H = 1) = P(D1 = 1 | H = 1) = 1.
Is there any thing wrong with my intuition?

7 Aug
goldpiggy
Hi @HyuPete, please see my previous response.

 goldpiggy:
 zplovekq:
P(D2 = 1 | H = 1)

This is not equal to 1. It is 0.98, as the Table 2.6.2 says.

Let me know if it doesn’t make sense to you.

1 reply
8 Aug▶ goldpiggy
Hyu​Pete
I think I should give more details here so you can help me figure out my problem.
First, let me quote the question here:

In Section 2.6.2.6, the first test is more accurate. Why not just run the first test a second time?
Now here are my thoughts:

In the reading section, it states that D2 is different from D1.

The second test has different characteristics and it is not as good as the first one, as shown in Table 2.6.2.

I totally agree that in the reading section, P(D2 = 1 | H = 1) = 0.98, as you said.

I also want to briefly recall this reading section here:

First time: run first test D1.

Second time: run second test D2.

The the probability of the patient having AIDS given both positive tests is:
P(H = 1 | D1 = 1, D2 = 1) = … = 0.8307.

Go back to the question, it says “run the first test a second time”. So my understanding is D2 is now the same as D1. I think you have misunderstood what I said because of my abuse of notation. So let me correct it:

First time: run first test D1, call this run as D^(1)_1.
Second time: run first test D1 again, call this run as D^(2)_1.
P(D^(1)_1 | H = 1) = P(D^(2)_1 | H = 1) = 1.
And my calculation for this case, “the probability of the patient having AIDS given both positive tests is”:


Since 0.9376 > 0.8307, I think “run the first test a second time” is a better choice here. But the question is “Why not just run the first test a second time?” which leads to a conflict.

Therefore, I still don’t know how to answer this question. Hope you could guide me to it.
Thanks in advance for your help.

2 replies
8 Aug
Steven​Jokes
Probability
“2.6” repeated!
In Section 2.6, the first test is more accurate. Why not just run the first test a second time?
I’m not sure about answer.
Maybe we just want to know Probability by repeating 1000 times’ frequency, according to law of large numbers.
Help me too.:face_with_raised_eyebrow:

13 Aug
Prateek_​​Vyas
np.random.multinomial(10, fair_probs), is not working, its giving result array([ 0, 0, 0, 0, 0, 10], dtype=int64) also the code counts = np.random.multinomial(1000, fair_probs).astype(np.float32)
counts / 1000, Giving results array([ 0., 0., 0., 0., 0., 1000.]). There is a error in np lib of mxnet please check

2 replies
14 Aug▶ Prateek_Vyas
Steven​Jokes
@Prateek_Vyas
You’re right. Win10?
Check: https://discuss.mxnet.io/t/probability-np-random-multinomial/5667/6
issue: https://github.com/apache/incubator-mxnet/issues/15383
Wait for fixing…@mli

15 Aug
goldpiggy
 Prateek_Vyas:
np.random.multinomial(10, fair_probs), is not working, its giving result array([ 0, 0, 0, 0, 0, 10], dtype=int64) also the code counts = np.random.multinomial(1000, fair_probs).astype(np.float32)
counts / 1000, Giving results array([ 0., 0., 0., 0., 0., 1000.]). There is a error in np lib of mxnet please check

Thanks for reporting @Prateek_Vyas. The fix should be on 2.0 roadmap.

17 Aug▶ HyuPete
Hyu​Pete
@goldpiggy Please help me.

Continue Discussion

---
9 replies
12 Jun
Steven​Jokes
def experiment_fig(n, m):
    counts = torch.from_numpy(np.random.multinomial(n, fair_probs, size=m))
    cum_counts = counts.type(torch.float32).cumsum(axis=0)
    estimates = cum_counts / cum_counts.sum(axis=1, keepdims=True)
    d2l.set_figsize((6, 4.5))
    for i in range(6):
        d2l.plt.plot(estimates[:, i].numpy(),
                    label=("P(die=" + str(i + 1) + ")"))
    d2l.plt.axhline(y=0.167, color='black', linestyle='dashed')
    d2l.plt.gca().set_xlabel('Groups of experiments')
    d2l.plt.gca().set_ylabel('Estimated probability')
    d2l.plt.title(f'm (experiment groups) = {m} groups, n (samples) = {n} ')
    d2l.plt.legend()
experiment_fig(30, 1000)
2-6
“2.6” repeated!
In Section 2.6, the first test is more accurate. Why not just run the first test a second time?
I’m not sure about answer.
Maybe we just want to know Probability by repeating 1000 times’ frequency, according to law of large numbers. :roll_eyes:
1 reply
13 Jun
alicanb
Couple things:

You can import Multinomial directly from torch.distributions. ie. from torch.distributions import Multinomial

distribution.sample() takes a sample_size argument. So instead of sampling from numpy and converting into pytorch you can simply say Multinomial(10, fair_probs).sample((3,)) (sample_shape needs to be tuple).

1 reply
14 Jun▶ alicanb
anirudh
Thanks @alicanb. We have addressed your suggestions and updated the section in this commit

16 Jun
Emanuel_​​Afanador
Hello, Preformatted text I have a question about question 3 (Markov Chain), I’m not sure about my answer:

P(A,B,C) = P(C|B,C)P(B,C) = P(C|B,A)P(B|A)P(A)

as A,B,C states have Markov chain property, P(C|B,A) = P(C|B)

P(A,B,C) = P(C|B)P(B|A)P(A)

thanks in advance :grinning:

1 reply
18 Jun▶ Emanuel_Afanador
goldpiggy
Hi @Emanuel_Afanador, since 𝐵 only depends on 𝐴, and 𝐶 only depends on 𝐵, then

$P(A, B, C) = P(C | A, B) * P(A, B) = P(C | A, B) * [P(B | A) * P(A)] $ .

23 Jun▶ StevenJokes
JohnG
Wonder anyone has encountered the same problem as me related to the code above. In version 0.7 of Dive into Deep Learning, the code works as shown above, with all the probabilities converging to the expected value of 1/6. However, with code in version 0.8.0 of the same book, the curves (see the image on the right) do not look right. Both curves were obtained by running the code from the book(s) without any changes and ran on the same PC. So there might be bugs in version 0.8.0 of the book? Thanks!

v0.7 and v08
1 reply
24 Jun▶ JohnG
Steven​Jokes
Maybe it is just a coincidence that almost 90 groups of experiments is “die = 6”？
It would be more clear if you counts / 1000 # Relative frequency as the estimate.

24 Jun
ness​001
In L2/5 Naive Bayes, in terms of Nvidia Turing GPUs, why Alex said adding more silicons is almost free for Nvidia?

1 reply
26 Jun
goldpiggy
 ness001:
adding more silicons is almost free for Nvidia

Hi @ness001, great question! Check here for more details about GPUs http://d2l.ai/chapter_computational-performance/hardware.html

Continue Discussion
