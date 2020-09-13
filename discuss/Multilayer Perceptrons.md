

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 18:50:28
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 18:50:48
 * @Description:https://discuss.d2l.ai/t/multilayer-perceptrons/91
 * @TODO::
 * @Reference:
-->

the derivative of the tanh:
dtanh(x)/dx=1−tanh^(2)=
{2exp(−2x)-[exp(−2x)]^2}/(1+exp(−2x))^2.
https://www.math24.net/derivatives-hyperbolic-functions/
the derivative of the pReLU(x):
dpReLU(x)/dx = 1 (if x > 0);α (if x < 0);doesn’t exist (if x = 0)
h= ReLU(x) = max(x, 0)
y = ReLU(h) = max(h, 0) = max (x, 0) =ReLU(x)
h= pReLU(x)=max(0,x)+αmin(0,x).
y = pReLU(h) =max(0,h)+αmin(0,h)
One linear functions add,minus other linear function still is linear function.
[1−exp(−2x)]/[1+exp(−2x)]+1 = 2/[1+exp(−2x)] = 2 * 1/[1+exp(−2x)] = 2 sigmoid(2x).
d/2 dimensions will cause linearly dependent?
overfit?
