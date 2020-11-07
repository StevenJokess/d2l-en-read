

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 19:45:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-07 19:45:47
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/nyz5211314/article/details/106276697
-->
def load_image(filename):
    imgs = os.listdir(filename)
    x_train = np.empty((imgs.__len__(), 64, 64, 3), dtype='float32')

    for i in range(len(imgs)):
        img = Image.open(filename + imgs[i])
        img = img.resize((64,64))
        img_arr = np.asarray(img, dtype='float32')
        x_train[i, :, :, :] = img_arr/127.5 - 1.

    return x_train
