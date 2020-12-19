

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 23:10:35
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 23:10:43
 * @Description:
 * @TODO::
 * @Reference:https://github.com/anilsathyan7/Portrait-Segmentation/blob/master/slim512.ipynb
-->

converter = tf.lite.TFLiteConverter.from_keras_model_file('/content/slim_reshape.h5')
tflite_model = converter.convert()
open("slim_reshape.tflite", "wb").write(tflite_model)
