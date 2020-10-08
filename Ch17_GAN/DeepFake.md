

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-28 18:57:58
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-10-08 18:59:31
 * @Description:MT
 * @TODO::
 * @Reference:
-->

[5]:MT

# DeepFakes and Beyond: A Survey of Face Manipulation and Fake Detection

## 摘要

免费访问大型公共数据库，再加上深度学习技术（尤其是生成对抗网络）的迅猛发展，已经导致产生了非常现实的伪造内容，并在这个假新闻时代对社会产生了相应的影响 。

这项调查对操纵人脸图像的技术（包括DeepFake方法）以及检测此类操纵的方法进行了全面回顾。 特别地，审查了四种类型的面部操纵：i）全脸综合 entire face synthesis, ，ii）身份交换（DeepFakes），iii）属性操纵和iv）表情交换。 对于每个操纵组，我们提供有关操纵技术，现有公共数据库以及伪造检测方法技术评估的关键基准的详细信息，包括这些评估结果的摘要。

在调查中讨论的所有方面中，我们特别关注最新一代的DeepFakes，着重介绍了它的改进和对假冒检测的挑战

除了调查信息之外，我们还讨论了该领域需要考虑的开放问题和未来趋势。

索引术语-假新闻，深度伪造，媒体取证，面部操作，人脸识别，生物识别，数据库，基准(—Fake News, DeepFakes, Media Forensics, Face Manipulation, Face Recognition, Biometrics, Databases, Benchmark)



## 简介

假冒的图像和视频，包括通过数字操作（尤其是DeepFake方法[1]）通过数字操作生成的面部信息，最近已成为公众关注的焦点[2]，[3]。 非常流行的术语“ DeepFake”是指基于深度学习的技术，该技术能够通过将一个人的脸与另一个人的脸交换来创建假视频。 这个术语起源于一个名叫“ deepfakes”的Reddit用户在2017年底声称开发了一种机器学习算法，该算法可以帮助他将名人面孔转换为色情视频[4]。 除了伪造色情内容外，此类伪造内容的一些更有害的用法包括伪造新闻，恶作剧和财务欺诈。 结果，传统上致力于一般媒体取证的研究领域[5] – [11]受到了鼓舞，并且现在正致力于检测图像和视频中的面部操纵[12]。

这些在伪造人脸检测方面所做的新努力的一部分，是建立在过去对生物特征识别反欺诈[13]-[15]和现代数据驱动的深度学习[16]，[17]的研究基础之上的。 在顶级会议[18]-[22]，国际项目（例如由国防高级研究计划局（DARPA）资助的MediFor等国际项目）以及最近的媒体等竞赛中，越来越多的人证明了对假脸检测的兴趣日益浓厚。 由美国国家标准与技术协会(NIST)和Facebook分别推出Media Forensics Challenge(MFC2018)1and the Deepfake Detection Challenge (DFDC)2


传统上，由于缺乏复杂的编辑工具，所需的领域专业知识以及所涉及的复杂且耗时的过程，面部操作的数量和真实性受到了限制。 例如，该主题的早期工作[23]通过在音频轨道的声音和对象的脸部形状之间建立联系，可以修改使用不同音频轨道讲话的人的嘴唇动作。 然而，从这些早期工作至今，最近几年发生了许多事情。 如今，由于以下原因，在图像/视频中自动合成不存在的面孔或操纵一个人的真实面孔变得越来越容易，这要归功于：i）大规模公共数据的可访问性，以及ii）深度学习的发展 消除了许多手动编辑步骤的技术，例如自动编码器（AE）和生成对抗网络（GAN）[24]，[25]。

因此，已经发布了开放软件和移动应用程序，例如ZAO3和FaceApp4，这使任何人都可以创建伪造的图像和视频，而无需任何现场经验。

为了应对这些日益复杂和现实的操纵内容，研究界正在作出巨大努力，设计改进的面部操纵检测方法。媒体取证中传统的假检测方法通常基于:i)机内指纹,内在指纹分析引入的摄像头设备,硬件和软件,如光学镜头[27],滤色器数组和插值[28],[29],和压缩[30],[31],其中,和2)outcamera指纹,指纹分析外部引入的编辑软件,如复制粘贴或copymove图像的不同元素[32],[33],减少视频的帧率[34]-[36],等等。然而，传统的伪检测方法中考虑的大部分特征都高度依赖于特定的训练场景，因此对看不见的条件[6]，[8]，[16]不具有鲁棒性。

这在我们所处的时代尤为重要，因为大多数媒体的虚假内容都是在社交网络上分享的，社交网络的平台会自动修改原始的图片/视频，比如通过[12]压缩和调整大小等操作

这项调查提供了一个深入的审查数字操作技术应用于面部内容，由于可能的有害应用的大量，例如，虚假新闻的产生，将提供错误的信息，在政治选举和安全威胁[37]，[38]。具体来说，我们涵盖了四种类型的操作:i)全脸合成，ii)身份互换，iii)属性操作，iv)表情互换。

这四种主要类型的面部处理已经被研究团体很好地确定，在过去的几年里得到了最多的关注。此外，我们还回顾了一些其他挑战性和危险的面部处理技术，但不太流行，如面部变形。

最后，为了完整起见，我们将重点介绍该领域最近的其他调查。在[39]中，作者从一般的角度讨论了深度造假的话题，提出了管理深度造假风险的R.E.A.L框架。此外，Verdoliva最近在[40]中调查了一般媒体取证中考虑的传统操作和假检测方法，以及最新的深度学习技术。

