

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 19:06:32
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-10 19:06:51
 * @Description:
 * @TODO::
 * @Reference:GAN学习指南：从原理入门到制作生成Demo - 何之源的文章 - 知乎
https://zhuanlan.zhihu.com/p/24767059
-->

cascade = cv2.CascadeClassifier(cascade_file)
image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
