

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 21:07:30
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 21:07:46
 * @Description:
 * @TODO::
 * @Reference:https://0809zheng.github.io/2020/04/27/elmo-bert-gpt.html
-->
人类进行NLP任务时，会使用许多并未出现在上下文中的知识，通常称为“先验知识”，预训练模型引入了大量文本库的先验知识，在NLP任务上取得了优异的表现。

基本思路为：

在大规模语料库上进行pre-training，学习语法、句法、语言逻辑、先验知识等。
针对不同的任务进行fine-tuning。
