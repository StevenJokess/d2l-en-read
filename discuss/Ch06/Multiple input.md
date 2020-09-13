

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 20:46:03
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 20:46:21
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_convolutional-neural-networks/channels.html
 * @TODO::
 * @Reference:
-->
2 replies
21 Jul
lregistros
It would be nice to have some discussion about using other color representations like HSV/HSL. Would it help to reduce the memory usage by eliminating one dimension of the kernel if we don’t have to aggregate RGB channels?

1 reply
23 Jul▶ lregistros
goldpiggy
Hey @lregistros, great question! Actually RGB and HSV/HSL have defined conversion: https://en.wikipedia.org/wiki/HSL_and_HSV#To_RGB, which should be easily implemented :slight_smile:

Continue Discussion
