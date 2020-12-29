

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 17:46:41
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 18:08:20
 * @Description:
 * @TODO::
 * @Reference:https://cs330.stanford.edu/slides/cs330_frontiers_2020.pdf
-->

ARM - adaptive risk minimization
DRNN - distributional robustness  (Sagawa, Koh et al. ICLR ’20)
ERM - standard deep network training
UW - ERM but upweight groups to the uniform distribution

MAML can learn equivariant initial featuresbut equivariance may not be preserved in the gradient update!012344r✓LGoal: Can we decompose weights into equivariant structure & corresponding parameters?If so: update onlyparameters in the inner loop, retaining equivariance.


Open Challenges in Multi-Task and Meta Learning

Addressing fundamental problem assumptions

- Generalization: Out-of-distribution tasks, long-tailed task distributions
-Multimodality: Can you learn priors from multiple modalities of data?
- Algorithm, Model Selection: When will multi-task learning help you?Benchmarks-Breadth: That challenge current algorithms to find common structure
- Realistic: That reflect real-world problems

Improving core algorithms-Computation & Memory:

- Making large-scale bi-level optimization practical
- Theory: Develop a theoretical understanding of the performance of these algorithms
- Multi-Step Problems: Performing tasks in sequence presents challenges.

+ the challenges you discovered in your homework & final projects!
