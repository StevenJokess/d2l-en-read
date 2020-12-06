

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 22:15:37
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 19:48:25
 * @Description:
 * @TODO::
 * @Reference:
-->

https://zhuanlan.zhihu.com/p/87942922

什么是一字多义
以前word2vec是把lookup_table拿出来作为词向量，一个词只对应唯一一个向量，没法区分一字多义。ELMo、BERT是把字的上下文编码，取最后的h（分类层之前）作为字表示，基于分布式语义假设：

One shall know a word by the company it keeps. 我们可以通过一个词出现的语境知道这个词的意思。
所以一个字根据上下文不同会有不同的h，可以表示一字多义的情况

2. h经过分类层后越来越像自己的embedding
要知道embedding有很多个维度，不同维度包含不同的信息，刚才说词的emb对应唯一的向量（编码），可没说是对应富士苹果还是手机苹果，很可能这两种信息都包含在编码里

BERT[2]
paper：BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
arXiv：https://arxiv.org/abs/1810.04805
code：tensorflow、pytorch

Google AI 2018年提出的Bidirectional Encoder Representations from Transformers(BERT)是从大量未标注文本学习得到的语言模型。

模型在机器阅读理解顶级水平测试SQuAD1.1中表现出惊人的成绩：全部两个衡量指标上全面超越人类。在SQuAD2.0上也排名第一。并且还在其他10种不同NLP任务测试中创出最佳成绩，包括将GLUE基准推至80.4％（绝对改进7.6％），MultiNLI准确度达到86.7% （绝对改进率5.6％）等。

BERT的结构是Transformer的Encoder：


BERT
Google’s 2018 Bidirectional Encoder Representations from Transformers (BERT) model was one of the first successful examples of bringing transfer learning of a powerful model to test. BERT itself is a massive Transformer-based model (weighing in at 110 million parameters in its smallest version), pretrained on Wikipedia and the BookCorpus dataset. The issue that both Transformer and convolutional networks traditionally have when working with text is that because they see all of the data at once, it’s difficult for those networks to learn the temporal structure of language. BERT gets around this in its pretraining stage by masking 15% of the text input at random and forcing the model to predict the parts that have been masked. Despite being conceptually simple, the combination of the massive size of the 340 million parameters in the largest model with the Transformer architecture resulted in new state-of-the-art results for a whole series of text-related benchmarks.

Of course, despite being created by Google with TensorFlow, there are implementations of BERT for PyTorch. Let’s take a quick look at one now.

FastBERT
An easy way to start using the BERT model in your own classification applications is to use the FastBERT library that mixes Hugging Face’s repository with the fast.ai API (which you’ll see in a bit more detail when we come to ULMFiT shortly). It can be installed via pip in the usual manner:

pip install fast-bert
Here’s a script that can be used to fine-tune BERT on our Sentiment140 Twitter dataset that we used into Chapter 5:

import torch
import logger

from pytorch_transformers.tokenization import BertTokenizer
from fast_bert.data import BertDataBunch
from fast_bert.learner import BertLearner
from fast_bert.metrics import accuracy

device = torch.device('cuda')
logger = logging.getLogger()
metrics = [{'name': 'accuracy', 'function': accuracy}]

tokenizer = BertTokenizer.from_pretrained
                ('bert-base-uncased',
                  do_lower_case=True)


databunch = BertDataBunch([PATH_TO_DATA],
                          [PATH_TO_LABELS],
                          tokenizer,
                          train_file=[TRAIN_CSV],
                          val_file=[VAL_CSV],
                          test_data=[TEST_CSV],
                          text_col=[TEST_FEATURE_COL], label_col=[0],
                          bs=64,
                          maxlen=140,
                          multi_gpu=False,
                          multi_label=False)


learner = BertLearner.from_pretrained_model(databunch,
                      'bert-base-uncased',
                      metrics,
                      device,
                      logger,
                      is_fp16=False,
                      multi_gpu=False,
                      multi_label=False)

learner.fit(3, lr='1e-2')
After our imports, we set up the device, logger, and metrics objects, which are required by the BertLearner object. We then create a BERTTokenizer for tokenizing our input data, and in this base we’re going to use the bert-base-uncased model (which has 12 layers and 110 million parameters). Next, we need a BertDataBunch object that contains paths to the training, validation, and test datasets, where to find the label column, our batch size, and the maximum length of our input data, which in our case is simple because it can be only the length of a tweet, at that time 140 characters. Having done that, we will set up a BERT model by using the BertLearner.from_pretrained_model method. This passes in our input data, our BERT model type, the metric, device, and logger objects we set up at the start of the script, and finally some flags to turn off training options that we don’t need but aren’t given defaults for the method signature.

Finally, the fit() method takes care of fine-tuning the BERT model on our input data, running on its own internal training loop. In this example, we’re training for three epochs with a learning rate of 1e-2. The trained PyTorch model can be accessed afterward using learner.model.

And that’s how to get up and running with BERT. Now, onto the competition.

[2]: https://0809zheng.github.io/2020/04/27/elmo-bert-gpt.html
[3]: https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch09.html#idm45762347307368
