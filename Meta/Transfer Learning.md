

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-19 18:26:30
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 18:27:01
 * @Description:
 * @TODO::
 * @Reference:
-->

迁移学习是机器学习的一个重要分支，是指利用数据、任务、或模型之间的相似性，将在源领域学习过的模型，应用于新领域的一种学习过程。比如我们大部分人学摩托车的时候，都是把骑自行车的经验迁移了过来。

2010年时Sinno Jialin Pan和 Qiang Yang发表文章《迁移学习的调查》，详细介绍了迁移学习的分类问题。当以迁移学习的场景为标准时分为三类：归纳式迁移学习（Inductive Transfer Learning）、直推式迁移学习（Transductive Transfer Learning）、和直推式迁移学习(Unsupervised Transfer Learning)。

深度迁移学习主要就是模型的迁移，一个最简单最常用的方法就是fine-tuning，就是利用别人已经训练好的网络，针对目标任务再进行调整。近年来大火的BERT、GPT、XLNET等都是首先在大量语料上进行预训练，然后在目标任务上进行fine-tuning。

[1]: https://www.aminer.cn/ai-history
