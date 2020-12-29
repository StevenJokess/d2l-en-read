

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 17:40:19
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 17:27:44
 * @Description:
 * @TODO::
 * @Reference:
-->
Few-Shot Learning[1]

In 2015, Brendan Lake et al.[2] published a paper that challenged modern machine learning methods to be able to learn new concepts from one or a few instances of that concept. As an example, Lake suggested that humans can learn to identify “novel two-wheel vehicles” from a single picture (e.g. as shown on the right), whereas machines cannot generalize a concept from just a single image. (Humans can also draw a character in a new alphabet after seeing just one example). Along with the paper, Lake included a dataset of handwritten characters, Omniglot, the “transpose” of MNIST, with 1623 character classes, each with 20 examples. Two deep learning models quickly followed with papers at ICML 2016 that used memory-augmented neural networks and sequential generative models; showing it is possible for deep models to learn to learn from a few examples, though not yet at the level of humans.

by leveraging prior experience!“few-shot learning”[3]


[1]: https://bair.berkeley.edu/blog/2017/07/18/learning-to-learn/
[2]: https://www.cs.cmu.edu/~rsalakhu/papers/LakeEtAl2015Science.pdf
[3]: https://cs330.stanford.edu/slides/cs330_intro.pdf
