

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 18:21:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-07 18:51:18
 * @Description:
 * @TODO::
 * @Reference:https://github.com/PacktPublishing/Deep-Learning-with-TensorFlow-2-and-Keras
-->
Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter 2.

The code will look like the following:

@tf.function
def fn(input, state):
    return cell(input, state)

input = tf.zeros([100, 100])
state = [tf.zeros([100, 100])] * 2
# warmup
cell(input, state)
fn(input, state)

Install the latest version of conda, tensorflow, h5py, opencv
conda update conda
conda update --all
pip install --upgrade tensorflow
pip install --upgrade h5py
pip install opencv-python

-----


==> WARNING: A newer version of conda exists. <==
  current version: 4.8.5
  latest version: 4.9.0

Please update conda by running

    $ conda update -n base conda
