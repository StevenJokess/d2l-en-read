# Geometric GAN

对目标函数的优化是折页损失( Hinge Loss)形式的损失函数,它起源于 Geometric GAN。

在 GeometricGAN中,研究者将GAN解释为在特征空间进行的三步操作:(1)分类超平面搜索;(2)判别器向远离超平面的方向更新;(3)生成器向超平面的方向更新。各种GAN之间的主要区别就在于分类超平面的构建方法以及特征向量的几何尺度缩放因子的选择,具体理论推导参见文献[3]。在训练阶段,批(mini- batch)的大小往往远小于特征空间的维度,这种情况下的分类问题被称为高维低采样尺寸(High- Dimension-Low- Sample-size, HDLSS)问题。支持向量机(SVM)中最大化两类的分类边界以及软边界的思想被广泛应用在 HDLSS问题中,并被证明具有鲁棒性。 GeometriC GAN借鉴SM的思想,判别器的损失函数形式与SVM中的折页损失的形式很相似。 GeometriC GAN出现后,这种具有折页损失形式的GAN损失函数在很多方法中被采用,包括2018年热门的 SAGAN[4]和 BigGAN

[1]: 《百面深度学习》试读 | 系列二：回顾GAN的发展之路 - Hulu的文章 - 知乎 https://zhuanlan.zhihu.com/p/163616780s
