

/*
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-28 20:39:11
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-28 20:39:30
 * @Description:
 * @TODO::
 * @Reference:https://github.com/lanpa/tensorboardX/edit/master/HISTORY.rst
 */
History
=======
2.1 (2020-07-05)
-----------------
* Global SummaryWriter that mimics python's default logger class, concurrent write is supported.
* 200x speed up for add_audio. Please install the soundfile package for this feature.
* Supports jax tensors.
* The add_graph function is delegated to the one in torch.utils.tensorboard.
* Bug fixes, see the commit log in Github.

2.0 (2019-12-31)
-----------------
* Now you can tag Hparams trials with custom name instead of the default epoch time
* Fixed a bug that add_hparams are rendered incorrectly with non-string values
* Supports logging to Amazon S3 or Google Cloud Storage
* Bug fixes and error message for add_embedding function
* Draw openvino format with add_openvino_graph
