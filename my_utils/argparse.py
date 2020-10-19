# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-05 21:24:15
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-19 19:03:43
Description:
TODO::
Reference:https://github.com/enhuiz/transformer-pytorch/blob/master/scripts/train.py
'''
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=str)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    # opts = parse_config(args.config)
    # print(opts)

---

# https://tianshou.readthedocs.io/en/master/tutorials/tictactoe.html

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=1626)
    parser.add_argument('--eps-test', type=float, default=0.05)
    parser.add_argument('--eps-train', type=float, default=0.1)
    parser.add_argument('--buffer-size', type=int, default=20000)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--gamma', type=float, default=0.9,
                        help='a smaller gamma favors earlier win')
    parser.add_argument('--n-step', type=int, default=3)
    parser.add_argument('--target-update-freq', type=int, default=320)
    parser.add_argument('--epoch', type=int, default=10)
    parser.add_argument('--step-per-epoch', type=int, default=1000)
    parser.add_argument('--collect-per-step', type=int, default=10)
    parser.add_argument('--batch-size', type=int, default=64)
    parser.add_argument('--layer-num', type=int, default=3)
    parser.add_argument('--training-num', type=int, default=8)
    parser.add_argument('--test-num', type=int, default=100)
    parser.add_argument('--logdir', type=str, default='log')
    parser.add_argument('--render', type=float, default=0.1)
    parser.add_argument('--board_size', type=int, default=6)
    parser.add_argument('--win_size', type=int, default=4)
    parser.add_argument('--win-rate', type=float, default=np.float32(0.9),
                        help='the expected winning rate')
    parser.add_argument('--watch', default=False, action='store_true',
                        help='no training, watch the play of pre-trained models')
    parser.add_argument('--agent_id', type=int, default=2,
                        help='the learned agent plays as the agent_id-th player. Choices are 1 and 2.')
    parser.add_argument('--resume_path', type=str, default='',
                        help='the path of agent pth file for resuming from a pre-trained agent')
    parser.add_argument('--opponent_path', type=str, default='',
                        help='the path of opponent agent pth file for resuming from a pre-trained agent')
    parser.add_argument('--device', type=str,
                        default='cuda' if torch.cuda.is_available() else 'cpu')
    return parser.parse_args()
