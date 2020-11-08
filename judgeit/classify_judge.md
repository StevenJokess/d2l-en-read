

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-08 16:20:51
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-08 16:21:15
 * @Description:
 * @TODO::
 * @Reference:https://www.cnblogs.com/veagau/p/11768919.html
-->

分类 (Classification) 任务的损失函数采用交叉嫡 (cross entropy)：
$$
\mathcal{L}_{\mathcal{T}_{i}}\left(f_{\phi}\right)=\sum_{x^{(j)}, y^{(j)} \sim \mathcal{T}_{i}} y^{(j)} \log f_{\phi}\left(x^{(j)}\right)+\left(1-y^{(j)}\right) \log \left(1-f_{\phi}\left(x^{(j)}\right)\right)
$$
