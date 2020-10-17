

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-17 15:23:20
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-17 15:26:37
 * @Description:
 * @TODO::
 * @Reference:
-->
 数据集整理自 https://www.pyimagesearch.com/2018/04/16/keras-and-convolutional-neuralnetworks-cnnsd

宝可梦数据 集共收集了皮卡丘(Pikachu)、超梦(Mewtwo)、杰尼龟(Squirtle)、小火龙(Charmander)和妙蛙 种子(Bulbasaur)共 5 种精灵生物，每种精灵的信息如表 15.1 所示，共 1168 张图片。

实战宝可梦数据集的加载以及训练。
15.3.1 创建 Dataset 对象
首先通过 load_pokemon 函数返回 images、labels 和编码表信息，代码如下：

```py
    # 加载 pokemon 数据集，指定加载训练集
    # 返回训练集的样本路径列表，标签数字列表和编码表字典
    images, labels, table = load_pokemon('pokemon', 'train')
    print('images:', len(images), images)
    print('labels:', len(labels), labels)
    print('table:', table)
```

构建 Dataset 对象，并完成数据集的随机打散、预处理和批量化操作，代码如下：

```py
    # images: string path
        # 创建 TensorBoard summary 对象
        writter = tf.summary.create_file_writer('logs')
        for step, (x,y) in enumerate(db):
        # x: [32, 224, 224, 3]
        # y: [32]
        with writter.as_default():
            x = denormalize(x) # 反向 normalize，方便可视化
            # 写入图片数据
            tf.summary.image('img',x,step=step,max_outputs=9)
            time.sleep(5) # 延迟 5s，再此循环
```
