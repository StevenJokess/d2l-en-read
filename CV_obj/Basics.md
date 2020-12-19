

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 20:21:44
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 20:22:05
 * @Description:
 * @TODO::
 * @Reference:https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Object-Detection#single-shot-detector-ssd
-->


## Concepts

Object Detection. duh.

Single-Shot Detection. Earlier architectures for object detection consisted of two distinct stages – a region proposal network that performs object localization and a classifier for detecting the types of objects in the proposed regions. Computationally, these can be very expensive and therefore ill-suited for real-world, real-time applications. Single-shot models encapsulate both localization and detection tasks in a single forward sweep of the network, resulting in significantly faster detections while deployable on lighter hardware.

Multiscale Feature Maps. In image classification tasks, we base our predictions on the final convolutional feature map – the smallest but deepest representation of the original image. In object detection, feature maps from intermediate convolutional layers can also be directly useful because they represent the original image at different scales. Therefore, a fixed-size filter operating on different feature maps will be able to detect objects of various sizes.

Priors. These are pre-computed boxes defined at specific positions on specific feature maps, with specific aspect ratios and scales. They are carefully chosen to match the characteristics of objects' bounding boxes (i.e. the ground truths) in the dataset.

Multibox. This is a technique that formulates predicting an object's bounding box as a regression problem, wherein a detected object's coordinates are regressed to its ground truth's coordinates. In addition, for each predicted box, scores are generated for various object types. Priors serve as feasible starting points for predictions because they are modeled on the ground truths. Therefore, there will be as many predicted boxes as there are priors, most of whom will contain no object.

Hard Negative Mining. This refers to explicitly choosing the most egregious false positives predicted by a model and forcing it to learn from these examples. In other words, we are mining only those negatives that the model found hardest to identify correctly. In the context of object detection, where the vast majority of predicted boxes do not contain an object, this also serves to reduce the negative-positive imbalance.

Non-Maximum Suppression. At any given location, multiple priors can overlap significantly. Therefore, predictions arising out of these priors could actually be duplicates of the same object. Non-Maximum Suppression (NMS) is a means to remove redundant predictions by suppressing all but the one with the maximum score.
