

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-09 18:47:53
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-09 19:30:00
 * @Description:
 * @TODO::
 * @Reference:
 * [2]： https://blog.csdn.net/u014453898/article/details/85126733
-->
初始化随机权重和偏差
把输入传入网络，得到输出值
计算预测值与真实值之间的误差
对每一个产生误差的神经元，改变相应的值以减小误差
迭代更新，直到找到最优权重


能被3整除的共有333个，能被5整除的共有199个，二者有交叉，即能同时被3和5整除的共有66个。所以能被3整除或能被5整除的共有333+199-66=466个，则答案为999-466=533个。

int a=strlen(str); //a=10; >>>> strlen 计算字符串的长度，以结束符 0x00 为字符串结束。
int b=sizeof(str); //而b=20; >>>> sizeof 计算的则是分配的数组 str[20] 所占的内存空间的大小，不受里面存储的内容改变。

N=(W-F+2P)/S+1, W:输入特征图尺寸，F:kernel尺寸，P:padding大小，S：stride大小

(128-3+2) / 2 + 1
若除不尽，则取较小的数

Padding的作用用于解决图像边缘信息损失的问题

---

空洞卷积(也称扩张卷积，膨胀卷积)--dilated convolution
$W=\frac{W-d(k-1)-1+2 p}{s}+1$[2]

---

主定理：https://blog.csdn.net/lanchunhui/article/details/52451362

---
将50个红球和50个白球放到两个盒子中，放法不限，从中抽出一个球，那么抽到的是红球的最大概率是

1/2+1/2 * 49/99=74/99

所谓"存储结构无关"是指既可以用数组实现,又可以用链表实现。
