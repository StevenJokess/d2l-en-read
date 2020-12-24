

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-24 22:58:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 22:58:59
 * @Description:
 * @TODO::
 * @Reference:https://colab.research.google.com/github/huggingface/transformers/blob/master/notebooks/05-benchmark.ipynb#scrollTo=jG-SjOQTskcX
-->
| | CPU | CPU + torchscript | GPU | GPU + torchscript | GPU + FP16 | TPU |
:-- | :--- | :--- | :--- | :--- | :--- | :--- |
**Speed - Inference** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
**Memory - Inference** | ✔ | ✔ | ✔ | ✔ | ✔ | ✘ |
**Speed - Train** | ✔ | ✘ | ✔ | ✘ | ✔ | ✔ |
**Memory - Train** | ✔ | ✘ | ✔ | ✘ | ✔ | ✘ |
