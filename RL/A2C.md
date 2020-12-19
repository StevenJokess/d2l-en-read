

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 21:55:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 21:44:36
 * @Description:
 * @TODO::
 * @Reference:
-->
Original paper: https://arxiv.org/abs/1602.01783
Baselines blog post: https://blog.openai.com/baselines-acktr-a2c/
python -m baselines.run --alg=a2c --env=PongNoFrameskip-v4 runs the algorithm for 40M frames = 10M timesteps on an Atari Pong. See help (-h) for more options
also refer to the repo-wide README.md

[1]: https://github.com/openai/baselines/tree/master/baselines/a2c
[2]: https://github.com/rpatrik96/pytorch-a2c
