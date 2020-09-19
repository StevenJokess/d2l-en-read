

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:12:16
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:12:48
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_linear-networks/image-classification-dataset.html
 * @TODO::
 * @Reference:
-->
4 replies
17 Jun
Inzamam​Anwar
I have tested that num_workers parameter in torch DataLoader does work. By selecting num_workers=4 reduce the read time to half.

18 Jun
Steven​Jokes
batch size = 1, stochastic gradient descent (SGD)
batch size = 256, mini-batch gradient descent (MBGD)
Because using GPU to parallel read data, so MBGD is quicker.
Reducing the batch_size will make overall read performance slower.
:face_with_monocle:Does my guess right?
I’m a Windows user. Try it next time!
https://pytorch.org/docs/stable/torchvision/datasets.html
Datasets:

MNIST
Fashion-MNIST
KMNIST
EMNIST
QMNIST
FakeData
COCO
Captions
Detection
LSUN
ImageFolder
DatasetFolder
ImageNet
CIFAR
STL10
SVHN
PhotoTour
SBU
Flickr
VOC
Cityscapes
SBD
USPS
Kinetics-400
HMDB51
UCF101
CelebA
26 Jun
apohllo
I suggest using %%timeit -r1, which is a built-in function in Jupyter, instead of the d2l timer.

1 reply
26 Jun▶ apohllo
Steven​Jokes
%%time is better. One time is enough :grinning:

Continue Discussion

---

5 replies
29 Jul
Harvinder_​singh
{51678703-F1C0-46CD-8003-ABA93779FC75}.png
In This example, X shape is (32,64,64,1).

32 is the number of examples in minibatch
64 is the heigth of image
64 is width of image
But where is the last dimension is refering to?
1 reply
29 Jul▶ Harvinder_singh
goldpiggy
Hi @Harvinder_singh, “1” refers to the number of channel. Since this is a greyscale image, the number of channel will be 1, while a color image (with RGB channel) has a channel equaled to 3.

1 reply
30 Jul▶ goldpiggy
Harvinder_​singh
Thanks @goldpiggy , Now I understood what is 1 referring here.

28 Aug
Morteza
Which one is preferred? First divide into batches and then shuffle or first shuffle and then batch? Here the first one is coded and looks suspicious for me. Specially if batch_size is big, you would always have same training data in the batch and only the order of batches would change. This would create problems if for example training data are ordered by labels.
Check the result of this:
tmp = tf.data.Dataset.from_tensor_slices([1,1,1,2,2,2]).batch(3).shuffle(buffer_size = 6)

30 Aug
gpk​2000
I am literally scared by looking at the TensorFlow code provided here so I want to make it simple for others

# importing the libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# download and load the fashion-mnist datset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# get the first picture in train data
plt.imshow(x_train[0])

# data normalization to make everything between 0 and 1.
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Putting it all together
def load_data_fashion_mnist(batch_size, resize=None):
    """Download the Fashion-MNIST dataset and then load it into memory."""
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

    # Divide all numbers by 255 so that all pixel values are between
    # 0 and 1
    x_train = x_train.astype('float32') / 255
    x_test = x_test.astype('float32') / 255

    # casting the label to int32`
    y_train = tf.cast(y_train, 'int32')
    y_test = tf.cast(y_test, 'int32')

    return (
        tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_size).shuffle(len(x_train)),
        tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(batch_size).shuffle(len(x_test))
    )

train_iter, test_iter = load_data_fashion_mnist(32, resize=64)
for X, y in train_iter:
    print(X.shape, X.dtype, y.shape, y.dtype)
    break
The only thing I was not able to implement is the resize function, I want to know why we are resizing the images? If someone knows a way to resize according to the code above please do, it will help me.

Thanks.

Continue Discussion
