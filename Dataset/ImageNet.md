

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-10 21:39:47
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 17:21:19
 * @Description:
 * @TODO::
 * @Reference:[4]: https://cv.gluon.ai/build/examples_deployment/cpp_inference.html
 * [6]: https://github.com/0809zheng/pedestrain-detection-towncentre
 * [7]: https://0809zheng.github.io/2020/05/17/paper-recent.html
 * [8]: https://github.com/udacity/deep-learning-v2-pytorch/blob/master/dcgan-svhn/DCGAN_Exercise.ipynb
-->
Imagenet-1k dataset.
MNIST
CIFAR-10: http://www.cs.toronto.edu/~kriz/cifar.html
CIFAR-100
STL-10
Street View House Numbers (SVHN) dataset.[8]

dataset built-in to the PyTorch datasets library.
svhn_train = datasets.SVHN(root='data/', split='train', download=True, transform=transform)

ILSVRC2012 task 1

Recommended datasets
celebA: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
celebAHQ: https://github.com/nperraud/download-celebA-HQ
fashionGen: https://fashion-gen.com/
DTD: https://www.robots.ox.ac.uk/~vgg/data/dtd/

GANs:
celebaHQ
fashionGen
cifar10
celeba

[4]
Prepare ADE20K dataset.
Prepare COCO datasets
Prepare COCO datasets
Prepare Cityscapes dataset.
Prepare ILSVRC 2015 DET dataset
Prepare ILSVRC 2015 VId dataset
Prepare Multi-Human Parsing V1 dataset
Prepare OTB 2015 dataset
Prepare PASCAL VOC datasets
Prepare Youtube_bb dataset
Prepare custom datasets for object detection
Prepare the 20BN-something-something Dataset V2
Prepare the HMDB51 Dataset
Prepare the ImageNet dataset
Prepare the Kinetics400 dataset
Prepare the UCF101 dataset
Prepare your dataset in ImageRecord format

