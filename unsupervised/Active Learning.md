

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-03 19:46:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-03 19:47:03
 * @Description:
 * @TODO::
 * @Reference:
-->
为了让机器快速学习，对沟通数据（电话录音、在线IM沟通记录）进行标注是必不可少的一步。但是，数据标注需要昂贵的人工或各种成本，面对海量的非结构化数据，如何经济又准确地进行标注是一个的棘手问题。



而主动学习（Active Learning）被认为是一种非常有效的解决方案：通过使用少量已有标注数据，让机器学习到的模型与标注专家进行高效的交互，选出最有价值和信息量的样本进行标注，能够在达到预设标准的情况下，有效降低模型学习所需要的标注数据量。

[1]: https://www.rcrai.com/newsinfo/450691.html
