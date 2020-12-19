

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-19 22:38:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 22:38:27
 * @Description:
 * @TODO::
 * @Reference:https://github.com/bentrevett/pytorch-rl/blob/master/q_learning.py
-->
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--env', default='CartPole-v1', type=str)
parser.add_argument('--seed', default=1234, type=int)
parser.add_argument('--n_layers', default=1, type=int)
parser.add_argument('--grad_clip', default=0.5, type=float)
parser.add_argument('--hid_dim', default=32, type=int)
parser.add_argument('--init', default='xavier', type=str)
parser.add_argument('--n_runs', default=5, type=int)
parser.add_argument('--n_episodes', default=1000, type=int)
parser.add_argument('--discount_factor', default=0.99, type=float)
parser.add_argument('--start_epsilon', default=1.0, type=float)
parser.add_argument('--end_epsilon', default=0.01, type=float)
parser.add_argument('--exploration_time', default=0.5, type=float)
parser.add_argument('--optim', default='adam', type=str)
parser.add_argument('--lr', default=1e-3, type=float)
args = parser.parse_args()
