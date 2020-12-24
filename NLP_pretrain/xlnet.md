

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 16:28:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 21:45:12
 * @Description:
 * @TODO::
 * @Reference:
-->

# XLNet: Generalized Autoregressive Pretrain

XLNet 是一个类似 BERT 的模型，而不是完全不同的模型。总之，XLNet是一种通用的自回归预训练方法。它是CMU和Google Brain团队在2019年6月份发布的模型，最终，XLNet 在 20 个任务上超过了 BERT 的表现，并在 18 个任务上取得了当前最佳效果（state-of-the-art），包括机器问答、自然语言推断、情感分析和文档排序。

作者表示，BERT 这样基于去噪自编码器的预训练模型可以很好地建模双向语境信息，性能优于基于自回归语言模型的预训练方法。然而，由于需要 mask 一部分输入，BERT 忽略了被 mask 位置之间的依赖关系，因此出现预训练和微调效果的差异（pretrain-finetune discrepancy）。

基于这些优缺点，该研究提出了一种泛化的自回归预训练模型 XLNet。XLNet 可以：

1. 通过最大化所有可能的因式分解顺序的对数似然，学习双向语境信息；
1. 用自回归本身的特点克服 BERT 的缺点；
1. 此外，XLNet 还融合了当前最优自回归模型 Transformer-XL 的思路。[6]

介绍两种无监督目标函数：

## AR(autoregressive)

AR(autoregressive)：自回归，假设序列数据存在线性关系，用 [公式] 预测 [公式] 。以前传统的单向语言模型（ELMo、GPT）都是以AR作为目标。

AR语言模型的优点：是擅长NLP生成任务。因为在生成上下文时，通常是正向的。AR语言模型在这类NLP任务中很自然地工作得很好。

AR语言模型有一些缺点：它只能使用前向上下文或后向上下文，这意味着它不能同时使用前向上下文和后向上下文。

## AE(autoencoding)

AE(autoencoding)：自编码，将输入复制到输出。BERT的MLM就是AE的一种。

与其说XLNet解决了BERT的问题，不如说它基于AR采用了一种新的方法实现双向编码，因为AR方法不存在上述两个痛点。

XLNet的创新点是Permutation Language Modeling


模型最终可以学习到如何聚集所有位置的信息。

However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy. In light of these pros and cons, we propose XLNet, a generalized autoregressive pretraining method that (1) enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order and (2) overcomes the limitations of BERT thanks to its autoregressive formulation. Furthermore, XLNet integrates ideas from Transformer-XL, the state-of-the-art autoregressive model, into pretraining.[1]

新的想法还是难得的：

Permutation Language Modeling：先给我们统一了之前语言模型的思想框架（AR or AE），再一个permutation把两者的优点结合起来，而且整体框架又回归到了AR，感觉生成模型的新SOTA指日可待。
Transformer-XL + Relative segment encoding：这个不是作者重点强调的，但却让我觉得很有用处，目前短文本的任务还好，文本一长难度就会上去，段落级甚至文章级，这两个操作让我看到了NLU在长文本上取得更大成果的可能。

## XLNet与BERT比较

尽管看上去，XLNet在预训练机制引入的Permutation Language Model这种新的预训练目标，和Bert采用Mask标记这种方式，有很大不同。其实你深入思考一下，会发现，两者本质是类似的。

区别主要在于：

- Bert是直接在输入端显示地通过引入Mask标记，在输入侧隐藏掉一部分单词，让这些单词在预测的时候不发挥作用，要求利用上下文中其它单词去预测某个被Mask掉的单词；
- 而XLNet则抛弃掉输入侧的Mask标记，通过Attention Mask机制，在Transformer内部随机Mask掉一部分单词（这个被Mask掉的单词比例跟当前单词在句子中的位置有关系，位置越靠前，被Mask掉的比例越高，位置越靠后，被Mask掉的比例越低），让这些被Mask掉的单词在预测某个单词的时候不发生作用。

所以，本质上两者并没什么太大的不同，只是Mask的位置，Bert更表面化一些，XLNet则把这个过程隐藏在了Transformer内部而已。这样，就可以抛掉表面的[Mask]标记，解决它所说的预训练里带有[Mask]标记导致的和Fine-tuning过程不一致的问题。至于说XLNet说的，Bert里面被Mask掉单词的相互独立问题，也就是说，在预测某个被Mask单词的时候，其它被Mask单词不起作用，这个问题，你深入思考一下，其实是不重要的，因为XLNet在内部Attention Mask的时候，也会Mask掉一定比例的上下文单词，只要有一部分被Mask掉的单词，其实就面临这个问题。而如果训练数据足够大，其实不靠当前这个例子，靠其它例子，也能弥补被Mask单词直接的相互关系问题，因为总有其它例子能够学会这些单词的相互依赖关系。

当然，XLNet这种改造，维持了表面看上去的自回归语言模型的从左向右的模式，这个Bert做不到，这个有明显的好处，就是对于生成类的任务，能够在维持表面从左向右的生成过程前提下，模型里隐含了上下文的信息。所以看上去，XLNet貌似应该对于生成类型的NLP任务，会比Bert有明显优势。另外，因为XLNet还引入了Transformer XL的机制，所以对于长文档输入类型的NLP任务，也会比Bert有明显优势。

---
https://www.rcrai.com/
https://www.rcrai.com/newsinfo/2074664.html
循环智能（Recurrent AI）与快手、滴滴、知乎、海康威视等企业一起入选了年度“三十大AI最佳应用案例”

案例名称：循环智能基于对话数据的AI销售中台，帮助新东方在线等企业提升客户转化

关于杨植麟博士

杨植麟 2019 年获得卡耐基梅隆大学计算机专业博士学位。在深度学习和自然语言处理领域有深入研究且取得了显著成果。作为第一作者与卡内基梅隆大学、Google Brain 团队联合推出NLP 领域热门的国际前沿预训练 XLNet 模型，在 20 个标准任务上超过了曾经保持最优性能记录的 Google BERT 模型，并在18个标准任务上取得历史最好结果，入选NeurIPS 2019 Oral。作为共同第一作者提出 Transformer-XL 模型并在多项主流序列建模数据集上取得历史最好结果。Google 学术引用超 2400 次。

在中国人工智能学会CAAI和清华大学联合发布的《2019人工智能发展报告》中，杨植麟为第一作者的 XLNet 被称为“BERT 之后的重要进展”。2019年，XLNet 论文被多家 AI 媒体机构评选为年度深度学习论文 TOP10，包括 TopBots、Heartbeat和Rubik's Code等。2017年和2018年，杨植麟连续入选机器学习和NLP领域顶级会议和期刊的第一作者全球排行榜，全球仅有三名学者两年皆入选。





[1]: https://arxiv.org/abs/1906.08237
[2]: https://huggingface.co/transformers/model_doc/xlnet.html
[3]: https://zhuanlan.zhihu.com/p/70218096
[4]: https://www.bilibili.com/video/BV1zJ411P7X6?from=search&seid=6818714359543590460
[5]: （Paper）XLNet: Generalized Autoregressive Pretrain - 弃之的文章 - 知乎
https://zhuanlan.zhihu.com/p/240077047
[6]: https://github.com/NLP-LOVE/ML-NLP/tree/master/NLP/16.9%20XLNet
