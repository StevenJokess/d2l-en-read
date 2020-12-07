

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 19:50:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 19:50:23
 * @Description:
 * @TODO::
 * @Reference:https://dl.acm.org/doi/10.1145/3356250.3360038
-->

This paper aims to **predict the apps a user will open on her mobile device next**. Such an information is essential for many smartphone operations, e.g., app pre-loading and content pre-caching, to save mobile energy. However, it is hard to build an explicit model that accurately depicts the affecting factors and their affecting mechanism of time-varying app usage behavior. This paper presents a deep reinforcement learning framework, named as DeepAPP, which learns a model-free predictive neural network from historical app usage data. Meanwhile, an online updating strategy is designed to adapt the predictive network to the time-varying app usage behavior. To transform DeepAPP into a practical deep reinforcement learning system, several challenges are addressed by developing a context representation method for complex contextual environment, a general agent for overcoming data sparsity and a lightweight personalized agent for minimizing the prediction time. Extensive experiments on a large-scale anonymized app usage dataset reveal that DeepAPP provides high accuracy (precision 70.6% and recall of 62.4%) and reduces the prediction time of the state-of-the-art by 6.58×. A field experiment of 29 participants also demonstrates DeepAPP can effectively reduce time of loading apps.
