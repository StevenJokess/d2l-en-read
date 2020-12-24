

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-07 16:28:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-24 22:50:55
 * @Description:
 * @TODO::
 * @Reference:
-->

# Transformer-XL

目前在NLP领域中，处理语言建模问题有两种最先进的架构：RNN和Transformer。RNN按照序列顺序逐个学习输入的单词或字符之间的关系，而Transformer则接收一整段序列，然后使用self-attention机制来学习它们之间的依赖关系。这两种架构目前来看都取得了令人瞩目的成就，但它们都局限在捕捉长期依赖性上。

为了解决这一问题，CMU联合Google Brain在2019年1月推出的一篇新论文《Transformer-XL：Attentive Language Models beyond a Fixed-Length Context》同时结合了RNN序列建模和Transformer自注意力机制的优点，在输入数据的每个段上使用Transformer的注意力模块，并使用循环机制来学习连续段之间的依赖关系。

Transformer-XL在多种语言建模数据集（如单词级别的enwik8和字符级别的text8）上实现了目前的SoTA效果，且该模型在推理阶段速度更快，比之前最先进的利用Transformer进行语言建模的方法快300～1800倍。 同时，该论文也放出了其配套源码（包括TensorFlow和PyTorch的）、预训练模型及在各个数据集上训练的超参数，可以说是非常良心了～造福我等伸手党！[3]

With the capability of modeling bidirectional contexts, denoising autoencoding based pretraining like BERT achieves better performance than pretraining approaches based on autoregressive language modeling. However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy.[2]

Transformers have a potential of learning longer-term dependency, but are limited by a fixed-length context in the setting of language modeling. We propose a novel neural architecture Transformer-XL that enables learning dependency beyond a fixed length without disrupting temporal coherence. It consists of a segment-level recurrence mechanism and a novel positional encoding scheme. Our method not only enables capturing longer-term dependency, but also resolves the context fragmentation problem.[1]

## PyTorch实现

class PositionalEmbedding(nn.Module):
    def __init__(self, demb):
        super(PositionalEmbedding, self).__init__()
        self.demb = demb
        inv_freq = 1 / (10000 ** (torch.arange(0.0, demb, 2.0) / demb))

    def forward(self, pos_seq):
        sinusoid_inp = torch.ger(pos_seq, self.inv_freq)
        pos_emb = torch.cat([sinusoid_inp.sin(), sinusoid_inp.cos()], dim=-1)
        return pos_emb[:,None,:]


测试阶段的速度
Transformer-XL的推理速度也明显快于vanilla Transformer，尤其是对于较长的上下文。比如，在上下文长度为800时，Transformer-XL提速363倍；而当上下文长度增加到3800时，Transformer-XL提速1874倍！


[1]: https://arxiv.org/abs/1901.02860
[2]: https://huggingface.co/transformers/model_doc/transformerxl.html
[3]: https://github.com/NLP-LOVE/ML-NLP/tree/master/NLP/16.9%20XLNet
[4]: https://blog.csdn.net/magical_bubble/article/details/89060213
[5]: https://github.com/kimiyoung/transformer-xl
