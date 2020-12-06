

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 21:06:10
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 21:11:28
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch08.html#idm45762350231624
-->

TorchScript

If you can remember as far back as the introduction (I know!), you know that the main difference between PyTorch and TensorFlow is that TensorfFlow has a graph-based representation of a model, whereas PyTorch has an eager execution with tape-based differentiation. The eager method allows you to do all sorts of dynamic approaches to specifying and training models that makes PyTorch appealing for research purposes. On the other hand, the graph-based representation may be static, but it gains power from that stability; optimizations may be applied to the graph representation, safe in the knowledge that nothing is going to change. And just as TensorFlow has moved to support eager execution in version 2.0, version 1.0 of PyTorch introduced TorchScript, which is a way of bringing the advantages of graph-based systems without completely giving up the flexibility of PyTorch. This is done in two ways that can be mixed and matched: tracing and using TorchScript directly.

