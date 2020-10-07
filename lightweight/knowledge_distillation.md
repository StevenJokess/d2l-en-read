

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 23:06:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-07 21:11:18
 * @Description:
 * @TODO::
 * @Reference:
-->

背景

集成来提升任务性能，耗时耗力，不利于部署。
将知识压缩到方便部署单个模型是可行的，性能相近。

distill 压缩模型，利用大模型生成的类别概率作为soft targets，待压缩 hard targets。

61.1%
60.8%

旨在把一个大模型或者多个模型ensemble学到的知识迁移到另一个轻量级单模型上，方便部署。简单的说就是用新的小模型去学习大模型的预测结果，改变一下目标函数。听起来是不难，但在实践中小模型真的能拟合那么好吗？所以还是要多看看别人家的实验，掌握一些trick。[3]

蒸馏的目标是让student学习到teacher的泛化能力，理论上得到的结果会比单纯拟合训练数据的student要好。另外，对于分类任务，如果soft targets的熵比hard targets高，那显然student会学习到更多的信息。


## Transfer Set和Soft target

实验证实，Soft target可以起到正则化的作用（不用soft target的时候需要early stopping，用soft target后稳定收敛）
数据过少的话无法完整表达teacher学到的知识，需要增加无监督数据（用teacher的预测作为标签）或进行数据增强，可以使用的方法有：1.增加[MASK]，2.用相同POS标签的词替换，2.随机n-gram采样，具体步骤参考文献2

## 超参数T

T越大越能学到teacher模型的泛化信息。比如MNIST在对2的手写图片分类时，可能给2分配0.9的置信度，3是1e-6，7是1e-9，从这个分布可以看出2和3有一定的相似度，因此这种时候可以调大T，让概率分布更平滑，展示teacher更多的泛化能力
T可以尝试1～20之间

## BERT蒸馏

蒸馏单BERT[2]：模型架构：单层BiLSTM；目标函数：logits的MSE
蒸馏Ensemble BERT[3]：模型架构：BERT；目标函数：soft prob+hard prob；方法：MT-DNN。该论文用给每个任务训练多个MT-DNN，取soft target的平均，最后再训一个MT-DNN，效果比纯BERT好3.2%。但感觉该研究应该是刷榜的结晶，平常应该没人去训BERT ensemble吧。。
BAM[4]：Born-aging Multi-task。用多个任务的Single BERT，蒸馏MT BERT；目标函数：多任务loss的和；方法：在mini-batch中打乱多个任务的数据，任务采样概率为  ，防止某个任务数据过多dominate模型、teacher annealing、layerwise-learning-rate，LR由输出层到输出层递减，因为前面的层需要学习到general features。最终student在大部分任务上超过teacher，而且上面提到的tricks也提供了不少帮助。文献4还不错，推荐阅读一下。
TinyBERT[5]：截止201910的SOTA。利用Two-stage方法，分别对预训练阶段和精调阶段的BERT进行蒸馏，并且不同层都设计了损失函数。与其他模型的对比如下：



[1]: https://arxiv.org/abs/1503.02531 Distilling the Knowledge in a Neural Network
[2]: https://ai.deepshare.net/detail/v_5f164b66e4b0aebca61a59e3/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
[3]: https://zhuanlan.zhihu.com/p/71986772?utm_source=wechat_session&utm_medium=social&utm_oi=772887009306906624&utm_campaign=shareopn
补充一些资源，还没仔细看：

[dkozlov/awesome-knowledge-distillation](https://github.com/dkozlov/awesome-knowledge-distillation)
[Distilling BERT Models with spaCy](http://www.nlp.town/blog/distilling-bert/?utm_campaign=NLP%20News&utm_medium=email&utm_source=Revue%20newsletter)
[DistilBERT](https://medium.com/huggingface/distilbert-8cf3380435b5)
[Multilingual MiniBERT: Tsai et al. (EMNLP 2019)](https://arxiv.org/pdf/1909.00100)
参考

^蒸馏开山鼻祖Hinton@NIPS2014：Distilling the Knowledge in a Neural Network https://arxiv.org/abs/1503.02531
^BERT -> 单层LSTM：Distilling Task-Specific Knowledge from BERT into Simple Neural Networks https://arxiv.org/abs/1903.12136
^MT-DNN ensemble -> MT-DNN：Improving Multi-Task Deep Neural Networks via Knowledge Distillation for Natural Language Understanding https://arxiv.org/abs/1904.09482
^Google Single-task ensemble -> Multi-task：BAM! Born-Again Multi-Task Networks for Natural Language Understanding https://arxiv.org/abs/1907.04829
^Huawei -> TinyBERT: Distilling BERT for Natural Language Understanding https://arxiv.org/abs/1909.10351
