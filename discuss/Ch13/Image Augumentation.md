

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:13:56
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:14:00
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_computer-vision/image-augmentation.html
 * @TODO::
 * @Reference:
-->
5 replies
15 Jul
lkforward
As mentioned in the beginning of this section, one reason image augmentation could improve the performance of a DL model is that it increases the size of the training dataset by generated the augmented samples. However, in our example, load_cifar10(), it seems we applied the transformation without upsampling. So just curious, in practice, do we apply the transformation repeatedly (by n times) to upsample the data (get a training dataset of n times larger)? Could you please give an example of how to do that using gluon?

Thank you in advance!

1 reply
17 Jul▶ lkforward
goldpiggy
Hi @lkforward, great question! It really depends on the size of original training set. For example, some domain images (such as medical domain) are lack of samples, then we have to upsample n times to get a decent size of training examples. However, if the original training set already has sufficient number of samples, what image augmentation does is to add variety or diversity of features (e.g., it may rotate the cat from different angles rather than only one angle).

1 reply
18 Jul▶ goldpiggy
lkforward
That makes sense. Thank you, @goldpiggy

3 Aug
lkforward
I did some experiments trying to address Exercise 1, “… Can your comparative experiment support the argument that image augmentation can mitigate overfitting? Why?”

I used a subset of CIFAR10, with 500 images (50 for each class, and 10 classes in all) for training and 100 images for validation. Resnet18 was used to predict the probability of an image belongs to one of the classes.

Settings:
Case 1. Benchmark, the original images without augmentations.
Case 2. Apply the following augmentations:

   aug = transforms.Compose(
    [transforms.Resize(40),
     transforms.RandomResizedCrop(32, scale=(0.64, 1.0), ratio=(1.0, 1.0)),
     transforms.RandomHorizontalFlip(),
     transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
Case 3. A up-sampling is applied using the same augmentation. The augmentation is applied with replacement for four times for each original image, so the data size becomes 2000/400 for training / validation.

Results for case 1:

sec13p1_augmentation_case1

Results for case 2:
sec13p1_augmentation_case2

Results for case 3:
sec13p1_augmentation_case3
Based on the loss and the accuracy in the plots, the results from case 3 and case 2 are better than the benchmark, which seems to verify our expectation. However, there are two issues I am not quite sure:

(1) In case 3, the gap (of both loss and accuracy) between the training and the validation curve is larger than other cases. Is it fair to state that “augmentation with upsampling could mitigate overfitting”? As some one can argue that the overfitting is worse in this case.
(2) The loss in the validation data seem to reach a stable value faster (taking about 8 epochs) than the training data in all the cases here. Can we say the model starts to overfit after about 8 epochs?
11 Sep
adamadatasci
Why it’s often only a percentage of the data is augmented, not the whole data? If I have 1K images, why can’t I augment my data to 5K with 5 different transformations?

Continue Discussion