本调查对[39]和[40]进行了补充，并对每个面部操作组进行了更详细的审查，包括操作技术、现有的公共数据库和伪检测方法技术评估的关键基准，包括对这些评估结果的总结。

此外，我们特别关注最新一代的深度假货，突出其改进和假货检测的挑战。

本文的其余部分组织如下。我们首先在第二节中对不同类型的面部手法进行了概述。然后，从第三节到第六节，我们描述了每种类型面部操作的关键方面，包括用于研究的公共数据库、检测方法和基准测试结果。第七节重点介绍了其他有趣的面部处理技术，这些技术在前几节中没有涉及。最后，我们在第VIII节中作结束语，强调未决问题和未来趋势。









属性操作:面部合成(GAN指纹去除)的相同方面也适用于这里，因为大多数操作都基于GAN架构。此外，还值得注意的是，用于研究的公共数据库非常少(只有DFFD数据库是公开的[17])，缺乏标准的实验方案来进行研究之间的公平比较。

表情交换：与身份交换相反，身份交换随着改进的DeepFake数据库的发布而迅速发展，据我们所知，表达式交换中唯一的公共数据库是FaceForensics ++。

该数据库的特征是易于检测的视觉伪像，因此，在几种伪造检测方法中，AUC结果接近100％。 我们鼓励研究人员基于最新技术[125]，[151]，[184]生成并公开更现实的数据库。


所有这些方面，加上改进的GAN方法的发展和最近的深度假检测挑战(DeepFake Detection Challenge, DFDC)，将促进新一代真实感假图像/视频[70]，以及更先进的人脸操纵检测技术

---

DeepFaceLab is an open-source deepfake system created by iperovfor face swapping with more than 3,000 forks and 14,000 stars in Github: it provides an imperative and easy-to-use pipeline for people to use with no comprehensive understanding of deep learning framework or with model implementation required, while remains a ﬂexible and loose coupling structure for people who need to strengthen theirownpipelinewithotherfeatureswithoutwritingcomplicatedboilerplatecode. [4]



---
[7]

  deepfake  creation  model  using  two  encoder-decoder  pairs.  Twonetworks  use  the  same  encoder  but  different  decoders  for  training  process(top). An image of face A is encoded with the common encoder and decodedwith decoder B to create a deepfake (bottom)




```md
[1]: https://paperswithcode.com/paper/deepfakes-and-beyond-a-survey-of-face
[2]: https://paperswithcode.com/paper/deepfacelab-a-simple-flexible-and-extensible
[3]: https://github.com/iperov/DeepFaceLab/  repo
[4]: https://arxiv.org/abs/2005.05535 DeepFaceLab
[5]: Deepfakes. Deepfakes. https://github.com/deepfakes/faceswap, 2017.
[6]: https://arxiv.org/pdf/2001.00179v3.pdf DeepFakes and Beyond: A Survey of Face Manipulation and Fake Detection
[7]: https://arxiv.org/pdf/1909.11573

```

```md
TODO:
1 https://www.nist.gov/itl/iad/mig/media-forensics-challenge-2018
2 https://deepfakedetectionchallenge.ai/
3 https://apps.apple.com/cn/app/id1465199127
4 https://apps.apple.com/gb/app/faceapp-ai-face-editor/id1180884341
5 https://thispersondoesnotexist.com
6 https://github.com/MarekKowalski/FaceSwap
7 https://github.com/deepfakes/faceswap
8 https://www.youtube.com/watch?v=UlvoEW7l5rs
9 https://www.bbc.com/news/technology-48607673

19 https://github.com/Guim3/IcGAN
20 https://github.com/facebookresearch/FaderNetworks
21 https://github.com/yunjey/stargan/blob/master/README.md
22 https://github.com/LynnHo/AttGAN-Tensorflow
23 https://github.com/csmliu/STGAN
34 https://deepfakedetectionchallenge.ai/

garwal, S., and Varshney, L. R. (2019). Limits of deepfake detection:A robust estimation viewpoint.arXiv preprintarXiv:1905.03493.
```

```

https://app.dimensions.ai

Tools Links Key  Features

Faceswaphttps://github.com/deepfakes/faceswap- Using two encoder-decoder pairs.- Parameters of the encoder are shared.

Faceswap-GANhttps://github.com/shaoanlu/faceswap-GANAdversarial loss and perceptual loss (VGGface) are added to an auto-encoder architec-ture.

Few-ShotFaceTranslation GANhttps://github.com/shaoanlu/fewshot-face-translation-GAN-  Use  a  pre-trained  face  recognition  model  to  extract  latent  embeddings  for  GANprocessing.- Incorporate semantic priors obtained by modules from FUNIT [39] and SPADE [40].

DeepFaceLabhttps://github.com/iperov/DeepFaceLab-  Expand  from  the  Faceswap  method  with  new  models,  e.g.  H64,  H128,  LIAEF128,SAE [41].- Support multiple face extraction modes, e.g. S3FD, MTCNN, dlib, or manual [41].

DFakerhttps://github.com/dfaker/df- DSSIM loss function [42] is used to reconstruct face.- Implemented based on Keras library.DeepFaketfhttps://github.com/StromWine/DeepFaketfSimilar to DFaker but implemented based on tensorflow.

Deepfakes webβhttps://deepfakesweb.com/Commercial website for face swapping using deep learning algorithms.
```
