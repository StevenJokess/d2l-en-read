# D-GAN

论文提出D-GAN, 一个对抗网络能够近似逼近真实数据的策略和根据一坝仿真的图片生成实际动作 论文认为, 在游戏中, 有时存在不止一种正确或者实际的动作可以选择。论文的目标是使用D-GAN来 逼近近似人类在玩游戏时候的驾驶行为。有些文献认为, 鉴别模型更加适合这个任务, 论文认为事实 上, 这将会限制训练数据解决空间 (解决方案的选择项)，但是GAN不会限制动作选项。论文采样人 的驾驶行为: [1]$\mathcal{X}_{E}=\left\{\left(s_{1}, a_{1}\right),\left(s_{2}, a_{2}\right), \ldots,\left(s_{n}, a_{n}\right)\right\},$ 最终的GAN的算法如下:
$$
\min _{G} \max _{D} \mathbb{E}_{(s, a) \sim \mathcal{X}_{E}}[\log D(s, a)]+\mathbb{E}_{s \sim \mathcal{X}_{E}, z \sim \mathbb{P}_{z}}[\log (1-D(s, G(s, z)))]
$$
论文给出了鉴别器和生成器的网络架构, 论文不同于传统的GAN结构, 输入是向量, 输出是图片, 论

[1]: https://blog.csdn.net/qq_31239495/article/details/82964630
