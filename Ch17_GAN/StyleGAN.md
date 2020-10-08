

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-25 18:38:57
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-08 02:24:13
 * @Description:
 * @TODO::
 * @Reference:
-->

# StyleGAN

StyleGAN is a type of generative adversarial network. It uses an alternative generator architecture for generative adversarial networks, borrowing from style transfer literature; in particular, the use of adaptive instance normalization. Otherwise it follows Progressive GAN in using a progressively growing training regime. Other quirks include the fact it generates from a fixed value tensor not stochastically generated latent variables as in regular GANs. The stochastically generated latent variables are used as style vectors in the adaptive instance normalization at each resolution after being transformed by an 8-layer feedforward network. Lastly, it employs a form of regularization called mixing regularization, which mixes two style latent variables during training.[8]

To quantify interpolation quality and disentanglement,we propose two new, automated methods that are applica-ble to any generator architecture.[9]

Fr ́echet inception distance (FID) for various generator de-signs (lower is better).  In this paper we calculate the FIDs using50,000 images drawn randomly from the training set, and reportthe lowest distance encountered over the course of training




The new architecture leads to an automatically learned, unsupervised separation of high-level attributes (e.g., pose and identity when trained on human faces) and stochastic variation in the generated images (e.g., freckles, hair), and it enables intuitive, scale-specific control of the synthesis. The new generator improves the state-of-the-art in terms of traditional distribution quality metrics, leads to demonstrably better interpolation properties, and also better disentangles the latent factors of variation.[4]

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

https://github.com/NVlabs/ffhq-dataset





traditional GAN gen-erator architecture is in every way inferior to a style-baseddesign.





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
[11]:


TODO:


A. Brock, J. Donahue, and K. Simonyan.  Large scale GANtraining  for  high  fidelity  natural  image  synthesis.CoRR,abs/1809.11096, 2018. 1, 3, 810


