

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-05 23:06:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-05 23:34:01
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

[1]: https://arxiv.org/abs/1503.02531 Distilling the Knowledge in a Neural Network
[2]: https://ai.deepshare.net/detail/v_5f164b66e4b0aebca61a59e3/3?from=p_5ee641d2e8471_5z8XYfL6&type=6
