

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 20:12:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 20:12:28
 * @Description:
 * @TODO::
 * @Reference:https://github.com/chenyuntc/pytorch-best-practice
-->
训练
必须首先启动visdom：

python -m visdom.server
然后使用如下命令启动训练：

# 在gpu0上训练,并把可视化结果保存在visdom 的classifier env上
python main.py train --data-root=./data/train --use-gpu=True --env=classifier
