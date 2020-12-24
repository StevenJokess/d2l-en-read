

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-25 00:16:48
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 00:17:03
 * @Description:
 * @TODO::
 * @Reference:https://pytorch.org/tutorials/recipes/deployment_with_flask.html
-->

What is Flask?
Flask is a lightweight web server written in Python. It provides a convenient way for you to quickly set up a web API for predictions from your trained PyTorch model, either for direct use, or as a web service within a larger system.

Setup and Supporting Files
We’re going to create a web service that takes in images, and maps them to one of the 1000 classes of the ImageNet dataset. To do this, you’ll need an image file for testing. Optionally, you can also get a file that will map the class index output by the model to a human-readable class name.
