

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-29 18:10:05
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-29 18:18:34
 * @Description:
 * @TODO::
 * @Reference:https://cs330.stanford.edu/slides/cs330_skill_discovery_karol.pdf
-->

# Hierarchical RL and Skill Discovery

## Entropy

$p(\mathbf{x}) \quad$ distribution (e.g., over observations $\mathbf{x})$
$$
\mathcal{H}(p(\mathbf{x}))=-E_{\mathbf{x} \sim p(\mathbf{x})}[\log p(\mathbf{x})]
$$
entropy - how "broad" $p(\mathbf{x})$ is

## KL-divergence

Distance between two distributions
$$
\mathbb{D}_{K L}(q \| p)=\mathbb{E}_{q}\left[\log \frac{q(x)}{p(x)}\right]=\mathbb{E}_{q} \log q(x)-\mathbb{E}_{q} \log p(x)=-\mathbb{E}_{q} \log p(x)-\mathcal{H}(q(x))
$$

## Mutual information

$\begin{aligned} \mathcal{I}(\mathbf{x} ; \mathbf{y})=& D_{\mathrm{KL}}(p(\mathbf{x}, \mathbf{y}) \| p(\mathbf{x}) p(\mathbf{y})) \\ &=E_{(\mathbf{x}, \mathbf{y}) \sim p(\mathbf{x}, \mathbf{y})}\left[\log \frac{p(\mathbf{x}, \mathbf{y})}{p(\mathbf{x}) p(\mathbf{y})}\right] \\=\mathcal{H}(p(\mathbf{y})) &-\mathcal{H}(p(\mathbf{y} \mid \mathbf{x}))=\mathcal{H}(p(\mathbf{x}))-\mathcal{H}(p(\mathbf{x} \mid \mathbf{y})) \end{aligned}$

Why Hierarchical RL?

Performing tasks at various levels of abstractions

Bake a cheesecake
Buy ingredients
Go to the storeWalk to the door
Take a step
Contract muscle X

Exploration


HRL Summary

- Multiple design choices and frameworks
- Helps with exploration and temporally extended tasks
- Can be difficult to get it to work
- Seems like a natural direction for harder RL problems

Design choices:

- goal-conditioned vs not
- pre-trained vs e2e
- self-terminating vs fixed rate
- on-policy vs off-policy
