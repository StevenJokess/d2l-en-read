

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 16:28:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 23:12:39
 * @Description:
 * @TODO::
 * @Reference:
-->

# XLNet: Generalized Autoregressive Pretrain


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
