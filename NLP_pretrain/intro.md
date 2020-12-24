

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 21:07:30
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 22:35:18
 * @Description:
 * @TODO::
 * @Reference:https://0809zheng.github.io/2020/04/27/elmo-bert-gpt.html
-->
人类进行NLP任务时，会使用许多并未出现在上下文中的知识，通常称为“先验知识”，预训练模型引入了大量文本库的先验知识，在NLP任务上取得了优异的表现。

基本思路为：

在大规模语料库上进行pre-training，学习语法、句法、语言逻辑、先验知识等。
针对不同的任务进行fine-tuning。[1]


主要整理了论文里面测试的场景，当然想用并且愿意调的话，哪哪儿都能用

- ULMFiT：论文里面只用在了文本分类（分类、序列标注等）上，但看它那个套路，应该用到别的任务上也没有问题，只是调起来比较麻烦
- ELMo：这个就随便用了吧，就当成embedding用，论文里面是用在了问答、情感分类、语义角色标注、共指消解、命名实体识别、文本蕴含等任务
- GPT：文本蕴含、问答、推理、分类、文本相似度任务等
- BERT：单句分类、句子对分类、问答、命名实体识别等任务
- MT-DNN：单句分类、句子相似度、句子对分类、相关度排序等任务
- XLM：多语的文本蕴含、无监督机器翻译、有监督机器翻译等任务
- GPT-2：啥都行吧，论文里面都是用ZSL验证的各种任务

[1]: https://0809zheng.github.io/2020/04/27/elmo-bert-gpt.html
[2]: https://blog.csdn.net/Magical_Bubble/article/details/89524404