[5]
[FFHQ](https://github.com/NVlabs/ffhq-dataset)

[6]
TownCentre

[7]
用于行人检测的benchmarks包括：

CityPersons：5000张
Caltech：训练集：测试集 = 42782：4024
ETH：1804张，经常被用作测试集
INRIA：2120张，训练集：测试集 = 1832：288
KITTI：训练集：测试集 = 7481：7518，包括两个子类：pedestrian和cyclist，有easy、moderate、hard三种

著作权归作者所有。
商业转载请联系作者获得授权,非商业转载请注明出处。
原文: https://0809zheng.github.io/2020/05/17/paper-recent.html

图像处理相关数据集
1.MNIST
2.MS-COCO
3.ImageNet
4.Open Images Dataset
5.VisualQA
6.The Street View House Numbers (SVHN)
7.CIFAR-10
8.Fashion-MNIST
自然语言处理相关数据集
1.IMDB Reviews
2.Twenty Newsgroups
3.Sentiment140
4.WordNet
5.Yelp Reviews
6.The Wikipedia Corpus
7.The Blog Authorship Corpus
8.Machine Translation of Various Languages
语音处理相关数据集
1.Free Spoken Digit Dataset
2.Free Music Archive (FMA)
3.Ballroom
3.Million Song Dataset
4.LibriSpeech
5.VoxCeleb
Supplement
1.Twitter Sentiment Analysis
2.Age Detection of Indian Actors
3.Urban Sound Classification

https://zhuanlan.zhihu.com/p/35449783#3.Urban%20Sound%20Classification

https://github.com/bo-xiong/Awesome-Deep-Learning-for-Chinese
MNIST 手写数字体识别
Google House Numbers from street view
CIFAR-10 and CIFAR-100
IMAGENET 图片识别
Tiny Images 8千万张图片
Flickr Data 100 Million Yahoo dataset
Berkeley Segmentation Dataset 500
UC Irvine Machine Learning Repository
Flickr 8k
Flickr 30k
Microsoft COCO
VQA
Image QA
AT&T Laboratories Cambridge face database
AVHRR Pathfinder
Air Freight - The Air Freight data set is a ray-traced image sequence along with ground truth segmentation based on textural characteristics. (455 images + GT, each 160x120 pixels). (Formats: PNG)
Amsterdam Library of Object Images - ALOI is a color image collection of one-thousand small objects, recorded for scientific purposes. In order to capture the sensory variation in object recordings, we systematically varied viewing angle, illumination angle, and illumination color for each object, and additionally captured wide-baseline stereo images. We recorded over a hundred images of each object, yielding a total of 110,250 images for the collection. (Formats: png)
Annotated face, hand, cardiac & meat images - Most images & annotations are supplemented by various ASM/AAM analyses using the AAM-API. (Formats: bmp,asf)
Image Analysis and Computer Graphics
Brown University Stimuli - A variety of datasets including geons, objects, and "greebles". Good for testing recognition algorithms. (Formats: pict)
CAVIAR video sequences of mall and public space behavior - 90K video frames in 90 sequences of various human activities, with XML ground truth of detection and behavior classification (Formats: MPEG2 & JPEG)
Machine Vision Unit
CCITT Fax standard images - 8 images (Formats: gif)
CMU CIL's Stereo Data with Ground Truth - 3 sets of 11 images, including color tiff images with spectroradiometry (Formats: gif, tiff)
CMU PIE Database - A database of 41,368 face images of 68 people captured under 13 poses, 43 illuminations conditions, and with 4 different expressions.
CMU VASC Image Database - Images, sequences, stereo pairs (thousands of images) (Formats: Sun Rasterimage)
Caltech Image Database - about 20 images - mostly top-down views of small objects and toys. (Formats: GIF)
Columbia-Utrecht Reflectance and Texture Database - Texture and reflectance measurements for over 60 samples of 3D texture, observed with over 200 different combinations of viewing and illumination directions. (Formats: bmp)
Computational Colour Constancy Data - A dataset oriented towards computational color constancy, but useful for computer vision in general. It includes synthetic data, camera sensor data, and over 700 images. (Formats: tiff)
Computational Vision Lab
Content-based image retrieval database - 11 sets of color images for testing algorithms for content-based retrieval. Most sets have a description file with names of objects in each image. (Formats: jpg)
Efficient Content-based Retrieval Group
Densely Sampled View Spheres - Densely sampled view spheres - upper half of the view sphere of two toy objects with 2500 images each. (Formats: tiff)
Computer Science VII (Graphical Systems)
Digital Embryos - Digital embryos are novel objects which may be used to develop and test object recognition systems. They have an organic appearance. (Formats: various formats are available on request)
Univerity of Minnesota Vision Lab
El Salvador Atlas of Gastrointestinal VideoEndoscopy - Images and Videos of his-res of studies taken from Gastrointestinal Video endoscopy. (Formats: jpg, mpg, gif)
FG-NET Facial Aging Database - Database contains 1002 face images showing subjects at different ages. (Formats: jpg)
FVC2000 Fingerprint Databases - FVC2000 is the First International Competition for Fingerprint Verification Algorithms. Four fingerprint databases constitute the FVC2000 benchmark (3520 fingerprints in all).
Biometric Systems Lab - University of Bologna
Face and Gesture images and image sequences - Several image datasets of faces and gestures that are ground truth annotated for benchmarking
German Fingerspelling Database - The database contains 35 gestures and consists of 1400 image sequences that contain gestures of 20 different persons recorded under non-uniform daylight lighting conditions. (Formats: mpg,jpg)
Language Processing and Pattern Recognition
Groningen Natural Image Database - 4000+ 1536x1024 (16 bit) calibrated outdoor images (Formats: homebrew)
ICG Testhouse sequence - 2 turntable sequences from ifferent viewing heights, 36 images each, resolution 1000x750, color (Formats: PPM)
Institute of Computer Graphics and Vision
IEN Image Library - 1000+ images, mostly outdoor sequences (Formats: raw, ppm)
INRIA's Syntim images database - 15 color image of simple objects (Formats: gif)
INRIA
INRIA's Syntim stereo databases - 34 calibrated color stereo pairs (Formats: gif)
Image Analysis Laboratory - Images obtained from a variety of imaging modalities -- raw CFA images, range images and a host of "medical images". (Formats: homebrew)
Image Analysis Laboratory
Image Database - An image database including some textures
JAFFE Facial Expression Image Database - The JAFFE database consists of 213 images of Japanese female subjects posing 6 basic facial expressions as well as a neutral pose. Ratings on emotion adjectives are also available, free of charge, for research purposes. (Formats: TIFF Grayscale images.)
ATR Research, Kyoto, Japan
JISCT Stereo Evaluation - 44 image pairs. These data have been used in an evaluation of stereo analysis, as described in the April 1993 ARPA Image Understanding Workshop paper ``The JISCT Stereo Evaluation'' by R.C.Bolles, H.H.Baker, and M.J.Hannah, 263--274 (Formats: SSI)
MIT Vision Texture - Image archive (100+ images) (Formats: ppm)
MIT face images and more - hundreds of images (Formats: homebrew)
Machine Vision - Images from the textbook by Jain, Kasturi, Schunck (20+ images) (Formats: GIF TIFF)
Mammography Image Databases - 100 or more images of mammograms with ground truth. Additional images available by request, and links to several other mammography databases are provided. (Formats: homebrew)
ftp://ftp.cps.msu.edu/pub/prip - many images (Formats: unknown)
Middlebury Stereo Data Sets with Ground Truth - Six multi-frame stereo data sets of scenes containing planar regions. Each data set contains 9 color images and subpixel-accuracy ground-truth data. (Formats: ppm)
Middlebury Stereo Vision Research Page - Middlebury College
Modis Airborne simulator, Gallery and data set - High Altitude Imagery from around the world for environmental modeling in support of NASA EOS program (Formats: JPG and HDF)
NIST Fingerprint and handwriting - datasets - thousands of images (Formats: unknown)
NIST Fingerprint data - compressed multipart uuencoded tar file
NLM HyperDoc Visible Human Project - Color, CAT and MRI image samples - over 30 images (Formats: jpeg)
National Design Repository - Over 55,000 3D CAD and solid models of (mostly) mechanical/machined engineerign designs. (Formats: gif,vrml,wrl,stp,sat)
Geometric & Intelligent Computing Laboratory
OSU (MSU) 3D Object Model Database - several sets of 3D object models collected over several years to use in object recognition research (Formats: homebrew, vrml)
OSU (MSU/WSU) Range Image Database - Hundreds of real and synthetic images (Formats: gif, homebrew)
OSU/SAMPL Database: Range Images, 3D Models, Stills, Motion Sequences - Over 1000 range images, 3D object models, still images and motion sequences (Formats: gif, ppm, vrml, homebrew)
Signal Analysis and Machine Perception Laboratory
Otago Optical Flow Evaluation Sequences - Synthetic and real sequences with machine-readable ground truth optical flow fields, plus tools to generate ground truth for new sequences. (Formats: ppm,tif,homebrew)
Vision Research Group
ftp://ftp.limsi.fr/pub/quenot/opflow/testdata/piv/ - Real and synthetic image sequences used for testing a Particle Image Velocimetry application. These images may be used for the test of optical flow and image matching algorithms. (Formats: pgm (raw))
LIMSI-CNRS/CHM/IMM/vision
LIMSI-CNRS
Photometric 3D Surface Texture Database - This is the first 3D texture database which provides both full real surface rotations and registered photometric stereo data (30 textures, 1680 images). (Formats: TIFF)
SEQUENCES FOR OPTICAL FLOW ANALYSIS (SOFA) - 9 synthetic sequences designed for testing motion analysis applications, including full ground truth of motion and camera parameters. (Formats: gif)
Computer Vision Group
Sequences for Flow Based Reconstruction - synthetic sequence for testing structure from motion algorithms (Formats: pgm)
Stereo Images with Ground Truth Disparity and Occlusion - a small set of synthetic images of a hallway with varying amounts of noise added. Use these images to benchmark your stereo algorithm. (Formats: raw, viff (khoros), or tiff)
Stuttgart Range Image Database - A collection of synthetic range images taken from high-resolution polygonal models available on the web (Formats: homebrew)
Department Image Understanding
The AR Face Database - Contains over 4,000 color images corresponding to 126 people's faces (70 men and 56 women). Frontal views with variations in facial expressions, illumination, and occlusions. (Formats: RAW (RGB 24-bit))
Purdue Robot Vision Lab
The MIT-CSAIL Database of Objects and Scenes - Database for testing multiclass object detection and scene recognition algorithms. Over 72,000 images with 2873 annotated frames. More than 50 annotated object classes. (Formats: jpg)
The RVL SPEC-DB (SPECularity DataBase) - A collection of over 300 real images of 100 objects taken under three different illuminaiton conditions (Diffuse/Ambient/Directed). -- Use these images to test algorithms for detecting and compensating specular highlights in color images. (Formats: TIFF )
Robot Vision Laboratory
The Xm2vts database - The XM2VTSDB contains four digital recordings of 295 people taken over a period of four months. This database contains both image and video data of faces.
Centre for Vision, Speech and Signal Processing
Traffic Image Sequences and 'Marbled Block' Sequence - thousands of frames of digitized traffic image sequences as well as the 'Marbled Block' sequence (grayscale images) (Formats: GIF)
IAKS/KOGS
U Bern Face images - hundreds of images (Formats: Sun rasterfile)
U Michigan textures (Formats: compressed raw)
U Oulu wood and knots database - Includes classifications - 1000+ color images (Formats: ppm)
UCID - an Uncompressed Colour Image Database - a benchmark database for image retrieval with predefined ground truth. (Formats: tiff)
UMass Vision Image Archive - Large image database with aerial, space, stereo, medical images and more. (Formats: homebrew)
UNC's 3D image database - many images (Formats: GIF)
USF Range Image Data with Segmentation Ground Truth - 80 image sets (Formats: Sun rasterimage)
University of Oulu Physics-based Face Database - contains color images of faces under different illuminants and camera calibration conditions as well as skin spectral reflectance measurements of each person.
Machine Vision and Media Processing Unit
University of Oulu Texture Database - Database of 320 surface textures, each captured under three illuminants, six spatial resolutions and nine rotation angles. A set of test suites is also provided so that texture segmentation, classification, and retrieval algorithms can be tested in a standard manner. (Formats: bmp, ras, xv)
Machine Vision Group
Usenix face database - Thousands of face images from many different sites (circa 994)
View Sphere Database - Images of 8 objects seen from many different view points. The view sphere is sampled using a geodesic with 172 images/sphere. Two sets for training and testing are available. (Formats: ppm)
PRIMA, GRAVIR
Vision-list Imagery Archive - Many images, many formats
Wiry Object Recognition Database - Thousands of images of a cart, ladder, stool, bicycle, chairs, and cluttered scenes with ground truth labelings of edges and regions. (Formats: jpg)
3D Vision Group
Yale Face Database - 165 images (15 individuals) with different lighting, expression, and occlusion configurations.
Yale Face Database B - 5760 single light source images of 10 subjects each seen under 576 viewing conditions (9 poses x 64 illumination conditions). (Formats: PGM)
Center for Computational Vision and Control
DeepMind QA Corpus - Textual QA corpus from CNN and DailyMail. More than 300K documents in total. Paper for reference.
YouTube-8M Dataset - YouTube-8M is a large-scale labeled video dataset that consists of 8 million YouTube video IDs and associated labels from a diverse vocabulary of 4800 visual entities.
Open Images dataset - Open Images is a dataset of ~9 million URLs to images that have been annotated with labels spanning over 6000 categories.
