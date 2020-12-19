

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 00:12:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 00:26:33
 * @Description:
 * @TODO::
 * @Reference:https://github.com/NishantTharani/LearningDeepLearning/blob/master/d2l.ai/Ch7/util.ipynb
 * https://stackoverflow.com/questions/51503851/calculate-the-accuracy-every-epoch-in-pytorch
-->
def evaluate_accuracy_gpu(net, data_iter, device):
    """
    Evaluate the accuracy of the model given by 'net' on
    the DataLoader given by 'data_iter' using the device 'device'
    """
    net.eval()
    num_correct, num_total = 0, 0
    for i, (X, y) in enumerate(data_iter):
        X, y = X.to(device), y.to(device)
        _, predicted = torch.max(net(X), 1)
        correct = (predicted == y).sum()
        num_correct += correct
        num_total += y.shape[0]
    return float(num_correct) / num_total

---

https://discuss.pytorch.org/t/how-does-one-get-the-predicted-classification-label-from-a-pytorch-model/91649/2

note you need to choose .indices since you want to return the
# position of where the most likely label is (not it's raw logit value)
pred = logits.max(1).indices

---
https://stackoverflow.com/questions/51503851/calculate-the-accuracy-every-epoch-in-pytorch

.item() works when there is exactly 1 value in a tensor. Otherwise, it will give an error. (output == labels) is a boolean tensor with many values, by converting it to a float, Falses are casted to 0 and Trues are casted to 1.
