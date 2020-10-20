

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-25 18:38:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-19 21:29:29
 * @Description:
 * @TODO::
 * @Reference:
-->

# StyleGAN

A new paper by NVIDIA, A Style-Based Generator Architecture for GANs (StyleGAN), presents a novel model which addresses this challenge. StyleGAN generates the artificial image gradually, starting from a very low resolution and continuing to a high resolution (1024×1024). By modifying the input of each level separately, it controls the visual features that are expressed in that level, from coarse features (pose, face shape) to fine details (hair color), without affecting other levels. [11]

StyleGAN is a type of generative adversarial network. It uses an alternative generator architecture for generative adversarial networks, borrowing from style transfer literature; in particular, the use of adaptive instance normalization. Otherwise it follows Progressive GAN in using a progressively growing training regime. Other quirks include the fact it generates from a fixed value tensor not stochastically generated latent variables as in regular GANs. The stochastically generated latent variables are used as style vectors in the adaptive instance normalization at each resolution after being transformed by an 8-layer feedforward network. Lastly, it employs a form of regularization called mixing regularization, which mixes two style latent variables during training.[8]

To quantify interpolation quality and disentanglement,we propose two new, automated methods that are applica-ble to any generator architecture.[9]

Fr ́echet inception distance (FID) for various generator de-signs (lower is better).  In this paper we calculate the FIDs using50,000 images drawn randomly from the training set, and reportthe lowest distance encountered over the course of training




The new architecture leads to an automatically learned, unsupervised separation of high-level attributes (e.g., pose and identity when trained on human faces) and stochastic variation in the generated images (e.g., freckles, hair), and it enables intuitive, scale-specific control of the synthesis. The new generator improves the state-of-the-art in terms of traditional distribution quality metrics, leads to demonstrably better interpolation properties, and also better disentangles the latent factors of variation.[4]

The paper divides the features into three types:
Coarse – resolution of up to 82 – affects pose, general hair style, face shape, etc
Middle – resolution of 162 to 322  – affects finer facial features, hair style, eyes open/closed, etc.
Fine – resolution of 642 to 10242 – affects color scheme (eye, hair and skin) and micro features.[11]

## Style-based generator

specializewtostylesy= (ys,yb)that control adaptive instance normalization(AdaIN) [27, 17, 21, 16] operations after each convolutionlayer of the synthesis networkg.

AdaIN isparticularly well suited for our purposes due to its efficiencyand compact representation

100,000  la-beled latent-space vectors


describe two new ways of quanti-fying disentanglement, neither of which requires an encoderor known factors of variation,




we propose two new automated metrics —perceptual path length and linear separability

## generator

our generator admits a more linear, less entangled represen-tation of different factors of variation

Thus the network learns to use the global and local channels appro-priately, without explicit guidance

## Linear separability

If  a  latent  space  is  sufficiently  disentangled,  it  should be possible to find direction vectors that consistently corre-spond to individual factors of variation. We propose anothermetric that quantifies this effect by measuring how well thelatent-space points can be separated into two distinct setsvia a linear hyperplane,  so that each set corresponds to aspecific binary attribute of the image.



Furthermore, increasing the depth of the mapping networkimproves both image quality and separability inW, whichis in line with the hypothesis that the synthesis network in-herently favors a disentangled input representation.  Inter-estingly, adding a mapping network in front of a traditionalgenerator results in severe loss of separability inZbut im-proves the situation in the intermediate latent spaceW, andthe FID improves as well.  This shows that even the tradi-tional generator architecture performs better when we in-troduce an intermediate latent space that does not have tofollow the distribution of the training data

## FFHQ dataset


Flickr-Faces-HQ (FFHQ), which consists of images of “regular” people and is more diversified. The chart below shows the Frèchet inception distance (FID) score of different configurations of the model.

https://github.com/NVlabs/ffhq-dataset


## source code

https://github.com/NVlabs/stylegan



traditional GAN gen-erator architecture is in every way inferior to a style-baseddesign.

## Mapping Network[11]

The Mapping Network’s goal is to encode the input vector into an intermediate vector whose different elements control different visual features. This is a non-trivial process since the ability to control visual features with the input vector is limited, as it must follow the probability density of the training data. For example, if images of people with black hair are more common in the dataset, then more input values will be mapped to that feature. As a result, the model isn’t capable of mapping parts of the input (elements in the vector) to features, a phenomenon called features entanglement. However, by using another neural network the model can generate a vector that doesn’t have to follow the training data distribution and can reduce the correlation between features.
The Mapping Network consists of 8 fully connected layers and its output w is of the same size as the input layer (512×1).


## Adaptive Instance Normalization (AdaIN)[11]

The AdaIN (Adaptive Instance Normalization) module transfers the encoded information w, created by the Mapping Network, into the generated image. The module is added to each resolution level of the Synthesis Network and defines the visual expression of the features in that level:
Each channel of the convolution layer output is first normalized to make sure the scaling and shifting of step 3 have the expected effect.
The intermediate vector w is transformed using another fully-connected layer (marked as A) into a scale and bias for each channel.
The scale and bias vectors shift each channel of the convolution output, thereby defining the importance of each filter in the convolution. This tuning translates the information from w to a visual representation.

The use of different style vectors at diﬀerent points of the synthesis network gives control over the styles of the resulting image at diﬀerent levels of detail. For example, blocks of layers in the synthesis network at lower resolutions (e.g. 4 × 4 and 8 × 8) control high-level styles such as pose and hairstyle. Blocks of layers in the middle of the network (e.g. as 16 × 16 and 32 × 32) control hairstyles and facial expression. Finally, blocks of layers closer to the output end of the network (e.g. 64 × 64 to 1024 × 1024) control color schemes and very ﬁne details.





2018/12
![（a）无条件GAN和（b）有条件GAN的流程图。](img\StyleGAN.md)[7]

[1]: https://www.bilibili.com/video/BV1ot4y197MG
[2]: https://medium.com/swlh/hairstyle-transfer-semantic-editing-gan-latent-code-b3a6ccf91e82
[3]: https://github.com/Azmarie/Hairstyle-Transfer
[4]: https://arxiv.org/abs/1812.04948
[5]: https://twitter.com/dl_from_scratch/status/1308266572503367680
[6]: https://paperswithcode.com/paper/analyzing-and-improving-the-image-quality-of
[7]: https://syncedreview.com/2019/08/29/ai-creates-fashion-models-with-custom-outfits-and-poses/
[8]: https://paperswithcode.com/method/stylegan
[9]: https://arxiv.org/abs/1812.04948
[10]: X.  Huang  and  S.  J.  Belongie.Arbitrary  style  transferin  real-time  with  adaptive  instance  normalization.CoRR,abs/1703.06868, 2017. 1, 2
[11]: https://www.lyrn.ai/2018/12/26/a-style-based-generator-architecture-for-generative-adversarial-networks/
[12]: http://questioneurope.blogspot.com/search/label/AI

TODO:


A. Brock, J. Donahue, and K. Simonyan.  Large scale GANtraining  for  high  fidelity  natural  image  synthesis.CoRR,abs/1809.11096, 2018. 1, 3, 810


