

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-20 01:25:59
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-20 01:25:59
 * @Description:
 * @TODO::
 * @Reference:https://github.com/ibrahimjelliti/Deeplearning.ai-GAN-Specialization-Generative-Adversarial-Networks/blob/master/3%20-%20Apply%20Generative%20Adversarial%20Network%20(GAN)/Week%203/C3W3_Assignment.ipynb
-->
def show_tensor_images(image_tensor, num_images=25, size=(1, 28, 28)):
    '''
    Function for visualizing images: Given a tensor of images, number of images, and
    size per image, plots and prints the images in an uniform grid.
    '''
    image_tensor = (image_tensor + 1) / 2
    image_shifted = image_tensor
    image_unflat = image_shifted.detach().cpu().view(-1, *size)
    image_grid = make_grid(image_unflat[:num_images], nrow=5)
    plt.imshow(image_grid.permute(1, 2, 0).squeeze())
    plt.show()
