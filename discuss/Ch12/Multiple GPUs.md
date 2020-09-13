

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 20:24:49
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 20:24:58
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_computational-performance/multiple-gpus.html
 * @TODO::
 * @Reference:
-->
2 replies
4 Sep
yannis
Given we increase the effective batch size by a factor of k when training with k GPUs, shouldn’t we be decreasing (instead of increasing as stated) the LR by a factor of k to make up for the approximately k-times larger weight update that results from the increased batch size per iteration?

1 reply
4 Sep▶ yannis
Steven​Jokes
Why?
I think LR should increase to catch up with batch size increasing.
