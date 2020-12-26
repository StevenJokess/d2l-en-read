

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-26 21:53:39
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-26 21:59:53
 * @Description:
 * @TODO::
 * @Reference:http://www.cleverhans.io/2020/07/20/unlearning.html
 * https://github.com/cleverhans-lab/machine-unlearning
-->

Finding answers to this question is particularly pressing given that recent legislation requires organizations to give users the ability to delete their data (e.g., GDPR, Right to be forgotten). These pieces of legislation call for increased clarity around data usage in policy and technology. Thus, we now need the ability to make a trained machine learning model forget anything it could have learned from specific data samples.

How do we perform unlearning?
We now describe our approach to unlearning. We illustrate it with a single unlearning request (i.e., delete du), but the procedure for processing multiple such requests concurrently is similar.


We improve over the strawman strategy of retraining a model from scratch in two ways:

Our first optimization is called sharding. Recall that retraining a model without d_u is computationally intensive and time consuming when we have a large dataset; sharding aims to reduce this resource usage. In sharding, we partition the dataset into disjoint partitions (or shards). We then train a separate model, called a constituent model, on each shard. When making predictions, we ask all of the constituent models to vote and output the class which received the most number of votes. The sharding procedure ensures that each point is in only one of the shards and its influence is restricted to that particular constituent model, since the constituent models were trained in isolation. Now, an unlearning request can be mapped to a particular shard, where only the constituent model trained on that shard needs to be retrained. This approach speeds up retraining by (a) reducing the total number of data points that are affected by an unlearning request and (b) reducing the volume of data used to train each of the constituent models.

For example, imagine 1,000,000 data points are evenly split into S=10 shards, where each shard has 100,000 data points. On arrival of an unlearning request (after sharding), only the constituent model corresponding to the affected shard needs to be retrained – amounting to retraining a model with 99,999 points. The baseline would require retraining of the large “monolithic” model with 999,999 points, which is nearly 10x more data. This result can be generalized: for a single unlearning request, on creating N shards, the speed-up is N-fold.

Our second optimization is called slicing. We divide the data in a shard into disjoint subsets; each subset is called a slice. We then train a new model by ‘fine-tuning’ on incremental sets of slices, as opposed to including all the data in the shard in each of the epochs during training. We find that this process yields a final model that has comparable prediction accuracy to a model trained without slicing. It also decreases the time needed to retrain the model if we save a checkpoint, or intermediate model, of the model before introducing the next slice in training, which we must do since each new slice introduces new user data that may need to be unlearned.

For example, if a shard is divided into R=5 slices (say slice 1 to slice 5), we first train intermediate model 1 using slice 1, and then train intermediate model 2 by fine-tuning model 1 on both slice 1 and slice 2. We do so until we’ve trained our final model, model 5, which we do by fine tuning model 4 with data from slices 1 through 5; we use model 5 to make predictions. This process can be easily implemented using model checkpoints – saved, backup model parameters from different stages of training that are very common to ML pipelines. To unlearn d_u, we need only retrain all (intermediate) models that were trained/fine-tuned using the slice containing d_u. In the worst-case, this data point will be in slice 1, where we will have to retrain all models; however, in expectation we will only have to retrain half of them. As before, we can use any unaffected models to speed-up the fine-tuning process, which we find leads to an average 1.5-fold reduction in training time.

At best, we can achieve a 1.5N-fold speed-up for a single unlearning request by using our techniques, collectively called Sharded Isolated Sliced Aggregated (SISA) training. For more unlearning requests, we incur more retraining costs when the unlearned data points fall into new shards or slices because we would then have more models to retrain. Our paper contains more details for evaluating speed-ups when we receive higher volumes of unlearning requests. Our evaluation shows that we can efficiently handle more unlearning requests than shown by available historical data on search engines.
