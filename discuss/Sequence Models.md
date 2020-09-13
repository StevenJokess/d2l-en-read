

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 18:53:30
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 18:53:53
 * @Description:https://discuss.d2l.ai/t/sequence-models/114
 * @TODO::
 * @Reference:
-->
8.1.2. A Toy Example
features = d2l.zeros((T-tau, tau))
AttributeError : module ‘d2l.torch’ has no attribute ‘zeros’
Then I search http://preview.d2l.ai/d2l-en/PR-1077/search.html?q=d2l.zeros&check_keywords=yes&area=default
No source code:
http://preview.d2l.ai/d2l-en/PR-1077/chapter_appendix-tools-for-deep-learning/d2l.html?highlight=d2l%20zeros#d2l.torch.zeros
I can use ``features = d2l.torch.zeros((T-tau, tau))` to replace now, and try to code next time!
:cold_face:An hour to debug!
