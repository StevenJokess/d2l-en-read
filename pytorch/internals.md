

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 15:16:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 15:23:37
 * @Description:
 * @TODO::
 * @Reference:https://mp.weixin.qq.com/s/8J-vsOukt7xwWQFtwnSnWw
-->


PyTorch 中大量核都仍然是用传统的 TH 风格编写的。（顺便一提，TH 代表 TorcH。这是个很好的缩写词，但很不幸被污染了；如果你看到名称中有 TH，可认为它是传统的。）传统 TH 风格是什么意思呢？

它是以 C 风格书写的，没有（或很少）使用 C++。

其 refcounted 是人工的（使用了对 THTensor_free 的人工调用以降低你使用张量结束时的 refcounts）。

其位于 generic/ 目录，这意味着我们实际上要编译这个文件很多次，但要使用不同的 #define scalar_t

这种代码相当疯狂，而且我们讨厌回顾它，所以请不要添加它。如果你想写代码但对核编写了解不多，你能做的一件有用的事情：将某些 TH 函数移植到 ATen。
