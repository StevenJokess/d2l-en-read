

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 18:49:05
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 18:49:12
 * @Description:https://discuss.d2l.ai/t/document/39/2
 * @TODO::
 * @Reference:
-->
2.7.5. Exercises
Q：
Pytorch:

Look up ones_like and autograd on the PyTorch website.

What are all the possible outputs after running np.random.choice(4, 2) ?

Can you rewrite np.random.choice(4, 2) by using the np.random.randint function?

q1.
In my github.

q2.

import numpy as np

np.random.choice(4,2)

array([0, 1])

api:

In my github.

q3.

def my_random_choice(x, y):

    my_list = []

    while y > 0:

        my_list.append(np.random.randint(0, x))

        y -= 1

    return np.array(my_list)

my_random_choice(4, 2)

array([2, 0])

For more:

In my github.

My github: https://github.com/StevenJokes/D2L_enread/blob/master/Chapter2/2-7.md



