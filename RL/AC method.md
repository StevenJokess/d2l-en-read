

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 20:06:23
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-07 20:10:37
 * @Description:
 * @TODO::
 * @Reference:
-->
Actor-Critic methods

Actor-Critic methods are temporal difference (TD) learning methods that represent the policy function independent of the value function.

A policy function (or policy) returns a probability distribution over actions that the agent can take based on the given state. A value function determines the expected return for an agent starting at a given state and acting according to a particular policy forever after.

In the Actor-Critic method, the policy is referred to as the actor that proposes a set of possible actions given a state, and the estimated value function is referred to as the critic, which evaluates actions taken by the actor based on the given policy.

In this tutorial, both the Actor and Critic will be represented using one neural network with two outputs.

https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic

The actor-critic loss
Since we are using a hybrid actor-critic model, we will use loss function that is a combination of actor and critic losses for training, as shown below:


https://www.tensorflow.org/agents/overview
