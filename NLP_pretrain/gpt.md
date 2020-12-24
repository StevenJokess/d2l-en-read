

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 19:54:54
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 00:37:00
 * @Description:
 * @TODO::
 * @Reference:https://0809zheng.github.io/2020/04/27/elmo-bert-gpt.html
-->
Generative Pre-Training (GPT)的结构是

Transformer的Decoder：


paper：Improving Language Understanding by Generative Pre-Training
arXiv：NLPIR



GPT主要的目标还是当好一个预训练模型该有的样子。用非监督的人类语言数据，训练一个预训练模型，然后拿着这个模型进行finetune， 基本上就可以让你在其他任务上也表现出色。因为下游要finetune的任务千奇百怪，在这个教学中，我会更专注GPT模型本身。 告诉你GPT模型到底长什么样，又会有什么样的特性。至于后续的finetune部分，其实比起模型本身，要容易不少。



GPT 已经比ELMo好上很多了，但研究人员为了达到更高的效果，目前还有两个升级版。 GPT2（稍微调整了一下结构，主结构不变）增大了模型的体量， 它有1600维隐藏层，参数规模达15亿。 GPT3在GPT2的基础上再次拓展，变得更大，效果更好。1750亿个参数，真是大力出奇迹。如果你看数字没什么概念，给你上张图。[2]

[2]: https://mofanpy.com/tutorials/machine-learning/nlp/gpt/
