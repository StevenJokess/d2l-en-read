

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:22:49
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:22:51
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_preliminaries/lookup-api.html
 * @TODO::
 * @Reference:
-->

1 reply
12 Jun
Steven​Jokes
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

Continue Discussion
