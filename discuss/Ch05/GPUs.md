

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:54:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:55:22
 * @Description:
 * @TODO::
 * @Reference:
-->


<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:54:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:55:08
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_deep-learning-computation/use-gpu.html
 * @TODO::
 * @Reference:
-->
1 reply
23 Aug
Steven​Jokes
https://mxnet.apache.org/versions/1.6/api/python/docs/tutorials/getting-started/crash-course/6-use_gpus.html

4 replies
26 Jun
Steven​Jokes
I didn’t use nvidia.So I didn’t install GPU version and cuda.
torch.cuda.device('cuda')
AssertionError : Torch not compiled with CUDA enabled
torch.cuda.device_count()
0

Why didn’t AssertionError happen when I run the following code?
torch.cuda.device('cuda:1')
<torch.cuda.device at 0x16349fb2488>

26 Jun
Steven​Jokes
5.6.5. Exercises
you should see almost linear scaling? I’m confused what is linear scaling.
1 reply
27 Jul▶ StevenJokes
Chen​Yangyao
‘Linear scaling’ is that the computation speed is proportional to the number of GPUs you use.
e.g., With one GPU, two tasks take 2 sec, and with two GPUs, two tasks (each on one GPU) takes only 1 sec.

17 Aug
Steven​Jokes
awsblog – 玩转GPU实例之系统工具 – NVIDIA 篇
https://aws.amazon.com/cn/blogs/china/play-with-system-tools-of-gpu-instance-nvidia-chapter/

Continue Discussion
