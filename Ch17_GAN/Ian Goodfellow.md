

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 21:13:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 21:13:23
 * @Description:
 * @TODO::
 * @Reference:
-->

Ian Goodfellow，人工智能领域的顶级专家，因提出了生成对抗网络（GANs）而闻名，被誉为“GANs之父”。他分别从斯坦福大学获得计算机科学学士、硕士学位，蒙德利尔大学博士学位。毕业后，Goodfellow加入Google，成为Google Brain研究团队的一员。然后他离开谷歌加入新成立的OpenAI研究所。Ian Goodfellow 在OpenAI短暂工作后，于2017年3月从OpenAI重回谷歌Goodfellow最出名的是发明了生成性对抗网络，这是Facebook经常使用的机器学习方法。他也是Deep Learning教科书的主要作者。2017年，Goodfellow被麻省理工学院技术评论评为35位35岁以下的创新者之一。

2018年年初，William Fedus、Ian Goodfellow和Andrew M. Dai在ICLR 2018共同提交的论文中使用 GAN 和强化学习方法在 NLP 中做了自己的探索(https://arxiv.org/abs/1801.07736)。

2018年7月，Ian等人提出一种新型对抗攻击（对抗攻击通常会使得神经网络分类错误），对神经网络重新编程，诱导模型执行攻击者选定的新任务。该研究首次表明了神经网络惊人的脆弱性和灵活性。(https://arxiv.org/pdf/1806.11146.pdf )。

8月的一篇论文中，和Augustus Odena共同提出了一种新方法覆盖引导模糊测试（coverage guided fuzzing，CGF），将其应用于神经网络的测试（https://arxiv.org/pdf/1808.02822.pdf ），该方法能够自动Debug神经网络。Goodfellow表示，希望这将成为涉及ML的复杂软件回归测试的基础，例如，在推出新版本的网络之前，使用fuzz来搜索新旧版本之间的差异。

此外开源了名为TensorFuzz的CGF软件库。 此外，Ian与团队的人提出对抗正则化方法（https://arxiv.org/pdf/1807.07543v2.pdf ）显著改善了自编码器的平滑插值能力，这不仅能提高自编码器的泛化能力，对于后续任务的表征学习也会大有帮助。
