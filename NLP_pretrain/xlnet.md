

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 16:28:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-07 22:26:49
 * @Description:
 * @TODO::
 * @Reference:
-->

# XLNet


介绍两种无监督目标函数：

AR(autoregressive)：自回归，假设序列数据存在线性关系，用 [公式] 预测 [公式] 。以前传统的单向语言模型（ELMo、GPT）都是以AR作为目标。
AE(autoencoding)：自编码，将输入复制到输出。BERT的MLM就是AE的一种。

与其说XLNet解决了BERT的问题，不如说它基于AR采用了一种新的方法实现双向编码，因为AR方法不存在上述两个痛点。

XLNet的创新点是Permutation Language Modeling


模型最终可以学习到如何聚集所有位置的信息。

However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy. In light of these pros and cons, we propose XLNet, a generalized autoregressive pretraining method that (1) enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order and (2) overcomes the limitations of BERT thanks to its autoregressive formulation. Furthermore, XLNet integrates ideas from Transformer-XL, the state-of-the-art autoregressive model, into pretraining.[1]

新的想法还是难得的：

Permutation Language Modeling：先给我们统一了之前语言模型的思想框架（AR or AE），再一个permutation把两者的优点结合起来，而且整体框架又回归到了AR，感觉生成模型的新SOTA指日可待。
Transformer-XL + Relative segment encoding：这个不是作者重点强调的，但却让我觉得很有用处，目前短文本的任务还好，文本一长难度就会上去，段落级甚至文章级，这两个操作让我看到了NLU在长文本上取得更大成果的可能。


[1]: https://arxiv.org/abs/1906.08237
[2]: https://huggingface.co/transformers/model_doc/xlnet.html
[3]: https://zhuanlan.zhihu.com/p/70218096
