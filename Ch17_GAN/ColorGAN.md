

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-16 20:02:43
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-16 20:17:04
 * @Description:
 * @TODO::
 * @Reference:
-->
下面就通过CGAN来实现一个可以自动给图像上色的GAN网络，将其称为ColorGAN。[1]

# 转换为灰度图

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


[1]: https://weread.qq.com/web/reader/4653238071e86dd54654969ka1d32a6022aa1d0c6e83eb4
[2]: https://weread.qq.com/web/reader/4653238071e86dd54654969k17e328b022b17e62166fad4
