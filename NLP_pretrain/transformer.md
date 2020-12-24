

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 16:28:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 22:52:53
 * @Description:
 * @TODO::
 * @Reference:
-->

## Transformer

Google于2017年提出了《Attention is all you need》，抛弃了传统的RNN结构，「设计了一种Attention机制，通过堆叠Encoder-Decoder结构」，得到了一个Transformer模型，在机器翻译任务中「取得了BLEU值的新高」。

RNN系列模型的顺序计算方式带来了两个问题

某个时间状态，依赖于上一时间步状态，导致模型「不能通过并行计算来加速」
RNN系列的魔改模型比如GRU, LSTM，虽然「引入了门机制」(gate)，但是对「长时间依赖的问题缓解能力有限」，不能彻底解决


2017年6月，Google Brain在论文《Attention Is All You Need》中提出的Transformer架构，完全摒弃了RNN的循环机制，采用一种self-attention的方式进行全局处理。其接收一整段序列，并使用三个可训练的权重矩阵——Query、Key和Value来一次性学习输入序列中各个部分之间的依赖关系。Transformer网络由多个层组成，每个层都由多头注意力机制和前馈网络构成。由于在全局进行注意力机制的计算，忽略了序列中最重要的位置信息。Transformer为输入添加了位置编码（Positional Encoding），使用正弦函数完成，为每个部分的位置生成位置向量，不需要学习，用于帮助网络学习其位置信息。其示意如下图所示：[7]



![transformer_Encoder](img\transformer_Encoder.png)

Embedding：输入序列经过词嵌入得到词嵌入向量；
Positional Encoding：词嵌入向量加上位置编码；
Multi-head self-attention：多头自注意力层；
Add & Norm：残差连接和Layer Norm；

![transformer_Decoder](img\transformer_Decoder.png)

Embedding：训练时使用右移(shifted right)的目标序列，经过词嵌入得到词嵌入向量；
Positional Encoding：词嵌入向量加上位置编码；
Masked Self-Attention：使用自注意力模型对已生成的前缀序列进行编码，通过mask阻止每个位置选择后面的输入信息；
Multi-head self-attention：多头自注意力层；
Feed Forward:逐位置的前馈神经网络。

```py
#位置编码
def get_angles(pos, i, d_model):
  angle_rates = 1 / np.power(10000, (2 * (i//2)) / np.float32(d_model))
  return pos * angle_rates

def positional_encoding(position, d_model):
  angle_rads = get_angles(np.arange(position)[:, np.newaxis],
                          np.arange(d_model)[np.newaxis, :],
                          d_model)

  # apply sin to even indices in the array; 2i
  angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])

  # apply cos to odd indices in the array; 2i+1
  angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])

  pos_encoding = angle_rads[np.newaxis, ...]

  return tf.cast(pos_encoding, dtype=tf.float32)
```

```py
#Scaled-Dot Attention
def scaled_dot_product_attention(q, k, v, mask):
  """Calculate the attention weights.
  q, k, v must have matching leading dimensions.
  k, v must have matching penultimate dimension, i.e.: seq_len_k = seq_len_v.
  The mask has different shapes depending on its type(padding or look ahead)
  but it must be broadcastable for addition.

  Args:
    q: query shape == (..., seq_len_q, depth)
    k: key shape == (..., seq_len_k, depth)
    v: value shape == (..., seq_len_v, depth_v)
    mask: Float tensor with shape broadcastable
          to (..., seq_len_q, seq_len_k). Defaults to None.

  Returns:
    output, attention_weights
  """

  matmul_qk = tf.matmul(q, k, transpose_b=True)  # (..., seq_len_q, seq_len_k)

  # scale matmul_qk
  dk = tf.cast(tf.shape(k)[-1], tf.float32)
  scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)

  # add the mask to the scaled tensor.
  if mask is not None:
    scaled_attention_logits += (mask * -1e9)

  # softmax is normalized on the last axis (seq_len_k) so that the scores
  # add up to 1.
  attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)  # (..., seq_len_q, seq_len_k)

  output = tf.matmul(attention_weights, v)  # (..., seq_len_q, depth_v)

  return output, attention_weights
```

```py
#MultiheadAttention
class MultiHeadAttention(tf.keras.layers.Layer):
  def __init__(self, d_model, num_heads):
    super(MultiHeadAttention, self).__init__()
    self.num_heads = num_heads
    self.d_model = d_model

    assert d_model % self.num_heads == 0

    self.depth = d_model // self.num_heads

    self.wq = tf.keras.layers.Dense(d_model)
    self.wk = tf.keras.layers.Dense(d_model)
    self.wv = tf.keras.layers.Dense(d_model)

    self.dense = tf.keras.layers.Dense(d_model)

  def split_heads(self, x, batch_size):
    """Split the last dimension into (num_heads, depth).
    Transpose the result such that the shape is (batch_size, num_heads, seq_len, depth)
    """
    x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
    return tf.transpose(x, perm=[0, 2, 1, 3])

  def call(self, v, k, q, mask):
    batch_size = tf.shape(q)[0]

    q = self.wq(q)  # (batch_size, seq_len, d_model)
    k = self.wk(k)  # (batch_size, seq_len, d_model)
    v = self.wv(v)  # (batch_size, seq_len, d_model)

    q = self.split_heads(q, batch_size)  # (batch_size, num_heads, seq_len_q, depth)
    k = self.split_heads(k, batch_size)  # (batch_size, num_heads, seq_len_k, depth)
    v = self.split_heads(v, batch_size)  # (batch_size, num_heads, seq_len_v, depth)

    # scaled_attention.shape == (batch_size, num_heads, seq_len_q, depth)
    # attention_weights.shape == (batch_size, num_heads, seq_len_q, seq_len_k)
    scaled_attention, attention_weights = scaled_dot_product_attention(
        q, k, v, mask)

    scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])  # (batch_size, seq_len_q, num_heads, depth)

    concat_attention = tf.reshape(scaled_attention,
                                  (batch_size, -1, self.d_model))  # (batch_size, seq_len_q, d_model)

    output = self.dense(concat_attention)  # (batch_size, seq_len_q, d_model)

    return output, attention_weights
```

```py
#FFN
def point_wise_feed_forward_network(d_model, dff):
  return tf.keras.Sequential([
      tf.keras.layers.Dense(dff, activation='relu'),  # (batch_size, seq_len, dff)
      tf.keras.layers.Dense(d_model)  # (batch_size, seq_len, d_model)
  ])
```

模型特点：采用全attention的方式，完全摒弃了RNN和CNN的做法。
优势：训练速度更快，在两个翻译任务上取得了SoTA。
不足：在decode阶段还是自回归的，即还是不能并行，而且对于每个step的计算，都是要重新算一遍，没有前面的记忆。


```md
[1]: https://mp.weixin.qq.com/s/kjLFPyTb7pal7oorX3ejkw
[2]: Tensorflow官方notebook transformer.ipynb: ('https://github.com/tensorflow/docs/blob/master/site/en/tutorials/text/transformer.ipynb')
[3]: illustrated-transformer: (http://jalammar.github.io/illustrated-transformer/) 该作者的图示很明晰，相对容易理解
TODO:
[4]: https://github.com/lilianweng/transformer-tensorflow
[5]: https://0809zheng.github.io/2020/04/25/transformer.html
[6]: https://blog.csdn.net/Magical_Bubble/article/details/89083225
[7]: https://blog.csdn.net/magical_bubble/article/details/89060213
```
