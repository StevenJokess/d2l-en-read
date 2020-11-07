

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 20:59:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-07 21:00:24
 * @Description:
 * @TODO::
 * @Reference:https://www.tensorflow.org/tutorials/audio/simple_audio
-->
import seaborn as sns


sns.heatmap(confusion_mtx, xticklabels=commands, yticklabels=commands,
            annot=True, fmt='g')

