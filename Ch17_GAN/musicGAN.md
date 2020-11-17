

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-17 20:37:26
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-17 20:37:49
 * @Description:
 * @TODO::
 * @Reference:https://0809zheng.github.io/2020/10/26/musicgen.html
-->

人类历史上第一个通过算法生成音乐的例子是莫扎特的Dice Music


音乐生成模型
一篇关于深度学习中的音乐生成模型综述：From Artificial Neural Networks to Deep Learning for Music Generation – History, Concepts and Trends
按照模型使用的基本结构不同，可将音乐生成模型划分为以Recurrent、Convolutional、Transformer、VAE和GAN为基础的模型。

（1）Recurrent模型
⚪A Recurrent Neural Network Music Generation Tutorial
首个使用LSTM生成MIDI形式的音乐。
⚪Song From PI: A Musically Plausible Network for Pop Music Generation
可以生成多音轨（multi-track）的流行音乐。
⚪DeepBach: a Steerable Model for Bach Chorales Generation
生成巴赫风格的四声部合唱。
（2）Convolutional模型
⚪Counterpoint by Convolution
根据固定的规则将一段或几段旋律结合起来。
（3）Transformer模型
⚪Music Transformer: Generating Music with Long-Term Structure
降低Transformer的时间复杂度，从而实现更长序列的音乐生成。
⚪MuseNet
（4）VAE模型
⚪A Hierarchical Latent Vector Model for Learning Long-Term Structure in Music
重建出与输入“相同”的音乐。
⚪MidiMe: Personalizing a MusicVAE model with user data
MidiMe是MusicVAE的一个扩展应用，目的是生成与输入“类似”但又不同的音乐。
（5）GAN模型
⚪C-RNN-GAN: Continuous recurrent neural networks with adversarial training
以噪声为输入生成MIDI形式的古典音乐。
⚪MidiNet: A Convolutional Generative Adversarial Network for Symbolic-domain Music Generation
可以生成任意小节的MIDI音乐。
