

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-10-14 22:51:45
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 17:45:19
 * @Description:
 * @TODO::
 * @Reference:
-->

# 多任务学习（Multi-task Learning）

## What is a task? (more formally this time)

A task: $\mathscr{T}_{i} \triangleq\left\{p_{i}(\mathbf{x}), p_{i}(\mathbf{y} \mid \mathbf{x}), \mathscr{L}_{i}\right\}$
data generating distributions
Corresponding datasets: $\quad \mathscr{D}_{i}^{t r} \quad \mathscr{D}_{i}^{\text {est}}$
will use $\mathscr{D}_{i}$ as shorthand for $\mathscr{D}_{i}^{t r}$ :[2]

如果有两个任务比较相关，它们之间会存在一定的共享知识，这些知识对两个任务都会有所帮助．这些共享的知识可以是表示（特征）、模型参数或学习算法等．目前，主流的多任务学习方法主要关注表示层面的共享．




多任务学习（Multi-task Learning）是指同时学习多个相关任务，让这些任务在学习过程中共享知识，利用多个任务之间的相关性来改进模型在每个任务上的性能和泛化能力．多任务学习可以看作一种归纳迁移学习（InductiveTransfer Learning），即通过利用包含在相关任务中的信息作为归纳偏置（In-ductive Bias）来提高泛化能力[Caruana,1997]

\text { Vanilla MTL Objective: } \min _{\theta} \sum_{i=1}^{T} \mathscr{L}_{i}\left(\theta, \mathscr{D}_{i}\right)[2]

Basic Version:
1. Sample mini-batch of tasks $\mathscr{B} \sim\left\{\mathscr{T}_{i}\right\}$
2. Sample mini-batch datapoints for each task $\mathscr{D}_{i}^{b} \sim \mathscr{D}_{i}$
3. Compute loss on the mini-batch: $\hat{\mathscr{L}}(\theta, \mathscr{B})=\sum_{\mathscr{T}_{k} \in \mathscr{B}} \mathscr{L}_{k}\left(\theta, \mathscr{D}_{k}^{b}\right)$
4. Backpropagate loss to compute gradient $\nabla_{\theta} \hat{\mathscr{L}}$
5. Apply gradient with your favorite neural net optimizer (e.g. Adam)
Note: This ensures that tasks are sampled uniformly, regardless of data quantities.
Tip: For regression problems, make sure your task labels are on the same scale!


Multitask Learning (MTL) is an inductive transfer mechanism whose principle goal is to improve generalization performance. MTL improves generalization by leveraging the domain-specific information contained in the training signals of related tasks. It does this by training tasks in parallel while using a shared representation. In effect, the training signals for the extra tasks serve as an inductive bias.[2]

共享机制多任务学习的主要挑战在于如何设计多任务之间的共享机制．在传统的机器学习算法中，引入共享的信息是比较困难的，通常会导致模型变得复杂．但是在神经网络模型中，模型共享变得相对比较容易．深度神经网络模型提供了一种很方便的信息共享方式，可以很容易地进行多任务学习．多任务学习的共享机制比较灵活，有很多种共享模式．图10.1给出了多任务学习中四种常见的共享模式，其中𝐴、𝐵和𝐶表示三个不同的任务，红色框表示共享模块，蓝色框表示任务特定模块．这四种常见的共享模式分别为：
（1）硬共享模式：让不同任务的神经网络模型共同使用一些共享模块（一般是低层）来提取一些通用特征，然后再针对每个不同的任务设置一些私有模块（一般是高层）来提取一些任务特定的特征．
（2）软共享模式：不显式地设置共享模块，但每个任务都可以从其他任务中“窃取”一些信息来提高自己的能力．窃取的方式包括直接复制使用其他任务的隐状态，或使用注意力机制来主动选取有用的信息．
（3）层次共享模式：一般神经网络中不同层抽取的特征类型不同，低层一般抽取一些低级的局部特征，高层抽取一些高级的抽象语义特征．因此如果多任务学习中不同任务也有级别高低之分，那么一个合理的共享模式是让低级任务在低层输出，高级任务在高层输出．
（4）共享-私有模式：一个更加分工明确的方式是将共享模块和任务特定（私有）模块的责任分开．共享模块捕捉一些跨任务的共享特征，而私有模块只捕捉和特定任务相关的特征．最终的表示由共享特征和私有特征共同构成．


An Alternative View on the Multi-Task Architecture
Split $\theta$ into share parameters $s^{s h}$ and task-specifíc parameters $\theta^{i}$
$$
\text { Then, our objective is: } \min _{\theta^{\prime \prime}, g^{\prime}, \ldots, \theta^{\top}} \sum_{i=1}^{T} \mathscr{L}_{i}\left(\left\{\theta^{s h}, \theta^{i}\right\}, \mathscr{D}_{i}\right)
$$
Choosing how to condition on $\boldsymbol{z}_{i}$ equivalent to share parameters

多任务学习通常可以获得比单任务学习更好的泛化能力，主要有以下几个原因：
（1）多任务学习在多个任务的数据集上进行训练，比单任务学习的训练集更大．由于多个任务之间有一定的相关性，因此多任务学习相当于是一种隐式的数据增强，可以提高模型的泛化能力．
（2）多任务学习中的共享模块需要兼顾所有任务，这在一定程度上避免了模型过拟合到单个任务的训练集，可以看作一种正则化．
（3）既然一个好的表示通常需要适用于多个不同任务，参见第1.3节．多任务学习的机制使得它会比单任务学习获得更好的表示．
（4）在多任务学习中，每个任务都可以“选择性”利用其他任务中学习到的隐藏特征，从而提高自身的能力

```python
# https://gist.github.com/dominique003/679e641210b9aade06b513b7b6750746/raw/976c370a9c789bfa8927560157b57b813411c86e/MTCNNExtractFaces.py
# extract and plot each detected face in a photograph
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN

# draw each face separately
def draw_faces(filename, result_list):
	# load the image
	data = pyplot.imread(filename)
	# plot each face as a subplot
	for i in range(len(result_list)):
		# get coordinates
		x1, y1, width, height = result_list[i]['box']
		x2, y2 = x1 + width, y1 + height
		# define subplot
		pyplot.subplot(1, len(result_list), i+1)
		pyplot.axis('off')
		# plot face
		pyplot.imshow(data[y1:y2, x1:x2])
	# show the plot
	pyplot.show()

filename = 'poupees.jpg'
# load image from file
pixels = pyplot.imread(filename)
# create the detector, using default weights
detector = MTCNN()
# detect faces in the image
faces = detector.detect_faces(pixels)
# display faces on the original image
draw_faces(filename, faces)
```

[1]: Caruana R, 1997. Multi-task learning[J]. Machine Learning, 28(1):41-75.
TODO:http://questioneurope.blogspot.com/2020/07/running-mtcnn-on-my-own-photos.html
[2]: https://cs330.stanford.edu/slides/cs330_intro.pdf
