

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-07 20:06:23
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 17:15:11
 * @Description:
 * @TODO::
 * @Reference:
-->

## Actor-Critic Methods

In reinforcement learning, an agent makes observations and takes actions within an environment, and in return it receives rewards. Its objective is to learn to act in a way that will maximize its expected long-term rewards.

There are several types of RL algorithms, and they can be divided into three groups:

- Critic-Only: Critic-Only methods, also known as Value-Based methods, first find the optimal value function and then derive an optimal policy from it.
- Actor-Only: Actor-Only methods, also known as Policy-Based methods, search directly for the optimal policy in policy space. This is typically done by using a parameterized family of policies over which optimization procedures can be used directly.
- Actor-Critic: Actor-Critic methods combine the advantages of actor-only and critic-only methods. In this method, the critic learns the value function and uses it to determine how the actor's policy parramerters should be changed. In this case, the actor brings the advantage of computing continuous actions without the need for optimization procedures on a value function, while the critic supplies the actor with knowledge of the performance. Actor-critic methods usually have good convergence properties, in contrast to critic-only methods.

Actor-Critic methods

Actor-Critic methods are temporal difference (TD) learning methods that represent the policy function independent of the value function.

A policy function (or policy) returns a probability distribution over actions that the agent can take based on the given state. A value function determines the expected return for an agent starting at a given state and acting according to a particular policy forever after.

In the Actor-Critic method, the policy is referred to as the actor that proposes a set of possible actions given a state, and the estimated value function is referred to as the critic, which evaluates actions taken by the actor based on the given policy.

In this tutorial, both the Actor and Critic will be represented using one neural network with two outputs.

https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic

The actor-critic loss
Since we are using a hybrid actor-critic model, we will use loss function that is a combination of actor and critic losses for training, as shown below:


https://www.tensorflow.org/agents/overview


[1]: https://github.com/pytorch/examples/blob/master/reinforcement_learning/actor_critic.py
[2]: https://github.com/udacity/deep-reinforcement-learning/blob/master/finance/DRL.ipynb
